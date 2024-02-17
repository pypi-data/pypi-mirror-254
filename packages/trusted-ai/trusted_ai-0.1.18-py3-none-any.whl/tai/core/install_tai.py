from __future__ import annotations

import argparse
import dataclasses
import io
import json
import os
import platform
import re
import shutil
import site
import subprocess
import sys
import urllib.request
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Sequence

if sys.version_info < (3, 12):
    sys.exit("Python 3.12 or above is required to install trusted-ai.")

_plat = platform.system()
MACOS = _plat == "Darwin"
JSON_URL = "https://pypi.org/pypi/trusted-ai/json"

FOREGROUND_COLORS = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}


def _call_subprocess(args: list[str]) -> int:
    try:
        return subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True).returncode
    except subprocess.CalledProcessError as e:
        print(f"An error occurred when executing {args}:", file=sys.stderr)
        print(e.output.decode("utf-8"), file=sys.stderr)
        sys.exit(e.returncode)


def _echo(text: str) -> None:
    sys.stdout.write(text + "\n")


def _add_to_path(target: Path) -> None:
    value = os.path.normcase(target)

    paths = [os.path.normcase(p) for p in os.getenv("PATH", "").split(os.pathsep)]
    if value in paths:
        return
    _echo(
        "Post-install: Please add {} to PATH by executing:\n    {}".format(
            colored("green", value),
            colored("cyan", f"export PATH={value}:$PATH"),
        )
    )


def support_ansi() -> bool:
    if not hasattr(sys.stdout, "fileno"):
        return False

    try:
        return os.isatty(sys.stdout.fileno())
    except io.UnsupportedOperation:
        return False


def colored(color: str, text: str, bold: bool = False) -> str:
    if not support_ansi():
        return text
    codes = [FOREGROUND_COLORS[color]]
    if bold:
        codes.append(1)

    return "\x1b[{}m{}\x1b[0m".format(";".join(map(str, codes)), text)


@dataclasses.dataclass
class Installer:
    location: str | None = None
    version: str | None = None
    prerelease: bool = False
    additional_deps: Sequence[str] = ()
    skip_add_to_path: bool = False
    output_path: str | None = None

    def __post_init__(self):
        self._path = self._decide_path()
        self._path.mkdir(parents=True, exist_ok=True)
        if self.version is None:
            self.version = self._get_latest_version()

    def _get_latest_version(self) -> str:
        resp = urllib.request.urlopen(JSON_URL)
        metadata = json.load(resp)

        def version_okay(v: str) -> bool:
            return self.prerelease or all(p.isdigit() for p in v.split("."))

        def sort_version(v: str) -> tuple:
            parts = []
            for part in v.split("."):
                if part.isdigit():
                    parts.append(int(part))
                else:
                    digit, rest = re.match(r"^(\d*)(.*)", part).groups()
                    if digit:
                        parts.append(int(digit))
                    parts.append(rest)
            return tuple(parts)

        installable_versions = {
            k for k, v in metadata["releases"].items() if version_okay(k) and not v[0].get("yanked")
        }
        releases = sorted(installable_versions, key=sort_version, reverse=True)

        return releases[0]

    def _decide_path(self) -> Path:
        if self.location is not None:
            return Path(self.location).expanduser().resolve()

        if MACOS:
            path = os.path.expanduser("~/Library/trusted-ai")
        else:
            path = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
            path = os.path.join(path, "trusted-ai")

        return Path(path)

    def _make_env(self) -> Path:
        venv_path = self._path / "venv"

        _echo(
            "Installing {} ({}): {}".format(
                colored("green", "trusted-ai", bold=True),
                colored("yellow", self.version),
                colored("cyan", "Creating virtual environment"),
            )
        )

        try:
            import venv

            venv.create(venv_path, clear=False, with_pip=True)
        except (ModuleNotFoundError, subprocess.CalledProcessError):
            try:
                import virtualenv
            except ModuleNotFoundError:
                python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
                url = f"https://bootstrap.pypa.io/virtualenv/{python_version}/virtualenv.pyz"
                with TemporaryDirectory(prefix="trusted-ai-installer-") as tempdir:
                    virtualenv_zip = Path(tempdir) / "virtualenv.pyz"
                    urllib.request.urlretrieve(url, virtualenv_zip)
                    _call_subprocess([sys.executable, str(virtualenv_zip), str(venv_path)])
            else:
                virtualenv.cli_run([str(venv_path)])

        return venv_path

    def _install(self, venv_path: Path) -> None:
        _echo(
            "Installing {} ({}): {}".format(
                colored("green", "trusted-ai", bold=True),
                colored("yellow", self.version),
                colored("cyan", "Installing trusted-ai and dependencies"),
            )
        )

        # if WINDOWS:
        #     venv_python = venv_path / "Scripts/python.exe"
        # else:
        venv_python = venv_path / "bin" / "python"

        # Re-install the venv pip to ensure it's not DEBUNDLED
        # See issue/685
        try:
            _call_subprocess([str(venv_python), "-m", "ensurepip"])
        except SystemExit:
            pass
        _call_subprocess([str(venv_python), "-m", "pip", "install", "-IU", "pip"])

        if self.version:
            req = f"trusted-ai=={self.version}"
        else:
            req = "trusted-ai"
        args = [req] + [d for d in self.additional_deps if d]
        pip_cmd = [str(venv_python), "-Im", "pip", "install", *args]

        _call_subprocess(pip_cmd)

    def _make_bin(self, venv_path: Path) -> Path:
        if self.location:
            bin_path = self._path / "bin"
        else:
            userbase = Path(site.getuserbase())
            bin_path = userbase / "bin"

        _echo(
            "Installing {} ({}): {} {}".format(
                colored("green", "trusted-ai", bold=True),
                colored("yellow", self.version),
                colored("cyan", "Making binary at"),
                colored("green", str(bin_path)),
            )
        )
        bin_path.mkdir(parents=True, exist_ok=True)
        script = bin_path / "tai"
        target = venv_path / "bin" / "tai"

        if script.exists():
            script.unlink()
        try:
            script.symlink_to(target)
        except OSError:
            shutil.copy(target, script)
        return bin_path

    def _post_install(self, venv_path: Path, bin_path: Path) -> None:
        script = bin_path / "tai"
        subprocess.check_call([str(script), "--help"])
        print()
        _echo(
            "Successfully installed: {} ({}) at {}".format(
                colored("green", "trusted-ai", bold=True),
                colored("yellow", self.version),
                colored("cyan", str(script)),
            )
        )
        if not self.skip_add_to_path:
            _add_to_path(bin_path)
        self._write_output(venv_path, script)

    def _write_output(self, venv_path: Path, script: Path) -> None:
        if not self.output_path:
            return
        print("Writing output to", colored("green", self.output_path))
        output = {
            "trusted_ai_version": self.version,
            "trusted_ai_bin": str(script),
            "install_python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "install_location": str(venv_path),
        }
        with open(self.output_path, "w") as f:
            json.dump(output, f, indent=2)

    def install(self) -> None:
        venv = self._make_env()
        self._install(venv)
        bin_dir = self._make_bin(venv)
        self._post_install(venv, bin_dir)

    def uninstall(self) -> None:
        _echo(
            "Uninstalling {}: {}".format(
                colored("green", "trusted-ai", bold=True),
                colored("cyan", "Removing venv and script"),
            )
        )
        if self.location:
            bin_path = self._path / "bin"
        else:
            userbase = Path(site.getuserbase())
            bin_path = userbase / "bin"

        script = bin_path / "trusted-ai"

        shutil.rmtree(self._path / "venv")
        script.unlink()

        print()
        _echo("Successfully uninstalled")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        help="Specify the version to be installed",
        default=os.getenv("TRUSTED_AI_VERSION"),
    )
    parser.add_argument(
        "--prerelease",
        action="store_true",
        help="Allow prereleases to be installed",
        default=os.getenv("TRUSTED_AI_PRERELEASE"),
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Remove the trusted-ai installation",
        default=os.getenv("TRUSTED_AI_REMOVE"),
    )
    parser.add_argument(
        "-p",
        "--path",
        help="Specify the location to install trusted-ai",
        default=os.getenv("TRUSTED_AI_HOME"),
    )
    parser.add_argument(
        "-d",
        "--dep",
        action="append",
        default=os.getenv("TRUSTED_AI_DEPS", "").split(","),
        help="Specify additional dependencies, can be given multiple times",
    )
    parser.add_argument(
        "--skip-add-to-path",
        action="store_true",
        help="Do not add binary to the PATH.",
        default=os.getenv("TRUSTED_AI_SKIP_ADD_TO_PATH"),
    )
    parser.add_argument("-o", "--output", help="Output file to write the installation info to")

    options = parser.parse_args()
    installer = Installer(
        location=options.path,
        version=options.version,
        prerelease=options.prerelease,
        additional_deps=options.dep,
        skip_add_to_path=options.skip_add_to_path,
        output_path=options.output,
    )
    if options.remove:
        installer.uninstall()
    else:
        installer.install()


if __name__ == "__main__":
    main()
import yaml
from typing import Optional


EMAIL_TEMPLATE = "<your@mail.com>"
FULL_NAME_TEMPLATE = "<Your Full Name for gitea>"
PASSWORD_TEMPLATE = "<Your password for gitea>"
USERNAME_TEMPLATE = "<Your username for gitea>"

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def read_config(conf_path: str):
    with open(conf_path) as f:
        config = yaml.safe_load(f)
    return config


def add_to_config(conf_path: str, data, key):
    with open(conf_path) as file:
        try:
            list_doc = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
    list_doc[key] = data
    with open(conf_path, "w") as f:
        yaml.dump(list_doc, f)


def create_template_user_config(conf_path: str,
                                email: Optional[str] = None,
                                full_name: Optional[str] = None,
                                password: Optional[str] = None,
                                username: Optional[str] = None,
                                ):
    data = {
        "email": EMAIL_TEMPLATE if email is None else email,
        "full_name": FULL_NAME_TEMPLATE if full_name is None else full_name,
        "password": PASSWORD_TEMPLATE if password is None else password,
        "username": USERNAME_TEMPLATE if username is None else username,
    }
    with open(conf_path, "w") as f:
        yaml.dump(data, f)
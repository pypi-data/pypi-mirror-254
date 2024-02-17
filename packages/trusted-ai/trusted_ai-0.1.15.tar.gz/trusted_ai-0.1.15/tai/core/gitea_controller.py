import requests
from tai.core.utils import read_config


class GiteaUser:
    def __init__(self, conf_path):
        user_config = read_config(conf_path)

        self.config_path = conf_path
        self.username = user_config["username"]
        self.password = user_config["password"]
        self.email = user_config["email"]
        self.full_name = user_config["full_name"]

class GiteaController:
    def __init__(self, admin_config_path: str):
        config = read_config(admin_config_path)

        self._headers = {"Authorization": "token " + config["admin_token"]}
        self.protocol = "https"
        self.host = "git.ai.intra.ispras.ru"

    def check_user_existing(self, username):
        url = f"{self.protocol}://{self.host}/api/v1/users/{username}"
        r = requests.get(url)
        if r.status_code == 200:
            exist = True
            status = 'ok'
        elif r.status_code == 404:
            exist = False
            status = 'ok'
        else:
            exist = None
            status = 'fail'
            print(r.json())
        return exist, status
    
    def create_new_user(self, user) :
        username = user.username
        password = user.password
        email = user.email
        full_name = user.full_name

        data = {
        "email": email,
        "username": username,
        "password": password,
        "login_name": username,
        "must_change_password": False,
        "full_name": full_name,
        }

        url = f"{self.protocol}://{self.host}/api/v1/admin/users"
        r = requests.post(url, json=data, headers=self._headers)

        if r.status_code == 201:
            status = 'ok'
        else:
            status = 'fail'
            print(r.json(), r.status_code)
        return status
    
    def create_repo(self, repo_name: str, user: GiteaUser, description: str = ""):
        url = f"{self.protocol}://{user.username}:{user.password}@{self.host}/api/v1/user/repos"

        data = {
            "default_branch": "master",
            "description": description,
            "license": "MIT",
            "name": repo_name,
            "private": False,
            "trust_model": "default"
            }
        r = requests.post(url, data=data, headers=self._headers)
        if r.status_code == 201:
            status = 'ok'
        elif r.status_code == 409:
            status = 'fall'
            print(f"Repository with name {repo_name} already exist.")
        else:
            status = 'fail'
            print(r.json())
        return status
    
    def remove_repo(self, repo_name, user):
        url = f"{self.protocol}://{self.host}/api/v1/repos/{user.username}/{repo_name}"

        r = requests.delete(url, headers=self._headers)

        if r.status_code == 204:
            status = 'ok'
        else:
            status = 'fail'
            print(r.json())

        r.text, r.status_code
    
    def remove_user(self, username):
        url = f"{self.protocol}://{self.host}/api/v1/admin/users/{username}"

        r = requests.delete(url, headers=self._headers)

        if r.status_code == 204:
            status = 'ok'
        else:
            status = 'fail'
            print(r.json())
        return status

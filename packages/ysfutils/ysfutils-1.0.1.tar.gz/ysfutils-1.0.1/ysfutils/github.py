import os
import shutil
from pathlib import Path

import requests


class Repository:

    def __init__(self, repo_owner, repo_name, branch='main', github_token=None):
        try:
            self.__token = github_token if github_token else os.environ["GITHUB_TOKEN"]
        except KeyError:
            self.__token = None
        self.__repo_owner = repo_owner
        self.__repo_name = repo_name
        self.__branch = branch

    def get_repo_file_path(self):
        """ 读取该branch下的所有文件的path

        Returns:
            {"文件名": ["该分支下该文件的路径"]......}, 例如fortune仓库, main分支的例子如下:
                {"cut_daily.py": ["fortune/bin/cut_daily.py"]......}

        """
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"token {self.__token}"
        }
        tree_api = f"https://api.github.com/repos/{self.__repo_owner}/{self.__repo_name}/git/trees/{self.__branch}?recursive=1"
        response = requests.get(tree_api, headers=headers)
        result = {}
        if response.status_code == 200:
            for git_element in response.json()["tree"]:
                if git_element["type"] == "blob":
                    path = Path(git_element["path"])
                    if path.name in result:
                        result[path.name].append(git_element["path"])
                    else:
                        result[path.name] = [git_element["path"]]
            return result
        else:
            return result

    def download_file(self, github_file_path, local_file_path):
        """ 下载文件到本地

        Args:
            github_file_path: 文件的仓库路径, 例如fortune/jobs/akshare/bomb_pool.py
            local_file_path: 写入的本地路径, 注意只有目录名, 文件名默认是github里的文件名

        Returns:
            本地文件路径

        """
        local_file = None
        headers = {"Authorization": f"token {self.__token}"}
        content_url = f"https://api.github.com/repos/{self.__repo_owner}/{self.__repo_name}/contents/{github_file_path}"
        response = requests.get(content_url, headers=headers)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            with requests.get(data["download_url"], stream=True) as resp:
                local_file = f"{os.path.join(local_file_path, data['name'])}"
                with open(local_file, 'wb') as f:
                    shutil.copyfileobj(resp.raw, f)
                return local_file
        else:
            return local_file

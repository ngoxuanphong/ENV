import subprocess
import json
from git import Repo
from tests.CheckEnv import check_pytest


def get_changed_files():
    repo_path = ""
    repo = Repo(repo_path)
    latest_commit = repo.head.commit

    changed_files = []
    for diff in latest_commit.diff(None):
        changed_files.append(diff.a_path)
    print((latest_commit.hexsha))

    commit = "78b1588e67b36502797dd4a93f2929af9fd170dc"
    api_path = f"https://api.github.com/repos/ngoxuanphong/ENV/commits/{commit}"
    command = f"curl -s {api_path}"
    output = subprocess.check_output(
        command, shell=True, stderr=subprocess.STDOUT
    ).decode("utf-8")

    output = json.loads(output)
    for file in output["files"]:
        print(file["filename"])

    return changed_files


def test_print_name():
    changed_files = get_changed_files()
    # for file in changed_files:
    #     if "Base/" in file and "/_env.py" in file:
    #         env_name = file.replace("Base/", "").replace("/_env.py", "")
    #         print(env_name, "checking...")
    #         check_env, list_bug = check_pytest(env_name)
    #         if check_env == False:
    #             print("ENV:", env_name, "FALSE:", list_bug)
    #             assert False
    #         else:
    #             print("ENV:", env_name, "TRUE")
    #             assert True

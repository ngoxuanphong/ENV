# import pytest
# @pytest.fixture(scope="session")
# def name(pytestconfig):
#     return pytestconfig.getoption("name")

from git import Repo
from tests.CheckEnv import check_pytest


def get_changed_files():
    # Đường dẫn tới thư mục git
    repo_path = ""

    # Khởi tạo đối tượng Repo từ đường dẫn thư mục git
    repo = Repo(repo_path)

    # Lấy commit gần nhất
    latest_commit = repo.head.commit

    # Liệt kê các tệp tin đã thay đổi trong commit gần nhất
    changed_files = []
    for diff in latest_commit.diff(None):
        changed_files.append(diff.a_path)
    print(latest_commit)
    commits = list(repo.iter_commits())
    second_latest_commit = commits[-2]
    print(second_latest_commit)
    changed_files = []
    for diff in second_latest_commit.diff(None):
        changed_files.append(diff.a_path)
    print(changed_files)
    return changed_files


def test_print_name():
    changed_files = get_changed_files()
    for file in changed_files:
        if "Base/" in file and "/_env.py" in file:
            env_name = file.replace("Base/", "").replace("/_env.py", "")
            print(env_name, "checking...")
            check_env, list_bug = check_pytest(env_name)
            if check_env == False:
                print("ENV:", env_name, "FALSE:", list_bug)
                assert False
            else:
                print("ENV:", env_name, "TRUE")
                assert True

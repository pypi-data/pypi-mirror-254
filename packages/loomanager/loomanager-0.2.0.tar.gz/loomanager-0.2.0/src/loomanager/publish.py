from src.loomanager.errors import err, VERBOSE
from zenyx import printf
import src.loomanager.files as files
import src.loomanager.input as inp
import os
import time


def get_new_version(update_type: str):
    version_list: list[int, int, int] = []
    step_version: list[int, int, int] = []

    try:
        version_list = [int(x) for x in str(files.CONFIG.get("version")).split(".")]
    except Exception as e:
        err(
            msg=f"Wrong version data: {e}",
            hint="\n".join(
                [
                    "The given version is not numberic.",
                    "The version should be <int>.<int>.<int>",
                ]
            ),
        )

    try:
        step_version = [int(x) for x in update_type.get("increment").split(".")]
    except Exception as e:
        err(
            msg=f"Wrong increment data: {e}",
            hint="\n".join(
                [
                    "The given increment is not numberic.",
                    "The increment should be <int>.<int>.<int>",
                ]
            ),
        )

    if step_version[2] > 0:
        version_list[2] += step_version[2]

    if step_version[1] > 0:
        version_list[2] = 0
        version_list[1] += step_version[1]

    if step_version[0] > 0:
        version_list[2] = 0
        version_list[1] = 0
        version_list[0] += step_version[0]
    
    return ".".join([str(x) for x in version_list])

def git():
    printf.title("Configure Commit")

    branch: str = ""

    printf("@!Select Commit Type$&")
    update_type = inp.select_dict_key(files.CONFIG.get("types"))

    if files.CONFIG.get("project-type") == "python" and update_type.get("publish"):
        time.sleep(0.2)
        printf("@!Select PyPi Branch$&")
        branch: str = inp.select_dict_key(inp.TEST_MAIN_CHOICE).get("value")

    printf("\n@!Enter Commit Message$&")
    commit_message = inp.get_input(incomplete_err=True)

    printf("\n\n@!Enter Commit Message$&")
    commit_description = inp.get_input()

    version = get_new_version(update_type) 

    printf.title("Confirm")
    printf(f"@!New Version$&\n {version}")
    printf(f'\n@!Commit Message$&\n "{commit_message}"')
    printf(f'\n@!Commit Description$&\n {commit_description}"')

    time.sleep(0.2)

    printf("\n\n@!Publish?$&")
    publish = inp.select_dict_key(inp.YES_NO_CHOICE).get("value")

    if publish != "yes":
        printf("\n\n@!Commit aborted!$&\n")
        return
    
    files.modify_file_for_new_version(version)

    printf.title("✨ Creating Commit & Pushing Changes ✨")
    
    printf("\n@~@?git add .$&")
    os.system("git add .")
    
    printf(f"\n@~@?git commit -m \"{version} | {update_type.get('symbol')} | {commit_message}\" -m \"{commit_description}\"$&")
    os.system(f"git commit -m \"{version} | {update_type.get('symbol')} | {commit_message}\" -m \"{commit_description}\"")

    printf("\n@~@?git push$&")
    os.system("git push")

    if branch == "":
        return
    
    files.delete_files_in_folder("./dist")

    printf("\n@~@?python -m build$&")
    os.system("python -m build")

    if branch == "test":
        printf("\n@~@?python -m twine upload --repository testpypi dist/*$&")
        os.system(f"python -m twine upload {'--verbose' if VERBOSE else ''} --repository testpypi dist/*")
        return
    
    printf("\n@~@?python -m twine upload dist/*$&")
    os.system(f"python -m twine upload {'--verbose' if VERBOSE else ''} dist/*")



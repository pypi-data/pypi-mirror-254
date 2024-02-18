from src.loomanager.errors import err
import toml
import zenyx
import os

BASE_CONFIG: str = """
[loom]
version = "0.0.0"
project-type = "python"

[loom.types.patch]
symbol = "📜"
increment = "0.0.1"
publish = false

[loom.types.minor]
symbol = "✅"
increment = "0.1.0"
publish = true

[loom.types.major]
symbol = "📦"
increment = "1.0.0"
publish = true

[loom.types.chore]
symbol = "🔨"
increment = "0.0.0"
publish = false
"""


BATCH_FILE = """
python -m loomanager --INNER.cls %*
"""

CONFIG: dict | None


def read_config(file_path: str):
    try:
        with open(os.path.realpath(file_path), "r", encoding="utf-8") as config_file:
            config = toml.load(config_file)
            return config
    except Exception:
        return None


def init():
    global CONFIG

    config = read_config("loom.toml")
    if (
        config is None
        or config.get("loom") is None
        or config.get("loom").get("version") is None
    ):
        err(
            msg="Config file does not exist, or isn't configured correctly.",
            hint="\n".join(
                [
                    "Create a @?loom.toml$& config file in the root directory of you project.",
                    "The @?loom.toml$& file should have a @?[loom]$& section.",
                    "You can do this by running: python -m loomanager new",
                    "Or you can manually set up the @?loom.toml$& file.\n" "\nSyntax:",
                    "| [loom]",
                    '| version = "0.0.0"',
                    '| project-type = "python"',
                ]
            ),
        )

    config = config.get("loom")

    if config.get("types") is None:
        err(
            msg="No commit types configured.",
            hint="\n".join(
                [
                    "For loomanager to run, you need to configure commit types.",
                    "When you run the manager, these will be your commit type options.",
                    "\nSyntax:",
                    "| [loom.types.example]",
                    '| symbol = "📦"',
                    '| increment = "1.0.0"',
                    "| publish = true",
                    "\nExplanation:",
                    "  @~Commit message syntax will look like this:",
                    "    <version> | <symbol?> | <message>$&",
                    "  @?increment$& -> specifies which part of the",
                    "               version number should be incremented.",
                    "  @?symbol$&    -> specifies the symbol used in the commit message",
                    "  @?publish$&   -> if a project-type is set and publish is true, ",
                    "               auto publishes to PyPi",
                ]
            ),
        )

    if not os.path.exists(os.path.realpath("./pyproject.toml")) and config.get(
        "project-type"
    ):
        config["project-type"] = "not-module-python"

    CONFIG = config


def new_config():
    """Create a new loom.toml file"""
    global BASE_CONFIG

    if os.path.exists(os.path.realpath("./loom.toml")):
        err(
            msg="Cannot create new config.",
            hint="\n".join(
                [
                    "The loom.toml file already exists.",
                    "To create a new config delete the current one.",
                ]
            ),
        )

    with open(os.path.realpath("./loom.toml"), "w", encoding="utf-8") as wf:
        wf.write(BASE_CONFIG)


def create_batch():
    """Create a ./loom.bat file"""
    global BATCH_FILE

    if os.path.exists(os.path.realpath("./loom.bat")):
        err(
            msg="Cannot create new batch file.",
            hint="\n".join(
                [
                    "The loom.bat file already exists.",
                    "To create a new batch file delete the current one.",
                ]
            ),
        )

    with open(os.path.realpath("./loom.bat"), "w", encoding="utf-8") as wf:
        wf.write(BATCH_FILE)


def modify_file_for_new_version(new_v: str):
    with open(os.path.realpath("./loom.toml"), "r+") as f:
        content = f.read()
        f.seek(0)
        f.write(
            content.replace(
                f"version = \"{CONFIG.get('version')}\"", f'version = "{new_v}"'
            )
        )

    if not CONFIG.get("project-type"):
        return

    with open(os.path.realpath("./pyproject.toml"), "r+") as f:
        content = f.read()
        f.seek(0)
        f.write(
            content.replace(
                f"version = \"{CONFIG.get('version')}\"", f'version = "{new_v}"'
            )
        )


def delete_files_in_folder(folder_path):
    if not os.path.exists(os.path.realpath(folder_path)):
        return

    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        # Iterate through the files and delete each one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        print(f"All files in {folder_path} have been deleted.")
        
    except Exception as e:
        err(
            msg=f"Failed to delete \"{folder_path}\": {e}"
        )

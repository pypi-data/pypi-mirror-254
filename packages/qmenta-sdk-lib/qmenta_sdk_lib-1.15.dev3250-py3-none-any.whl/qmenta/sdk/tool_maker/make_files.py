import os

from qmenta import client  # noqa: ignore=E402

SCRIPT = "tool.py"
SETTINGS = "settings.json"
RES_CONF = "results_configuration.json"
DESCRIPTION = "description.html"
local_dockerfile = "Dockerfile"
local_requirements = "requirements.txt"
TEST_TOOL = "test_tool.py"

default_requirements = ["qmenta-sdk-lib"]
repo_dir = os.path.join(
    os.path.dirname(__file__), "../python/qmenta/tools", "..", "..", "..", ".."
)  # this needs to be updated in the sdk repo


def build_local_dockerfile() -> None:
    """
    Building the Dockerfile in the local folder to run locally
    """
    # Here we are in the local/ folder, we switch to the test/ folder
    if not os.path.exists(local_dockerfile):
        with open(local_dockerfile, "w") as w1:
            with open(os.path.join(os.path.dirname(__file__), "Dockerfile_schema")) as r1:
                w1.write(r1.read())


def build_local_requirements() -> None:
    """
    Preparing the python requirements file in the local folder to run locally

    """
    if not os.path.exists(local_requirements):
        with open(local_requirements, "w") as f1:
            f1.writelines(["# Python requirements for tool:\n", "# Ex: matplotlib==3.4.2\n"] + default_requirements)


def build_script(tool_id: str) -> None:
    """

    Writing the tool class with the tool_inputs(), run(), and tool_outputs() examples

    Parameters
    ----------
    tool_id: str
        Tool ID provided by the GUI

    """
    with open(os.path.join(os.path.dirname(__file__), "tool_schema")) as r1:
        with open(SCRIPT, "w") as w1:
            w1.write(r1.read().replace("TOOL_CLASS", convert_to_camel_case(tool_id)))


def build_description() -> None:
    """
    Write an empty file, to be filled by the developer
    """
    with open(os.path.join(os.path.dirname(__file__), "description_schema.html")) as r1:
        with open(DESCRIPTION, "w") as w1:
            w1.write(r1.read())


def convert_to_camel_case(tool_id: str) -> str:
    """
    Utils function to convert the ID of the tool to camel case convention string for the class of the tool and the test.

    Parameters
    ----------
    tool_id : str
        Tool ID provided by the GUI

    Returns
    -------
    str
    """
    return "".join([t.capitalize() for t in tool_id.split("_")])


def build_test(tool_id: str, tool_folder: str, version: str) -> None:
    """
    Create internal structure for the local folder, test and sample data

    Parameters
    ----------
    tool_id : str
        Tool ID provided by the GUI
    tool_folder : str
        Tool folder provided by the GUI
    version : str
        Tool version provided by the GUI

    """
    os.makedirs("test/", exist_ok=True)
    os.makedirs("test/sample_data", exist_ok=True)
    os.chdir("test")
    with open(os.path.join(os.path.dirname(__file__), "test_tool_schema")) as r1:
        with open(TEST_TOOL, "w") as w1:
            w1.write(
                r1.read()
                .replace("TOOL_CLASS", convert_to_camel_case(tool_id))
                .replace("TOOL_ID", tool_id)
                .replace("TOOL_FOLDER", os.path.join(tool_folder, tool_id))
                .replace("VERSION", version)
            )

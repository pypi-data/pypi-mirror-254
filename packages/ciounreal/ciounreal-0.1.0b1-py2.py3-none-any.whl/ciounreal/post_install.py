import os
import sys
import errno
import shutil
import zipfile


def fslash(path):
    return path.replace("\\", "/")


PACKAGE_DIR = fslash(os.path.dirname(os.path.abspath(__file__)))
CIO_DIR = os.path.dirname(PACKAGE_DIR)
HOME = fslash(os.path.expanduser("~"))
UNREAL_BASE_PATH = r"C:\Program Files\Epic Games"

PROJECT_BASE_PATH = os.path.join(HOME, "Documents", "Unreal Projects", "MRQ_Dev")
DEV_MODE = False
PLUGIN_NAME = "Conductor"

INIT_SCRIPT_CONTENT = f"""
import sys

CIO_DIR = "{CIO_DIR}"

if CIO_DIR not in sys.path:
    sys.path.append(CIO_DIR)

from ciounreal import ConductorExecutor

print("APPENDED CIO_DIR to sys.path: ", CIO_DIR)
print("Imported ConductorExecutor.py")
"""


def main():
    print(f"CIO_DIR: {CIO_DIR}")

    # Get the list of Unreal Engine Plugins directories
    ue_plugin_directories = find_unreal_engine_plugins()

    for plugin_directory in ue_plugin_directories:
        print(f"Installing the {PLUGIN_NAME} plugin to {plugin_directory}")
        install_into_unreal(plugin_directory)

    print("Completed Unreal tool setup!")


def find_unreal_engine_plugins():
    BASE_PATH = PROJECT_BASE_PATH if DEV_MODE else UNREAL_BASE_PATH
    if not os.path.exists(BASE_PATH):
        print("The default installation path does not exist.")
        return []

    if DEV_MODE:
        return [os.path.join(PROJECT_BASE_PATH, "Plugins")]

    engine_versions = [
        d
        for d in os.listdir(BASE_PATH)
        if os.path.isdir(os.path.join(BASE_PATH, d)) and d.startswith("UE_5")
    ]
    plugin_paths = []

    for version in engine_versions:
        engine_path = os.path.join(BASE_PATH, version)
        plugins_path = os.path.join(engine_path, "Engine", "Plugins")
        if os.path.exists(plugins_path):
            plugin_paths.append(plugins_path)
        else:
            print(f"Plugins directory not found for {version}")

    print(f"Found {len(plugin_paths)} Unreal Engine plugin directories")
    # Print the full paths
    for path in plugin_paths:
        print(path)
    return plugin_paths


def install_into_unreal(plugins_directory):
    ensure_directory(plugins_directory)
    # Delete existing installation if it exists.
    plugin_directory = os.path.join(plugins_directory, PLUGIN_NAME)
    # Create or empty a folder for the plugin.
    try:
        if os.path.isdir(plugin_directory):
            shutil.rmtree(plugin_directory)
    except Exception as e:
        print(f"Failed to remove existing {plugin_directory}. Reason: {e}")
        return

    zipped = os.path.join(CIO_DIR, "Resources", "Conductor.zip")
    target = os.path.join(plugins_directory, "Conductor")
    ensure_directory(target)
    with zipfile.ZipFile(zipped, "r") as zip_ref:
        zip_ref.extractall(target)

    with open(os.path.join(target, "Content", "Scripts", "init_unreal.py"), "w") as f:
        f.write(INIT_SCRIPT_CONTENT)


def ensure_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as ex:
        if ex.errno == errno.EEXIST and os.path.isdir(directory):
            pass
        else:
            raise


if __name__ == "__main__":
    main()

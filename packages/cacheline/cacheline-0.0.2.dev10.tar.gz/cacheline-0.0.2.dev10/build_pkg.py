import logging
import os
import subprocess
import sys

import toml


def build(setup_kwargs):

    if sys.platform == "linux":

        plat = os.environ.get("PLAT", "")
        python_version = f"{sys.version_info.major}{sys.version_info.minor}"
        build_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"build_{python_version}_{plat}")
        cmake_args = ["-DPYTHON_EXECUTABLE=" + sys.executable]
        if not os.path.exists(build_path):
            os.makedirs(build_path)

        subprocess.check_call(["cmake", ".."] + cmake_args, cwd=build_path)
        subprocess.check_call(["cmake", "--build", "."], cwd=build_path)

    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src/cacheline/__init__.py")

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pyproject.toml")) as stream:
        data = toml.load(stream)
        version = data["tool"]["poetry"]["version"]

    suffix = ""
    with open(script, "a+") as f:
        git_hash = ""
        try:
            if os.environ.get("GIT_HASH", ""):
                git_hash = os.environ["GIT_HASH"]
            else:
                git_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()
            suffix = f"+{git_hash}"
        except Exception as e:
            logging.warning(f"Failed to get git hash: {e}")



if __name__ == "__main__":
    build({})

from pathlib import Path
from importlib import import_module
import pytest
import argparse
import inspect

root_dir = Path(__file__).parent
test_files = root_dir.glob("features/core/test_*.py")
scopes = """
features/
  core/
"""
for file in test_files:
    scopes += "    " + str(file.name) + "::\n"
    module = import_module(str(file)[str(file).find('features'):].replace("/", ".").replace(".py", ""))
    funcs = [
        func[0]
        for func in inspect.getmembers(module, inspect.isfunction)
        if func[0].startswith("test")
    ]
    for func in funcs:
        scopes += "      " + func + "\n"
helpmsg = f"""
OGC API Test Suite

Use the Scope arg to specify which tests to run.
(uses pytest scoping syntax)

The available tests are:
{scopes}
"""
parser = argparse.ArgumentParser(
    prog="ogctests",
    description=helpmsg,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument(
    "scope", type=str, help="Specify tests to run", nargs="+", default="features/core"
)
args = parser.parse_args()


paths = [str(root_dir / path) for path in args.scope]
arglist = paths + ["--no-header", "--no-summary", "-p no:warnings", "--tb=no"]
pytest.main(args=arglist)

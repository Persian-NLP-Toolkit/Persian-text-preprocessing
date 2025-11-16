# Usage Examples

This folder shows how to use `preproc-pkg` both in Python code and via the CLI.

## Install (reproducible)

```powershell
# Windows/PowerShell / Python 3.8
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r constraints/py38-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu
pip install ..\dist\preproc_pkg-0.1.0-py3-none-any.whl --no-deps

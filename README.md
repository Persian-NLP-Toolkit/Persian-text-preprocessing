# preproc-pkg

Persian preprocessing pipelines (normalize, spell, informal→formal, stopword, lemma, stem).

## Python & OS
- Python: **3.8 only** (`>=3.8,<3.9`)
- See `constraints/py38-cpu.txt` for fully pinned environment (including `torch==2.2.2+cpu`).

## Install (reproducible)
```bash
python -m venv .venv && . .venv/bin/activate
python -m pip install --upgrade pip
pip install preproc-pkg[formalizer] -c constraints/py38-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu

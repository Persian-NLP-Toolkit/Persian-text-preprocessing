# Usage Examples

This folder contains ready-to-run examples for using `preproc-pkg`.

## Prerequisites

- Python `3.8`
- Install the project package (preferably in a virtual environment)

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ..
```

If you need formalizer support:

```bash
python -m pip install "preproc-pkg[formalizer]" \
  -c ../constraints/py38-cpu.txt \
  --extra-index-url https://download.pytorch.org/whl/cpu
```

## Recommended Run Order

1. `quickstart_example.py`
2. `normalization_example.py`
3. `spell_example.py`
4. `formal_t5_example.py` (requires extra dependencies)
5. `stopword_example.py`
6. `lemma_example.py`
7. `stem_example.py`

## Run the Examples

From inside this folder:

```bash
python quickstart_example.py
python normalization_example.py
python spell_example.py
python stopword_example.py
python lemma_example.py
python stem_example.py
```

For formalizer:

```bash
python formal_t5_example.py
```

## CLI Examples

### Linux/macOS

```bash
bash cli_examples.sh
```

### Windows PowerShell

```powershell
./cli_examples.ps1
```

## Notes

- All examples use the public `create_*_pipeline` API.
- If transformer dependencies are not installed, the formal example will fail with a dependency error (expected).
- For quick text tests, use `preproc-cli` with `--text` or `--input-file`.

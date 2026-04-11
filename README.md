# preproc-pkg

Persian text preprocessing package with multiple independent pipelines:

- Normalization (`normalize`)
- Spell correction (`spell`)
- Informal-to-formal conversion (`formal`)
- Stopword removal (`stopword`)
- Lemmatization (`lemma`)
- Stemming (`stem`)

This repository is designed so each processing task has its own pipeline and can be used through both Python API and CLI.

## Python Version and Dependencies

- Python: `>=3.8,<3.9`
- Core dependencies:
  - `hazm==0.9.4`
  - `parsivar==0.2.3.1`
  - `nltk==3.9.1`
- Optional formalizer dependencies:
  - `transformers==4.41.2`
  - `torch==2.2.2+cpu`

For reproducible installs, use the pinned file at `constraints/py38-cpu.txt`.

## Installation

### 1) Base install

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2) Install with formalizer support (Transformer)

```bash
python -m pip install "preproc-pkg[formalizer]" \
  -c constraints/py38-cpu.txt \
  --extra-index-url https://download.pytorch.org/whl/cpu
```

### 3) Local project install

```bash
python -m pip install -e .
```

## Python API

All pipelines take `str` input and return `str` output (except normalizer when `return_report=True`).

```python
from preproc_pkg import (
    create_normalizer_pipeline,
    create_spell_pipeline,
    create_formal_pipeline,
    create_stopword_pipeline,
    create_lemma_pipeline,
    create_stem_pipeline,
)

text = "میخوام    آدرس www.example.com رو بفرستم؛ شماره‌اش 09123456789 ــ اوکیه؟"

norm = create_normalizer_pipeline(enable_metrics=True)
normalized, report = norm(text, return_report=True)

spell = create_spell_pipeline()
formal = create_formal_pipeline(model_name="PardisSzah/PersianTextFormalizer")
stopword = create_stopword_pipeline()
lemma = create_lemma_pipeline(prefer_past=False)
stem = create_stem_pipeline(prefer_past=False)
```

## CLI

Entry point:

```bash
preproc-cli --help
preproc-cli --version
```

### Text input precedence

For all subcommands, input is resolved in this order:

1. `--text`
2. `--input-file`
3. `stdin`

### Examples

```bash
preproc-cli normalize --text "سلام    دنیا"
preproc-cli normalize --input-file input.txt
echo "سلام دنیا" | preproc-cli normalize

preproc-cli spell --text "این ی متن ناسحیح است"
preproc-cli spell --text "متن" --use-transformer --model-name "your-seq2seq-model"

preproc-cli formal --text "میخوام برم بیرون"
preproc-cli stopword --text "این یک متن نمونه است"
preproc-cli lemma --text "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
preproc-cli stem --text "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
```

## Pipeline Details

### 1) Normalizer

`create_normalizer_pipeline(...)`

Main stages:

1. Initial cleanup (HTML/URL/Email/Mention/Hashtag/Phone/Non-BMP)
2. Pinglish conversion (optional)
3. Parsivar (optional)
4. Hazm (optional)
5. Final punctuation and spacing cleanup

Key parameters:

- `enable_parsivar`
- `enable_hazm`
- `enable_pinglish`
- `enable_metrics`
- `collapse_keep_newlines`

### 2) Spell

`create_spell_pipeline(use_parsivar=True, use_transformer=False, **kwargs)`

- If `use_transformer=True`, you must provide a valid Seq2Seq model (`model_name`).

### 3) Formal

`create_formal_pipeline(use_rules=True, **kwargs)`

- Includes rule-based + transformer steps
- Default model: `PardisSzah/PersianTextFormalizer`

### 4) Stopword

`create_stopword_pipeline(extra_stopwords=None)`

### 5) Lemma

`create_lemma_pipeline(use_hazm=True, use_parsivar=True, prefer_past=False)`

### 6) Stem

`create_stem_pipeline(use_hazm=True, use_parsivar=True, prefer_past=False)`

## Package Structure

Main paths:

- `preproc_pkg/cli.py`
- `preproc_pkg/normalizer/`
- `preproc_pkg/spell/`
- `preproc_pkg/formal/`
- `preproc_pkg/stopword/`
- `preproc_pkg/lemma/`
- `preproc_pkg/stem/`

## Usage Examples

Runnable examples are available in `usage_examples/`:

- `quickstart_example.py`
- `normalization_example.py`
- `spell_example.py`
- `formal_t5_example.py`
- `stopword_example.py`
- `lemma_example.py`
- `stem_example.py`
- `cli_examples.sh`
- `cli_examples.ps1`

## Development and Build

```bash
python -m pip install -e .
python -m pip install -r requirements.txt
```

Project file:

- `pyproject.toml`

CLI entrypoint:

- `preproc-cli = preproc_pkg.cli:main`

## Compatibility Notes

- Public API (`create_*_pipeline`) is preserved.
- Core pipeline logic has not been changed.
- Package folders were standardized to conventional names without `_pkg` suffix.
- Legacy `_pkg` module paths have been removed.

## License

See `LICENSE`.

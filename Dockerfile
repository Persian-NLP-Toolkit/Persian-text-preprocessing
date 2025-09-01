FROM python:3.8
ENV LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential git wget unzip && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip setuptools wheel

RUN python -m pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch==2.2.2+cpu

RUN python -m pip install --no-cache-dir \
    hazm==0.9.4 \
    parsivar==0.2.3.1 \
    nltk==3.9.1 \
    transformers==4.41.2

RUN python - <<'PY'
import os, urllib.request, zipfile, io, pathlib, parsivar
dst = os.path.join(os.path.dirname(parsivar.__file__), "resource", "spell")
pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
data = urllib.request.urlopen("https://www.dropbox.com/s/tlyvnzv1ha9y1kl/spell.zip?dl=1").read()
zipfile.ZipFile(io.BytesIO(data)).extractall(dst)
PY

RUN python - <<'PY'
from transformers import AutoTokenizer, T5ForConditionalGeneration
model = "PardisSzah/PersianTextFormalizer"
AutoTokenizer.from_pretrained(model)
T5ForConditionalGeneration.from_pretrained(model)
PY

WORKDIR /app
COPY preproc_pkg /app/preproc_pkg
COPY usage_examples /app/usage_examples

ENTRYPOINT ["python"]

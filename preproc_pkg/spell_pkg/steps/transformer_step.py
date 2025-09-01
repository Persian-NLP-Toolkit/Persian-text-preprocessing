from typing import Optional
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .base import SpellStep


class TransformerSpellStep(SpellStep):
    """Context-aware spell correction using a Seq2Seq model (e.g. Nevise v2)."""

    def __init__(
        self,
        model_name: str = "HooshvareLab/bert-fa-base-uncased-clf-persian-spell-correct",
        *,
        device: Optional[str] = None,
    ):
        self.tok = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        if device:
            self.model.to(device)
        self.device = device

    def apply(self, text: str) -> str:
        enc = self.tok(text, return_tensors="pt", truncation=True, max_length=256)
        if self.device:
            enc = {k: v.to(self.device) for k, v in enc.items()}
        out_ids = self.model.generate(**enc, num_beams=4, max_length=256)
        return self.tok.decode(out_ids[0], skip_special_tokens=True)

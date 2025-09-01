from typing import Optional
from transformers import T5ForConditionalGeneration, AutoTokenizer
from .base import FormalStep


class TransformerFormalStep(FormalStep):
    """Seq2Seq T5 model fine-tuned for Persian formalization."""

    def __init__(
        self,
        model_name: str = "PardisSzah/PersianTextFormalizer",
        *,
        device: Optional[str] = None,
    ):
        self.tok = AutoTokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        if device:
            self.model.to(device)
        self.device = device

    def apply(self, text: str) -> str:
        enc = self.tok(
            "informal: " + text, return_tensors="pt", truncation=True, max_length=256
        )
        if self.device:
            enc = {k: v.to(self.device) for k, v in enc.items()}
        out_ids = self.model.generate(**enc, num_beams=4, max_length=256)
        return self.tok.decode(out_ids[0], skip_special_tokens=True)

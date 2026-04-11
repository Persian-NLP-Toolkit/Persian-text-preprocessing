from typing import Optional, Dict
import torch
from .base import FormalStep
from ..._hf_cache import load_t5


class TransformerFormalStep(FormalStep):
    """
    Seq2Seq T5 model fine-tuned for Persian formalization.

    Parameters
    ----------
    model_name : str
        HuggingFace model id (must be a Seq2Seq model).
    device : Optional[str]
        e.g. 'cuda:0' or 'cpu'. If None, keep model on default device.
    generate_kwargs : Optional[Dict]
        Extra kwargs passed to `model.generate` (e.g., num_beams, max_new_tokens).

    Notes
    -----
    Tokenizer/model are cached process-locally (see _hf_cache.load_t5).
    """

    def __init__(
        self,
        model_name: str = "PardisSzah/PersianTextFormalizer",
        *,
        device: Optional[str] = None,
        generate_kwargs: Optional[Dict] = None,
    ):
        # Load from shared cache per (model, device)
        dev = device or "cpu"
        self.tok, self.model = load_t5(model_name, dev)
        self.device = dev
        self._gen = {"num_beams": 4, "max_new_tokens": 128}
        if generate_kwargs:
            self._gen.update(generate_kwargs)

    def apply(self, text: str) -> str:
        enc = self.tok(
            "informal: " + text, return_tensors="pt", truncation=True, max_length=256
        )
        # Move inputs only if not on CPU
        if self.device and self.device != "cpu":
            enc = {k: v.to(self.device) for k, v in enc.items()}
        with torch.no_grad():
            out_ids = self.model.generate(**enc, **self._gen)
        return self.tok.decode(out_ids[0], skip_special_tokens=True)

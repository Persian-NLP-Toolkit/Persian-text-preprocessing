import argparse
import importlib.util
import sys
from pathlib import Path
from typing import Callable, List
from . import (
    create_normalizer_pipeline,
    create_spell_pipeline,
    create_formal_pipeline,
    create_stopword_pipeline,
    create_lemma_pipeline,
    create_stem_pipeline,
)

try:
    from . import __version__ as _PKG_VERSION
except Exception:
    _PKG_VERSION = "0.0.0"


def _read_text(args) -> str:
    """Read input text from --text, --input-file, or stdin (in this order)."""
    if args.text is not None:
        return args.text
    if getattr(args, "input_file", None):
        return Path(args.input_file).read_text(encoding="utf-8")
    return sys.stdin.read()


def _require_transformers_or_exit():
    """Validate optional transformer dependencies and exit with install guidance."""
    if (
        importlib.util.find_spec("transformers") is None
        or importlib.util.find_spec("torch") is None
    ):
        msg = (
            "  python -m pip install preproc-pkg[formalizer] "
            "-c constraints/py38-cpu.txt "
            "--extra-index-url https://download.pytorch.org/whl/cpu"
        )
        print(msg, file=sys.stderr)
        raise SystemExit(2)


def cmd_normalize(args):
    """Run the normalization pipeline and print text (and optional metrics)."""
    pipe = create_normalizer_pipeline(
        enable_metrics=args.metrics,
        enable_parsivar=not args.no_parsivar,
        enable_hazm=not args.no_hazm,
    )
    out = pipe(_read_text(args), return_report=args.metrics)
    if args.metrics:
        text, rep = out
        print(text)
        print("\n--- METRICS ---")
        print(rep)
    else:
        print(out)


def cmd_spell(args):
    """Run spell-correction pipeline and print corrected output."""
    kw = {"use_parsivar": not args.no_parsivar}
    if args.use_transformer:
        _require_transformers_or_exit()
        kw["use_transformer"] = True
        kw["model_name"] = args.model_name
    pipe = create_spell_pipeline(**kw)
    print(pipe(_read_text(args)))


def cmd_formal(args):
    """Run informal-to-formal conversion using transformer step."""
    _require_transformers_or_exit()
    pipe = create_formal_pipeline(model_name=args.model_name)
    print(pipe(_read_text(args)))


def cmd_stopword(args):
    """Run stopword-removal pipeline and print output."""
    pipe = create_stopword_pipeline()
    print(pipe(_read_text(args)))


def cmd_lemma(args):
    """Run lemmatization pipeline and print output."""
    pipe = create_lemma_pipeline(
        use_hazm=not args.no_hazm,
        use_parsivar=not args.no_parsivar,
        prefer_past=args.prefer_past,
    )
    print(pipe(_read_text(args)))


def cmd_stem(args):
    """Run stemming pipeline and print output."""
    pipe = create_stem_pipeline(
        use_hazm=not args.no_hazm,
        use_parsivar=not args.no_parsivar,
        prefer_past=args.prefer_past,
    )
    print(pipe(_read_text(args)))


def _add_common_text_input_flags(parser: argparse.ArgumentParser) -> None:
    """Attach shared text-input flags to a sub-command parser."""
    parser.add_argument(
        "--text",
        type=str,
        help="Input text. If omitted, --input-file is used, otherwise stdin.",
    )
    parser.add_argument(
        "--input-file",
        type=str,
        help="Path to a UTF-8 text file as input.",
    )


def _build_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI argument parser."""
    p = argparse.ArgumentParser(
        prog="preproc-cli", description="Persian NLP Preprocessing CLI"
    )

    # --version
    p.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {_PKG_VERSION}",
        help="View the version of the package",
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("normalize", help="Run the normalizer pipeline")
    _add_common_text_input_flags(sp)
    sp.add_argument("--metrics", action="store_true", help="Print per-step metrics")
    sp.add_argument("--no-parsivar", action="store_true", help="Disable Parsivar stage")
    sp.add_argument("--no-hazm", action="store_true", help="Disable Hazm stage")
    sp.set_defaults(func=cmd_normalize)

    sp = sub.add_parser("spell", help="Run spell-correction pipeline")
    _add_common_text_input_flags(sp)
    sp.add_argument("--no-parsivar", action="store_true", help="Disable Parsivar step")
    sp.add_argument(
        "--use-transformer", action="store_true", help="Enable transformer step"
    )
    sp.add_argument(
        "--model-name",
        type=str,
        default="",
        help="Seq2Seq model name for transformer step",
    )
    sp.set_defaults(func=cmd_spell)

    sp = sub.add_parser("formal", help="Convert informal -> formal")
    _add_common_text_input_flags(sp)
    sp.add_argument(
        "--model-name", type=str, default="PardisSzah/PersianTextFormalizer"
    )
    sp.set_defaults(func=cmd_formal)

    sp = sub.add_parser("stopword", help="Remove stopwords")
    _add_common_text_input_flags(sp)
    sp.set_defaults(func=cmd_stopword)

    sp = sub.add_parser("lemma", help="Lemmatize")
    _add_common_text_input_flags(sp)
    sp.add_argument("--no-hazm", action="store_true")
    sp.add_argument("--no-parsivar", action="store_true")
    sp.add_argument("--prefer-past", action="store_true")
    sp.set_defaults(func=cmd_lemma)

    sp = sub.add_parser("stem", help="Stem")
    _add_common_text_input_flags(sp)
    sp.add_argument("--no-hazm", action="store_true")
    sp.add_argument("--no-parsivar", action="store_true")
    sp.add_argument("--prefer-past", action="store_true")
    sp.set_defaults(func=cmd_stem)

    return p


def main(argv: List[str] = None):
    """CLI entry point."""
    p = _build_parser()

    args = p.parse_args(argv)
    func: Callable = args.func
    func(args)


if __name__ == "__main__":
    main()

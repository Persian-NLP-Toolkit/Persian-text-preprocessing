import argparse
import sys
from typing import List
from . import (
    create_normalizer_pipeline,
    create_spell_pipeline,
    create_formal_pipeline,
    create_stopword_pipeline,
    create_lemma_pipeline,
    create_stem_pipeline,
)


def _read_text(args) -> str:
    if args.text is not None:
        return args.text
    return sys.stdin.read()


def cmd_normalize(args):
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
    kw = {"use_parsivar": not args.no_parsivar}
    if args.use_transformer:
        kw["use_transformer"] = True
        kw["model_name"] = args.model_name
    pipe = create_spell_pipeline(**kw)
    print(pipe(_read_text(args)))


def cmd_formal(args):
    pipe = create_formal_pipeline(model_name=args.model_name)
    print(pipe(_read_text(args)))


def cmd_stopword(args):
    pipe = create_stopword_pipeline()
    print(pipe(_read_text(args)))


def cmd_lemma(args):
    pipe = create_lemma_pipeline(
        use_hazm=not args.no_hazm,
        use_parsivar=not args.no_parsivar,
        prefer_past=args.prefer_past,
    )
    print(pipe(_read_text(args)))


def cmd_stem(args):
    pipe = create_stem_pipeline(
        use_hazm=not args.no_hazm,
        use_parsivar=not args.no_parsivar,
        prefer_past=args.prefer_past,
    )
    print(pipe(_read_text(args)))


def main(argv: List[str] = None):
    p = argparse.ArgumentParser(
        prog="preproc-cli", description="Persian NLP Preprocessing CLI"
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("normalize", help="Run the normalizer pipeline")
    sp.add_argument("--text", type=str, help="Input text (default: stdin)")
    sp.add_argument("--metrics", action="store_true", help="Print per-step metrics")
    sp.add_argument("--no-parsivar", action="store_true", help="Disable Parsivar stage")
    sp.add_argument("--no-hazm", action="store_true", help="Disable Hazm stage")
    sp.set_defaults(func=cmd_normalize)

    sp = sub.add_parser("spell", help="Run spell-correction pipeline")
    sp.add_argument("--text", type=str, help="Input text (default: stdin)")
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
    sp.add_argument("--text", type=str, help="Input text (default: stdin)")
    sp.add_argument(
        "--model-name", type=str, default="PardisSzah/PersianTextFormalizer"
    )
    sp.set_defaults(func=cmd_formal)

    sp = sub.add_parser("stopword", help="Remove stopwords")
    sp.add_argument("--text", type=str, help="Input text (default: stdin)")
    sp.set_defaults(func=cmd_stopword)

    sp = sub.add_parser("lemma", help="Lemmatize")
    sp.add_argument("--text", type=str, help="Input text (default: stdin)")
    sp.add_argument("--no-hazm", action="store_true")
    sp.add_argument("--no-parsivar", action="store_true")
    sp.add_argument("--prefer-past", action="store_true")
    sp.set_defaults(func=cmd_lemma)

    sp = sub.add_parser("stem", help="Stem")
    sp.add_argument("--text", type=str, help="Input text (default: stdin)")
    sp.add_argument("--no-hazm", action="store_true")
    sp.add_argument("--no-parsivar", action="store_true")
    sp.add_argument("--prefer-past", action="store_true")
    sp.set_defaults(func=cmd_stem)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()

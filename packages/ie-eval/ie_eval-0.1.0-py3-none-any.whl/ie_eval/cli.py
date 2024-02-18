"""Command Line Arguments"""

import argparse
from pathlib import Path

from ie_eval.metrics.bag_of_entities import (
    compute_bag_of_entities,
    compute_bag_of_tagged_words,
    compute_bag_of_words,
)
from ie_eval.metrics.utils import compute_all_metrics


def add_bow_parser(commands):
    """Add parser for the bag-of-words computation subcommand."""
    parser = commands.add_parser(
        "bow",
        help="Compute bag-of-entities metrics.",
    )
    parser.set_defaults(func=compute_bag_of_words)
    parser.add_argument(
        "--label-dir",
        "-l",
        type=Path,
        required=True,
        help="Path to the directory containing BIO label files.",
    )
    parser.add_argument(
        "--prediction-dir",
        "-p",
        type=Path,
        required=True,
        help="Path to the directory containing BIO prediction files.",
    )
    parser.add_argument(
        "--by-category",
        "-c",
        action="store_true",
        help="Whether to compute scores for each semantic category.",
    )


def add_botw_parser(commands):
    """Add parser for the bag-of-tagged-words computation subcommand."""
    parser = commands.add_parser(
        "botw",
        help="Compute bag-of-tagged-words metrics.",
    )
    parser.set_defaults(func=compute_bag_of_tagged_words)
    parser.add_argument(
        "--label-dir",
        "-l",
        type=Path,
        required=True,
        help="Path to the directory containing BIO label files.",
    )
    parser.add_argument(
        "--prediction-dir",
        "-p",
        type=Path,
        required=True,
        help="Path to the directory containing BIO prediction files.",
    )
    parser.add_argument(
        "--by-category",
        "-c",
        action="store_true",
        help="Whether to compute scores for each semantic category.",
    )


def add_boe_parser(commands):
    """Add parser for the bag-of-entities computation subcommand."""
    parser = commands.add_parser(
        "boe",
        help="Compute bag-of-entities metrics.",
    )
    parser.set_defaults(func=compute_bag_of_entities)
    parser.add_argument(
        "--label-dir",
        "-l",
        type=Path,
        required=True,
        help="Path to the directory containing BIO label files.",
    )
    parser.add_argument(
        "--prediction-dir",
        "-p",
        type=Path,
        required=True,
        help="Path to the directory containing BIO prediction files.",
    )
    parser.add_argument(
        "--by-category",
        "-c",
        action="store_true",
        help="Whether to compute scores for each semantic category.",
    )


def add_summary_parser(commands):
    """Add parser subcommand to compute all metrics."""
    parser = commands.add_parser(
        "all",
        help="Compute all metrics.",
    )
    parser.set_defaults(func=compute_all_metrics)
    parser.add_argument(
        "--label-dir",
        "-l",
        type=Path,
        required=True,
        help="Path to the directory containing BIO label files.",
    )
    parser.add_argument(
        "--prediction-dir",
        "-p",
        type=Path,
        required=True,
        help="Path to the directory containing BIO prediction files.",
    )
    parser.add_argument(
        "--by-category",
        "-c",
        action="store_true",
        help="Whether to compute scores for each semantic category.",
    )


def main():
    parser = argparse.ArgumentParser(
        prog="ie-eval",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    commands = parser.add_subparsers(
        help="Available metrics to evaluate IE models.",
    )
    add_bow_parser(commands)
    add_botw_parser(commands)
    add_boe_parser(commands)
    add_summary_parser(commands)

    args = vars(parser.parse_args())
    if "func" in args:
        args.pop("func")(**args)
    else:
        parser.print_help()

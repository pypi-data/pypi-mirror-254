"""Compute the bag-of-words/bag-of-tagged-words/bag-of-entities metrics from a label/prediction dataset."""

import logging
from collections import defaultdict
from enum import Enum

from bio_parser import GLOBAL_STAT_NAME
from bio_parser.parse.document import Document
from bio_parser.utils import load_dataset
from prettytable import PrettyTable

from ie_eval.scorer import (
    BagOfWords,
    MicroAverageErrorRate,
    MicroAverageFScore,
)
from ie_eval.table_formatter import make_bag_of_entities_prettytable

logger = logging.getLogger(__name__)


class WordType(Enum):
    """Word Type."""

    word = "word"
    tagged_word = "tagged_word"
    entity = "entity"


def prepare_word_list(document: Document) -> dict[str, list[str]]:
    """Get list of words (overall and by category).

    Args:
        document (Document): An input document.

    Returns:
        A dictionary with categories as keys and corresponding list of words as values.
    """
    words = defaultdict(list)
    for category, text in document.word_entities:
        words[category].append(text)
        words[GLOBAL_STAT_NAME].append(text)
    return words


def prepare_tagged_word_list(document: Document) -> dict[str, list[tuple[str, str]]]:
    """Get list of tagged words (overall and by category).

    Args:
        document (Document): An input document.

    Returns:
        A dictionary with categories as keys and corresponding list of tagged words as values.
    """
    words = defaultdict(list)
    for category, text in document.word_entities:
        words[category].append((category, text))
        words[GLOBAL_STAT_NAME].append((category, text))
    return words


def prepare_tagged_entity_list(document: Document) -> dict[str, list[tuple[str, str]]]:
    """Get list of tagged entities/fields (overall and by category).

    Args:
        document (Document): An input document.

    Returns:
        A dictionary with categories as keys and corresponding list of tagged entities as values.
    """
    words = defaultdict(list)
    for category, text in document.entities:
        words[category].append((category, text))
        words[GLOBAL_STAT_NAME].append((category, text))
    return words


def tokenize_entities(
    label: Document,
    prediction: Document,
    word_type: WordType,
) -> tuple[
    dict[str, list[str | tuple[str, str]]],
    dict[str, list[str | tuple[str, str]]],
]:
    """Prepare label and prediction for BagOfWord computation.

    Args:
        label (Document): the label document
        prediction (Document): the prediction document
        word_type (WordType): Whether to consider a list of words, list tagged words, or list of tagged entities.

    Returns:
        a label dictionary with categories as keys and corresponding list of words, tagged words or tagged entities as values.
        a prediction dictionary with categories as keys and corresponding list of words, tagged words or tagged entities as values.
    """
    match word_type:
        case WordType.word:
            # Return list of words
            return (prepare_word_list(label), prepare_word_list(prediction))
        case WordType.tagged_word:
            # Return list of tagged words
            return (
                prepare_tagged_word_list(label),
                prepare_tagged_word_list(prediction),
            )
        case _:
            # Return list of tagged entities
            return (
                prepare_tagged_entity_list(label),
                prepare_tagged_entity_list(prediction),
            )


def compute_bag_of_anything(
    dataset: list[tuple[Document, Document]],
    by_category: bool = False,
    word_type: str = WordType.word,
    print_table: bool = True,
) -> PrettyTable:
    """Compute bag-of-words, bag-of-tagged-words, or bag-of-entities.

    Args:
        dataset (list[tuple[Document, Document]]): a dataset containing a list of tuple with the label and corresponding prediction.
        word_type (WordType): Type of words to use for bag-of-words computation.
        by_category (bool, optional): Whether to compute the metric globally or for each category. Defaults to False.
        print_table (bool, optional): Whether to print the table. Defaults to True.

    Returns:
        PrettyTable: The evaluation table formatted in Markdown.
    """
    # Initialize scores
    total_score_f1 = MicroAverageFScore()
    total_score_err = MicroAverageErrorRate()

    # Iterate over the dataset
    for label, prediction in dataset:
        # Compute scores
        categories = {entity for entity, _word in label.word_entities}
        label_list, prediction_list = tokenize_entities(
            label,
            prediction,
            word_type=word_type,
        )

        score = BagOfWords(
            labels=label_list[GLOBAL_STAT_NAME],
            predictions=prediction_list[GLOBAL_STAT_NAME],
        )

        # Micro average
        total_score_f1.update(GLOBAL_STAT_NAME, score)
        total_score_err.update(GLOBAL_STAT_NAME, score)

        # Compute bag-of-tagged words by category
        if not by_category:
            continue

        for category in categories:
            # Compute scores
            category_score = BagOfWords(
                label_list.get(category, []),
                prediction_list.get(category, []),
            )

            # Micro average
            total_score_err.update(category, category_score)
            total_score_f1.update(category, category_score)

    # Format and display results
    table = make_bag_of_entities_prettytable(
        errors=total_score_err,
        detections=total_score_f1,
    )
    if print_table:
        print(table)  # noqa: T201
    return table


def compute_bag_of_words(
    label_dir: Document,
    prediction_dir: Document,
    by_category: bool = False,
) -> PrettyTable:
    """Compute bag-of-words.

    Args:
        label_dir (Path): Path to the label directory.
        prediction_dir (Path): Path to the prediction directory.
        by_category (bool, optional): Whether to compute the metric globally or for each category. Defaults to False.

    Returns:
        PrettyTable: The evaluation table formatted in Markdown.
    """
    return compute_bag_of_anything(
        load_dataset(label_dir=label_dir, prediction_dir=prediction_dir),
        by_category=by_category,
        word_type=WordType.word,
    )


def compute_bag_of_tagged_words(
    label_dir: Document,
    prediction_dir: Document,
    by_category: bool = False,
) -> PrettyTable:
    """Compute bag-of-tagged-words.

    Args:
        label_dir (Path): Path to the label directory.
        prediction_dir (Path): Path to the prediction directory.
        by_category (bool, optional): Whether to compute the metric globally or for each category. Defaults to False.

    Returns:
        PrettyTable: The evaluation table formatted in Markdown.
    """
    return compute_bag_of_anything(
        load_dataset(label_dir=label_dir, prediction_dir=prediction_dir),
        by_category=by_category,
        word_type=WordType.tagged_word,
    )


def compute_bag_of_entities(
    label_dir: Document,
    prediction_dir: Document,
    by_category: bool = False,
) -> PrettyTable:
    """Compute bag-of-entities.

    Args:
        label_dir (Path): Path to the label directory.
        prediction_dir (Path): Path to the prediction directory.
        by_category (bool, optional): Whether to compute the metric globally or for each category. Defaults to False.

    Returns:
        PrettyTable: The evaluation table formatted in Markdown.
    """
    return compute_bag_of_anything(
        load_dataset(label_dir=label_dir, prediction_dir=prediction_dir),
        by_category=by_category,
        word_type=WordType.entity,
    )

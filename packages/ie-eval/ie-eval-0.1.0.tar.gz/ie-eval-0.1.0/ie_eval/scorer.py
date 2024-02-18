"""Scorer."""
from collections import Counter, defaultdict
from typing import NamedTuple

import numpy as np


class BagOfWords(NamedTuple):
    """Base class for bag-of-word metrics. Extension of bWER defined in End-to-End Page-Level Assessment of Handwritten Text Recognition (https://arxiv.org/pdf/2301.05935.pdf)."""

    labels: list[str | tuple[str, str]]
    predictions: list[str | tuple[str, str]]

    @property
    def label_counter(self) -> Counter[str]:
        """Split the label into a list of words."""
        return Counter(self.labels)

    @property
    def prediction_counter(self) -> Counter[str]:
        """Split the prediction into a list of words."""
        return Counter(self.predictions)

    @property
    def true_positives(self) -> int:
        """Count true positive words."""
        return sum((self.label_counter & self.prediction_counter).values())

    @property
    def false_positives(self) -> int:
        """Count false positive words."""
        return sum((self.prediction_counter - self.label_counter).values())

    @property
    def false_negatives(self) -> int:
        """Count false negatives words."""
        return sum((self.label_counter - self.prediction_counter).values())

    @property
    def all_words(self) -> list[str | tuple[str, str]]:
        """All tagged words."""
        return sorted(set(self.labels + self.predictions))

    @property
    def label_word_vector(self) -> np.array:
        """Iterate over the set of tagged words and count occurrences in the label."""
        return np.array(
            [self.labels.count(w) for w in self.all_words],
        )

    @property
    def prediction_word_vector(self) -> np.array:
        """Iterate over the set of words and count occurrences in the prediction."""
        return np.array(
            [self.predictions.count(word) for word in self.all_words],
        )

    @property
    def insertions_deletions(self) -> int:
        """Count unavoidable insertions and deletions. See Equation 8 from https://arxiv.org/pdf/2301.05935.pdf."""
        return abs(len(self.labels) - len(self.predictions))

    @property
    def substitutions(self) -> int:
        """Count substitutions. See Equation 8 from https://arxiv.org/pdf/2301.05935.pdf."""
        return (
            np.absolute(self.prediction_word_vector - self.label_word_vector).sum()
            - self.insertions_deletions
        ) / 2

    @property
    def errors(self) -> int:
        """Count total number of errors."""
        return self.substitutions + self.insertions_deletions


class MicroAverageErrorRate:
    """Compute total error rates."""

    def __init__(self) -> None:
        """Initialize errors and counts.

        Examples:
            >>> score = MicroAverageErrorRate()
        """
        self.label_word_count = defaultdict(int)
        self.error_count = defaultdict(int)
        self.count = defaultdict(int)

    def update(self, key: str, score: BagOfWords) -> None:
        """Update the score with the current evaluation for a given key.

        Args:
            key (str): Category to update.
            score (TextEval): Current score.

        Examples:
            >>> score.update("total", [("person", "Georges"), ("person", "Washington")])
        """
        self.label_word_count[key] += len(score.labels)
        self.count[key] += 1
        self.error_count[key] += score.errors

    @property
    def error_rate(self) -> dict[str, float]:
        """Error rate for each key."""
        return {
            key: min(100 * self.error_count[key] / self.label_word_count[key], 100)
            for key in self.label_word_count
        }

    @property
    def categories(self) -> list[str]:
        """Get all categories in the label."""
        return list(self.label_word_count.keys())


class MicroAverageFScore:
    """Compute total precision, recall, and f1 scores."""

    def __init__(self) -> None:
        """Initialize error counts.

        Examples:
            >>> score = MicroAverageFScore()
        """
        self.label_word_count = defaultdict(int)
        self.count = defaultdict(int)
        self.true_positives = defaultdict(int)
        self.false_positives = defaultdict(int)
        self.false_negatives = defaultdict(int)

    def update(self, key: str, score: BagOfWords) -> None:
        """Update the score with the current evaluation for a given key.

        Args:
            key (str): Category to update.
            score (BagOfWords): Current score.

        Examples:
            >>> score.update("total", BagOfWords(label.entities, pred.entities))
        """
        self.label_word_count[key] += len(score.labels)
        self.count[key] += 1
        self.true_positives[key] += score.true_positives
        self.false_positives[key] += score.false_positives
        self.false_negatives[key] += score.false_negatives

    @staticmethod
    def _recall_score(true_positives: int, false_negatives: int) -> float:
        """Compute the recall."""
        return (
            100 * true_positives / (true_positives + false_negatives)
            if true_positives + false_negatives > 0
            else 100
        )

    @staticmethod
    def _precision_score(true_positives: int, true_negatives: int) -> float:
        """Compute the precision."""
        return (
            100 * true_positives / (true_positives + true_negatives)
            if true_positives + true_negatives > 0
            else 100
        )

    @staticmethod
    def _f1_score(precision: float, recall: float) -> float:
        """Compute the F1 score."""
        return (
            2 * precision * recall / (precision + recall)
            if precision + recall > 0
            else 0
        )

    @property
    def recall(self) -> dict[str, float]:
        """Recall score for each key."""
        return {
            key: self._recall_score(self.true_positives[key], self.false_negatives[key])
            for key in self.count
        }

    @property
    def precision(self) -> dict[str, float]:
        """Precision score for each key."""
        return {
            key: self._precision_score(
                self.true_positives[key],
                self.false_positives[key],
            )
            for key in self.count
        }

    @property
    def f1_score(self) -> dict[str, float]:
        """F1 score for each key."""
        return {
            key: self._f1_score(self.precision[key], self.recall[key])
            for key in self.count
        }

    @property
    def categories(self) -> list[str]:
        """Get all categories in the label."""
        return list(self.label_word_count.keys())

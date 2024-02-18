"""Computing CER/WER."""

import numpy as np
import pytest
from bio_parser import GLOBAL_STAT_NAME
from ie_eval.metrics.bag_of_entities import (
    compute_bag_of_entities,
    compute_bag_of_tagged_words,
    compute_bag_of_words,
)
from ie_eval.scorer import (
    BagOfWords,
    MicroAverageErrorRate,
    MicroAverageFScore,
)
from ie_eval.table_formatter import make_bag_of_entities_prettytable
from prettytable import PrettyTable

from tests import FIXTURES


@pytest.mark.parametrize(
    (
        "labels",
        "predictions",
        "expected_all_words",
        "expected_label_vector",
        "expected_prediction_vector",
        "expected_insertions_deletions",
        "expected_substitutions",
        "expected_errors",
    ),
    [
        (
            ["Georges", "Washington", "cat"],
            ["Georg", "Washington", "cat"],
            ["Georg", "Georges", "Washington", "cat"],
            np.array([0, 1, 1, 1], dtype=int),
            np.array([1, 0, 1, 1], dtype=int),
            0,
            1,
            1,
        ),
        (
            ["Georges", "Washington", "cat"],
            ["Georges", "Washington"],
            ["Georges", "Washington", "cat"],
            np.array([1, 1, 1], dtype=int),
            np.array([1, 1, 0], dtype=int),
            1,
            0,
            1,
        ),
        (
            ["Georges", "Washington", "cat"],
            ["Georg", "Washington"],
            ["Georg", "Georges", "Washington", "cat"],
            np.array([0, 1, 1, 1], dtype=int),
            np.array([1, 0, 1, 0], dtype=int),
            1,
            1,
            2,
        ),
    ],
)
def test_bag_of_words_eval(
    labels,
    predictions,
    expected_all_words,
    expected_label_vector,
    expected_prediction_vector,
    expected_insertions_deletions,
    expected_substitutions,
    expected_errors,
):
    score = BagOfWords(labels, predictions)
    assert score.all_words == expected_all_words
    np.testing.assert_equal(score.label_word_vector, expected_label_vector)
    np.testing.assert_equal(score.prediction_word_vector, expected_prediction_vector)
    assert score.insertions_deletions == expected_insertions_deletions
    assert score.substitutions == expected_substitutions
    assert score.errors == expected_errors


@pytest.mark.parametrize(
    (
        "labels",
        "predictions",
        "expected_all_words",
        "expected_label_vector",
        "expected_prediction_vector",
        "expected_insertions_deletions",
        "expected_substitutions",
        "expected_errors",
    ),
    [
        (
            [("person", "Georges"), ("person", "Washington"), ("animal", "cat")],
            [("person", "Georg"), ("person", "Washington"), ("animal", "cat")],
            [
                ("animal", "cat"),
                ("person", "Georg"),
                ("person", "Georges"),
                ("person", "Washington"),
            ],
            np.array([1, 0, 1, 1], dtype=int),
            np.array([1, 1, 0, 1], dtype=int),
            0,
            1,
            1,
        ),
        (
            [("person", "Georges"), ("person", "Washington"), ("animal", "cat")],
            [("person", "Georges"), ("person", "Washington")],
            [("animal", "cat"), ("person", "Georges"), ("person", "Washington")],
            np.array([1, 1, 1], dtype=int),
            np.array([0, 1, 1], dtype=int),
            1,
            0,
            1,
        ),
        (
            [("person", "Georges"), ("person", "Washington"), ("animal", "cat")],
            [("person", "Georg"), ("animal", "Washington")],
            [
                ("animal", "Washington"),
                ("animal", "cat"),
                ("person", "Georg"),
                ("person", "Georges"),
                ("person", "Washington"),
            ],
            np.array([0, 1, 0, 1, 1], dtype=int),
            np.array([1, 0, 1, 0, 0], dtype=int),
            1,
            2,
            3,
        ),
    ],
)
def test_bag_of_tagged_words_eval(
    labels,
    predictions,
    expected_all_words,
    expected_label_vector,
    expected_prediction_vector,
    expected_insertions_deletions,
    expected_substitutions,
    expected_errors,
):
    score = BagOfWords(labels, predictions)
    assert score.all_words == expected_all_words
    np.testing.assert_equal(score.label_word_vector, expected_label_vector)
    np.testing.assert_equal(score.prediction_word_vector, expected_prediction_vector)
    assert score.insertions_deletions == expected_insertions_deletions
    assert score.substitutions == expected_substitutions
    assert score.errors == expected_errors


@pytest.mark.parametrize(
    (
        "labels",
        "predictions",
        "expected_all_words",
        "expected_label_vector",
        "expected_prediction_vector",
        "expected_insertions_deletions",
        "expected_substitutions",
        "expected_errors",
    ),
    [
        (
            [("person", "Georges Washington"), ("animal", "a fish called Wanda")],
            [("person", "Georges Washington"), ("animal", "a fish called Wanda")],
            [("animal", "a fish called Wanda"), ("person", "Georges Washington")],
            np.array([1, 1], dtype=int),
            np.array([1, 1], dtype=int),
            0,
            0,
            0,
        ),
        (
            [("person", "Georges Washington"), ("animal", "a fish called Wanda")],
            [("person", "Georges Washingtonn"), ("animal", "a fish called Wanda")],
            [
                ("animal", "a fish called Wanda"),
                ("person", "Georges Washington"),
                ("person", "Georges Washingtonn"),
            ],
            np.array([1, 1, 0], dtype=int),
            np.array([1, 0, 1], dtype=int),
            0,
            1,
            1,
        ),
        (
            [("person", "Georges Washington"), ("animal", "a fish called Wanda")],
            [("object", "Georges Washington"), ("animal", "a fish called Wanda")],
            [
                ("animal", "a fish called Wanda"),
                ("object", "Georges Washington"),
                ("person", "Georges Washington"),
            ],
            np.array([1, 0, 1], dtype=int),
            np.array([1, 1, 0], dtype=int),
            0,
            1,
            1,
        ),
        (
            [
                ("person", "Georges Washington"),
                ("person", "Hari Seldon"),
                ("animal", "a fish called Wanda"),
            ],
            [("person", "Hari Seldon"), ("animal", "a fish called Wanda")],
            [
                ("animal", "a fish called Wanda"),
                ("person", "Georges Washington"),
                ("person", "Hari Seldon"),
            ],
            np.array([1, 1, 1], dtype=int),
            np.array([1, 0, 1], dtype=int),
            1,
            0,
            1,
        ),
        (
            [
                ("person", "Georges Washington"),
                ("person", "Hari Seldon"),
                ("animal", "a fish called Wanda"),
            ],
            [("person", "Hari Seldon"), ("animal", "fish called Wanda")],
            [
                ("animal", "a fish called Wanda"),
                ("animal", "fish called Wanda"),
                ("person", "Georges Washington"),
                ("person", "Hari Seldon"),
            ],
            np.array([1, 0, 1, 1], dtype=int),
            np.array([0, 1, 0, 1], dtype=int),
            1,
            1,
            2,
        ),
    ],
)
def test_bag_of_entities_eval(
    labels,
    predictions,
    expected_all_words,
    expected_label_vector,
    expected_prediction_vector,
    expected_insertions_deletions,
    expected_substitutions,
    expected_errors,
):
    score = BagOfWords(labels, predictions)
    assert score.all_words == expected_all_words
    np.testing.assert_equal(score.label_word_vector, expected_label_vector)
    np.testing.assert_equal(score.prediction_word_vector, expected_prediction_vector)
    assert score.insertions_deletions == expected_insertions_deletions
    assert score.substitutions == expected_substitutions
    assert score.errors == expected_errors


@pytest.mark.parametrize(
    (
        "error_count",
        "true_positives",
        "false_positives",
        "false_negatives",
        "label_count",
        "count",
        "expected_table",
    ),
    [
        (
            {"per": 2, "date": 0, GLOBAL_STAT_NAME: 2},
            {"per": 10, "date": 20, GLOBAL_STAT_NAME: 30},
            {"per": 1, "date": 0, GLOBAL_STAT_NAME: 1},
            {"per": 1, "date": 0, GLOBAL_STAT_NAME: 1},
            {"per": 12, "date": 20, GLOBAL_STAT_NAME: 22},
            {"per": 5, "date": 5, GLOBAL_STAT_NAME: 5},
            """| Category | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:---------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| date     |   0.00   |     100.00    |   100.00   | 100.00 |      20 |           5 |
| per      |  16.67   |     90.91     |   90.91    | 90.91  |      12 |           5 |
| total    |   9.09   |     96.77     |   96.77    | 96.77  |      22 |           5 |""",
        ),
    ],
)
def test_make_pretty_table(
    error_count,
    true_positives,
    false_positives,
    false_negatives,
    label_count,
    count,
    expected_table,
) -> None:
    err_scores = MicroAverageErrorRate()
    err_scores.error_count = error_count
    err_scores.label_word_count = label_count
    err_scores.count = count
    det_scores = MicroAverageFScore()
    det_scores.true_positives = true_positives
    det_scores.false_positives = false_positives
    det_scores.false_negatives = false_negatives
    det_scores.label_word_count = label_count
    det_scores.count = count
    table = make_bag_of_entities_prettytable(detections=det_scores, errors=err_scores)
    assert isinstance(table, PrettyTable)
    assert table.field_names == [
        "Category",
        "bWER (%)",
        "Precision (%)",
        "Recall (%)",
        "F1 (%)",
        "N words",
        "N documents",
    ]
    assert table.get_string(sortby="Category") == expected_table


@pytest.mark.parametrize(
    (
        "label_dir",
        "prediction_dir",
        "shuffled_prediction_dir",
        "by_category",
        "expected_table",
    ),
    [
        (
            FIXTURES / "labels",
            FIXTURES / "predictions",
            FIXTURES / "shuffled_predictions",
            True,
            """| Category                | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:------------------------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| birth_date              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| cote_article            |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| cote_serie              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| fac                     |  80.00   |     100.00    |   20.00    | 33.33  |       5 |           1 |
| firstname               |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| gpe                     |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| husband_location        |   0.00   |     100.00    |   100.00   | 100.00 |       4 |           1 |
| husband_name            |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| husband_occupation      |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| husband_surname         |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| intitule                |  25.00   |     75.00     |   75.00    | 75.00  |      16 |           1 |
| link                    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| location_of_birth       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| norp                    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| ordinal                 |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| per                     |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| precisions_sur_cote     |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| surname                 |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| time                    |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| total                   |  25.45   |     81.48     |   80.00    | 80.73  |      55 |           5 |
| wife_name               |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wife_state              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_location   |   0.00   |     100.00    |   100.00   | 100.00 |       5 |           1 |
| wifes_father_name       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_occupation |   0.00   |     100.00    |   100.00   | 100.00 |       3 |           1 |
| wifes_father_surname    |   0.00   |     100.00    |   100.00   | 100.00 |       2 |           1 |
| wifes_mother_name       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |""",
        ),
        (
            FIXTURES / "labels",
            FIXTURES / "predictions",
            FIXTURES / "shuffled_predictions",
            False,
            """| Category | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:---------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| total    |  25.45   |     81.48     |   80.00    | 80.73  |      55 |           5 |""",
        ),
    ],
)
def test_compute_bag_of_words(
    label_dir,
    prediction_dir,
    shuffled_prediction_dir,
    by_category,
    expected_table,
):
    table = compute_bag_of_words(label_dir, prediction_dir, by_category)
    table_shuffled = compute_bag_of_words(
        label_dir,
        shuffled_prediction_dir,
        by_category,
    )
    assert table.get_string(sortby="Category") == expected_table
    assert table_shuffled.get_string(sortby="Category") == expected_table


@pytest.mark.parametrize(
    (
        "label_dir",
        "prediction_dir",
        "shuffled_prediction_dir",
        "by_category",
        "expected_table",
    ),
    [
        (
            FIXTURES / "labels",
            FIXTURES / "predictions",
            FIXTURES / "shuffled_predictions",
            True,
            """| Category                | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:------------------------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| birth_date              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| cote_article            |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| cote_serie              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| fac                     |  80.00   |     100.00    |   20.00    | 33.33  |       5 |           1 |
| firstname               |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| gpe                     |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| husband_location        |   0.00   |     100.00    |   100.00   | 100.00 |       4 |           1 |
| husband_name            |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| husband_occupation      |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| husband_surname         |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| intitule                |  25.00   |     75.00     |   75.00    | 75.00  |      16 |           1 |
| link                    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| location_of_birth       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| norp                    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| ordinal                 |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| per                     |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| precisions_sur_cote     |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| surname                 |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| time                    |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| total                   |  29.09   |     77.78     |   76.36    | 77.06  |      55 |           5 |
| wife_name               |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wife_state              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_location   |   0.00   |     100.00    |   100.00   | 100.00 |       5 |           1 |
| wifes_father_name       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_occupation |   0.00   |     100.00    |   100.00   | 100.00 |       3 |           1 |
| wifes_father_surname    |   0.00   |     100.00    |   100.00   | 100.00 |       2 |           1 |
| wifes_mother_name       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |""",
        ),
        (
            FIXTURES / "labels",
            FIXTURES / "predictions",
            FIXTURES / "shuffled_predictions",
            False,
            """| Category | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:---------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| total    |  29.09   |     77.78     |   76.36    | 77.06  |      55 |           5 |""",
        ),
    ],
)
def test_compute_bag_of_tagged_words(
    label_dir,
    prediction_dir,
    shuffled_prediction_dir,
    by_category,
    expected_table,
):
    table = compute_bag_of_tagged_words(label_dir, prediction_dir, by_category)
    table_shuffled = compute_bag_of_tagged_words(
        label_dir,
        shuffled_prediction_dir,
        by_category,
    )
    assert table.get_string(sortby="Category") == expected_table
    assert table_shuffled.get_string(sortby="Category") == expected_table


@pytest.mark.parametrize(
    (
        "label_dir",
        "prediction_dir",
        "shuffled_prediction_dir",
        "by_category",
        "expected_table",
    ),
    [
        (
            FIXTURES / "labels",
            FIXTURES / "predictions",
            FIXTURES / "shuffled_predictions",
            True,
            """| Category                | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:------------------------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| birth_date              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| cote_article            |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| cote_serie              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| fac                     |  100.00  |      0.00     |    0.00    |  0.00  |       2 |           1 |
| firstname               |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| gpe                     |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| husband_location        |   0.00   |     100.00    |   100.00   | 100.00 |       2 |           1 |
| husband_name            |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| husband_occupation      |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| husband_surname         |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| intitule                |  100.00  |      0.00     |    0.00    |  0.00  |       1 |           1 |
| link                    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| location_of_birth       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| norp                    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| ordinal                 |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| per                     |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| precisions_sur_cote     |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| surname                 |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| time                    |  100.00  |     100.00    |    0.00    |  0.00  |       1 |           1 |
| total                   |  32.14   |     71.43     |   71.43    | 71.43  |      28 |           5 |
| wife_name               |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wife_state              |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_location   |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_name       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_occupation |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_father_surname    |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |
| wifes_mother_name       |   0.00   |     100.00    |   100.00   | 100.00 |       1 |           1 |""",
        ),
        (
            FIXTURES / "labels",
            FIXTURES / "predictions",
            FIXTURES / "shuffled_predictions",
            False,
            """| Category | bWER (%) | Precision (%) | Recall (%) | F1 (%) | N words | N documents |
|:---------|:--------:|:-------------:|:----------:|:------:|--------:|------------:|
| total    |  32.14   |     71.43     |   71.43    | 71.43  |      28 |           5 |""",
        ),
    ],
)
def test_compute_bag_of_entities(
    label_dir,
    prediction_dir,
    shuffled_prediction_dir,
    by_category,
    expected_table,
):
    table = compute_bag_of_entities(label_dir, prediction_dir, by_category)
    table_shuffled = compute_bag_of_entities(
        label_dir,
        shuffled_prediction_dir,
        by_category,
    )
    assert table.get_string(sortby="Category") == expected_table
    assert table_shuffled.get_string(sortby="Category") == expected_table

import json

from bio_parser.parse.validate import run as validate

from tests.parse import DATA_DIR


def test_valid():
    filepath = DATA_DIR / "valid.bio"
    validate([filepath])

    # A JSON file should have been generated
    output = filepath.with_suffix(".json")
    assert output.exists()

    # Check content of JSON
    assert json.loads(output.read_text()) == {
        "bio_repr": "San B-GPE\nFrancisco I-GPE\nconsiders O\nbanning B-VERB\nsidewalk O\ndelivery O\nrobots O",
        "filename": "valid",
        "tokens": [
            {"idx": 0, "text": "San B-GPE"},
            {"idx": 1, "text": "Francisco I-GPE"},
            {"idx": 2, "text": "considers O"},
            {"idx": 3, "text": "banning B-VERB"},
            {"idx": 4, "text": "sidewalk O"},
            {"idx": 5, "text": "delivery O"},
            {"idx": 6, "text": "robots O"},
        ],
        "spans": [
            {
                "tokens": [
                    {"idx": 0, "text": "San B-GPE"},
                    {"idx": 1, "text": "Francisco I-GPE"},
                ]
            },
            {"tokens": [{"idx": 3, "text": "banning B-VERB"}]},
        ],
    }

    # Cleanup
    output.unlink()

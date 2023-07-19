import pytest
from linguistlab import Glossary


@pytest.fixture
def glossary():
    test_glossary_content = {
        "hello": ["hej", "hallå"],
        "car": ["bil"],
        "card": ["kort"],
        "short": ["kort"],
        "shorter": ["kortare"],
    }
    test_glossary = Glossary("Test", test_glossary_content)
    return test_glossary


def test_search_source_term(glossary):
    search_one = glossary.search_source_term("hello")
    assert search_one == {"hello": ["hej", "hallå"]}

    search_two = glossary.search_source_term("car")
    assert search_two == {"car": ["bil"], "card": ["kort"]}

    search_three = glossary.search_source_term("card")
    assert search_three == {"car": ["bil"], "card": ["kort"]}

    search_four = glossary.search_source_term("hej")
    assert search_four == {}

    search_five = glossary.search_source_term("helicopter")
    assert search_five == {}


def test_search_target_term(glossary):
    search_one = glossary.search_target_term("hej")
    assert search_one == {"hello": ["hej", "hallå"]}

    search_two = glossary.search_target_term("hallå")
    assert search_two == {"hello": ["hej", "hallå"]}

    search_three = glossary.search_target_term("kort")
    assert search_three == {"card": ["kort"], "short": ["kort"]}

    search_four = glossary.search_target_term("kortare")
    assert search_four == {"shorter": ["kortare"]}

    search_five = glossary.search_target_term("hello")
    assert search_five == {}

    search_six = glossary.search_target_term("helikopter")
    assert search_six == {}


def test_add_source_term(glossary):
    with pytest.raises(ValueError, match="Source term already exists in Test"):
        glossary.add_source_term("car")

    assert glossary.glossary_content == {
        "hello": ["hej", "hallå"],
        "car": ["bil"],
        "card": ["kort"],
        "short": ["kort"],
        "shorter": ["kortare"],
    }

    glossary.add_source_term("bed")

    assert glossary.glossary_content == {
        "hello": ["hej", "hallå"],
        "car": ["bil"],
        "card": ["kort"],
        "short": ["kort"],
        "shorter": ["kortare"],
        "bed": [],
    }

    glossary.add_source_term("walk", ["gå", "vandra"])

    assert glossary.glossary_content == {
        "hello": ["hej", "hallå"],
        "car": ["bil"],
        "card": ["kort"],
        "short": ["kort"],
        "shorter": ["kortare"],
        "bed": [],
        "walk": ["gå", "vandra"],
    }

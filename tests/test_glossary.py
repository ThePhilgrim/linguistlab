import pytest
from linguistlab import Glossary


@pytest.fixture
def glossary():
    test_glossary_content = {
        "hello": ["hej", "hallå"],
        "car": ["bil"],
        "card": ["kort"],
        "shorter": ["kortare"],
    }
    test_glossary = Glossary(test_glossary_content)
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
    assert search_three == {"card": ["kort"], "shorter": ["kortare"]}

    search_four = glossary.search_target_term("kortare")
    assert search_four == {"card": ["kort"], "shorter": ["kortare"]}

    search_five = glossary.search_source_term("hello")
    assert search_five == {}

    search_six = glossary.search_source_term("helikopter")
    assert search_six == {}

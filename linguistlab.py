import csv
import sys

from typing import Dict, List, Any, Optional


def read_glossary(csv_file: Any) -> Dict[str, List[str]]:
    glossary_content = {}
    with open(csv_file, newline="") as glossary_file:
        glossary = csv.reader(glossary_file)
        for row in glossary:
            translations = []
            for translation in row[1:]:
                translations.append(translation)
            glossary_content[row[0]] = translations

    return glossary_content


class Glossary:
    def __init__(self, name: str, glossary_content: Dict[str, List[str]] | Dict[Any, Any]):
        self.name = name
        self.glossary_content = glossary_content

    def search_source_term(self, search_term: str) -> Dict[str, List[str]]:
        search_results = {}
        for source_term in self.glossary_content.keys():
            if (
                search_term.lower() in source_term.lower()
                or source_term.lower() in search_term.lower()
            ):
                search_results[source_term] = self.glossary_content[source_term]

        return search_results

    def search_target_term(self, search_term: str) -> Dict[str, List[str]]:
        search_results = {}
        for source_term in self.glossary_content.keys():
            if search_term in self.glossary_content[source_term]:
                search_results[source_term] = self.glossary_content[source_term]
        return search_results

    # TODO: Add functionality for merging/replacing terms if source term already in glossary.
    def add_source_term(self, source_term: str, target_terms: Optional[List[str]] = None) -> None:
        if source_term in self.glossary_content.keys():
            raise ValueError(f"Source term already exists in {self.name}.")
        elif source_term not in self.glossary_content.keys() and target_terms is None:
            self.glossary_content[source_term] = []
        elif source_term not in self.glossary_content.keys() and target_terms is not None:
            self.glossary_content[source_term] = target_terms

    def delete_source_term(self, source_term: str) -> None:
        if source_term not in self.glossary_content.keys():
            raise KeyError(f"The term does not exist in {self.name}")
        elif source_term in self.glossary_content.keys():
            del self.glossary_content[source_term]

    # TODO
    # def add_target_term(self):
    #     pass

    # def edit_term(self):
    #     pass

    # def delete_target_term(self):
    #     pass

    # def delete_glossary_unit(self):
    #     pass


if __name__ == "__main__":
    glossary_content = read_glossary(sys.argv[1])

    general = Glossary("Developing", glossary_content)
    general.search_source_term(sys.argv[2])

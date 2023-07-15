import csv
import sys


def read_glossary(csv_file):
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
    def __init__(self, glossary_content):
        self.glossary_content = glossary_content

    def search_source_term(self, search_term):
        search_results = {}
        for source_term in self.glossary_content.keys():
            if search_term.lower() in source_term.lower() or source_term.lower() in search_term.lower():
                search_results[source_term] = self.glossary_content[source_term]

        return search_results

    # TODO
    # def search_target_term(self):
    #     pass

    # def add_source_term(self):
    #     pass

    # def add_target_term(self):
    #     pass

    # def edit_term(self):
    #     pass

    # def delete_source_term(self):
    #     pass

    # def delete_target_term(self):
    #     pass

    # def delete_glossary_unit(self):
    #     pass


glossary_content = read_glossary(sys.argv[1])

general = Glossary(glossary_content)
general.search_source_term(sys.argv[2])

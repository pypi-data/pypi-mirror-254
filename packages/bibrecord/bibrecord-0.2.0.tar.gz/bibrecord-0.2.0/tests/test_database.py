import unittest

from bibrecord import bibtex, database, record

ARTICLE = """
@Article{doe-foo-1-1,
    author = {John Doe},
    title = {Lorem ipsum},
    journal = {Foo},
    pages = {1--2},
    year = {2024}
}
"""

BOOK = """
@Book{doe-j-2024,
    author = {John Doe},
    title = {Lorem ipsum},
    publisher = {Foo},
    address = {Bar},
    year = {2024}
}
"""

UNKNOWN = """
@Unknown{hut-p-2024,
    author = {Pizza Hut},
    title = {Eat!}
}
"""

DATABASE = "".join([ARTICLE, BOOK])


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = database.Database()
        self.bibliography = bibtex.Bibliography()
        self.bibliography.from_bib(DATABASE)

    def test_instantiate_class(self):
        pass

    def test_from_bibliography_populates_records(self):
        self.database.from_bibliography(self.bibliography)
        self.assertTrue(self.database.records)

    def test_from_bibliography_creates_actual_records(self):
        self.database.from_bibliography(self.bibliography)
        for _, entry in self.database.records.items():
            self.assertIsInstance(entry, record.Record)

    def test_from_bibliography_without_bibliography_raises(self):
        with self.assertRaises(ValueError):
            self.database.from_bibliography(None)

    def test_from_bibliography_with_duplicates_logs_warning(self):
        self.database.from_bibliography(self.bibliography)
        with self.assertLogs(__package__, level="WARNING") as cm:
            self.database.from_bibliography(self.bibliography)
        self.assertIn("Duplicate key", cm.output[0])

    def test_from_bibliography_with_duplicates_does_not_overwrite(self):
        self.database.from_bibliography(self.bibliography)
        self.bibliography.entries[0].title = "Unknown"
        with self.assertLogs(__package__, level="WARNING") as cm:
            self.database.from_bibliography(self.bibliography)
        self.assertEqual(
            "Lorem ipsum", self.database.records["doe-foo-1-1"].title
        )

    def test_from_bibliography_with_unknown_type_logs_warning(self):
        bibliography = bibtex.Bibliography()
        bibliography.from_bib(UNKNOWN)
        with self.assertLogs(__package__, level="WARNING") as cm:
            self.database.from_bibliography(bibliography)
        self.assertIn("Unknown record type", cm.output[0])

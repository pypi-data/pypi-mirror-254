import os
import unittest

from bibrecord import bibtex


ARTICLE = """
@Article{doe-foo-1-1,
    author = {John Doe and Jane Doe},
    title = {Lorem ipsum},
    journal = {Foo},
    pages = {1--2},
    year = {2024}
}
"""

BOOK = """
@Book{doe-j-2024,
    author = {John Doe},
    title = {Lorem ipsum dolor sit amet},
    publisher = {Foo},
    address = {Bar},
    year = {2024}
}
"""

EDITEDBOOK = """
@Book{doe-j-2024,
    editor = {John Doe},
    title = {Lorem ipsum},
    publisher = {Foo},
    address = {Bar},
    year = {2024}
}
"""


class TestEntry(unittest.TestCase):
    def setUp(self):
        self.entry = bibtex.Entry()
        self.article_entry = ARTICLE
        self.book_entry = BOOK

    def test_instantiate_class(self):
        pass

    def test_from_bib_sets_record(self):
        self.entry.from_bib(self.article_entry)
        self.assertTrue(self.entry.record)
        self.assertEqual(self.article_entry, self.entry.record)

    def test_from_bib_with_article_sets_type(self):
        self.entry.from_bib(self.article_entry)
        self.assertTrue(self.entry.type)
        self.assertEqual("article", self.entry.type)

    def test_from_bib_with_book_sets_type(self):
        self.entry.from_bib(self.book_entry)
        self.assertTrue(self.entry.type)
        self.assertEqual("book", self.entry.type)

    def test_from_bib_sets_key(self):
        self.entry.from_bib(self.book_entry)
        self.assertTrue(self.entry.key)
        self.assertEqual("doe-j-2024", self.entry.key)

    def test_from_bib_sets_fields_dict(self):
        self.entry.from_bib(self.book_entry)
        self.assertTrue(self.entry.fields)

    def test_from_bib_sets_author_as_list(self):
        self.entry.from_bib(self.article_entry)
        self.assertIsInstance(self.entry.fields["author"], list)

    def test_from_bib_sets_editor_as_list(self):
        self.entry.from_bib(EDITEDBOOK)
        self.assertIsInstance(self.entry.fields["editor"], list)

    def test_from_bib_with_equals_sign_in_field_doesnt_split_field(self):
        self.entry.from_bib(
            ARTICLE.replace("{Lorem ipsum}", "{Lorem = ipsum}")
        )
        self.assertEqual("Lorem = ipsum", self.entry.fields["title"])

    def test_from_bib_does_not_omit_first_field(self):
        self.entry.from_bib(ARTICLE.strip())
        self.assertTrue(self.entry.fields["author"])


class TestBibliography(unittest.TestCase):
    def setUp(self):
        self.bibliography = bibtex.Bibliography()
        self.bibtex = "".join([ARTICLE, BOOK])
        self.filename = "test.bib"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def create_bibtex_file(self):
        with open(self.filename, "w+", encoding="utf8") as file:
            file.write(self.bibtex)

    def test_instantiate_class(self):
        pass

    def test_from_bib_populates_entries(self):
        self.bibliography.from_bib(self.bibtex)
        self.assertTrue(self.bibliography.entries)

    def test_from_bib_adds_entries_to_entries(self):
        self.bibliography.from_bib(self.bibtex)
        self.assertIsInstance(self.bibliography.entries[0], bibtex.Entry)

    def test_from_bib_without_bibliography_raises(self):
        with self.assertRaises(ValueError):
            self.bibliography.from_bib("")

    def test_from_file_adds_entries_to_entries(self):
        self.create_bibtex_file()
        self.bibliography.from_file(self.filename)
        self.assertIsInstance(self.bibliography.entries[0], bibtex.Entry)

    def test_from_file_without_filename_raises(self):
        with self.assertRaises(ValueError):
            self.bibliography.from_file("")

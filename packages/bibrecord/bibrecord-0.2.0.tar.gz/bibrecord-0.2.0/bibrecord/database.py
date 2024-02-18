"""
Facilities for representing bibliographic databases.

While individual bibliographic records are handled by the
:mod:`bibrecord.record` module and BibTeX files and records are dealt with by
the :mod:`bibrecord.bibtex` module, this module provides means to handle
bibliographic databases, *i.e.* a collection of individual
:obj:`bibrecord.record.Record` objects.


Use cases
=========

If you "only" want to have a bibliographic record as an attribute in a class,
say for an implementation of an algorithm where you would like to give credit
to the people who originally described the algorithm, one of the subclasses of
:class:`bibrecord.record.Record` is what you usually are interested in.

However, suppose you write a package that contains data from different sources
(*i.e.*, with different references) and you want to provide these references for
each individual dataset. In this case, you will probably have a BibTeX
bibliography file somewhere in the package data of your package that would be
the original source of the bibliographic information. In this case, being able
to convert this BibTeX bibliography file into an actionable representation for
your package would come quite handy. This is what the :class:`Database` class
provides you with.

Creating such a database is a matter of only a few lines. Suppose your BibTeX
database to reside in the file "literature.bib":

.. code-block::

    import bibrecord

    bibliography = bibrecord.bibtex.Bibliography()
    bibliography.from_file("literature.bib")
    database = bibrecord.database.Database()
    database.from_bibliography(bibliography)

Now you can access all bibliographic records from your :obj:`Database` object.


Module documentation
====================

"""

import inspect
import logging

import bibrecord.record


logger = logging.getLogger(__name__)


class Database:
    """
    Database of bibliographic records.

    Each record is of type :class:`bibrecord.record.Record` (actually, it is
    a subtype corresponding to the actual BibTeX entry type). Records are stored
    in the :attr:`records` attribute as a dictionary whose keys are the BibTeX
    keys used to cite the bibliographic record and the corresponding value the
    instance of the corresponding :class:`bibrecord.record.Record` subclass.


    Attributes
    ----------
    records : :class:`dict`
        Bibliographic records

        The keys are the BibTeX keys used to cite the bibliographic record and
        the value the instance of the corresponding
        :class:`bibrecord.record.Record` subclass.


    Examples
    --------
    Suppose you have a BibTeX database residing in the file "literature.bib".
    Creating a database containing the records in a form processable by the
    bibrecord package requires a few steps:

    .. code-block::

        import bibrecord

        bibliography = bibrecord.bibtex.Bibliography()
        bibliography.from_file("literature.bib")
        database = bibrecord.database.Database()
        database.from_bibliography(bibliography)

    The result is a database containing bibliographic records in a form that is
    processable by the bibrecord package and hence from within your code.


    .. versionadded:: 0.2

    """

    def __init__(self):
        self.records = {}

    def from_bibliography(self, bibliography):
        """
        Populate database from bibliography.

        Each BibTeX entry in the bibliography will be converted to an object
        of the corresponding :class:`bibrecord.record.Record` subclass if this
        exists and added to the :attr:`records` dictionary. The key is the
        BibTeX key of the BibTeX entry used to cite the entry, the corresponding
        value the :class:`bibrecord.record.Record` object.

        Parameters
        ----------
        bibliography : :class:`bibrecord.bibtex.Bibliography`
            Representation of a BibTeX bibliography, *e.g.* as read from a file.

        """
        if not bibliography:
            raise ValueError
        record_types = {}
        for item in inspect.getmembers(bibrecord.record, inspect.isclass):
            record_types[item[0]] = item[1]
        for entry in bibliography.entries:
            record_type = entry.type.capitalize()
            if record_type in record_types:
                if entry.key in self.records:
                    logger.warning("Duplicate key %s", entry.key)
                    break
                record = record_types[record_type]()
                record.from_bib(entry.record)
                self.records[entry.key] = record
            else:
                logger.warning("Unknown record type %s", record_type)

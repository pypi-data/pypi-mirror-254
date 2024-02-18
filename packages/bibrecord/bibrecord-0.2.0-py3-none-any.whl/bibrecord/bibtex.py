r"""
Facilities for reading BibTeX bibliographies.

The BibTeX bibliography file format is not too explicitly specified, but there
is a bunch of information available, both from the original author of BibTeX
(Oren Patashnik) and from the documentation of tools working with BibTeX
bibliographies and entries.

For the time being, this module implements parsing facilities for BibTeX
databases using a best effort approach and requiring well-formatted BibTeX
entries.

Generally, individual entries of a bibliography are represented by an object
of the :class:`Entry` class. This class does *not* provide extended logic for
dealing with the particular types of bibliographic records, as this is part of
the :mod:`bibrecord.record` module.

Entire BibTeX bibliographies (as typically residing in \*.bib files) can be read
and converted into :obj:`Entry` objects using the :class:`Bibliography` class.


Classes
=======

The two important classes for representing BibTeX bibliographies are:

* :class:`Entry`

  Representation of a BibTeX entry.

* :class:`Bibliography`

  Representation of a BibTeX bibliography, *e.g.* as read from a file.


Limitations
===========

There are many limitations for the time being, as this module does not intend
to be a full BibTeX parser.

* BibTeX records are expected to be well-formatted.
* String replacement (*e.g.*, for Journal names) is currently *not* supported.


Module documentation
====================

"""

import logging
import re


logger = logging.getLogger(__name__)


class Entry:
    """
    Representation of a BibTeX entry.

    Regardless of the type of BibTeX entry, this class will contain all relevant
    information, such as type, key, and fields. This information can be used by
    objects of type :class:`bibrecord.record.Record` to read their contents
    from a BibTeX entry. The idea is to provide means by which the bibliographic
    records contained in a BibTeX file can be read and converted into
    :obj:`bibrecord.record.Record` objects of appropriate type.

    Attributes
    ----------
    type : :class:`str`
        Type of the BibTeX entry, such as "article" or "book"

        Note that regardless of the original way the BibTeX entry was written,
        type will always be all lowercase.

    key : :class:`str`
        BibTeX key used to refer to the record

    fields : :class:`dict`
        Key-value store of all the fields of a BibTeX entry

    record : :class:`str`
        Multiline string containing the original BibTeX entry


    Examples
    --------
    Assume a BibTeX entry to exist in a multiline string ``bibtex_record``.
    Converting this multiline string into a :obj:`Entry` object with all the
    information accessible for later conversion into a
    :obj:`bibrecord.record.Record` object would look as follows:

    .. code-block::

        entry = Entry()
        entry.from_bib(bibtex_record)

    For further details, see the documentation for :meth:`from_bib`.

    .. versionadded:: 0.2

    """

    def __init__(self):
        self.type = ""
        self.key = ""
        self.fields = None
        self.record = ""

    def from_bib(self, bibtex_record=None):
        """
        Read BibTeX entry from string and parse the contents.

        Currently, the format of the BibTeX records is quite restricted.
        They need to be a multiline string, with the type and key on the first
        line and all fields on separate lines. A typical BibTeX record looks
        similar to:

        .. code-block:: bibtex

            @Article{doe-foo-1-1,
                author = {John Doe},
                title = {Lorem ipsum},
                journal = {Foo},
                pages = {1--2},
                year = {2024}
            }

        More generally, a bibtex record could be understood as following this
        overall scheme:

        .. code-block:: bibtex

            @TYPE{KEY,
                FIELD = VALUE,
                FIELD = VALUE
            }

        Upon parsing such an entry, the attributes of the class :class:`Entry`
        with the corresponding names will be set, *i.e.* :attr:`Entry.type` will
        be set to the lower-case version of "TYPE", :attr:`Entry.key` to KEY,
        et cetera.

        All fields will be parsed and the :attr:`Entry.fields` dict populated
        accordingly. Here, it does not matter whether values are surrounded by
        ``{`` or ``"`` and whether they have a trailing comma.

        Authors and editors are split at the (case-insensitive) "AND" and stored
        as a list of strings.


        Parameters
        ----------
        bibtex_record : :class:`str`
            Multiline string containing a BibTeX record

        """
        self.record = bibtex_record
        self._parse_record()
        self._convert_author_editor()

    def _parse_record(self):
        self.type = re.search(r"@([A-Za-z]+){", self.record).group(1).lower()
        self.key = re.search(r"@[A-Za-z]+{([^,]+),", self.record).group(1)
        self.fields = {}
        for line in self.record.split("\n")[1:]:
            if "=" in line:
                field, value = line.split("=", maxsplit=1)
                value = re.match(
                    r'^[{"]?(.+?)[}"]?,?$',
                    value.strip(),
                ).group(1)
                self.fields[field.strip()] = value

    def _convert_author_editor(self):
        for key in ["author", "editor"]:
            if key in self.fields:
                names = re.split("and", self.fields[key], flags=re.IGNORECASE)
                self.fields[key] = [name.strip() for name in names]


class Bibliography:
    """
    Representation of a BibTeX bibliography, *e.g.* as read from a file.

    A BibTeX bibliography is a series of individual bibliographic records that
    can be of different types. For more information on the overall format of
    BibTeX bibliographies, have a look at the available online resources.

    Here, the bibliography represents the individual bibliographic records
    contained in a BibTeX bibliography as objects of class :class:`Entry`.


    Attributes
    ----------
    entries : :class:`list`
        Entries of the bibliography

        Each entry is an object of type :class:`Entry`.


    Examples
    --------
    Assume a BibTeX entry to exist in a multiline string ``bibtex_db``.
    Converting this multiline string into a :obj:`Bibliography` object with
    all the individual entries contained in :attr:`Bibliography.entries` as
    :obj:`Entry` objects would look as follows:

    .. code-block::

        bibliography = Bibliography()
        bibliography.from_bib(bibtex_db)

    The individual entries in turn make the information contained accessible
    for later conversion into a :obj:`bibrecord.record.Record` object.

    For further details, see the documentation for :meth:`from_bib`.


    .. versionadded:: 0.2

    """

    def __init__(self):
        self.entries = []

    def from_bib(self, bibliography=""):
        r"""
        Read BibTeX bibliography and convert it into individual entries.

        Each entry is of type :class:`Entry`.

        The bibliography is split on ``\n@``, *i.e.* a ``@`` sign following
        a linebreak.


        Parameters
        ----------
        bibliography : :class:`str`
            BibTeX bibliography, *e.g.* read from a file

        Raises
        ------
        ValueError
            Raised if no ``bibliography`` is provided

        """
        if not bibliography:
            raise ValueError
        for block in bibliography.split("\n@"):
            if block:
                if not block.startswith("@"):
                    block = f"@{block}"
                entry = Entry()
                entry.from_bib(block)
                self.entries.append(entry)

    def from_file(self, filename=""):
        """
        Read BibTeX bibliography and convert it into individual entries.

        For details of how the file contents are parsed, see :meth:`from_bib`.

        Parameters
        ----------
        filename : :class:`str`
            Name of the BibTeX file to read bibliography from

        """
        if not filename:
            raise ValueError
        with open(filename, "r", encoding="utf8") as file:
            bibliography = file.read()
        self.from_bib(bibliography)

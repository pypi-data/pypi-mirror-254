
.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.10607369.svg
   :target: https://doi.org/10.5281/zenodo.10607369
   :align: right

=========
bibrecord
=========

*Handling bibliographic records within source code.*

Did you ever feel the need of adding a reference to the literature to your code, *e.g.* to an article describing the algorithm you just (re)implemented? Are you somewhat familiar with how bibliographic records look like, *e.g.* from using BibTeX in conjunction with the TeX/LaTeX typesetting system? Then bibrecord may be the tool of choice for you.

Suppose you have implemented power-law noise and want to refer to the literature to give credit to those guys whose algorithm you've implemented. In this case, you could add the following record as an attribute to your class:

.. code-block::

    reference = bibrecord.Article(
        author=['J. Timmer', 'M. König'],
        title="On generating power law noise",
        journal="Astronomy and Astrophysics",
        volume="300",
        pages="707--710",
        year="1995"
    )

If you would like to output the reference as plain text, this would be as simple as:

.. code-block::

    reference.to_string()

The result:

J. Timmer, M. König: On generating power law noise. Astronomy and Astrophysics 300:707--710, 1995.


Features
========

A list of features:

* Support for (a growing list of) different types of bibliographic records (articles, books).

* Straight-forward definition of bibliographic records, similar to BibTeX.

* Easy integration of a bibliographic record into your existing code base.

* Simple, yet powerful ways of creating a string representation or a BibTeX record from each bibliographic record.


And to make it even more convenient for users and future-proof:

* Open source project written in Python (>= 3.7)

* Developed fully test-driven

* Extensive user and API documentation


Installation
============

To install the bibrecord package on your computer (sensibly within a Python virtual environment), open a terminal (activate your virtual environment), and type in the following:

.. code-block:: bash

    pip install bibrecord


License
=======

This program is free software: you can redistribute it and/or modify it under the terms of the **BSD License**.
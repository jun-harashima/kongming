========
kongming
========


.. image:: https://img.shields.io/pypi/v/kongming.svg
        :target: https://pypi.python.org/pypi/kongming

.. image:: https://img.shields.io/travis/jun-harashima/kongming.svg
        :target: https://travis-ci.com/jun-harashima/kongming

.. image:: https://readthedocs.org/projects/kongming/badge/?version=latest
        :target: https://kongming.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Collect arrows from parsing results.

Installation
------------

.. code-block:: bash

   $ pip install kongming

Usage
-----

.. code-block:: python

    from kongming.main import Komgming

    stopwords = ["。"]
    kongming = Kongming(stopwords)
    arrows = kongming.collect("今日は良い天気だ。")
    print(arrows)  # => [{'modifier': '今日', 'function': 'は', 'head': '天気'},
                         {'modifier': '良い', 'function': '', 'head': '天気'}]

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

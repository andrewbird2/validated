=============================
Validated
=============================

.. image:: https://badge.fury.io/py/validated.svg
    :target: https://badge.fury.io/py/validated

.. image:: https://travis-ci.org/andrewbird2/validated.svg?branch=master
    :target: https://travis-ci.org/andrewbird2/validated

.. image:: https://codecov.io/gh/andrewbird2/validated/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/andrewbird2/validated

A Django app for running tests on data

Documentation
-------------

The full documentation is at https://validated.readthedocs.io.

Quickstart
----------

Install Validated::

    pip install validated

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'validated.apps.ValidatedConfig',
        ...
    )

Add Validated's URL patterns:

.. code-block:: python

    from validated import urls as validated_urls


    urlpatterns = [
        ...
        url(r'^', include(validated_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage

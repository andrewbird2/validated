=====
Usage
=====

To use Validated in a project, add it to your `INSTALLED_APPS`:

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

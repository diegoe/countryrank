Country Rank
=====

Country Rank is a simple aggregator and visualization of CSV data from
some specific sources from data.worldbank.org. It's built specifically
as a demo project of quick full stack development divided into a toy
backend and an editable frontend.

## Prerequisites

`countryrank` is built targetting Django 3.0 and Python 3.6. You might
want to use something like `pyenv` to set your local `python`:

```shell
$ pyenv install 3.6.10
$ pyenv local 3.6.10
```

At the time of writing, Python 3.6.10 is the latest stable release in
the 3.6 branch.

### TODO: Explain how to install other prerequisites through pip

How to install
===

You can `git clone` this repository and run the usual django
bootstrapping. Notice that `countryrank/settings.py` is already
configured and you can simply deploy django migrations and
download/ingest the needed data.

```shell
# Create your local sqlite db
$ python manage.py migrate
# Download the CSV data from data.worldbank.org
$ python manage.py downloadsources
# Process the donwloaded data
$ python manage.py ingestcsv
```

The project should now be good to go, and you should be able to visit
Django's test server:

```shell
$ python manage.py runserver
```

Running tests
===

Tests for backcountry are available in `backcountry/tests.py`, coverage
is limited, prioritizing utility over completeness. You can run tests
with:

```shell
$ python manage.py test
```

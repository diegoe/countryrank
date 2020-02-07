Country Rank
=====

Country Rank is a simple aggregator and visualization of CSV data from
some specific sources from data.worldbank.org. It's built specifically
as a demo project of quick full stack development divided into a toy
backend and an editable frontend.

## Quick start

Clone this repository and make sure you have Django 3.x installed, and
any Python above 3.6, also yarn/npm/nodejs. Then run:

```shell
$ python manage.py migrate
$ python manage.py downloadsources
$ python manage.py ingestcsv
$ cd forevue/
$ yarn install
$ yarn build
$ cd ..
$ python manage.py runserver
```

Now you should be able to visit
`http://127.0.0.1:8000/static/backcountry/index.html` in your browser.

## Prerequisites

* python >= 3.6
* Django 3.x
* nodejs >= 10.x
* yarn/npm

`countryrank` is built targetting Django 3.0 and Python 3.6. You might
want to use something like `pyenv` to set your local `python`:

```shell
$ pyenv install 3.6.10
$ pyenv local 3.6.10
```

At the time of writing, Python 3.6.10 is the latest stable release in
the 3.6 branch. No external python modules are needed, except for
Django, of course.

`forevue`, the included frontend, was built targetting Vue 2.6 and node
10.x. `yarn install` should take care of all the JS module dependencies,
but keep in mind the above versions in case node or Vue give you any
trouble.

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

The backend should now be good to go, and you should be able to run
Django's test server:

```shell
$ python manage.py runserver
```

To get the frontend running you can just rely on the currently checked
in version in `backcountry/static/`, or you can run a development server
from `forevue`. You will need yarn, npm and nodejs -- at a minimum.

```shell
# Install all node dependencies
$ yarn install
```

You can either run a development server that reloads as you make changes
in `forevue/src`, or you can run the version currently checked in, or
produce a new build of it:

```shell
# Serve a development build that runs at
# http://127.0.0.1:8080/static/backcountry/
$ yarn serve

# Alternatively, produce a new build to be served by Django at
# http://127.0.0.1:8000/static/backcountry/index.html
$ yarn build
```

`yarn build` will output to `backcountry/static/backcountry/`, and `yarn
serve` will proxy any axios/fetch request to Django's server on
`127.0.0.1:8000`.

If you change the IP or port were Django is running, you will need to
update `forevue/vue.config.js`. Also note that `CORS` security/policy
might throw you off if you end up changing ports or IPs of the
development server(s).

Running tests
===

Tests for backcountry are available in `backcountry/tests.py`, coverage
is limited, prioritizing utility over completeness. You can run tests
with:

```shell
$ python manage.py test
```

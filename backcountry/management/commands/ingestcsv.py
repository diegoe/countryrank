from backcountry.models import Country, Indicator, CountryYearIndicator
from django.core.management.base import BaseCommand, CommandError
import os, csv
import pdb

class Command(BaseCommand):
    help = 'Process and ingest CSV data into Django models'

    def handle(self, *args, **options):
        csv_files = []

        for d in os.listdir('downloads'):
            csv_files += [os.path.join('downloads', d, fn)
                    for fn in os.listdir(os.path.join('downloads', d))
                    if fn.startswith('API_') and fn.endswith('csv')]

        for fn in csv_files:
            with open(fn, 'r') as fd:
                # FIXME: This `for` below is an absolute hack.
                # Skip 4 first lines, something very specific to our data
                # origins.
                for _ in range(4):
                    next(fd)

                data = csv.DictReader(fd)

                for row in data:
                    code = row.get('Country Code', None)
                    d = {}

                    if code is not None:
                        d['country.name'] = row['Country Name']
                        d['country.code'] = row['Country Code']

                        d['indicator.name'] = row['Indicator Name']
                        d['indicator.code'] = row['Indicator Code']

                        # This calls to get_or_create() are /reasonable/
                        # given that we call this once per file at most.
                        # I guess an optional optimization would be to
                        # cache the objects after creation (maybe?)
                        (db_c, created) = Country.objects.get_or_create(
                                name=d['country.name'],
                                code=d['country.code'])
                        (db_i, created) = Indicator.objects.get_or_create(
                                name=d['indicator.name'],
                                code=d['indicator.code'])

                        # README: Some rows might have empty cells in
                        # certain years, instead of trying to insert a
                        # CYI with value '0', just skip these empty
                        # values. Note that an empty string in `v` will
                        # evaluate to False.
                        years = [(k, v) for k, v in row.items() if k.isdigit() and v]

                        for y, v in years:
                            d[y] = v

                            # Note that this are blind creations because
                            # we only visit a combination of indicator
                            # (file) x country (row) once.
                            # Trying to secure this with a
                            # get_or_create() kills performance, as
                            # expected.
                            db_cyi = CountryYearIndicator(
                                    country=db_c,
                                    indicator=db_i,
                                    year=y,
                                    value=v)
                            db_cyi.save()

                            if db_cyi:
                                self.stdout.write(
                                        'Creating `CountryYearIndicator` %s: %s (%s %s)' %
                                        (d['country.code'], d['indicator.code'], y, v))

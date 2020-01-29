#from backcountry.models import Country, Indicators, CountryYearIndicator
import os, csv
import pdb

csv_dir = 'csvdata'
csv_files = [fn for fn in os.listdir(csv_dir) if fn.endswith('csv')]

country_db = {}
for fn in csv_files:
    with open(os.path.join(csv_dir, fn), 'r') as fd:
        # Skip 4 first lines, something very specific to our data
        # origins.
        for _ in range(4):
            next(fd)

        data = csv.DictReader(fd)

        for row in data:
            code = row.get('Country Code', None)
            d = {}
            if code is not None:
                d['name'] = row['Country Name']
                d['code'] = row['Country Code']
                d['indicator.code'] = row['Indicator Code']
                d['value'] = row['2019']

                years = [(k, v) for k, v in row.items() if k.isdigit()]

                for y, v in years:
                    d[y] = v
            print(d)

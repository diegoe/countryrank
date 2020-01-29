from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=3, unique=True)

class Indicator(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

class CountryYearIndicator(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)

    # Defining `value` as models.DecimalField is a reasonable compromise
    # for the varied kind of data we get from our known data sources.
    #
    # Most are either trivial integers on the higher side (10 digits or
    # more). Some are percentages expressed as decimal numbers with many
    # decimal places, and some are float-like numbers.
    #
    # Django offers DecimalField and luckily that's good enough for our
    # use case. A more agnostic or extensible version of this would
    # probably make Indicator able to describe itself from a list of
    # types, using something like Field.choices and a `value` property
    # based on models.CharField, handling validation and integrity
    # manually. But that's of course overkill for this demo.
    value = models.DecimalField(max_digits=19, decimal_places=5)

    def __str__(self):
        return "%s for %s on %s" % (
                self.indicator.name,
                self.country.name,
                self.year)

"""
Implementation note:
The above design is agnostic with regards to the information and
statistics that are being aggregated. That said, our reference
data/implementation is going to consume the following key indicators:

    * 'EN.ATM.CO2E.PC': 'CO2 emissions (metric tons per capita)'
    * 'IP.PAT.NRES': 'Patent applications, nonresidents'
    * 'IP.PAT.RESD':'Patent applications, residents'
    * 'NY.GDP.MKTP.CD':'GDP (current US$)'
    * 'SP.DYN.LE00.IN':'Life expectancy at birth, total (years)'
    * 'SP.POP.TOTL':'Population, total'
    * 'TX.VAL.TECH.MF.ZS':'High-technology exports (%)'
"""

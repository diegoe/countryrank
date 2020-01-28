from django.test import TestCase
from backcountry.models import Country, Indicator, CountryYearIndicator

class CountryYearIndicatorTestCase(TestCase):
    def setUp(self):
        per = Country.objects.create(name='Perú', code='PER')
        bol = Country.objects.create(name='Bolivia', code='BOL')
        chi = Country.objects.create(name='Chile', code='CHI')

        ind1 = Indicator.objects.create(name='CO2', code='env_co2')
        ind2 = Indicator.objects.create(name='GDP', code='eco_gdp')
        ind3 = Indicator.objects.create(name='POP', code='soc_pop')

        self.test_data_indicators = (
                (ind1, 2020, 10000),
                (ind1, 2010, 1000),
                (ind1, 2000, 100),
                (ind1, 1990, 10),

                (ind2, 2020, 41.0),
                (ind2, 2015, 20.5),
                (ind2, 2005, 10.25),
                (ind2, 1995, 5.125),

                (ind3, 2020, 100000.12345),
                (ind3, 2013, 10000.1234),
                (ind3, 2003, 1000.12),
                (ind3, 1993, 100.1),
                )
        self.test_data_countries = (per, bol, chi)

        for t_ind, t_year, t_value in self.test_data_indicators:
            for t_country in self.test_data_countries:
                CountryYearIndicator.objects.create(
                        country=t_country,
                        indicator=t_ind,
                        year=t_year,
                        value=t_value)

    def test_indicators_on_year_for_country(self):
        """Indicators for a country and year"""
        per = Country.objects.get(code='PER')
        cyi = CountryYearIndicator.objects.filter(
                country=per,
                year=2000)

        self.assertEqual(len(cyi), 1)

    def test_indicators_over_years_for_country(self):
        """Indicators for a specific country"""
        per = Country.objects.get(code='PER')
        cyi = CountryYearIndicator.objects.filter(
                country=per)

        self.assertEqual(len(cyi), len(self.test_data_indicators))
        self.assertEqual(len(cyi.filter(year=2020)), 1)

    def test_indicators_over_years_for_country(self):
        """Indicators for a specific country"""
        per = Country.objects.get(code='PER')
        cyi = CountryYearIndicator.objects.filter(
                country=per)

        self.assertEqual(len(cyi), len(self.test_data_indicators))
        self.assertEqual(len(cyi.filter(year=2020)), 3)

    def test_indicators_on_year_all_countries(self):
        """All data points for an indicator in a certain year"""
        ind1 = Indicator.objects.get(code='env_co2')
        per = Country.objects.get(code='PER')
        cyi = CountryYearIndicator.objects.filter(
                indicator=ind1,
                year=2000)

        self.assertEqual(len(cyi), len(self.test_data_countries))
        self.assertEqual(cyi[0].country.code, "PER")
        self.assertEqual(cyi[1].country.code, "BOL")
        self.assertEqual(cyi[2].country.code, "CHI")

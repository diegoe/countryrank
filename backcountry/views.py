from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from backcountry.models import CountryYearIndicator, Country, Indicator

def index(request):
    return HttpResponse('''
        Placeholder for enduser UI.
        ''')

def display_data(request):
    if request.method == 'GET':
        q_country = request.GET.get('country', None)
        q_indicator = request.GET.get('indicator', None)
        q_year = request.GET.get('year', None)

        r_cyi = CountryYearIndicator.objects.all()
        r_countries = Country.objects.all()
        r_indicators = Indicator.objects.all()

        if q_country is not None:
            r_countries = Country.objects.filter(code=q_country)
            if len(r_countries):
                r_cyi = r_cyi.filter(country=r_countries[0])

        if q_indicator is not None:
            r_indicators = Indicator.objects.filter(code=q_indicator)
            if len(r_indicators):
                r_cyi = r_cyi.filter(indicator=r_indicators[0])

        if q_year is not None and q_year.isdigit():
            r_cyi = r_cyi.filter(year=q_year)

        r_cyi = list(r_cyi.values())
        r_countries = list(r_countries.values())
        r_indicators = list(r_indicators.values())

        json = {
                'CountryYearIndicators' : r_cyi,
                'Countries' : r_countries,
                'Indicators' : r_indicators,
                }

    elif request.method == 'POST':
        json = { 'data' : None }

    return JsonResponse(json)

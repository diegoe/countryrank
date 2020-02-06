from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backcountry.models import CountryYearIndicator, Country, Indicator

import json

def index(request):
    return HttpResponse('''
        Placeholder for enduser UI.
        ''')

# TODO: This is a cheap way to avoid having to figure out what to do
# with the csfr cookie from Django.
@csrf_exempt
def display_data(request):
    jsonres = { 'data' : None }

    if request.method == 'GET':
        q_country = request.GET.get('country', None)
        q_indicator = request.GET.get('indicator', None)
        q_year = request.GET.get('year', None)

        r_countries = Country.objects.all()
        r_indicators = Indicator.objects.all()

        if q_country is not None:
            r_countries = Country.objects.filter(code=q_country)
        if q_indicator is not None:
            r_indicators = Indicator.objects.filter(code=q_indicator)

        tmp_r = {}
        for c in r_countries:
            tmp_r[c.code] = {}
            tmp_r[c.code]['code'] = c.code
            tmp_r[c.code]['name'] = c.name
            tmp_r[c.code]['id'] = c.id
            tmp_r[c.code]['indicators'] = {}

            # We could iterate over the whole countryyearindicator_set,
            # but that would require us to constantly access
            # indicator__code in each CountryYearIndicator, meaning we
            # would be hitting the Indicator table through the
            # ForeignKey in CYI.indicator.
            #
            # Instead we just go over our much smaller Indicator table,
            # and query the DB in chunks (per Indicator), reusing the
            # Indicator code in the process.
            for ind in r_indicators:
                cyi_pool = c.countryyearindicator_set.filter(indicator=ind)

                if q_year is not None and q_year.isdigit():
                    cyi_pool = cyi_pool.filter(year=q_year)

                tmp_r[c.code]['indicators'][ind.code] = {}
                tmp_r[c.code]['indicators'][ind.code]['data'] = [{ 'year' : x.year, 'value' : x.value, 'id': x.id } for x in cyi_pool]
                tmp_r[c.code]['indicators'][ind.code]['code'] = ind.code
                tmp_r[c.code]['indicators'][ind.code]['name'] = ind.name
                tmp_r[c.code]['indicators'][ind.code]['id'] = ind.id

        r_countries = list(r_countries.values())
        r_indicators = list(r_indicators.values())

        jsonres = {
                'CountryYearIndicators' : tmp_r,
                'Countries' : r_countries,
                'Indicators' : r_indicators,
                }
    elif request.method == 'POST':
        jsonres = { 'data' : None }
    elif request.method == 'PATCH':
        jsonres = { 'data' : 'PATCH' }
        patch = json.loads(request.body.decode())

        if patch and patch.get('op', None) == 'replace':
            if patch.get('path', None) and patch.get('value', None):
                path_id = patch['path'].split('/')[2]
                value = patch['value']

                cyi = CountryYearIndicator.objects.get(pk=path_id)
                cyi.value = value
                cyi.save()

    return JsonResponse(jsonres)

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
        q_limit = request.GET.get('limit', None)

        if q_country is not None:
            r_countries = Country.objects.filter(code=q_country)
        else:
            r_countries = Country.objects.all()

        if q_indicator is not None:
            r_indicators = Indicator.objects.filter(code=q_indicator)
        else:
            r_indicators = Indicator.objects.all()

        r_cyi = CountryYearIndicator.objects.all()

        cache_inds = {}
        for i in r_indicators:
            cache_inds[i.code] = {
                    'code' : i.code,
                    'name' : i.name,
                    'id' : i.id,
                    'data' : {},
                    }
        cache_ind_items = cache_inds.items()

        tmp_r = {}
        for c in r_countries:
            tmp_r[c.code] = {
                    'code' : c.code,
                    'name' : c.name,
                    'id' : c.id,
                    'indicators': cache_inds,
                    }

            for k,v in cache_ind_items:
                filters = {
                        'country' : c,
                        'indicator_id' : v['id'],
                        }
                if q_year is not None and q_year.isdigit():
                    filters['year'] = q_year

                if q_limit is not None:
                    cyi_pool = r_cyi.filter(**filters)[:1]
                else:
                    cyi_pool = r_cyi.filter(**filters)

                if not cyi_pool:
                    tmp_r[c.code]['indicators'][k]['data'] = []
                else:
                    tmp_r[c.code]['indicators'][k]['data'] = [{ 'year' : x.year, 'value' : x.value, 'id' : x.id } for x in cyi_pool]

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

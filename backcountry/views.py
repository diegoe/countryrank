from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        Placeholder for enduser UI.
        ''')

def display_data(request):
    return HttpResponse('''
        * GET: Retrieves data stored in the database.
        * PATCH: Updates fields in your data and save the changes to your datastore.''')

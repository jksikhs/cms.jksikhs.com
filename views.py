from django.shortcuts import render
import requests


def home(request):
    response = requests.get('https://api.covid19india.org/data.json')
    coviddata = response.json()
    try:
        for item in coviddata['statewise']:  # for name, age in dictionary.iteritems():  (for Python 2.x)
            if item['statecode'] == 'JK':
                return render(request, 'default.html', {
                    'confirmed': item['confirmed'],
                    'deltaconfirmed': item['deltaconfirmed'],
                    'deaths': item['deaths'],
                    'deltadeaths': item['deltadeaths'],
                    'lastupdatedtime': item['lastupdatedtime']
                })
    except Exception as err:
        print(err)
        return render(request, 'default.html', {
            'ip': "",
            'country': ""
        })

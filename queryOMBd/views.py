from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views import View
import requests
import urllib2
import json
# Create your views here.

from .forms import SubmitQueryForm

class queryIndexView(View):
    def get(self, request):
        the_form = SubmitQueryForm()
        context = {
            'title': 'Search your favourite movies and shows',
            'subTitle': 'Proudly powered by OMDb API',
            'form': the_form,
            'loadResults': 'False'
        }
        return render(request, "queryOMBd/index.html", context)

    def post(self, request):
        print(request.POST.get('query'))
        form = SubmitQueryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            query_response = omdbapi_search(form.cleaned_data['url'])
            context = {
                'title': 'Search your favourite movies and shows',
                'subTitle': 'Proudly powered by OMDb API',
                'form': form,
                'query': form.cleaned_data['url'],
                'loadResults': 'True',
                'response': query_response
            }
        return render(request, "queryOMBd/index.html", context)

def omdbapi_search(query):
    search_query = query.replace(' ', '+')
    url = 'http://www.omdbapi.com/?s=' + search_query
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    if data['Response'] == 'True':
        for item in data['Search']:
            print item['Title'], item['Year']
    return data;

'''
def index(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST['query'])
        print(request.POST.get('query'))
        form = SubmitQueryForm(request.POST)
        #if form.is_valid()
    return render(request, "queryOMBd/index.html", {})

def test(request):
    return HttpResponse('My second view!')

def profile(request):
    req = requests.get('http://www.omdbapi.com/?t=game+of+thrones')
    content = req.text
    return HttpResponse(content)
'''

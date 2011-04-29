# Create your views here.
from django.shortcuts import render_to_response

def landing_page(request):
    return render_to_response('main_site/index.html')

def index_blog(request):
    pass
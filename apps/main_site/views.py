# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main_site.models import Product,Product_category

def landing_page(request):
    return render_to_response('main_site/index.html',{
	'url' : 'blog',
	},context_instance=RequestContext(request))

def index_blog(request):
    return render_to_response('main_site/index.html',{
	'url' : 'blog',
	},context_instance=RequestContext(request))

def index_product(request):
    product = Product.objects.all()
    return render_to_response('main_site/product.html',{
	'url' : 'product',
	'product' : product,
	},context_instance=RequestContext(request))

def index_service(request):
    return render_to_response('main_site/index.html',{
	'url' : 'service',
	},context_instance=RequestContext(request))

def index_about(request):
    return render_to_response('main_site/index.html',{
	'url' : 'about',
	},context_instance=RequestContext(request))

def index_contact(request):
    return render_to_response('main_site/index.html',{
	'url' : 'contact',
	},context_instance=RequestContext(request))
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main_site.models import Product,Product_category,Static_content

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
    static = Static_content.objects.get(link='about')
    return render_to_response('main_site/about.html',{
	'url' : 'about',
	'content' : static,
	},context_instance=RequestContext(request))

def index_contact(request):
    return render_to_response('main_site/index.html',{
	'url' : 'contact',
	},context_instance=RequestContext(request))
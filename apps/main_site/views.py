# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from main_site.models import Product,Product_category,Static_content,Service

def index_product(request):
    product = Product.objects.all()
    return render_to_response('main_site/product.html',{
		'url' : 'product',
		'product' : product,
	},context_instance=RequestContext(request))

def index_service(request):
	service = Service.objects.all()
	return render_to_response('main_site/service.html',{
		'url' : 'service',
		'service' : service,
	},context_instance=RequestContext(request))

def index_about(request):
    static = Static_content.objects.get(link='about')
    return render_to_response('main_site/about.html',{
		'url' : 'about',
		'content' : static,
	},context_instance=RequestContext(request))

def index_contact(request):
	contact = Static_content.objects.get(link='contact')
	return render_to_response('main_site/contact.html',{
		'url' : 'contact',
		'contact' : contact,
	},context_instance=RequestContext(request))

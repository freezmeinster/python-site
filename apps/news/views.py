from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News

def index(request):
    news = News.objects.all()
    return render_to_response('main_site/index.html',{
	'url' : 'blog',
	'news' : news,
	},context_instance=RequestContext(request))
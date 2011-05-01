from main_site.models import Site_setting

def attr( request ) :
    site_setting = Site_setting.objects.all()
    site_attribute = {}
    for data in site_setting :
	site_attribute[''+data.key+''] = data.value
	
    return site_attribute
    
from django.contrib import admin
from main_site import models 

admin.site.register(models.Site_setting)
admin.site.register(models.Product)
admin.site.register(models.Product_category)
admin.site.register(models.Static_content)
admin.site.register(models.Service_category)
admin.site.register(models.Service)

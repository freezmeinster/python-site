from django.contrib import admin
from main_site.models import Site_setting,Product,Product_category

admin.site.register(Site_setting)
admin.site.register(Product)
admin.site.register(Product_category)
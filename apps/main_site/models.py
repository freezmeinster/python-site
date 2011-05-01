from django.db import models

class Site_setting( models.Model ):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    
    class Meta:
	verbose_name_plural = 'Daftar Setting'
	
    def __unicode__(self):
	return self.key
	
	
class Product_category( models.Model ):
    STATUS = (
	('A', 'Aktif'),
	('N', 'Tidak Aktif'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=1,choices=STATUS)
    
    class Meta:
	verbose_name_plural = 'Daftar Kategori'
	
    def __unicode__(self):
	return self.name
	
	
class Product( models.Model ):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="asset/product/")
    content = models.TextField()
    product_category = models.ManyToManyField(Product_category)
    
    class Meta:
	verbose_name_plural = 'Daftar Produk'
	
    def __unicode__(self):
	return self.name
	
    
    

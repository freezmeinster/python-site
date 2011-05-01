from django.db import models

class Site_setting( models.Model ):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    
    class Meta:
	verbose_name_plural = 'Daftar Setting'
	
    def __unicode__(self):
	return self.key
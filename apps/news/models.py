from django.db import models

class News( models.Model ):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="asset/news",blank=True,null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    news_category = models.ForeignKey('News_category')
    
    class Meta:
	verbose_name_plural = 'Daftar Berita'
	
    def __unicode__(self):
	return self.title
    

class News_category( models.Model ):
    STATUS = (
	('A' , 'Aktif'),
	('N' , 'Tidak Aktif'),
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=1,choices=STATUS)
    
    class Meta:
	verbose_name_plural = 'Daftar Kategori Berita'
	
    def __unicode__(self):
	return self.name

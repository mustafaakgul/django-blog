from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='isim', unique=True)   # auto slug olsuturmak icin unique ile otomatk kendi ayarlıcak sonuan 1 2 felna koyacak

    class Meta:
        db_table = 'kategori'    #db icindeki tablo adi
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.isim


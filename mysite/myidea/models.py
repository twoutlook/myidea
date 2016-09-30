from django.db import models

# Create your models here.
class Myidea(models.Model):
    f00 = models.CharField(default=".", max_length=99,verbose_name="編號")
    f01 = models.CharField(default=".", max_length=200,verbose_name="主題")
    f02 = models.CharField(default=".", max_length=2000,verbose_name="說明")

    def __str__(self):
        return self.f01+" "+self.f02;
    # class Meta:
    #     verbose_name = "項目需求說明"
    #     verbose_name_plural = "項目需求說明"
        # app_label = u"項目"

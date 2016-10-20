from django.db import models

# Create your models here.
class Mnemonics(models.Model):
    num1= models.IntegerField(default=19,verbose_name="幾式")
    num2 = models.IntegerField(default=1,verbose_name="第幾式")
    num3 = models.IntegerField(default=0,verbose_name="第幾動")
    data = models.CharField(max_length=200,verbose_name="口訣")
    def __str__(self):
        return str(self.num1)+"-"+str(self.num2).zfill(2)+"-"+str(self.num3).zfill(2)+" "+self.data
        
    class Meta:
        verbose_name = "口訣"
        verbose_name_plural = "口訣"

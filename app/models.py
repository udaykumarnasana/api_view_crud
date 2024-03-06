from django.db import models

# Create your models here.

class productcatogory(models.Model):
    pcid=models.IntegerField(primary_key=True)
    pcname=models.CharField(max_length=100)

    def __str__(self):
        return self.pcname


class product(models.Model):
    pcid=models.ForeignKey(productcatogory,on_delete=models.CASCADE)
    pcname=models.CharField(max_length=100)
    pcprice=models.IntegerField()
    pcbrand=models.CharField(max_length=100)

    def __str__(self):
        return self.pcname
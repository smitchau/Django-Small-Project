from django.db import models

# Create your models here.

class Product_mst(models.Model):
    product_name = models.CharField(max_length=30)
    
class Product_sub_cat(models.Model):
    pid = models.ForeignKey(Product_mst,on_delete=models.CASCADE,null=True) 
    p_price = models.PositiveIntegerField()
    p_image = models.ImageField(upload_to="images/")
    p_model = models.CharField(max_length=30)
    p_ram = models.CharField(max_length=30)
from django.db import models

# Create your models here.
class manTshirt(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class manShirt(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class womanScart(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class laptop(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class mobile(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class computer(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class jumkas(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class necklaces(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
    
class kangans(models.Model):
    productName= models.CharField(max_length=100)
    productPrice= models.FloatField()
    productImage= models.ImageField(upload_to='product_images')

    def __str__(self):
        return "%s" %(self.productName)  (self.productPrice)
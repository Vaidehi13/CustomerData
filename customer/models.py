from django.db import models  
class Customer(models.Model):  
    custid = models.CharField(max_length=20)  
    custname = models.CharField(max_length=100)  
    custaddress = models.CharField(max_length=1000) 
    meterno = models.CharField(max_length=20) 
    class Meta:  
        db_table = "customer"  
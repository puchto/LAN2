from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Auth_record(models.Model):
    loc_file = models.CharField(max_length = 50)
    cl_address = models.CharField(max_length = 50)
    mac = models.CharField(max_length = 17)
    ip_add = models.CharField(max_length = 15)
    kl_service = models.CharField(max_length = 1)
    downl = models.CharField(max_length = 6)
    upl = models.CharField(max_length = 6)
    
    class Meta:
        db_table = "LAN_Sosnowiec_klienci"
        
    def __str__(self):
        return self.cl_address
        
class Arp_ent(models.Model):
    cl_address = models.CharField(max_length = 100)
    mac = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "Arp_ent"
    
    def __str__(self):
        return self.cl_address
        
class Client_rec(models.Model):
    loc_file = models.CharField(max_length = 50)
    ln_nr = models.IntegerField()
    cl_address = models.CharField(max_length = 50)
    mac = models.CharField(max_length = 17)
    ip_add = models.CharField(max_length = 15)
    kl_service = models.CharField(max_length = 1)
    downl = models.CharField(max_length = 6)
    upl = models.CharField(max_length = 6)
    
    class Meta:
        db_table = "LAN_server_clients"
        
    def __str__(self):
        return self.cl_address
#model z oddzielnymi polami adresu, jak jest wiecej niz 3 
class Client_fw(models.Model):
    loc_file = models.CharField(max_length = 50)
    ln_nr = models.IntegerField()
    cl_address_ul = models.CharField(max_length = 50)
    cl_address_nr_d = models.CharField(max_length = 50)
    cl_address_nr_m = models.CharField(max_length = 50)
    cl_address_rest = models.CharField(max_length = 50)
    mac = models.CharField(max_length = 17)
    ip_add = models.CharField(max_length = 15)
    kl_service = models.CharField(max_length = 1)
    downl = models.CharField(max_length = 6)
    upl = models.CharField(max_length = 6)
    
    class Meta:
        db_table = "LAN_Client_fw"
        
    def __str__(self):
        return self.cl_address_ul
    
from django.db import models

# Create your models here.
class Requests(models.Model):
    r_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)

class Customer(models.Model):
    u_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)

class Manufacturer(models.Model):
    u_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)

class Distributor(models.Model):
    u_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)

class Pharmacy(models.Model):
    u_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    p_address=models.CharField(max_length=255)


class Medicine(models.Model):
    m_id=models.IntegerField(primary_key=True)
    med_name=models.CharField(max_length=255)
    ingredients=models.CharField(max_length=255)
    exp_date=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    dstbtr_lat=models.CharField(max_length=255)
    dstbtr_long=models.CharField(max_length=255)
    d_public_key=models.CharField(max_length=255)
    manufacturer_name=models.CharField(max_length=255)
    hash_value=models.CharField(max_length=255)
    avail_quantity=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

class Distributed_items(models.Model):
    m_id=models.IntegerField(primary_key=True)
    med_name=models.CharField(max_length=255)
    ingredients=models.CharField(max_length=255)
    exp_date=models.CharField(max_length=255)
    quantity=models.CharField(max_length=255)
    avail_quantity=models.CharField(max_length=255)
    hash_value=models.CharField(max_length=255)
    pharmacy_pub_key=models.CharField(max_length=255)
    dist_pub_key=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
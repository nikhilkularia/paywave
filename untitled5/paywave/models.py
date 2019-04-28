from django.db import models


# Create your models here.
class mobiles(models.Model):
    service_type=models.CharField(max_length=128)
    phone_number = models.BigIntegerField()
    operator = models.CharField(max_length=20)
    circle = models.CharField(max_length=20)
    amount = models.SmallIntegerField()

class dthcardform(models.Model):
    dth_operator = models.CharField(max_length=128)
    dth_customer = models.CharField(max_length=128)
    dth_amount = models.IntegerField()


class creditcard(models.Model):
    email = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    name_on_card=models.CharField(max_length=256)
    card_number=models.BigIntegerField()
    expire_month=models.SmallIntegerField()
    expire_year = models.SmallIntegerField()
    cvv_number=models.SmallIntegerField()

class eletricity(models.Model):
    service_provider=models.CharField(max_length=128)
    elec_customer_id=models.CharField(max_length=20)

class gasprovider(models.Model):
    gas_provider=models.CharField(max_length=128)
    bp_number=models.CharField(max_length=20)





class datacardform(models.Model):
    service_type=models.CharField(max_length=128)
    phone_number = models.BigIntegerField()
    operator = models.CharField(max_length=20)
    circle = models.CharField(max_length=20)
    amount = models.SmallIntegerField()

class waterform(models.Model):
    water_operator=models.CharField(max_length=128)
    wnumber=models.CharField(max_length=20)

class landlineform(models.Model):
    landline_operator=models.CharField(max_length=128)
    phone_number=models.CharField(max_length=20)

class broadbandform(models.Model):
    broadband_operator=models.CharField(max_length=128)
    phone_number=models.CharField(max_length=20)


class metroform(models.Model):
    metro_operator=models.CharField(max_length=128)
    metro_number=models.CharField(max_length=20)




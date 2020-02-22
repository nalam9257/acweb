from django.db import models
class details(models.Model):
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=100)
	mobile=models.IntegerField()
	order=models.CharField(max_length=20)
	actype=models.CharField(max_length=20)
	address=models.CharField(max_length=300)
	def __str__(self):
		return self.name
		return self.email
		return self.mobile
		return self.order
		return self.actype
		return self.address


from django.db import models
class details1(models.Model):
	name1=models.CharField(max_length=200)
	email1=models.EmailField(max_length=100)
	mobile1=models.IntegerField()
	order1=models.CharField(max_length=20)
	actype1=models.CharField(max_length=20)
	address1=models.CharField(max_length=300)
	def __str__(self):
		return self.name1
		return self.email1
		return self.mobile1
		return self.order1
		return self.actype1
		return self.address1

# Create your models here.

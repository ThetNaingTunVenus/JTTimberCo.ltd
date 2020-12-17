from django.db import models


# Create your models here.
class InquiryModel(models.Model):
	name = models.CharField(max_length=200)
	business = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	logs = models.CharField(max_length=200)
	veneers = models.CharField(max_length=200)
	decking = models.CharField(max_length=200)
	boards = models.CharField(max_length=200)
	flooring = models.CharField(max_length=200)
	skirtings = models.CharField(max_length=200)
	

	def __str__(self):
		return self.name

class VeneerModel(models.Model):
	vproductId = models.CharField(max_length=200)
	vthickness = models.CharField(max_length=200)
	vwidth = models.CharField(max_length=200)
	vlength = models.CharField(max_length=200)

	def __str__(self):
		return self.vproductId

class DeckingModel(models.Model):
	dproductId = models.CharField(max_length=200)
	dthickness = models.CharField(max_length=200)
	dwidth = models.CharField(max_length=200)
	dlength = models.CharField(max_length=200)

	def __str__(self):
		return self.dproductId

class LumberModel(models.Model):
	lproductId = models.CharField(max_length=200)
	lthickness = models.CharField(max_length=200)
	lwidth = models.CharField(max_length=200)
	llength = models.CharField(max_length=200)

	def __str__(self):
		return self.lproductId

class MoldingModel(models.Model):
	mproductId = models.CharField(max_length=200)
	mthickness = models.CharField(max_length=200)
	mwidth = models.CharField(max_length=200)
	mlength = models.CharField(max_length=200)

	def __str__(self):
		return self.mproductId


class AgedModel(models.Model):
	aproductId = models.CharField(max_length=200)
	athickness = models.CharField(max_length=200)
	awidth = models.CharField(max_length=200)
	alength = models.CharField(max_length=200)

	def __str__(self):
		return self.aproductId


from django.db import models
from django.conf import settings

# Create your models here.
class UserData(models.Model):
	Join_Date=models.DateTimeField(auto_now=True)
	User_ID=models.CharField(max_length=50, primary_key=True)
	User_Name=models.CharField(max_length=100)
	User_Email=models.CharField(max_length=100)
	User_Mobile=models.CharField(max_length=15)
	User_Gender=models.CharField(max_length=10)
	User_Age=models.CharField(max_length=5)
	User_City=models.CharField(max_length=50)
	User_Password=models.CharField(max_length=20, default='Not Set')
	User_Pic=models.FileField(upload_to='profilepictures/', default='download.png')
	Status=models.CharField(max_length=10, default='Deactive')
	class Meta:
		db_table="UserData"

class UserPictureData(models.Model):
	User_ID=models.CharField(max_length=50)
	User_Pic=models.FileField(upload_to='profilepictures/', default='download.png')
	class Meta:
		db_table="UserPictureData"

class Sitemap(models.Model):
	Sitemap=models.CharField(max_length=2000)
	class Meta:
		db_table="Sitemap"

class Keywords(models.Model):
	Keywords=models.CharField(max_length=2000)
	class Meta:
		db_table="Keywords"

class Description(models.Model):
	Description=models.CharField(max_length=2000)
	class Meta:
		db_table="Description"

class AdminData(models.Model):
	Password=models.CharField(max_length=20)
	class Meta:
		db_table="AdminData"
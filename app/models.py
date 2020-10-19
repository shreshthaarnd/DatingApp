from django.db import models

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
	Status=models.CharField(max_length=10, default='Deactive')
	class Meta:
		db_table="UserData"
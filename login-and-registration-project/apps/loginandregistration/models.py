from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]$')
NAME_REGEX = re.compile(r'^[a-zA-Z]$')

class UserManager(models.Manager):

	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors["first_name"] = "First name should be more than 1 characters"
		if NAME_REGEX.match(postData['first_name']):
			errors['first_name'] = "Please, enter a valid first name"
		if len(postData['last_name']) < 1:
			errors["last_name"] = "Last name should be more than 1 characters"
		if NAME_REGEX.match(postData['last_name']):
			errors['last_name'] = "Please, enter a valid last name"
		if len(postData['email']) < 1:
			errors['"email'] = "Email is needed"
		if EMAIL_REGEX.match(postData['email']):
			errors["email"] = "Not a valid Email"
		if len(postData['password']) < 8:
			errors['password'] = "Your password must be longer than 8 characters"
		if postData['password'] != postData['confirmpassword']:
			errors['password'] = "Your passwords do not match"
		dbemailcheck = User.objects.filter(email=postData['email'])
		if len(dbemailcheck) != 0:
			errors['password'] = "You already have a account, please login"
		if len(errors) < 1:
			errors['success'] = "Successfully registered!"
		return errors

	def login_validator(self, postData):
		errors = {}
		user = User.objects.filter(email=postData['email'])
		if len(user) == 0:
			errors['error2'] = "Not a registered email or password, please register"
		else:
			if postData['email'] == User.objects.get(email=postData['email']).email:
				dbpassword = User.objects.get(email=postData['email']).password
				if bcrypt.checkpw(postData['password'].encode(), dbpassword.encode()) == False:
					errors['error3'] = "Invalid login"
		return errors

class User(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)	
	objects = UserManager()
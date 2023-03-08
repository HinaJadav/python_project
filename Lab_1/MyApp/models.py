from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=20, default="20")
    user_password = models.CharField(max_length=20, default="20")
    name = models.CharField(max_length=20, default="20")
    address = models.TextField(max_length=50, default="null")
    contact_no = models.CharField(max_length=10, default="null")
    email_id = models.CharField(max_length=20, default="null")
    profession_details = models.TextField(max_length=50, default="np")
    # image_location = models.CharField(max_length=40, default="null")
    photo = models.ImageField(upload_to="img", default="null")
    gender = models.CharField(max_length=10, default="m")
    age = models.CharField(max_length=20, default="20")

class Administrator(models.Model):
    admin_id = models.CharField(max_length=20, primary_key=True)
    admin_username = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=20)

class Content(models.Model):
    content_id = models.CharField(max_length=20)
    content_name = models.CharField(max_length=40)
    content_location = models.CharField(max_length=40)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to="img", default="null")

class like_content(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    like_status = models.CharField(max_length=1)
    like_id = models.CharField(max_length=40, primary_key=True)

class Image(models.Model):
    photo = models.ImageField(upload_to="img")

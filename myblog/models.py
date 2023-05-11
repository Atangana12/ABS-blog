from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreateBlog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.title

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(CreateBlog, related_name='Comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="inconnu")
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added'] 

#class Contact(models.Model):
#name = models.CharField(max_length=100, default="inconnu")
    #email = models.EmailField()
   # body = models.TextField()
    #phone_number = models.CharField(max_length=20)
    #date_added = models.DateTimeField(auto_now=True)

   # def __str__(self):
      #  return self.name

    #class Meta:
       # ordering = ['-date_added'] 

#class User(models.Model):
    #username = models.CharField(max_length=50, default='inconnu')
   # Email= models.EmailField()
   # First_Name = models.CharField(max_length=100, default='inconnu')
   # Last_Name = models.CharField(max_length=100, default='inconnu')
   # Phone_Number = models.CharField(max_length=20)
    #date_added = models.DateTimeField(auto_now=True)

    #def __str__(self):
       # return self.username

   # class Meta:
       # ordering = ['-date_added']    

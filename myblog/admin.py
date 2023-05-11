from django.contrib import admin
from . models import CreateBlog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'slug',  'author', 'date_added')

#class ContactAdmin(admin.ModelAdmin):
   # list_display = ('name', 'email', 'phone_number', 'body', 'date_added') 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','body','email','name','date_added')

#class User(admin.ModelAdmin):
    #list_display = ('username', 'Email', 'First_Name', 'Last_Name', 'Phone_Number', 'date_added')   

    admin.site.register(CreateBlog, BlogAdmin)
    #admin.site.register(Contact)
    admin.site.register(Comment)
    #admin.site.register(User)

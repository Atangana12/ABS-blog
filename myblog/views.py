from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import CreateBlog, Comment
from . forms import BlogForm




# Create your views here.
class List(ListView):
    template_name = 'blog/index.html'
    queryset = CreateBlog.objects.all()
    paginate_by = 3

#  custom user

 # detail list view
def detailView(request, slug):
    post = CreateBlog.objects.get(slug=slug)
    Comment = post.Comments.all()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post = post
            form.save()
            return redirect('detailView', slug=post.slug)
    else:
        form = BlogForm()

    content = {
        'article':post,
        'Comment':Comment,
        'form':form,
    }
    return render(request, 'blog/update.html', content)

#def user(request):
   # user = request.user
   # if request.method == 'POST':
        #form = UserForm(request.POST, instance=user)
       # if form.is_valid():
           # form.save()
          #  return redirect('user')
    #else:
        #form = UserForm(instance=user)
        #return render(request, 'blog/user.html', {'form':form})        
   


def search(request):
    if request.method=="GET":
        search = request.GET.get('q')
        post = CreateBlog.objects.filter(title__icontains = search)
    return render(request, 'blog/search.html', {'post':post})

#def Contact(request):
    #if request.method == 'POST':
       # form = ContactForm(request.POST)
       # if form.is_valid():
           # form.save(commit=False)
           # form.instance.contact = contact
           # form.save()
          # return redirect('Contact')
    #else:
        #form = ContactForm()

#def Contact_list(request):
    #Contact = Contact.objects.all()
    #return render(request, 'blog/contact.html', {'Contact':Contact})



def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def Contact(request):
    return render(request, 'blog/contact.html')


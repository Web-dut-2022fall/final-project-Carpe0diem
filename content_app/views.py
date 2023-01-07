from django.shortcuts import render,redirect
from content_app.models import Blog
# Create your views here.
def home(request):
    blog=Blog.objects.all()
    return render(request,'home.html',{'blogs':blog})

def add(request):
    if  request.method == 'GET':
        return render(request,'add.html')
    else:
        title= request.POST['title']
        content=request.POST['content']
        Blog.objects.create(title=title,content=content,author_id=request.user.id)
        return redirect('home')

def edit(request,id):
    blog=Blog.objects.get(id=id)
    if request.method=='GET':
        return render(request,'edit.html',{'blogs':blog})
    
    else:
        blog.title=request.POST['title']
        blog.content=request.POST['content']
        blog.save()
        return redirect('home')

def delete(request,id):
    Blog.objects.get(id=id).delete()
    return redirect('home')

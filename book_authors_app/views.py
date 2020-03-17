from django.shortcuts import render, redirect
from .models import Book, Author
def index(request):
    context={
        "allbooks":Book.objects.all()
    }
    
    return render(request, "index.html", context)

def addabook(request):
    
    Book.objects.create(title=request.POST["title"], description=request.POST["description"])
    return redirect("/")

def bookdesc(request, id):
    context={
        "onebook":Book.objects.get(id=id),
        "appendauthor":Author.objects.all()
    }
    return render(request, "onebook.html",context)

def addauthor(request):
    b=Book.objects.get(id=request.POST["books"])
    a=Author.objects.get(id=request.POST["author"])
    b.author.add(a)
    return redirect(f"books/{b.id}")

def authors(request):

    context={
        "allauthors": Author.objects.all()
    }
    return render(request, "authorinfo.html", context)
    

def createauthor(request):
    Author.objects.create(first_name= request.POST["firstname"], last_name=request.POST["lastname"])
    
    return redirect("/authors")

def oneauthor(request, id):
    context={
        "author":Author.objects.get(id=id),
        "allbooks":Book.objects.all()
    }
    return render(request, "oneauthor.html", context)

def authoredby(request):
    b=Book.objects.get(id=request.POST["books"])
    a=Author.objects.get(id=request.POST["author"])
    b.author.add(a)

    return redirect(f"author/{a.id}")


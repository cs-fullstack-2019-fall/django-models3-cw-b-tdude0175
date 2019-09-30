from django.shortcuts import render, HttpResponse
from .models import Book
# Create your views here.
def index(req):
    return HttpResponse("You are in the index")

def all(req):
    books= Book.objects.all()
    endString = ""
    for singleBook in books:
        endString += str(singleBook)
    return HttpResponse(endString)

def past2018(req):
    books= Book.objects.all()
    endString = ""
    for singleBook in books:
        if(str(singleBook.publishDate) > "2018-01-01"):
            endString += str(singleBook)
    return HttpResponse(endString)

def addBook(req):
    newBook = Book(name="White Rose", pageNumber = 300, genre = "Dark Fantasy")
    newBook.save()
    return HttpResponse("check your admin")
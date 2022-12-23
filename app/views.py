import json
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET

from app.forms import BookForm, AuthorForm
from app.models import Book, Author


# Create your views here.
def index(request):
    authors = Author.objects.all()
    return render(request, 'index.html', {'authors': authors})


def book_list(request):
    return render(request, 'book_list.html', {
        'books': Book.objects.all(),
    })


def author_list(request):
    return render(request, 'author_list.html', {
        'authors': Author.objects.all(),
    })

def author_select(request):
    return render(request, 'author_select.html', {
        'authors': Author.objects.all(),
    })


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()

    return render(request, 'book_form.html', {
        'form': form,
    })


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "authorListChanged": None,
                        "showMessage": f"{author.name} adicionado."
                    })
                })
    else:
        form = AuthorForm()

    return render(request, 'author_form.html', {
        'form': form,
    })


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "bookListChanged": None,
                        "selectChanged": None,
                        "showMessage": f"{book.title} atualizado."
                    })
                }
            )
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {
        'form': form,
        'book': book,
    })


def remove_book(request, pk):
    movie = get_object_or_404(Book, pk=pk)
    movie.delete()
    return redirect('index')
    # return HttpResponse(
    #     status=204,
    #     headers={
    #         'HX-Trigger': json.dumps({
    #             "bookListChanged": None,
    #             "selectChanged": None,
    #             "showMessage": f"{movie.title} removido."
    #         })
    #     })

@require_GET
def remove_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "authorListChanged": None,
                "showMessage": f"{author.name} removido."
            })
        })
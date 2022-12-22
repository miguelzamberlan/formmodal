import json
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from app.forms import BookForm
from app.models import Book


# Create your views here.
def index(request):
    return render(request, 'index.html', {'selecionado': 0})


def book_list(request):
    return render(request, 'book_list.html', {
        'books': Book.objects.all(),
    })


def book_select(request, id):
    return render(request, 'book_select.html', {
        'books': Book.objects.all(),
        'selecionado': id,
    })


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "bookListChanged": None,
                        "selectChanged": None,
                        "showMessage": f"{book.title} adicionado."
                    })
                })
    else:
        form = BookForm()

    return render(request, 'book_form.html', {
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


@ require_POST
def remove_book(request, pk):
    movie = get_object_or_404(Book, pk=pk)
    movie.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "bookListChanged": None,
                "selectChanged": None,
                "showMessage": f"{movie.title} removido."
            })
        })
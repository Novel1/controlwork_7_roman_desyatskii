from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import GuestBook, StatusChoice


# Create your views here.


def index_view(request):
    book = GuestBook.objects.exclude(is_deleted=True).order_by('-created_at').filter(status='ACTIVE')
    context = {
        'book': book
    }
    return render(request, 'index.html', context=context)


def add_view(request):
    if request.method == 'GET':
        return render(request, 'add.html', context={'choices': StatusChoice.choices})
    book_get = {
        'author': request.POST.get('author'),
        'text': request.POST.get('text'),
        'email': request.POST.get('email'),
    }
    GuestBook.objects.create(**book_get)
    return redirect('index')


def update_view(request, pk):
    book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'POST':
        book.author = request.POST.get('author')
        book.text = request.POST.get('text')
        book.email = request.POST.get('email')
        book.save()
        return redirect('index')
    return render(request, 'update.html', context={'book': book})


def delete_view(request, pk):
    book = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'book_confirm_delete.html', context={'book': book})


def confirm_delete(request, pk):
    book = get_object_or_404(GuestBook, pk=pk)
    book.delete()
    return redirect('index')

# Коментарі для цього файлу я робив за допомогою Gemini 3.1 Pro


from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()  # Видаляємо об'єкт з бази
        return redirect("book_list")  # Повертаємось до списку

    return render(request, "library/delete_confirm.html", {"book": book})


def edit_book(request, pk):
    # Знаходимо книгу за її ID або видаємо помилку 404
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        # Передаємо дані з POST і вказуємо, яку саме книгу оновлюємо
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        # Відкриваємо форму з уже заповненими даними книги
        form = BookForm(instance=book)

    return render(request, "library/edit.html", {"form": form})


def book_list(request):
    # Отримуємо всі записи з таблиці Book
    books = Book.objects.all()
    # Передаємо їх у шаблон через словник
    return render(request, "library/index.html", {"books": books})


def create_book(request):
    if request.method == "POST":
        # Передаємо в форму те, що ввів користувач
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Після збереження перекидаємо на головну
    else:
        form = (
            BookForm()
        )  # Якщо користувач просто зайшов на сторінку - даємо йому порожню форму

    # Відправляємо форму в HTML
    return render(request, "library/create.html", {"form": form})

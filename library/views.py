# Коментарі для цього файлу я робив за допомогою Gemini 3.1 Pro


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff)
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
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/edit.html"
    success_url = reverse_lazy("book_list")

    def test_func(self):
        return self.request.user.is_staff

def book_list(request):
    # Отримуємо всі записи з таблиці Book
    books = Book.objects.all()
    # Передаємо їх у шаблон через словник
    return render(request, "library/index.html", {"books": books})


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/create.html"
    success_url = reverse_lazy("book_list")

    def test_func(self):
        return self.request.user.is_staff

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Автоматично логінимо після реєстрації
            return redirect("book_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

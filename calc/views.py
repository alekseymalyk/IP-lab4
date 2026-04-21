from django.shortcuts import render


# Математичні функції для обробки
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Помилка: Ділення на нуль!"
    return a / b


def kb_to_bytes(kb):
    if 1 <= kb <= 1000000:
        return kb * 1024
    return "Помилка: Значення KB має бути від 1 до 1,000,000"


# Головна VIEW, яка координує роботу
def index(request):
    res = None
    if request.method == "POST":
        try:
            num1_raw = request.POST.get("num1")
            num2_raw = request.POST.get("num2")
            operation = request.POST.get("operation")
            precision = int(request.POST.get("precision", 2))

            num1 = float(num1_raw) if num1_raw else 0
            num2 = float(num2_raw) if num2_raw else 0

            # Виклик відповідної функції залежно від операції
            if operation == "add":
                res = add(num1, num2)
            elif operation == "sub":
                res = sub(num1, num2)
            elif operation == "mul":
                res = mul(num1, num2)
            elif operation == "div":
                res = div(num1, num2)
            elif operation == "kb_to_b":
                res = kb_to_bytes(num1)

            # Форматування результату, якщо це число
            if isinstance(res, (int, float)):
                res = f"{res:.{precision}f}"

        except ValueError:
            res = "Помилка: Введіть коректні числа"

    return render(request, "calc/index.html", {"result": res})

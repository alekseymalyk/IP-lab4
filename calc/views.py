from django.shortcuts import render

# Create your views here.
def index(request):
    res = None
    if request.method == "POST":
        try:
            # Отримання даних з POST-запиту
            num1_raw = request.POST.get("num1")
            num2_raw = request.POST.get("num2")
            operation = request.POST.get("operation")
            precision = int(request.POST.get("precision", 2))

            # Перетворення в числа (num2 може бути порожнім для інженерних операцій)
            num1 = float(num1_raw) if num1_raw else 0
            num2 = float(num2_raw) if num2_raw else 0

            # Основна логіка калькулятора
            if operation == "add":
                res = num1 + num2
            elif operation == "sub":
                res = num1 - num2
            elif operation == "mul":
                res = num1 * num2
            elif operation == "div":
                if num2 == 0:
                    res = "Помилка: Ділення на нуль!"
                else:
                    res = num1 / num2
            elif operation == "kb_to_b":
                # Перевірка діапазону згідно з вимогами (1 - 1,000,000)
                if 1 <= num1 <= 1000000:
                    res = num1 * 1024
                else:
                    res = "Помилка: Значення KB має бути від 1 до 1,000,000"

            # Форматування результату з заданою точністю, якщо це число
            if isinstance(res, (int, float)):
                res = f"{res:.{precision}f}"

        except ValueError:
            res = "Помилка: Введіть коректні числові значення"

    return render(request, "calc/index.html", {"result": res})

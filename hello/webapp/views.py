from django.shortcuts import render


# Create your views here

def calculate(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        val1 = int(request.POST.get('num1'))
        val2 = int(request.POST.get('num2'))
        action = request.POST.get('action')
        res = 0
        if action == 'add':
            res = f"{val1} + {val2} = {val1 + val2}"
        elif action == 'subtract':
            res = f"{val1} - {val2} = {val1 - val2}"
        elif action == 'multiply':
            res = f"{val1} * {val2} = {val1 * val2}"
        elif action == 'divide':
            res = f"{val1} / {val2} = {val1 / val2}"
    return render(request, 'index.html', {"result": res})



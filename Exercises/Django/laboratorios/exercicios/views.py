from django.shortcuts import render

def ex1(request):
    return render(request, 'ex1.html')

def ex2(request):
    data = {}
    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        total = int(valor1) + int(valor2)
        data['total'] = total
    return render(request, 'ex2.html', data)

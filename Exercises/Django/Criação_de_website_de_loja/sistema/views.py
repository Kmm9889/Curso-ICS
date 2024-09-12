from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def Produtos(request):
    
    produtos_loja = {
    'produtos': [
        {
            'id': 2,
            'nome': 'Civic',
            'marca': 'Honda',
            'modelo': 'Civic EX',
            'ano': 2022,
            'preco': 95000.00
        },
        {
            'id': 1,
            'nome': 'Fusca',
            'marca': 'Volkswagen',
            'modelo': 'Fusca 1300',
            'ano': 1975,
            'preco': 15000.00
        },
        {
            'id': 3,
            'nome': 'Corolla',
            'marca': 'Toyota',
            'modelo': 'Corolla XEI',
            'ano': 2020,
            'preco': 85000.00
        },
        {
            'id': 4,
            'nome': 'Mustang',
            'marca': 'Ford',
            'modelo': 'Mustang GT',
            'ano': 2023,
            'preco': 250000.00
        },
        {
            'id': 5,
            'nome': 'Onix',
            'marca': 'Chevrolet',
            'modelo': 'Onix LT',
            'ano': 2021,
            'preco': 60000.00
        },
        {
            'id': 6,
            'nome': 'Santa Fé',
            'marca': 'Hyundai',
            'modelo': 'Santa Fé GLS',
            'ano': 2019,
            'preco': 120000.00
        }
    ]
}


    return render(request, "Produtos.html", produtos_loja)

def Sobre_a_loja(request):
    return render(request, "Sobre_a_loja.html")

def Contato(request):
    return render(request, "Contato.html")
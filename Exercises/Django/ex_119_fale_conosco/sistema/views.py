from django.shortcuts import render

localização_da_empresa = {
   "dados_da_empresa":[ 
    "Endereço: Rua Exemplo123"," Bairro Exemplo", "Cidade Exemplo - Estado", "CEP 12345-678",
   "Telefone: (12) 3456-7890",
   "E-mail: contato@empresa.com.br"]
}
def fale_conosco(request):
    return render(request, "fale_conosco.html")

def localização(request):
    return render(request, "localizacao.html", localização_da_empresa)
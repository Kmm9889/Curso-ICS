from django.shortcuts import render

todos_eventos = {
    "Todos_os_eventos": [
    "Primeiro Caminho do Homem na Lua - Realizado em 20 de julho de 1969",
    "Queda do Muro de Berlim - Ocorrido em 9 de novembro de 1989",
    "Início da Segunda Guerra Mundial - Começou em 1º de setembro de 1939",
    "Assinatura do Tratado de Versalhes - Assinado em 28 de junho de 1919",
    "Descoberta da Penicilina por Alexander Fleming - Anunciada em 1928"
    "Lançamento de um Novo Satélite Espacial - Previsto para 2025",
    "Cúpula Internacional sobre Mudanças Climáticas - Programada para 2024",
    "Exposição Mundial de Tecnologias Emergentes - Agendada para 2026",
    "Missão à Marte - Planejada para 2030",
    "Avanços na Medicina Genética - Conferência a ser realizada em 2025",
    ]
    
   
}

eventos_f =  {
    "eventosFuturos": [
    "Lançamento de um Novo Satélite Espacial - Previsto para 2025",
    "Cúpula Internacional sobre Mudanças Climáticas - Programada para 2024",
    "Exposição Mundial de Tecnologias Emergentes - Agendada para 2026",
    "Missão à Marte - Planejada para 2030",
    "Avanços na Medicina Genética - Conferência a ser realizada em 2025"
  ]

}
       

eventos_p = {
    "eventosPassados": [
    "Primeiro Caminho do Homem na Lua - Realizado em 20 de julho de 1969",
    "Queda do Muro de Berlim - Ocorrido em 9 de novembro de 1989",
    "Início da Segunda Guerra Mundial - Começou em 1º de setembro de 1939",
    "Assinatura do Tratado de Versalhes - Assinado em 28 de junho de 1919",
    "Descoberta da Penicilina por Alexander Fleming - Anunciada em 1928"
    ]
    }

def eventos_passados(request):
    return render(request, "eventos_passados.html", eventos_p)

def eventos_futuros(request):
    return render(request, "eventos_futuros.html", eventos_f)

def todos_os_eventos(request):
    return render(request, "todos_os_eventos.html", todos_eventos)

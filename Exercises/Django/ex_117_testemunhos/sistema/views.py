from django.shortcuts import render

testemunhos_f = {    
        "Funcionarios": ["Carlos Pereira:" "Trabalhar aqui tem sido uma experiência incrível. A empresa oferece um ambiente de trabalho acolhedor e oportunidades de crescimento profissional.",

        "Ana Costa: Adoro o ambiente de trabalho e a colaboração entre todos. A equipe é unida e sempre pronta para apoiar uns aos outros.",

        "Felipe Rocha: Aqui, sinto que posso crescer e me desenvolver constantemente. O apoio dos colegas e a liderança são excelentes.",

        "Juliana Martins: É um prazer trabalhar nesta empresa. A cultura de inovação e a dedicação ao bem-estar dos funcionários são notáveis."
        ]
}

testemunhos_c = {

    "Clientes":["João Silva: Excelente serviço! Recomendo a todos. A equipe foi extremamente atenciosa e resolveu todos os problemas de forma rápida e eficiente.",

    "Maria Oliveira: A experiência foi fantástica. A equipe demonstrou um profissionalismo impressionante e fez tudo para garantir que minhas necessidades fossem atendidas.",

    "Pedro Santos: Muito satisfeito com o atendimento! A qualidade dos produtos é excepcional e o suporte ao cliente é impecável.",

    "Luciana Almeida: O serviço superou minhas expectativas. A equipe foi cordial e o resultado final foi excelente. Com certeza voltarei a contratar."]

       }

def testemunho_funcionarios(request):
    return render(request, "testemunho_funcionarios.html", testemunhos_f)

def testemunho_clientes(request):
    return render(request, "testemunho_clientes.html", testemunhos_c)
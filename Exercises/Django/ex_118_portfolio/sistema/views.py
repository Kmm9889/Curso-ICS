from django.shortcuts import render

todos_protfólios = {
        "Todos_os_Portfólios":[
        "Logotipos",
        "Cartazes",
        "Materiais de marketing (flyers, banners)",
        "Capas de livros ou revistas",
        "Layouts de sites",
        "Interfaces de usuário (UI/UX)",
        "Mockups de aplicativos móveis",
        "Animações e interações",
        "Ilustrações digitais",
        "Artes conceituais",
        "Quadrinhos ou graphic novels",
        "Capas de álbuns ou livros",
        "Websites completos",
        "Aplicações web",
        "Plugins ou extensões",
        "Projetos de código aberto",
        "Aplicativos de desktop ou móveis",
        "Bibliotecas ou frameworks",
        "Scripts automatizados",
        "Projetos de inteligência artificial ou machine learning"]
}

protfólio_design = {    
        "Portfólios_de_Design_Gráfico":[
        "Logotipos",
        "Cartazes",
        "Materiais de marketing (flyers, banners)",
        "Capas de livros ou revistas",
        "Layouts de sites",
        "Interfaces de usuário (UI/UX)",
        "Mockups de aplicativos móveis",
        "Animações e interações",
        "Ilustrações digitais",
        "Artes conceituais",
        "Quadrinhos ou graphic novels",
        "Capas de álbuns ou livros"]
}

protfólio_desenvolvimento = {

        "Portfólios_de_Desenvolvimento":[
        "Websites completos",
        "Aplicações web",
        "Plugins ou extensões",
        "Projetos de código aberto",
        "Aplicativos de desktop ou móveis",
        "Bibliotecas ou frameworks",
        "Scripts automatizados",
        "Projetos de inteligência artificial ou machine learning"]

       }

def protfólio_de_desenvolvimento(request):
    return render(request, "portfolio_desenvolvimento.html", protfólio_desenvolvimento)

def protfólio_de_desing(request):
    return render(request, "portfolio_design.html", protfólio_design)

def todos_os_protfólios(request):
    return render(request, "portfolio_completo.html", todos_protfólios)
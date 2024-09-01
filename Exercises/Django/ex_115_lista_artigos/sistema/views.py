from django.shortcuts import render

Todos_Artigos = {
    "Todos_Artigos": [
    "Alimentação Saudável: O Guia Definitivo",
    "Manter uma alimentação saudável é fundamental para uma vida longa e plena. Este artigo apresenta dicas práticas para uma dieta balanceada, incluindo os melhores alimentos para consumir e aqueles que devem ser evitados.",
    "Exercícios Físicos: Benefícios para o Corpo e a Mente",
    "A prática regular de exercícios físicos traz inúmeros benefícios, não apenas para o corpo, mas também para a mente. Aqui, discutimos como diferentes tipos de exercícios podem melhorar a sua saúde mental, aumentar a energia e promover o bem-estar geral.",
    "Saúde Mental: Como Cuidar da Sua Mente em Tempos Difíceis",
    "A saúde mental é tão importante quanto a saúde física, especialmente em tempos de estresse e incerteza. Neste artigo, abordamos técnicas e hábitos que podem ajudar a manter a mente saudável e equilibrada.",
    "Alimentação Saudável: O Guia Definitivo",
    "Manter uma alimentação saudável é fundamental para uma vida longa e plena. Este artigo apresenta dicas práticas para uma dieta balanceada, incluindo os melhores alimentos para consumir e aqueles que devem ser evitados.",
    "Exercícios Físicos: Benefícios para o Corpo e a Mente",
    "A prática regular de exercícios físicos traz inúmeros benefícios, não apenas para o corpo, mas também para a mente. Aqui, discutimos como diferentes tipos de exercícios podem melhorar a sua saúde mental, aumentar a energia e promover o bem-estar geral.",
    "Saúde Mental: Como Cuidar da Sua Mente em Tempos Difíceis",
    "A saúde mental é tão importante quanto a saúde física, especialmente em tempos de estresse e incerteza. Neste artigo, abordamos técnicas e hábitos que podem ajudar a manter a mente saudável e equilibrada."
   ]
    
   
}

Artigos_s =  {
    "Artigos_Saude": [
    "Alimentação Saudável: O Guia Definitivo",
    "Manter uma alimentação saudável é fundamental para uma vida longa e plena. Este artigo apresenta dicas práticas para uma dieta balanceada, incluindo os melhores alimentos para consumir e aqueles que devem ser evitados.",
    "Exercícios Físicos: Benefícios para o Corpo e a Mente",
    "A prática regular de exercícios físicos traz inúmeros benefícios, não apenas para o corpo, mas também para a mente. Aqui, discutimos como diferentes tipos de exercícios podem melhorar a sua saúde mental, aumentar a energia e promover o bem-estar geral.",
    "Saúde Mental: Como Cuidar da Sua Mente em Tempos Difíceis",
    "A saúde mental é tão importante quanto a saúde física, especialmente em tempos de estresse e incerteza. Neste artigo, abordamos técnicas e hábitos que podem ajudar a manter a mente saudável e equilibrada."
   ]
}
       

Artigos_t = {
  "Artigos_Tecnologia": [
    "Inteligência Artificial: A Nova Fronteira da Tecnologia",
    "A inteligência artificial (IA) está revolucionando diversas indústrias, desde saúde até finanças, oferecendo soluções mais rápidas e precisas. Neste artigo, exploramos como a IA está mudando o mundo e quais são as perspectivas para o futuro.",
    "Blockchain: Além das Criptomoedas",
    "Embora o blockchain seja mais conhecido como a tecnologia por trás das criptomoedas como o Bitcoin, suas aplicações vão muito além disso. Este artigo discute como o blockchain está sendo usado para melhorar a segurança, transparência e eficiência em várias indústrias.",
    "Computação Quântica: O Futuro da Computação",
    "A computação quântica promete resolver problemas complexos que estão além da capacidade dos computadores clássicos. Este artigo explora os princípios básicos da computação quântica e como ela pode transformar setores como criptografia, pesquisa científica e otimização."
  ],
}

def Artigos_Saúde(request):
    return render(request, "artigos_saude.html", Artigos_s)

def Artigos_tecnologia(request):
    return render(request, "artigos_tecnologia.html", Artigos_t)

def Todos_os_artigos(request):
    return render(request, "todos_os_artigos.html", Todos_Artigos)

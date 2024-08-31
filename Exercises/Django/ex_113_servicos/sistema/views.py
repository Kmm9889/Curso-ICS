from django.shortcuts import render

todos_servicos = {
    "todos_os_servicos":[
        "SOAP (Simple Object Access Protocol)",
        "REST (Representational State Transfer)",
        "XML-RPC (XML Remote Procedure Call)",
        "JSON-RPC (JavaScript Object Notation Remote Procedure Call)",
        "gRPC (gRPC Remote Procedure Call)",
        "Google Ads",
        "Facebook Ads",
        "Mailchimp (email marketing)",
        "HubSpot (automação de marketing)",
        "Hootsuite (gerenciamento de redes sociais)",
        "SEMrush (SEO e marketing de conteúdo)",
        "Moz (SEO)",
        "Buffer (gerenciamento de redes sociais)",
        "Salesforce Marketing Cloud (automação de marketing)",
        "Google Analytics (análise de dados e desempenho)"
    ]
}

servicos_m = {
       "servicos_m":[
       "Google Ads",
       "Facebook Ads",
       "Mailchimp (email marketing)",
       "HubSpot (automação de marketing)",
       "Hootsuite (gerenciamento de redes sociais)",
       "SEMrush (SEO e marketing de conteúdo)",
       "Moz (SEO)",
       "Buffer (gerenciamento de redes sociais)",
       "Salesforce Marketing Cloud (automação de marketing)",
       "Google Analytics (análise de dados e desempenho)"]
       }

servicos_w= {
        "servicos_w":[
        "SOAP (Simple Object Access Protocol)",
        "REST (Representational State Transfer)",
        "XML-RPC (XML Remote Procedure Call)",
        "JSON-RPC (JavaScript Object Notation Remote Procedure Call)",
        "gRPC (gRPC Remote Procedure Call)"]
       }

def servicos_web(request):
    return render(request, "servicos_web.html", servicos_w)

def servicos_marketing(request):
    return render(request, "servicos_marketing.html", servicos_m)

def todos_os_servicos(request):
    return render(request, "todos_os_servicos.html", todos_servicos)
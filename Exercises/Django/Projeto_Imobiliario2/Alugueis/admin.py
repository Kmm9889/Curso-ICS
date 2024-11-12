from django.contrib import admin
from .models import Contato
from .models import Contrato
from .models import ImovelAluguel

admin.site.register(Contato)
admin.site.register(Contrato)
admin.site.register(ImovelAluguel)
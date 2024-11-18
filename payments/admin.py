from django.contrib import admin
from payments.models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'metodo', 'monto', 'estado')  
    search_fields = ('metodo', 'estado') 
    list_filter = ('estado',) 
    ordering = ('-id_pago',)  

from django.contrib import admin
from payments.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id_payment', 'method', 'amount', 'state')
    list_filter = ('method', 'state')
    search_fields = ('method', 'state')

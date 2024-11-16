from django.urls import path
from .views import PaymentListCreateView, PaymentRetrieveUpdateDestroyView

urlpatterns = [
    # Ruta para listar y crear pagos
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    
    # Ruta para recuperar, actualizar o eliminar un pago específico
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
]


from django.db import models
from accounting_order_sales.models import SalesOrder, SalesOrderItem
from django.utils import timezone
from django.contrib.auth.models import User

class RequirementOrder(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    requested_date = models.DateField()  # Fecha en la que necesitas los ítems
    notes = models.TextField(blank=True, null=True)  # Campo opcional para agregar notas
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    order_number = models.CharField(max_length=20, unique=True, blank=True)  # Número de la orden autogenerado
    estado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con el usuario que crea el requerimiento


    def __str__(self):
        return f"Requirement Order {self.order_number} for {self.sales_order.sapcode} on {self.requested_date}"

    def save(self, *args, **kwargs):
        # Si el order_number no existe, generarlo basado en el id
        if not self.order_number:
            super().save(*args, **kwargs)  # Guarda inicialmente para obtener el id
            self.order_number = f"OR-{self.id}"  # Genera el número de orden con el id autogenerado

        # Asegurarse de que se llame a super().save() después de generar el order_number
        super().save(*args, **kwargs)

class RequirementOrderItem(models.Model):
    ESTADO_CHOICES = [
        ('L', 'Listo'),
        ('P', 'Pendiente'),
        ('C', 'Comprando')
    ]
    
    requirement_order = models.ForeignKey(RequirementOrder, on_delete=models.CASCADE, related_name="items")
    sales_order_item = models.ForeignKey(SalesOrderItem, on_delete=models.CASCADE)
    quantity_requested = models.PositiveIntegerField(default=1)
    notes = models.CharField(max_length=255, blank=True, null=True) 
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')  

    def __str__(self):
        return f"{self.sales_order_item.description} ({self.quantity_requested}) - {self.get_estado_display()}"
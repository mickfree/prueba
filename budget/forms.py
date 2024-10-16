from django import forms
from .models import Budget, BudgetItem, CatalogItem
from django.forms import inlineformset_factory

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = [
            'client',
            'budget_name',
            'budget_number',
            'budget_days',
            'budget_date',
            'budget_expenses',
            'budget_utility',
            'budget_deliverytime',
            'budget_servicetime',
            'budget_warrantytime'
        ]
        widgets = {
            'budget_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'budget_expenses': forms.Select(attrs={
                'class': 'form-select',
            }),
            'budget_utility': forms.Select(attrs={
                'class': 'form-select',
            }),
            'budget_deliverytime': forms.Select(attrs={
                'class': 'form-select',
            }),
            'budget_servicetime': forms.Select(attrs={
                'class': 'form-select',
            }),
            'budget_warrantytime': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'client': 'Nombre de Cliente',
            'budget_name': 'Nombre del Presupuesto',
            'budget_number': 'Número de Cotización',
            'budget_days': 'Días del Presupuesto',
            'budget_date': 'Fecha del Presupuesto',
            'budget_expenses': 'Gastos Administrativos (%)',
            'budget_utility': 'Utilidad (%)',
            'budget_deliverytime': 'Tiempo de Entrega',
            'budget_servicetime': 'Tiempo de Servicio',
            'budget_warrantytime': 'Tiempo de Garantía',
        }

BudgetItemFormSet = inlineformset_factory(
    Budget,
    BudgetItem,
    fields=['item', 'quantity'],
    extra=0,
    can_delete=True,
    widgets={
        'item': forms.Select(attrs={'class': 'form-select'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 80px;'}),
    },
    labels={
        'item': 'Ítem',
        'quantity': 'Cantidad',
    }
)

class CatalogItemForm(forms.ModelForm):
    class Meta:
        model = CatalogItem
        fields = ('sap', 'description', 'category', 'price', 'price_per_day', 'unit', 'apply_price_per_day')  # Añadir el campo 'apply_price_per_day'
        labels = {
            'sap': 'SAP',
            'description': 'Nombre',
            'category': 'Categoria',
            'price': 'Precio',
            'price_per_day': 'Precio por día',
            'unit': 'Unidad de medida',
            'apply_price_per_day': 'Aplicar precio por día',  # Etiqueta para el nuevo campo
        }


class SearchCatalogItemForm(forms.Form):
    sap = forms.CharField(label="sap", max_length=100, required=False)
    description = forms.CharField(label="description", max_length=100, required=False)

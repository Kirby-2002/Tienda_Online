# MainApp/forms.py

from django import forms
from .models import Order

# 1. Definir un Widget Personalizado para Archivos Múltiples
class MultipleFileInput(forms.FileInput):
    # Este atributo es lo que Django comprueba. Al establecerlo a True,
    # se evita el ValueError.
    allow_multiple_selected = True 


class OrderRequestForm(forms.ModelForm):
    # 2. Usar el nuevo widget en el campo de formulario
    reference_images = forms.FileField(
        label='Imágenes de referencia (máximo 5)',
        required=False,
        # 💡 Usamos el nuevo widget sin pasar el atributo 'multiple' en attrs,
        # ya que el widget se encarga de configurarlo internamente.
        widget=MultipleFileInput() 
    )
    
    class Meta:
        model = Order
        fields = [
            'customer_name', 
            'email', 
            'phone', 
            'product_ref', 
            'description', 
            'requested_date'
        ]
        widgets = {
            'requested_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Teléfono o Red Social'}),
        }
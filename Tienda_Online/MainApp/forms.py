from django import forms
from .models import Order

class OrderRequestForm(forms.ModelForm):
    # Campo de subida de varias imágenes
    reference_images = forms.FileField(
        required=False,
        label="Imágenes de referencia (máximo 5)"
    )

    class Meta:
        model = Order
        fields = [
            'customer_name',
            'email',
            'phone',
            'product_ref',
            'description',
            'requested_date',  # ⚡ asegurarse de incluir la fecha
            'reference_images',
        ]
        widgets = {
            'requested_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'product_ref': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_reference_images(self):
        files = self.files.getlist('reference_images')
        if len(files) > 5:
            raise forms.ValidationError("Máximo 5 imágenes.")
        for f in files:
            if f.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError(f"El archivo {f.name} supera los 5MB.")
        return files

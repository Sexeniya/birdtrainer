from django import forms
from .models import Bird

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['name', 'image']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        if Bird.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"Птица с именем '{name}' уже существует.")

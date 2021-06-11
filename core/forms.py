from django.forms import ModelForm
from core.models import Cliente, Pet


class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class FormPet(ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

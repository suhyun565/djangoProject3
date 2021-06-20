from django.forms import ModelForm
from .models import Inventory


class itemForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

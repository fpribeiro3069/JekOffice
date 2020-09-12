from .models import CustomUser
from django.forms import ModelForm
from django.forms.widgets import FileInput

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'imagem',
            'first_name',
            'last_name',
            'cargo',
            'email',
            'telemovel',
            'cc_num',
            'mac_adress',
        ]
        widgets = {
            'imagem': FileInput(),
        }

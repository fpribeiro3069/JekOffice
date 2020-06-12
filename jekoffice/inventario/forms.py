from .models import Item
from bootstrap_modal_forms.forms import BSModalForm

class ItemForm(BSModalForm):
    class Meta:
        model = Item
        fields = ['nome', 'quantidade']

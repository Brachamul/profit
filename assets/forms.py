from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import DevelopmentProject

class DevelopmentProjectInlineForm(forms.ModelForm):
    materials = forms.CharField(
        label='materials needed',
        max_length=156,
        required=False,
        widget=forms.widgets.TextInput(attrs={'readonly': True})
    )

    class Meta:
        model = DevelopmentProject
        fields = ('was', 'becomes', 'materials', )

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            obj = kwargs['instance']
            materials_needed = {'materials': obj.types_of_materials_needed()}
            if 'initial' in kwargs:
                kwargs['initial'].update(materials_needed)
            else:
                kwargs['initial'] = materials_needed
        super(DevelopmentProjectInlineForm, self).__init__(*args, **kwargs)
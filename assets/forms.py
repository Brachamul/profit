from django import forms
from django.forms.models import inlineformset_factory
from .models import Feature, DevelopmentProject

DevelopmentProjectFormSet = inlineformset_factory(Feature, DevelopmentProject, fk_name='becomes')
development_project = DevelopmentProject.objects.get(becomes='Project Result')
formset = DevelopmentProjectFormSet(instance=development_project)
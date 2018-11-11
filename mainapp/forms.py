from django import forms
from .models import Placement

class MainForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ('name', 'email','course','number','branch','grad', 'desig','org', 'domain', 'degree', 'custatus', 'univname')

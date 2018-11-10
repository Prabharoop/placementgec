from django import forms
from .models import Placement

class MainForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ('name', 'reg', 'email','gender','course','number','branch','grad','org','desig','domain','degree','custatus','univname','texta','textb','textc','textd','texte','textf','textg')

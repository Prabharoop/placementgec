from django import forms
from .models import Placement

class MainForm(forms.ModelForm):

    class Meta:
        model = Placement
        fields = ('name', 'email','course','reg','gender','number','branch','grad', 'desig','org', 'domain', 'degree', 'custatus', 'univname','choicea','choiceb','choicec','choiced','choicee','texta','textb','textc','textd','texte','textf','textg')

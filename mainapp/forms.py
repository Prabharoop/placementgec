from django import forms
from .models import Placement

class MainForm(forms.ModelForm):


    class Meta:
        model = Placement
        fields = ('name', 'email','course','reg','gender','number','branch','grad', 'desig','org', 'domain','texta','choicea','textb','textc','choiceb','choicec','choiced','textd','choicee','textf','textg')
        widgets = {
            'choicea':forms.RadioSelect(),
            'choicee':forms.RadioSelect(),
            
        }

         # 'degree', 'custatus', 'univname', to be added

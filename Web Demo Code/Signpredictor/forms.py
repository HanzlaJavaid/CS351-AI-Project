from django import forms
class infoForm(forms.Form):
    preg = forms.IntegerField()
    gluc = forms.IntegerField()
    blood = forms.IntegerField()
    Skin = forms.IntegerField()
    Insul = forms.IntegerField()
    BMI = forms.IntegerField()
    dia = forms.IntegerField()
    age = forms.IntegerField()

class IMPREDICTORSCR(forms.Form):
    Image = forms.ImageField()
    Image.widget.attrs.update({
        'class':'form-control'
    })
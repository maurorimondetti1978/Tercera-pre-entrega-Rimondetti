from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=10)
    camada = forms.IntegerField()
    email = forms.EmailField(required=False)

class BuscaCursoForm(forms.Form):
    nombre = forms.CharField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)    

from django import forms
from.models import Cadastrados

class CadForm(forms.ModelForm):
    empresa_choices =( 
    ("Inova Rio", "Inova Rio"), 
    ("Land", "Land"), 
    ("Arpoador", "Arpoador"), 
    ("Espaço", "Espaço"), 
    ("Outro", "Outro"),
    )
    unidade_choices =( 
    ("Sede", "Sede"), 
    ("Silvado", "Silvado"), 
    ("Espraiado", "Espraiado"), 
    ("Flamengo", "Flamengo"), 
    ("Outro", "Outro"),
    )
    
    unidade = forms.ChoiceField(choices=unidade_choices,widget= forms.RadioSelect, required=True)
    empresa = forms.ChoiceField(choices=empresa_choices, widget= forms.RadioSelect, required=True)
    
    nome = forms.CharField(max_length=255, widget= forms.TextInput(attrs={'class':'form-control form-group-cad'}), required=True)
    telefone = forms.CharField(max_length=255, widget= forms.NumberInput(attrs={'class':'form-control'}), required=True)
    
    
    class Meta:
        fields = '__all__'
        model = Cadastrados

class UpdateForm(forms.ModelForm):
    empresa_choices =( 
    ("Inova Rio", "Inova Rio"), 
    ("Land", "Land"), 
    ("Arpoador", "Arpoador"), 
    ("Espaço", "Espaço"), 
    ("Outro", "Outro"),
    )
    unidade_choices =( 
    ("Sede", "Sede"), 
    ("Silvado", "Silvado"), 
    ("Espraiado", "Espraiado"), 
    ("Flamengo", "Flamengo"), 
    ("Outro", "Outro"),
    )
    
    unidade = forms.ChoiceField(choices=unidade_choices,widget= forms.RadioSelect, required=True)
    empresa = forms.ChoiceField(choices=empresa_choices, widget= forms.RadioSelect, required=True)
    
    nome = forms.CharField(max_length=255, widget= forms.TextInput(attrs={'class':'form-control form-group-cad'}), required=True)
    telefone = forms.CharField(max_length=255, widget= forms.NumberInput(attrs={'class':'form-control'}), required=True)
    
    
    class Meta:
        fields = '__all__'
        model = Cadastrados

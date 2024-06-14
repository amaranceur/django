from django import forms
from .models import LOgin

class Loginform(forms.ModelForm):  
    class Meta:
        model =LOgin
        fields = "__all__"

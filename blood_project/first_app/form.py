from django import forms
from  first_app.models import Name

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Name
        fields = '__all__'
   
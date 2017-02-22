from django import forms
from django.forms import ModelForm

from clients.models import Auth_record, Client_fw

class Edit_form(forms.ModelForm):

    class Meta:
        model = Auth_record
        fields = ('mac', 'ip_add', 'kl_service', 'downl', 'upl',)
       
       
class Src_form(forms.Form):

    address = forms.CharField()

class Search_add(forms.Form):
    address_ul = forms.CharField()
    address_nrd = forms.CharField(required=False)
    address_nrm = forms.CharField(required=False)
    
class Edit_form_CClient_fw(forms.ModelForm):
    
    class Meta:
        model = Client_fw
        fields = ('mac', 'ip_add', 'kl_service', 'downl', 'upl',)
        
        
        
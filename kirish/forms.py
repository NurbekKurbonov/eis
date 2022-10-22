from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(label='Ismingiz', max_length=100, required=True)
    email = forms.EmailField(label='Email adresingiz', required=False)
    subject = forms.CharField(label='Murojaat mavzusi', max_length=100, required=True)
    message = forms.CharField(label='Murojat bayoni', widget=forms.Textarea)
    

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
  
  
class captchaform(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
from django import forms
import pytz
class LocationForm(forms.Form):
    timezone = forms.ChoiceField(choices=[(tz, tz) for tz in pytz.all_timezones])

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    name.widget.attrs.update({'class': 'form-control'})
    email = forms.EmailField(required=True)
    email.widget.attrs.update({'class': 'form-control'})
    question = forms.CharField(widget=forms.Textarea)
    question.widget.attrs.update({'class': 'form-control'})
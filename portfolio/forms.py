from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-input bg-black border border-gray-600 rounded-lg w-full p-2 text-white'})
        )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-input bg-black border border-gray-600 rounded-lg w-full p-2 text-white'})
        )
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Comment', 'class': 'form-textarea bg-black border border-gray-600 rounded-lg w-full p-2 text-white h-20'})
        )

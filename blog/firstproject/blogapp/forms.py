from django import forms

class NewBlogForm(forms.Form):
    name = forms.CharField(label="Name",max_length=100)
    Gmail = forms.EmailField(label="Gmail")
    content = forms.CharField(label="Content", max_length=500, widget=forms.TextInput)

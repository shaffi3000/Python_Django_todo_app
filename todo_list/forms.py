from django import forms

class CreateTodo(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item to add'}))

    
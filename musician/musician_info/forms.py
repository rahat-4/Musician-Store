from django import forms
from musician_info.models import Musician, Album


# class Musician_Form(forms.ModelForm):
#     first_name = forms.CharField(label='First Name', widget=forms.TextInput(
#         attrs={'placeholder': 'First name'}))
#     last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
#         attrs={'placeholder': 'Last name'}))
#     instrument = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Instrument'}))

#     class Meta:
#         model = Musician
#         fields = '__all__'


class Album_Form(forms.ModelForm):
    album_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Album name'}))
    release_date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}))

    class Meta:
        model = Album
        fields = '__all__'

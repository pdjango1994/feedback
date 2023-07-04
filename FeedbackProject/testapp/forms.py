from django import forms
from django.core.validators import *

def rollNoValidator(value):
    if value<0 and value >=100:
        raise ValidationError("Roll Number must be positive and 3 digit")
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollNo=forms.IntegerField(validators=[rollNoValidator])
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[MaxLengthValidator(30),MinLengthValidator(10)])
    bot_handler=forms.CharField(widget=forms.HiddenInput, required=False)

    '''def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Name should be minimum 4 character")
        return inputname'''

    def clean(self):
        total_cleaned_data=super().clean()

        print('Total form is validated using single clean()')
        inputname=total_cleaned_data['name']
        if inputname[0]!='k':
            raise forms.ValidationError("Name should be starts with k")

        inputrollNo=total_cleaned_data['rollNo']
        if inputrollNo<0:
            raise forms.ValidationError("Roll number is positiive only")
        bot_handlerinput=total_cleaned_data['bot_handler']
        if len(bot_handlerinput) > 0:
            raise forms.ValidationError("Request from BOT is not submitted")

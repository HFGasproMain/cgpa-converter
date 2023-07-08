from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class GenerateTableForm(forms.Form):
    degree_choices = [('MSc', 'MSc'), ('PhD', 'PhD')]
    academic_scale_choices = [('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')]

    level = forms.ChoiceField(choices=degree_choices)
    academic_scale = forms.ChoiceField(choices=academic_scale_choices)
    num_courses = forms.IntegerField()



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['course_of_study', 'academic_scale', 'num_courses', 'photo', 'country', 'level']



class CourseForm(forms.Form):
    title = forms.CharField(label='Course Title')
    unit = forms.FloatField(label='Course Unit')
    score = forms.FloatField(label='Score')
    grade = forms.CharField(label='Grade')
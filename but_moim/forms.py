# coding: utf-8

from __future__ import unicode_literals

from django import forms

from but_moim.models import *

class Moim_list_Form(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ('tel','user_name', )
        # exclude = ('filtered_image_file',)

class Moim_join_Form(forms.ModelForm):
    class Meta:
        model = moim_info
        exclude = ('user', 'moim_person_count')

class MoimSearchForm(forms.Form):
    search_name = forms.CharField(max_length=100)

class User_Join_Form(forms.Form):
    UserId = forms.CharField(max_length=100)
    UserPW = forms.PasswordInput()
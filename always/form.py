#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Always"
# Date: 2017/11/12

from django import forms
from django.core.exceptions import ValidationError
import re


class UserForm(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput(attrs={"class":"form-control username", "placeholder":"请输入用户名！"}),
            max_length=20,
            error_messages={"required": "请输入用户名"}
    )
    password = forms.CharField(
            widget=forms.PasswordInput(attrs={"class":"form-control password", "placeholder": "请输入密码！"}),
            max_length=20,
            error_messages={"required": "请输入密码"}
    )
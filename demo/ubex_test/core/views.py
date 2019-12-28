from django.shortcuts import render
import django.apps


x = django.apps.apps.get_models(include_auto_created=True)
print('aaa', x)
y = 2

from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import forms

class MainUserView(View):
    def get(self, request):
        return HttpResponse('account page')

class CreateUserView(View):
    def get(self, request):
        context = {'form': forms.UserCreationForm().as_p()}
        return render(request, 'registration/create_user.html', context)
    def post(self, request):
        new_user = forms.UserCreationForm(request.POST)
        new_user.save()
        return redirect('/main/')

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# (logic of what we're sending!)

# Create your views here.
class SquaringView(View):

    def get(self, request, number):
        return HttpResponse(number ** 2)


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse('Hello World! Nikkole is a BADASS')

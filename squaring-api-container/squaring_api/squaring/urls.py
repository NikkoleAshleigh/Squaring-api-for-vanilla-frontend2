
from django.urls import path

from squaring.views import SquaringView, HelloWorldView

urlpatterns = [
    path('<int:number>', SquaringView.as_view(), name='number'),
    path('home', HelloWorldView.as_view())
]
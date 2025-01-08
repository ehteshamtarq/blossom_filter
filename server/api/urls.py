from django.urls import path
from . import views

urlpatterns = [
    path('unique_number/', views.unique_number, name='unique_number'),
    path('check_number/', views.check_number_in_filter, name='check-number')

]

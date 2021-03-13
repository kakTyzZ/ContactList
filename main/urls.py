from django.urls import path
from .views import (
    index,
    addContact,
    deleteContact,
    profile,
    edit,
)

urlpatterns = [
    path('', index , name='index'),
    path('/new', addContact, name='new'),
    path('/delete/<str:pk>', deleteContact, name='delete'),
    path('/contact-profile/<str:pk>', profile, name='contact-profile'),
    path('/edit/<str:pk>', edit, name='edit')
    
]
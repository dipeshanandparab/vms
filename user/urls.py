from django.urls import path
from .views import newVisitor

urlpatterns = [
    path('', newVisitor, name='new_visitor'),
]
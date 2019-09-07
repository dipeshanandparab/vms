from django.urls import path
from .views import visitorsList
from .views import visitorsDetail

urlpatterns = [
    path('<id>', visitorsDetail, name="visitors_detail"),
    path('', visitorsList, name="visitors_list"),
]
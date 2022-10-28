from . import views
from django.urls import path


urlpatterns = [
    path('login/' , views.index ,name='login')
]

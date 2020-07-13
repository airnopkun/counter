from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy),
    path('increment_two', views.increment_two),
    path('increment_new', views.increment_new)
]
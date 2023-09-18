
from django.urls import path,include
from . import views
from .views import perform_ocr
urlpatterns = [
    path('', views.index, name='index'),
    path('perform-ocr/', perform_ocr, name='perform-ocr'),

]
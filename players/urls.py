from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('message/',views.content,name='message'),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact_us, name="contact"),

]

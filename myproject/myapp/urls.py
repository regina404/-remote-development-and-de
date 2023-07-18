from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle/<str:led>/', views.toggle_led, name='toggle_led'),
    path('toggle_all/', views.toggle_all, name='toggle_all'),
    path('running_leds/', views.running_leds, name='running_leds'),
    path('random_leds_blink/', views.random_leds_blink, name='random_leds_blink'),
 ]

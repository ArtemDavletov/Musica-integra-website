from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('artodox/', views.artodox, name='artodox'),
    path('incubator/', views.incubator, name='incubator'),
    path('children/', views.children, name='children'),
    path('session/', views.session, name='session'),
]

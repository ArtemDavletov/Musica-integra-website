from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('artodox/', views.artodox, name='artodox'),
    path('incubator/', views.incubator, name='incubator'),
    path('children/', views.children, name='children'),
    path('session/', views.session, name='session'),
    path('teachers/', views.teachers, name='teachers'),
    path('inspiration/', views.inspiration, name='inspiration'),
    path('playing/', views.playing, name='playing'),

    path('not_ready/', views.not_ready, name='not_ready'),
    path('not_found/', views.e_handler404, name='not_found'),
    path('server_error/', views.e_handler500, name='server_error'),
]

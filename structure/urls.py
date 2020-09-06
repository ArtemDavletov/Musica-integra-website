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
    path('children_playing/', views.children_playing, name='children_playing'),
    path('konkurces/', views.konkurces, name='konkurces'),

    path('gumo/', views.gumo, name='gumo'),
    path('courses/', views.courses, name='courses'),
    path('konferences/', views.konferences, name='konferences'),
    path('remote/', views.remote, name='remote'),

    path('coursemat/', views.course_materials, name='course_materials'),
    path('methodsdev/', views.methods_dev, name='methods_dev'),
    path('notes/', views.notes, name='notes'),
    path('publications/', views.publications, name='publications'),
    path('videovonfmat/', views.videoconf_materials, name='videoconf_materials'),

    path('not_ready/', views.not_ready, name='not_ready'),
    path('not_found/', views.e_handler404, name='not_found'),
    path('server_error/', views.e_handler500, name='server_error'),
]

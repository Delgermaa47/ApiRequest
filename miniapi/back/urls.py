from django.urls import path, include
from . import views as backend_views

urlpatterns = [

    path('', include(([
        path('', backend_views.home, name='home'),
        path('test/', backend_views.request_res, name='test'),
    ], 'backend')),
    ),
]
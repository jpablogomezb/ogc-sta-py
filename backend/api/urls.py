from django import views
from django.urls import path, include
# from api.views import api_thing_get, api_thing_post

urlpatterns = [
    # path('', views.api_home),
    # path('thing/get/', api_thing_get),
    # path('thing/post/', api_thing_post),
    path('things/', include('things.urls'))
]

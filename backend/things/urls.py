from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.thing_list_create_view),
    path('<int:pk>/update/', views.thing_update_view),
    path('<int:pk>/delete/', views.thing_delete_view),
    path('<int:pk>/', views.thing_detail_view)
]
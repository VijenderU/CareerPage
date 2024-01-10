from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.jobs_list),
    path('add/', views.create_job),
    path('update/<int:id>', views.update_job),
    path('del/<int:id>', views.delete_job),
]
from django.urls import path, include
from builder import views
urlpatterns = [
    path('', views.builder_index, name='builder_index'),
    path('resume_details', views.resume_details, name='resume_details'),
    path('resume_template/<int:id>', views.resume_template, name='resume_template'),
]
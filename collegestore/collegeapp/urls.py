from django.urls import path
from .import views


app_name = 'collegeapp'

urlpatterns = [

    path('',views.Home,name='home'),
    path('student/',views.Student,name='student'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
    path('newpage/',views.Newpage,name='newpage')


]
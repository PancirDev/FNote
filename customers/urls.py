from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.CustomerListView.as_view(), name='list'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),
    path('projects/', views.ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail')
]

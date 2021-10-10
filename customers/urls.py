from django.urls import path

from . import views

app_name = 'customers'
urlpatterns = [
    path('', views.CustomerListView.as_view(), name='list'),
    path('create/', views.CustomerCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.CustomerUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.CustomerDelete.as_view(), name='delete'),
    path('projects/', views.ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project_detail')
]
#     path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),

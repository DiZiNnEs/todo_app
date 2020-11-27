from django.urls import path

from django.contrib.auth.decorators import login_required
from todo_app import views


urlpatterns = [
    path('', login_required(views.HomeView.as_view(), login_url='/login/'), name='home'),

    path('project/<int:pk>/', login_required(views.ProjectView.as_view(), login_url='/login/'), name='project'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('create-project', views.CreateProject.as_view(), name='create-project'),
    path('create-taks', views.CreateTask.as_view(), name='create-task'),
    path('<pk>/update-project', views.UpdateProject.as_view(), name='update-project'),
    path('<pk>/delete-project', views.DeleteProject.as_view(), name='delete-project'),

    path('project-delete/<int:pk>/', views.DestroyProjectRestFrameWork.as_view(), name='delete-project-through-api')
]

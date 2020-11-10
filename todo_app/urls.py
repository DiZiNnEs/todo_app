from django.urls import path

from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.HomeView.as_view(), login_url='/login/'), name='home'),
    path('project/<int:pk>/', login_required(views.ProjectView.as_view(), login_url='/login/'), name='project'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]

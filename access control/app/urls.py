from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetView, LogoutView


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts-create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('reset/', PasswordResetView.as_view(template_name = "password_reset.html"), name='reset'),
    path('reset/<uidb64>/<str:token>',PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/',PasswordResetDoneView.as_view(template_name='reset_done.html'), name='password_reset_done'),
    path('reset/complete/',PasswordResetCompleteView.as_view(template_name='reset_complete.html'), name='password_reset_complete'),
]

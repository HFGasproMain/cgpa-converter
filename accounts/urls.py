from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, user_login, dashboard, profile_update, generate_table, table_input


urlpatterns = [
	path('signup/', signup, name='signup'),
	path('login/', user_login, name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('dashboard/', dashboard, name='dashboard'),
	path('profile-update/', profile_update, name='profile_update'),
	path('generate_table/', generate_table, name='generate_table'),
    path('results/', table_input, name='table_input'),


]
from django.urls import path, re_path

from . import views

app_name = "e_reg"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('select_property/', views.select_property, name='select_property'),
    path('my_profile/contact_update/', views.contact_update, name="contact_update"),
    path('my_profile/room_preference_update/', views.room_preference_update, name="room_preference_update"),
    path('my_profile/hotel_membersip_update/', views.hotel_membership_update, name="hotel_membership_update"),
    path('my_profile/', views.my_profile, name="my_profile"),
]

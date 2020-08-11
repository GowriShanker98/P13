from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trial/',views.trial,name="Trial"),
    path('profile/',views.profile,name="Profile"),
    path('get_demo/',views.get_demo,name="Get Demo"),
    path('post_demo/',views.post_demo,name="Post Demo"),
]

from django.urls import path
from olx import views
from django.urls import path
# from .views import search

urlpatterns = [
    path("register",views.SignUpView.as_view(),name='signup'),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="home"),
    path("profile",views.UserProfileView.as_view(),name="profile"),
    path("products/add",views.ProductCreateView.as_view(),name="product-add"),
    path('Edit_profile', views.Edit_profile,name='Edit_profile'),
    path("product/detail/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("signout",views.logout_view,name="signout"),
    # path('search/', search, name='search')
    # path('send/', views.send_chat, name='chat-send'),
    # # path('renew/', views.get_messages, name='chat-renew')


   
    
   
]

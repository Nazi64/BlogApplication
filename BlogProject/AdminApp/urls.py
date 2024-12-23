from django.urls import path
from AdminApp import views
urlpatterns=[
    path('home',views.Home.as_view(),name='home_view'),
    # path('',views.Home.as_view(),name='home_view'),
    path('',views.RegisterView.as_view(),name='reg_view'),
    path('login',views.LoginView.as_view(),name='login_view'),
    path('logout',views.LogoutView.as_view(),name='logout_view'),
    path('create',views.CreateBlogView.as_view(),name='create_view'),
    path('detail/<int:id>',views.BlogDetailView.as_view(),name='detail_view'),
    path('delete/<int:id>',views.BlogDeleteView.as_view(),name='delete_view'),
    path('update/<int:id>',views.BlogUpdateView.as_view(),name='update_view'),
    
]
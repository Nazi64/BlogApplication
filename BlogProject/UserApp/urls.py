from django.urls import path
from UserApp import views
urlpatterns=[
    path('view',views.ViewerHomeView.as_view(),name='viewerhome_view'),
    path('viewdetail/<int:id>',views.ViewerDetailView.as_view(),name='viewerdetail_view'),
]
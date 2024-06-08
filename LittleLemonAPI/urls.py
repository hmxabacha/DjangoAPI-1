from django.urls import path
from . import views

urlpatterns = [
    path('api/userview/',views.UserView.as_view()),
    path('api/userview/<int:pk>',views.UserView.as_view()),
]

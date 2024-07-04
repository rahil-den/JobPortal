from django.urls import path
from .import views

urlpatterns = [
    # path("sec/",views.home.as_view()),
    path("index/",views.ind),
    # path('read/',views.read),
    # path('delete/<int:id>/',views.delete),
    # path('update/<int:id>/',views.update)
]
 
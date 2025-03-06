
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index), #사용자가 앱으로 들어올때
    path('create/',views.create), #사용자가 create로 들어올때
    path('read/<id>/',views.read)  #사용자가 read/1로 들어올때
]

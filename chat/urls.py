from django.urls import path
from chat.views import index,test_id,login1,registration,chat,logout1


urlpatterns = [
    path('',index,name='index'),
    path('login/',login1,name='login'),
    path('registration/',registration,name='registration'),
    path('chat/',chat, name='chat'),
    path('logout/',logout1, name='logout'),
    path('test/<int:id>/',test_id)
]
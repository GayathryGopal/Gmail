from django.urls import path
from mail import views
urlpatterns=[
    path('',views.home),
    path('hm',views.home),
    # path('reg',views.register),
    path('snt',views.sent),
    path('gmail',views.gmail),
    path('cmps',views.compose),
    path('smore',views.smore),
    path('inbox',views.inbox),
    path('deldata',views.deldata),
    path('deldata1',views.deldata1),
    path('bin',views.bin),
    path('inmore',views.inboxmore),
    path('stared',views.stared),
    path('stared1',views.stared1),
    path('strd',views.stareds),
    path('star',views.starmore),
    path('mystr',views.mystard),
    path('frwd',views.forward),
    path('regist',views.regist1),
    
   
    
]

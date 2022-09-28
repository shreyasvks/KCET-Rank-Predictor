from django.urls import path
from . import views
urlpatterns = [
    path('create/accountcreated/home/',views.home),
    path('create/accountcreated/home/cutoff/',views.finalcutoff),
    path('create/accountcreated/home/displaycutoff/',views.finaldisplaycutoff),
    path('create/accountcreated/home/predcollege/',views.finalpredcollege),
    path('create/accountcreated/home/dispredcollege/',views.disfinalpredcollege),
    path('create/accountcreated/home/predcourse/',views.finalpredcourse),
    path('create/accountcreated/home/dispredcourse/',views.disfinalpredcourse),
    path('create/accountcreated/home/kct/',views.kct),
    path('create/accountcreated/home/diskct/',views.diskct),
    path('create/accountcreated/home/rank/',views.rank_form),
    path('create/accountcreated/home/disrank/',views.disrank),
    path('',views.authenticate),
    path('create/',views.createaccount),
    path('accountcreated/',views.accountcreated),
    path('login/',views.login),
    path('loginsuccess/',views.loginsuccess),


]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('sendinjuiry/', views.sendinjuiry, name='sendinjuiry'),
    path('veneer/', views.veneer, name='veneer'),
    path('decking/', views.decking, name='decking'),
    path('agedwood/', views.agedwood, name='agedwood'),
    path('moulding/', views.moulding, name='moulding'),
    path('board_lumber/', views.lumber, name='lumber'),
    path('report/', views.report, name='report'),

]
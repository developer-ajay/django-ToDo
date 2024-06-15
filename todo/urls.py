from django.urls import path

from todo import views


urlpatterns = [
    path('addTask/',views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>',views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>',views.mark_as_undone, name="mark_as_undone"),
    path('deleteTask/<int:pk>',views.deleteTask, name='deleteTask'),
]

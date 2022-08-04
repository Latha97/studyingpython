


from.import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('add/',views.operations,name='operations'),
    path('div/',views.operations,name='operations'),
    path('sub/',views.operations,name='operations'),
    path('mul/',views.operations,name='operations'),
]
from django.urls import path, re_path, register_converter
from . import views
from extentions import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

app_name = 'blog'
urlpatterns = [
    #ex: hostname/blog/
    path('', views.index, name = 'index'),
    #ex: hostname/blog/5/
    path('<int:post_id>',views.detail, name = 'detail'),
    #ex: hostname/blog/archive/2018/
    #path('archive/<int:year>/', views.archive_year, name = 'arhive'),

    #use regex in url pattern is better
    #ex: hostname/blog/archive/2018/
    #re_path(r'^archive/(?P<year>[0-9]{4})/$',views.archive_year, name = 'archive')

    #better and simple way use regex converters
    path('archive/<yyyy:year>/',views.archive_year, name = 'archive'),

]

from django.urls import path
from django.contrib.auth import views as auth_views
from haru.views import post, get

app_name = 'haru'
urlpatterns =[
    path('post/', post.record, name='post'),
    path('calendar/<int:year>/<int:month>/', get.get_calendar,name='get_calendar'),
    path('get/<int:year>/<int:month>/<int:day>/', get.get_date, name='get'),
    path('build/',post.build_diary, name='build'),
    path('voice/<int:year>/<int:month>/<int:day>/<str:type>/', get.get_voice_file, name="get_voice_file")
]
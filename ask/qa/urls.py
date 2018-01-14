from django.conf.urls import url
from . import views


app_name = 'qa'
urlpatterns = [
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^ask/', views.ask_question, name='ask_question'),
    url(r'^new/', views.test),
    url(r'^question/(?P<id>(\d+))/', views.question, name='question'),
    url(r'^popular/', views.popular_questions, name='popular_questions'),
    url(r'^$', views.new_questions, name='new_questions')
]

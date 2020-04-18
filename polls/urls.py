from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<uuid:pk>/', views.DetailView.as_view(), name='detail'),
    path('new_question', views.CreateQuestion.as_view(), name='new_question'),
    path('<uuid:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<uuid:question_id>/vote/', views.vote, name='vote'),
]

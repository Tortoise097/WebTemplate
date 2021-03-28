from django.urls import path

from . import views

urlpatterns = [
    # ex: /web_board/
    path('', views.index, name='index'),
    # ex: /web_board/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /web_board/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /web_board/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
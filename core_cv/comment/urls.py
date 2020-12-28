from django.urls import path
from . import views

app_name = 'comment_api'

urlpatterns = [

    path('api/comment_create/', views.CreateCommentApi.as_view()),
    path('api/comment_list/', views.ListCommentApi.as_view()),
    path('api/comment_detail/<int:pk>/', views.DetailCommentApi.as_view(), name='detail'),

    # search field for comment ? dont know if need for now ?
    # path('api/search_field/', views.MessageSearchFieldApi.as_view()),  # ok
]

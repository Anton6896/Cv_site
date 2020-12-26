from django.urls import path
from . import views

app_name = 'comment_api'

urlpatterns = [
    # crud

    path('api/comment_create/', views.CommentCreateApi.as_view()),
    path('api/comment_detail/<int:pk>/', views.CommentDetailApi.as_view()),
    # see all messages/issues  , comments for them
    path('api/comment_list/<int:pk>', views.CommentListApi.as_view()),

    # search field for comment ? dont know if need for now ?
    # path('api/search_field/', views.MessageSearchFieldApi.as_view()),  # ok
]
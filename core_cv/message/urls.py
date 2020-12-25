from django.urls import path
from . import views

urlpatterns = [
    # crud
    path('api/message_create/', views.MessageCreateApi.as_view()),  # ok
    path('api/comment_create/', views.CommentCreateApi.as_view()),
    path('api/message_detail/<int:pk>/', views.MessageDetailApi.as_view()),
    path('api/comment_detail/<int:pk>/', views.CommentDetailApi.as_view()),
    # see all messages/issues  , comments for them
    path('api/message_list/', views.MessageListApi.as_view()),  # ok
    path('api/issue_list/', views.IssueMessageListApi.as_view()),  # ok
    path('api/comment_list/<int:pk>', views.CommentListApi.as_view()),
    # search field look up
    path('api/search_field/', views.MessageSearchFieldApi.as_view()),  # ?q=slug

]

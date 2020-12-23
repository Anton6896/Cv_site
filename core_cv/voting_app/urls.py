from django.urls import path
from . import views as my_view

app_name = 'voting_app'

urlpatterns = [
    path('api/create_voting/', my_view.CreateVotingApi.as_view()),
    path('api/voting_post/', my_view.VotingPost.as_view()),
    path('api/user_vote_detail/', my_view.AllUserVoteList.as_view()),
    path('api/user_un_vote_detail/', my_view.AllUserUnVoteList.as_view()),
    path('api/list_active_voting/', my_view.ListActiveVoting.as_view()),
    path('api/list_un_active_voting/', my_view.ListUnActiveVoting.as_view()),
    path('api/update_voting/<int:pk>/', my_view.UpdateVotingApi.as_view()),
    path('api/list_voting/', my_view.ListVotingWithChoices.as_view()),
]

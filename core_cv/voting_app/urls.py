from django.urls import path
from . import views as my_view

app_name = 'voting_app'

urlpatterns = [
    path('create_voting/', my_view.CreateVotingApi.as_view()),
    path('voting_post/', my_view.VotingPost.as_view()),
    path('voting_post_testing/<int:pk>', my_view.VotingPost_testing.as_view()),
    path('user_vote_detail/', my_view.AllUserVoteList.as_view()),
    path('user_un_vote_detail/', my_view.AllUserUnVoteList.as_view()),
    path('list_active_voting/', my_view.ListActiveVoting.as_view()),
    path('list_un_active_voting/', my_view.ListUnActiveVoting.as_view()),
    path('update_voting/<int:pk>/', my_view.UpdateVotingApi.as_view()),
    path('list_voting/', my_view.ListVotingWithChoices.as_view()),

]

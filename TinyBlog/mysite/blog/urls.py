from django.conf.urls import path
from blog import views



urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path('',views.PostListView.as_view(), name= 'post_list'),
    path('post/(?P<pk>\d+)',views.PostDetailView.as_view(), name= 'post_detail'),
    path("post/new", views.CreatePostView.as_view(), name="post_new"),
    path("post/(?P<pk>\d+)/edit/)", views.CreatePostView.as_view(), name="post_new"),
    path("post/(?P<pk>\d+)/remove/", views.PostDeleteView.as_view(), name="post_delete"),
    path("drsfts/", views.DraftListView.as_view(), name="post_draft_list"),
    path("post/(?P<pk>\d+)/comment/", views.add_comment_to_post.as_view(), name="add_comment_to_post"),
    path("comment/(?P<pk>\d+)/approve/", views.comment_approve.as_view(), name="comment_approve"),
    path("comment/(?P<pk>\d+)/remove/", views.comment_remove.as_view(), name="comment_remove"),
    path("post/(?P<pk>\d+)/publish/", views.post_publish.as_view(), name="post_publish"),
]

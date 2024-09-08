from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path(r'post/?P<pk>[^/]',PostDetailView.as_view(),name="post-view"),
    path('add-post',AddPostView.as_view(),name='add-post'),
    path(r'post/edit-post/?P<pk>[^/]',EditPostView.as_view(),name='edit-post'),
    path(r'post/delete-post/?P<pk>[^/]',DeletePostView.as_view(),name='delete-post'),
    path('sign-up',SignUpView.as_view(),name='sign-up'),
    path('log-out',LogOutView.as_view(),name='log-out'),
    path('log-in',LogInView.as_view(),name='log-in'),
    path('user',UserDetail.as_view(),name='user'),
    path('search/',SearchView.as_view(),name='search'),
    path(r'post/?P<pk>[^/]/comment',AddCommentView.as_view(),name='comment'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
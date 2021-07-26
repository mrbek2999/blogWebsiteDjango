from django.urls import path
from .views import create_user, main_page, logIn, create_post, articles, \
    logOut, filter_categories, filter_place, user_page, ChangePasswordView, UpdatePostView, user_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', create_user, name='registiration-page'),
    path('edit-user', user_page, name='edit-user'),
    path('edit-user/change-password', ChangePasswordView.as_view(template_name='profilePage/password-change.html'), name='password-page'),
    path('kirish', logIn, name='login-page'),
    path('create/post', create_post, name='create-post'),
    path('logout-user', logOut, name='logout'),
    path('category/<slug:slug>', filter_categories, name='filter-categories'),
    path('place/<slug:slug>', filter_place, name='filter-places'),
    path('article/<slug:slug>', articles, name='article-page'),
    path('article/edit/<slug:slug>', UpdatePostView.as_view(), name='article-edit'),
    path('bosh-sahifa/', main_page, name='main-page'),
    path('my-posts/', user_posts, name='user-page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
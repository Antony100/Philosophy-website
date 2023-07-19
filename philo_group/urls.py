from django.urls import path
from .views import AboutView, FaqView, Page404View, PostView, TagPostsView
from django.views.generic import TemplateView

app_name = 'philo_group'
urlpatterns = [

    path('about/', AboutView.as_view(), name='about'),
    path('', PostView.as_view(), name='sessions'),
    path('tag/<slug:tag_slug>/', TagPostsView.as_view(), name='tag_posts'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('404/', Page404View.as_view(template_name='404.html'), name='404')

]


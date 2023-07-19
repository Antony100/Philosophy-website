import pytest
from django.test import RequestFactory
from django.urls import reverse
from philo_group.views import (AboutView, FaqView, Page404View, 
                               PostView, TagPostsView)
from philo_group.models import PostsInSession
from taggit.models import Tag


@pytest.mark.django_db
@pytest.mark.parametrize('view_cls, url, template_name', [
    (AboutView, '/about', 'about.html'),
    (FaqView, '/faq', 'faq.html'),
    (PostView, '/sessions', 'sessions.html'),
])
def test_view(view_cls, url, template_name):
    factory = RequestFactory()
    request = factory.get(url)
    view = view_cls.as_view()
    response = view(request)

    assert response.status_code == 200
    assert template_name in response.template_name



@pytest.fixture
def factory():
    return RequestFactory()

@pytest.mark.django_db
def test_tag_posts_view(factory):
    # Create some test data
    tag = Tag.objects.create(name='Test Tag', slug='test-tag')
    post1 = PostsInSession.objects.create(title='Post 1', content='Content 1')
    post2 = PostsInSession.objects.create(title='Post 2', content='Content 2')
    post1.tags.add(tag)
    post2.tags.add(tag)

    # Create a request instance using RequestFactory
    url = reverse('tag_posts', kwargs={'tag_slug': tag.slug})
    request = factory.get(url)

    # Instantiate the TagPostsView class
    view = TagPostsView.as_view()

    # Dispatch the request to the view
    response = view(request, tag_slug=tag.slug)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response uses the correct template
    assert 'tag_posts.html' in response.template_name

    # Assert that the context contains the tag and paginated posts
    context = response.context_data
    assert context['tag'] == tag
    assert len(context['posts']) == 2
    assert context['posts'][0].title == 'Post 1'
    assert context['posts'][1].title == 'Post 2'

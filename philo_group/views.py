from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView

from taggit.models import Tag

from .models import Session, PostsInSession, SessionEventDate


class PostView(ListView):

    queryset = Session.objects.prefetch_related('postsinsession_set').all()
    context_object_name = 'sessions'
    template_name = 'sessions.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.order_by('name')
        sessiondate = SessionEventDate.objects.filter(id=1)
        paginator = Paginator(self.queryset, self.paginate_by)
        page = self.request.GET.get('page')
        sessions = paginator.get_page(page)
        context['sessions'] = sessions
        context['tags'] = tags
        context['sessiondate'] = sessiondate
        return context


class TagPostsView(ListView):

    template_name = 'tag_posts.html'
    paginate_by = 5

    def get_queryset(self):
        tag_slug = self.get_tag_slug()
        posts = PostsInSession.objects.filter(post__tags__slug=tag_slug)
        return posts

    def get_tag_slug(self):
        return self.kwargs['tag_slug']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.get_tag_slug()
        tag = get_object_or_404(Tag, slug=tag_slug)
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page = self.request.GET.get('page')
        paginated_posts = paginator.get_page(page)
        context['tag'] = tag
        context['posts'] = paginated_posts
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sessiondate = SessionEventDate.objects.filter(id=1)
        context['sessiondate'] = sessiondate
        return context


class FaqView(TemplateView):
    template_name = 'faq.html'


class Page404View (TemplateView):
    template_name = '404.html'

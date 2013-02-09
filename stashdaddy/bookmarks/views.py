from django.contrib import messages
from django.core import urlresolvers
from django.db.models import Q
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from .forms import BookmarkForm
from .models import Bookmark


class BookmarkQuerysetMixin(object):
    """
    Authenticated users see their own bookmarks; everyone else sees most
    recent public ones.
    """
    def get_queryset(self):
        q = Q(private=False)
        if self.request.user.is_authenticated():
            q |= Q(user=self.request.user)
        return self.model.objects.filter(q).order_by('-added_at')


class BookmarkList(BookmarkQuerysetMixin, ListView):
    """
    List of all bookmarks
    """
    model = Bookmark
    template_name = "bookmarks/index.html"
    context_object_name = 'bookmarks'
    navitem = "all"


class MyBookmarks(LoginRequiredMixin, BookmarkList):
    """
    "My bookmarks" page.
    """
    template_name = "bookmarks/mine.html"
    navitem = "mine"

    def get_queryset(self):
        return self.request.user.bookmarks.all()


class BookmarkDetail(BookmarkQuerysetMixin, DetailView):
    """
    Individual bookmark view.
    """
    model = Bookmark
    template_name = "bookmarks/detail.html"
    context_object_name = 'bookmark'

    def get_context_data(self, **kwargs):
        return super(BookmarkDetail, self).get_context_data(
            user_can_edit = (self.object.creator == self.request.user))


class BookmarkEditMixin(object):
    """
    Common helper for bookmark create/edit

    Provides:
        * success messages
        * redirect to user's bookmarks list on success
    """
    model = Bookmark
    form_class = BookmarkForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super(BookmarkEditMixin, self).form_valid(form)

    def get_success_url(self):
        return urlresolvers.reverse("bookmarks_list_mine", args=(self.object.id,))


class BookmarkCreate(LoginRequiredMixin, BookmarkEditMixin, CreateView):
    """
    Create a new bookmark.
    """
    template_name = "bookmarks/create.html"
    success_message = "Your bookmark has been saved."
    navitem = "new"

    def get_form_kwargs(self):
        kwargs = super(BookmarkCreate, self).get_form_kwargs()
        kwargs['instance'] = Bookmark(user=self.request.user)
        return kwargs


class BookmarkEdit(LoginRequiredMixin, BookmarkEditMixin, UpdateView):
    """
    Edit an existing bookmark.

    Naturally, only the person who created the bookmark can edit it again.
    """
    template_name = "bookmarks/edit.html"
    success_message = "Your bookmark has been updated."

    def get_queryset(self):
        return self.request.user.bookmarks.all()

import os

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.base import View


from accounts.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin

from book.forms import EditKid, DeleteKid, AddKid, EditStory, AddStory, DeleteStory
from book.models import Kids, Memory


class HomeView(View):
    def get(self, request):
        context = {}
        if not request.user.is_anonymous:
            current_user = User.objects.get(id=request.user.id)
            current_profile = UserProfile.objects.get(user=request.user.id)
            context = {
                   'user': current_user,
                   'profile': current_profile,
            }
        return render(request, 'home.html', context)


class MyKids(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        if not request.user.is_anonymous:
            current_user = User.objects.get(id=request.user.id)
            current_profile = UserProfile.objects.get(user=request.user.id)
            my_kids = Kids.objects.filter(user=current_user.id).order_by('date_of_birth')
            context = {
                'user': current_user,
                'profile': current_profile,
                'my_kids': my_kids
            }
        return render(request, 'my_kids.html', context)


class CreateKidView(LoginRequiredMixin, CreateView):
    model = Kids
    form_class = AddKid
    template_name = 'create_kid.html'
    success_url = reverse_lazy('my_kids')

    def get_initial(self):
        user = self.request.user
        return {
            'user': user,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        current_profile = UserProfile.objects.get(user_id=current_user.id)
        context['profile'] = current_profile
        context['user'] = current_user

        return context


class UpdateKid(LoginRequiredMixin, UpdateView):
    model = Kids
    form_class = EditKid
    template_name = 'edit_kid.html'
    context_object_name = 'kid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = UserProfile.objects.get(user_id=self.object.user_id)
        context['profile'] = profile
        return context

    def get_success_url(self):
        kid_id = self.kwargs['pk']
        #return reverse_lazy('edit_kid', kwargs={'pk': kid_id})
        return reverse_lazy('my_kids')

    def form_valid(self, form):
        current_kid = form.save(commit=False)
        old_picture = 'media/'
        old_picture += str(Kids.objects.get(pk=self.object.id).baby_profile_picture)
        current_kid.save()
        new_picture = 'media/'
        new_picture += str(Kids.objects.get(pk=self.object.id).baby_profile_picture)

        valid = super(UpdateKid, self).form_valid(form)
        if os.path.exists(old_picture) and old_picture != new_picture:
            os.remove(old_picture)
        return valid


class KidsDeleteView(LoginRequiredMixin, DeleteView):
    model = Kids
    form_class = DeleteKid
    template_name = "delete_kid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = UserProfile.objects.get(user_id=self.object.user_id)
        context['profile'] = profile
        return context

    def delete(self, request, *args, **kwargs):
        kid = Kids.objects.get(pk=self.kwargs['pk'])
        old_picture = 'media/'
        old_picture += str(kid.baby_profile_picture)
        related_stories = Memory.objects.filter(kid_id=kid.id)
        related_pictures = related_pictures_to_delete(related_stories)
        kid.delete()
        if os.path.exists(old_picture):
            os.remove(old_picture)
        delete_related_pictures(related_pictures)
        return HttpResponseRedirect(reverse_lazy('my_kids'))


class MyStories(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        if not request.user.is_anonymous:
            current_user = User.objects.get(id=request.user.id)
            current_profile = UserProfile.objects.get(user=request.user.id)
            kids = Kids.objects.filter(user=request.user.id)
            my_stories = Memory.objects.filter(user=current_user.id).order_by('-date_of_memory')
            context = {
                'user': current_user,
                'profile': current_profile,
                'my_stories': my_stories,
                'kids': kids
            }
        return render(request, 'my_stories.html', context)


class SharedStories(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        if not request.user.is_anonymous:
            current_user = User.objects.get(id=request.user.id)
            current_profile = UserProfile.objects.get(user=request.user.id)
            kids = Kids.objects.filter(user=request.user.id)
            my_stories = Memory.objects.exclude(status='PRIVATE').order_by('-date_of_memory')

            context = {
                'user': current_user,
                'profile': current_profile,
                'my_stories': my_stories,
                'kids': kids
            }
        return render(request, 'shared_stories.html', context)


class SneakPeekStories(View):
    def get(self, request):

        if not request.user.is_anonymous:
            current_user = User.objects.get(id=request.user.id)
            current_profile = UserProfile.objects.get(user=request.user.id)
            kids = Kids.objects.filter(user=request.user.id)
            my_stories = Memory.objects.filter(status='PUBLIC').order_by('-date_of_memory')

            context = {
                'user': current_user,
                'profile': current_profile,
                'my_stories': my_stories,
                'kids': kids
            }
        else:
            kids = Kids.objects.filter(user=request.user.id)
            my_stories = Memory.objects.filter(status='PUBLIC').order_by('-date_of_memory')
            context = {
                'my_stories': my_stories,
                'kids': kids
            }

        return render(request, 'sneak_peek.html', context)


class CreateStoryView(LoginRequiredMixin, CreateView):
    model = Memory
    form_class = AddStory
    template_name = 'create_story.html'
    success_url = reverse_lazy('my_stories')

    def get_initial(self):
        user = self.request.user
        return {
            'user': user,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        kids = Kids.objects.filter(user_id=current_user.id)
        current_profile = UserProfile.objects.get(user_id=current_user.id)
        kids = Kids.objects.filter(user_id=current_user.id)
        context['profile'] = current_profile
        context['user'] = current_user
        context['kids'] = kids

        return context


class UpdateStory(LoginRequiredMixin, UpdateView):
    model = Memory
    form_class = EditStory
    template_name = 'edit_story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = UserProfile.objects.get(user_id=self.object.user_id)
        context['profile'] = profile

        return context

    def get_success_url(self):
        kid_id = self.kwargs['pk']
        #return reverse_lazy('edit_kid', kwargs={'pk': kid_id})
        return reverse_lazy('my_stories')

    def form_valid(self, form):
        current_story = form.save(commit=False)
        old_picture = 'media/'
        old_picture += str(Memory.objects.get(pk=self.object.id).memory_picture)
        current_story.save()
        new_picture = 'media/'
        new_picture += str(Memory.objects.get(pk=self.object.id).memory_picture)

        valid = super(UpdateStory, self).form_valid(form)
        if os.path.exists(old_picture) and old_picture != new_picture:
            os.remove(old_picture)
        return valid


class StoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Memory
    form_class = DeleteStory
    template_name = "delete_story.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = UserProfile.objects.get(user_id=self.object.user_id)
        context['profile'] = profile
        return context

    def delete(self, request, *args, **kwargs):
        story = Memory.objects.get(pk=self.kwargs['pk'])
        old_picture = 'media/'
        old_picture += str(story.memory_picture)
        story.delete()
        if os.path.exists(old_picture):
            os.remove(old_picture)
        return HttpResponseRedirect(reverse_lazy('my_stories'))


def related_pictures_to_delete(related_stories):
    pictures_to_delete = []
    for story in related_stories:
        pictures_to_delete.append(str(story.memory_picture))
    return pictures_to_delete


def delete_related_pictures(related_pictures):
    for picture in related_pictures:
        picture_path = 'media/'
        picture_path += picture
        if os.path.exists(picture_path):
            os.remove(picture_path)

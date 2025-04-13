from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, CommentForm, EditAccountForm, EditProfileForm
from .models import Category, VideoContent, Comment, Profile, Ip
import random
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .tests import get_client_ip


# Create your views here.
# def index(request):
#     videos = VideoContent.objects.all()
#
#     context = {
#         'title': 'KinoFilm',
#         'video_contents': videos
#     }
#
#     return render(request, 'KinoFilm/index.html', context)

class ContentList(ListView):
    model = VideoContent
    template_name = 'KinoFilm/index.html'
    context_object_name = 'video_contents'
    extra_context = {
        'title': 'KinoFilm'
    }


def category_view(request, category_id):
    videos = VideoContent.objects.filter(category=category_id)
    category = Category.objects.get(id=category_id)

    context = {
        'video_contents': videos,
        'title': category.cat_name
    }

    return render(request, 'KinoFilm/index.html', context)



# def content_detail(request, pk):
#     video = VideoContent.objects.get(pk=pk)
#     videos = VideoContent.objects.all().exclude(pk=pk)
#     # videos = [i for i in videos if i.pk != pk]
#
#     context = {
#         'title': video.name,
#         'content': video,
#         'videos': videos
#     }
#
#     return render(request, 'KinoFilm/content_detail.html', context)

class ContentDetail(DetailView):
    model = VideoContent
    context_object_name = 'content'
    template_name = 'KinoFilm/content_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        videos = VideoContent.objects.all().exclude(pk=self.kwargs['pk'])
        video = VideoContent.objects.get(pk=self.kwargs['pk'])
        context['title'] = video.name
        context['contents'] = videos
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(content=video)

        ip = get_client_ip(self.request)

        if Ip.objects.filter(ip=ip).exists():
            video.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            video.views.add(Ip.objects.get(ip=ip))

        return context









def random_movie(request):
    movies = VideoContent.objects.all()
    if movies.exists():
        random_movie = random.choice(movies)
        return redirect('content', pk=random_movie.pk)
    else:
        return redirect('home')






def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user:
                    login(request, user)
                    messages.success(request, 'Успешный вход в аккаунт')
                    return redirect('main')
                else:
                    return redirect('login')
        else:
            form = LoginForm()

        context = {
            'title': 'Вход в аккаунт',
            'form': form
        }

        return render(request, 'KinoFilm/login.html', context)

def logout_view(request):
    logout(request)
    messages.warning(request, 'Выход с аккаунта')
    return redirect('main')

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                profile = Profile.objects.create(user=user)
                profile.save()
                return redirect('login')
        else:
            form = RegisterForm()
        context = {
            'title': 'Регистрация',
            'form': form
        }
        return render(request, 'KinoFilm/register.html', context)


class SearchContent(ContentList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        contents = VideoContent.objects.filter(name__iregex=word)
        return contents


def comment_save_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.content = VideoContent.objects.get(pk=pk)
                comment.save()
                return redirect('content', pk)

def comment_delete(request, pk):
    if request.user.is_authenticated:
        user = request.user
        try:
            comment = Comment.objects.get(pk=pk, user=user)
            if comment.user == user:
                comment.delete()

            return redirect('content', comment.content.pk)
        except:
            return redirect('main')

    else:
        return redirect('main')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user = request.user
        profile = Profile.objects.get(user=user)
        context = {
            'title': f'Профиль {profile.profile_name}',
            'profile': profile,
        }
        return render(request, 'KinoFilm/profile.html', context)


def edit_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = EditProfileForm(instance=request.user.profile)

        context = {
            'title': f'Изменить профиль',
            'form': form
        }
        return render(request, 'KinoFilm/edit.html', context)


def edit_account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = EditAccountForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                data = form.cleaned_data
                user = User.objects.get(id=request.user.id)
                if data['old_password']:
                    if user.check_password(data['old_password']):
                        if data['old_password'] and data['new_password'] == data['confirm_password']:
                            user.set_password(data['new_password'])
                            user.save()
                            update_session_auth_hash(request, user)
                            return redirect('profile')
                        else:
                            messages.warning(request, 'Пароли не соответствуют')
                            return redirect('edit_account')
                    else:
                        messages.warning(request, 'Неверный пароль')
                        return redirect('edit_account')
                else:
                    return redirect('profile')

        else:
            form = EditAccountForm(instance=request.user)

        context = {
            'title': 'Изменить данные аккаунта',
            'form': form
        }
        return render(request, 'KinoFilm/edit.html', context)
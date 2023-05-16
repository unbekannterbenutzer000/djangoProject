import django.views.generic
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.db.models import Q
from .blogs import RegisterUserForm
from .models import Post
from django.contrib.auth.models import User


class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = 'reg1.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class UserDetails(DetailView):
    template_name = 'users.html'
    model = User

class Bloglist(ListView):
    model = Post
    paginate_by = 5
    template_name = 'home.html'


class Bloglist1(Bloglist):
    paginate_by = 10


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class SearchResultsView(TemplateView):
    paginate_by = 5
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        ).distinct()
        context['object_list'] = object_list
        context['query'] = query
        return context


class SearchCategory_1(TemplateView):
    paginate_by = 5
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Post.objects.filter(
            Q(category__name='Новости дна')).distinct()
        context['object_list'] = object_list
        context['query'] = 'Новости дна'
        return context


class SearchCategory_2(TemplateView):
    paginate_by = 5
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Post.objects.filter(
            Q(category__name='Новости России')).distinct()
        context['object_list'] = object_list
        context['query'] = 'Новости России'
        return context


class SearchCategory_3(TemplateView):
    paginate_by = 5
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Post.objects.filter(
            Q(category__name='Новости мира')).distinct()
        context['object_list'] = object_list
        context['query'] = 'Новости мира'
        return context

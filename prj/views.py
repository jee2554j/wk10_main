from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from shop.models import Item


# TemplateView 제네릭 뷰를 상속받아서 HomeView 클래스 작성
class HomeView(TemplateView):
    # TemplateView를 상속받을 때 template_name 클래스 변수 오버라이딩은 필수
    # 템플릿 파일의 이름을 지정하는데, 파일의 위치는 settings.TEMPLATES.DIRS 항목에서 정의함
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class PostView(ListView):
    model = Post
    template_name = 'home.html'


class ItemView(ListView):
    model = Item
    template_name = 'home.html'


class CardView(ListView):
    model = Post
    template_name = 'cardviewhome.html'


class CarouselView(ListView):
    model = Item
    template_name = 'carouselhome.html'

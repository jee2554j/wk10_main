from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings                         # 추가 1
from django.conf.urls.static import static
from prj.views import UserCreateView, UserCreateDoneTV, HomeView
from prj.views import PostView
from prj.views import ItemView
from prj.views import CardView, CarouselView

urlpatterns = [
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    re_path(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    path('', PostView.as_view(), name='home'),
    path('card/', CardView.as_view(), name='CardView'),
    path('carousel/', CarouselView.as_view(), name='CarouselView'),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('pizzas/', include('pizzas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:                                       # 추가 2
    import debug_toolbar                                 # 추가 2
    urlpatterns += [                                     # 추가 2
        path('__debug__/', include(debug_toolbar.urls)), # 추가 2
    ]                                                    # 추가 2

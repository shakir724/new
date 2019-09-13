from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import (path, include, re_path)

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from accounts import views as accounts_view
from webpages import views as webpages_view
from settings import views as settings_view


router = DefaultRouter()

# accounts
router.register('Accounts', accounts_view.AccountViewSet, base_name='Accounts')

# webpages
router.register('Webpages', webpages_view.WebpageViewSet, base_name='Webpages')
router.register('Fonts', webpages_view.FontViewSet, base_name='Fonts')
router.register('Themes', webpages_view.ThemeViewSet, base_name='Themes')
router.register('WebpageImages', webpages_view.WebpageImageViewSet, base_name='WebpageImages')
router.register('WebpageVideos', webpages_view.WebpageVideoViewSet, base_name='WebpageVideos')
router.register('ToDoList', webpages_view.ToDoListViewSet, base_name='ToDoList')
router.register('GuestList', webpages_view.GuestListViewSet, base_name='GuestList')

# settings
router.register('Overview', settings_view.OverviewViewSet, base_name='Overview')
router.register('SocialMedia', settings_view.SocialMediaViewSet, base_name='SocialMedia')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('', TemplateView.as_view(template_name='react.html')),
    re_path(r'^dashboard/', TemplateView.as_view(template_name='react.html')),
    re_path(r'^login/', TemplateView.as_view(template_name='react.html')),
    re_path(r'^register/', TemplateView.as_view(template_name='react.html')),
]

# media url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

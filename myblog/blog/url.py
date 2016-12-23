"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns, urlpatterns
# from django.contrib import admin
import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index', views.index),
    url(r'^logout', views.logout),
    url(r'^login', views.login),
    url(r'^signup', views.signup),
    # url(r'^tag/(?P<tag>\w+)/$', views.TagView, name='tag-detail-view'),
    url(r'^article/detail/$', views.article_detail)
]

# urlpatterns += staticfiles_urlpatterns()

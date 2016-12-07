"""mutexdb URL Configuration

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
from django.contrib import admin
from mutexapp import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.searchproject, name='searchproject'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^faq/$', TemplateView.as_view(template_name='faq.html'), name='faq'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^thanks/$', views.thanks, name='thanks_for_feedback'),
    # url(r'^test-captcha/$', views.feedback, name='test-captcha-in-feedback-form'),
    # This is just to test the captcha to be used in feedback form. I made a different page
    # cause you never know if it might work, there is an ajax component in the template.
    # The url is https://github.com/mbi/django-simple-captcha/blob/master/docs/usage.rst
]

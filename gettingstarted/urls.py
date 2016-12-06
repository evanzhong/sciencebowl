from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

from django.contrib.auth import views as auth_views #For Login system
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^generateset', hello.views.generateset, name='generateset'),
    url(r'^questionset', hello.views.questionset, name='questionset'),
    url(r'^addquestions', hello.views.addquestions, name='addquestions'),
    url(r'^questionsconfirmed', hello.views.questionsconfirmed, name='questionsconfirmed'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^upload', hello.views.upload, name='upload'),
    # Login urls
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls))
]

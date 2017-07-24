from django.conf.urls import include, url,patterns
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Vdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^index/',index),
    url(r'^index/',base),
    url(r'^view/',shenghuo),
    url(r'^article/(?P<id>[0-9]+)/$',detail,name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r"^uploads/(?P<path>.*)$",\
    # "django.views.static.serve",\
    # {"document_root":settings.MEDIA_ROOT,}),
)

from django.conf.urls import include, url,patterns
from django.contrib import admin
from blog.views import *
from django.contrib.auth import views
#from blog import views
# namespace = 'blog'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Vdjango.views.home', name='home'),
    #url(r'^blog/', include('blog.urls',namespace = 'blog')),
    # url(r'^index/',index),
    url(r'^index/',base),
    url(r'^$/',index,name='index'),
    url(r'^logout/',views.logout,name='logput'),
    url(r'password_change/$',views.password_change,name='password_change'),
    url(r'password_change/done/$',views.password_change_done,name='password_change_done'),
    url(r'password_reset/',views.password_reset,name='password_reset'),
    url(r'password_reset/done/$',views.password_reset_done,name='password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset_confirm,name='password_reset_confirm'),
    url(r'reset/done/$',views.password_reset_complete,name='password_reset_comlete'),
    url(r'^view/',shenghuo),
    url(r'register/',register,name='register'),
   # url(r'login/',include('django.contrib.auth.urls')),
    url(r'login/',views.login,name='login'),
    url(r'^article/(?P<id>[0-9]+)/$',detail,name='detail'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r"^uploads/(?P<path>.*)$",\
    # "django.views.static.serve",\
    # {"document_root":settings.MEDIA_ROOT,}),
)

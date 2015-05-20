from django.conf.urls import patterns, include, url
from django.contrib import admin
from yonghu import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhongchou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^denglu/', views.denglu, name="denglu"),
    url(r'^zhuce/', views.zhuce, name="zhuce"),
    url(r'^index/', views.index, name="index"),
    url(r'^raisePublic/', views.raisePublic, name="raisePublic"),
    url(r'^raisePublicForm/', views.raisePublicForm, name="raisePublicForm")
)

from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	game,
	snt,
	cultural,
	fmc,
	vox,
	senate,
	post_detail,
	post_update,
	post_delete,

	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^accounts/profile/$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^game/$', game, name='game'),
	url(r'^snt/$', snt, name='snt'),
	
	url(r'^cultural/$', cultural, name='cultural'),
	url(r'^fmc/$', fmc, name='fmc'),
	url(r'^vox/$', vox, name='vox'),
	url(r'^senate/$', senate, name='senate'),

    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

	# url(r'^snt/$', "posts.views.snt"),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

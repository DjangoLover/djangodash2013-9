from django.conf.urls import patterns, url

import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(
        r'^(?P<slug>[\w-]+)/$',
        views.SuggestionView.as_view(),
        name='suggestion'
    )
)

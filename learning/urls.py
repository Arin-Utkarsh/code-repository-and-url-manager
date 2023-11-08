from django.urls import path

from learning.views import gallery,add_context,urls,snippets

urlpatterns=[
    path('',gallery ,name='gallery'),
    path('add_context/',add_context),
    path('add_context/gallery',gallery),
    path('url/',urls,name='urls'),
    path('snippets/',snippets,name='snippets'),
]
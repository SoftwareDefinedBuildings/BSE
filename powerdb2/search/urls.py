
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^getresultsStatus/', 'powerdb2.search.views.getresultsStatus'),
    (r'^genQuery/', 'powerdb2.search.views.genQuery'),
    (r'^getNextSearchResults/', 'powerdb2.search.views.getNextSearchResults'),
    (r'^getExtraResults/', 'powerdb2.search.views.getExtraResults'), 
    (r'^replace/', 'powerdb2.search.views.replace'), 
    (r'^getMetadata/', 'powerdb2.search.views.getMetadata'),
    (r'^getSimilar/', 'powerdb2.search.views.getSimilar'),
    (r'^updateMetadata/', 'powerdb2.search.views.updateMetadata'),
    (r'^getresults/', 'powerdb2.search.views.getresults'),
    (r'^$', 'powerdb2.search.views.search'),
)

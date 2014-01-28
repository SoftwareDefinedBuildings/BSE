import os
import sys
import site

os.environ['DJANGO_SETTINGS_MODULE'] = 'powerdb2.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
site.addsitedir('/Library/Python/2.7/site-packages')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

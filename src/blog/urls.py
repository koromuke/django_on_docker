
# coderedcms
from django.urls import path, include, re_path
from coderedcms import admin_urls as coderedadmin_urls
from coderedcms import search_urls as coderedsearch_urls
from coderedcms import urls as codered_urls

from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls

# from bakerydemo.search import views as search_views
# from .api import api_router

from puput import urls as puput_urls


urlpatterns = [
    # Admin
    path('django-admin/', admin.site.urls),
    path('admin/', include(coderedadmin_urls)),

    # Documents
    path('docs/', include(wagtaildocs_urls)),

    # Search
    path('search/', include(coderedsearch_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # the page serving mechanism. This should be the last pattern in
    # the list:

    # Alternatively, if you want CMS pages to be served from a subpath
    # of your site, rather than the site root:
    re_path(r'^pages/', include(codered_urls)),

    re_path(r'',include(puput_urls)),
    # re_path(r'', include(wagtail_urls)),
    re_path(r'', include(codered_urls)),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
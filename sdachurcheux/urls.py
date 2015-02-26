from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.site.site_header = 'St. Eustatius SDA Church Admin'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdachurcheux.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^announcements/', include('events.urls', namespace='events'),),
    url(r"^ajax/photos/upload/$", "assets.views.upload_photos", name="upload_photos"),
    url(r"^ajax/photos/recent/$", "assets.views.recent_photos", name="recent_photos")
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
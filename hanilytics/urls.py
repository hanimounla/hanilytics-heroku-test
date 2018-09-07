from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
     url(r'^admin/', admin.site.urls),
    url(r'', include(('core.urls', 'core'), namespace='core')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
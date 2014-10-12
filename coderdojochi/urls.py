from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'coderdojochi.views.home', name='home'),
    url(r'^faqs/$', 'coderdojochi.views.faqs', name='faqs'),
    url(r'^donate/$','coderdojochi.views.donate',name='donate'),
    url(r'^about/$','coderdojochi.views.about',name='about'),
    url(r'^volunteer/$', 'coderdojochi.views.volunteer', name='volunteer'),


    url(r'^student/(?P<student_id>[\d]+)/$', 'coderdojochi.views.student_detail', name='student_detail'),

    url(r'^classes/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'coderdojochi.views.sessions', name='sessions'),
    url(r'^classes/$', 'coderdojochi.views.sessions', name='sessions'),
    url(r'^class/(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<slug>[-\w]+)/(?P<session_id>[\d]+)/sign-up/(?P<student_id>[\d]+)/$', 'coderdojochi.views.session_sign_up', name='session_sign_up'),
    url(r'^class/(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<slug>[-\w]+)/(?P<session_id>[\d]+)/sign-up/$', 'coderdojochi.views.session_sign_up', name='session_sign_up'),
    url(r'^class/(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<slug>[-\w]+)/(?P<session_id>[\d]+)$', 'coderdojochi.views.session_detail', name='session_detail'),

    url(r'^meeting/(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<meeting_id>[\d]+)/sign-up/$', 'coderdojochi.views.meeting_sign_up', name='meeting_sign_up'),
    url(r'^meeting/(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/(?P<meeting_id>[\d]+)$', 'coderdojochi.views.meeting_detail', name='meeting_detail'),

    url(r'^welcome/$', 'coderdojochi.views.welcome', name='welcome'),

    url(r'^dojo/$', 'coderdojochi.views.dojo', name='dojo'),

    #override the default urls
    url(r'^password/change/$', auth_views.password_change, name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),

    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^contact/', include('contact_form.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

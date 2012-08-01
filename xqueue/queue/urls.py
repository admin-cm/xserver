from django.conf.urls import patterns, include, url

urlpatterns = patterns('queue.views',
    # General
    #------------------------------------------------------------
    url(r'^login/$', 'log_in'),
    url(r'^status/$', 'status'),

    # Push to queue from LMS
    #------------------------------------------------------------
    url(r'^submit/$', 'submit'),

    # External pulling interface
    #------------------------------------------------------------
    url(r'^get_queuelen/$', 'get_queuelen'),
    url(r'^get_submission/$', 'get_submission'),
    url(r'^put_result/$', 'put_result'),
)

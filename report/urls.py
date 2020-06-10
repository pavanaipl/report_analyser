from django.conf.urls import url
from .views import *



urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^category/new/$', category, name='category'),
    url(r'^category_detail/(?P<pk>\d+)/$', category_detail, name='category_detail'),
    url(r'^category_update/(?P<pk>\d+)/$', category_update, name='category_update'),
    url(r'^category-information/$', category_information, name='category_information'),

    url(r'^report/new/$', report, name='report'),
    url(r'^report_detail/(?P<pk>\d+)/$', report_detail, name='report_detail'),
    url(r'^report_update/(?P<pk>\d+)/$', report_update, name='report_update'),
    url(r'^report-information/$', report_information, name='report_information'),


    url(r'^comment/new/$', comment, name='comment'),
    url(r'^comment_detail/(?P<pk>\d+)/$', comment_detail, name='comment_detail'),
    url(r'^comment_update/(?P<pk>\d+)/$', comment_update, name='comment_update'),

    url(r'^report_comments/(?P<pk>\d+)/$', report_comments, name='report_comments'),
    url(r'^filter_report/$', filter_report, name='filter_report'),

    url(r'^signup/', UserAPIs.as_view({'post': 'signup'})),
    url(r'^login/', UserAPIs.as_view({'post': 'login'})),
    url(r'^users-list/', UsersOtherAPIs.as_view({'get': 'get_users_list'})),
    url(r'^pivot-queries/', UsersOtherAPIs.as_view({'get': 'pivot_queries'})),
    url(r'^send-template/', UsersOtherAPIs.as_view({'get': 'render_html'})),


    ]
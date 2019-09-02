# from django.urls import include, path, re_path
# # from .import views
# from wagtailimportexport import urls as wagtailimportexport_urls
# from wagtail.admin import urls as wagtailadmin_urls
# from coderedcms.views import import_pages_from_csv_file
#
# # app_name = 'base'
#
#
# urlpatterns = [
#     # path('', views.IndexView.as_view(), name='index'),
#     # path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
#     # path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # path('comment/<int:post_pk>/', views.CommentView.as_view(), name='comment'),
#     path('codered/import-export/import_from_csv/',
#          import_pages_from_csv_file, name="import_from_csv"),
#     re_path(r'', include(wagtailadmin_urls)),
#     re_path(r'', include(wagtailimportexport_urls)),
# ]

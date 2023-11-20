from django.contrib import admin
from django.urls import path
from admin_app import views as admin_view
from show_app import views as show_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',admin_view.home,name='home'),
    path('log_inaction/',admin_view.log_inaction,name='log_inaction'),
    path('registeraction/',admin_view.registeraction,name='registeraction'),
    path('user_profile/',show_view.user_profile,name='user_profile'),
    path('admin_profile/',admin_view.admin_profile,name='admin_profile'),
    path('categoryaction/',admin_view.categoryaction,name='categoryaction'),
    path('log_out/',admin_view.log_out,name='log_out'),
    path('approve<int:id>/',admin_view.approve,name='approve'),
    path('reject<int:id>/',admin_view.reject,name='reject'),
    path('add_show/',show_view.add_show,name='add_show'),
    path('add_showaction/',show_view.add_showaction,name='add_showaction'),
    path('edit_profile/',show_view.edit_profile,name='edit_profile'),
    path('find_show/',show_view.find_show,name='find_show'),
    path('searchaction/',show_view.searchaction,name='searchaction'),
    path('edit_profileaction/',show_view.edit_profileaction,name='edit_profileaction'),
    path('see_details<int:id>/',show_view.see_details,name='see_details'),
    path('gallery/',show_view.gallery,name='gallery'),
    path('add_to_watchlist/',show_view.add_to_watchlist,name='add_to_watchlist'),
    path('my_watchlist/',show_view.my_watchlist,name='my_watchlist'),
    path('my_shows/',show_view.my_shows,name='my_shows'),
    path('edit_shows_user<int:id>/',show_view.edit_shows_user,name='edit_shows_user'),
    path('edit_showaction/',show_view.edit_showaction,name='edit_showaction'),
    path('find_my_show/',show_view.find_my_show,name='find_my_show'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
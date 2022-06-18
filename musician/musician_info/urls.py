from django.urls import path
from musician_info import views

app_name = 'musician_info'

urlpatterns = [
    #     path('', views.index, name='index'),
    path('', views.index.as_view(), name='index'),
    #     path('add_musician/', views.add_musician, name='add_musician'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    #     path('add_album/', views.add_album, name='add_album'),
    path('add_album/', views.AddAlbum.as_view(), name='add_album'),
    #     path('musician_detail/<int:artist_id>/',views.musician_detail, name='musician_detail'),
    path('musician_detail/<pk>/',
         views.MusicianDetail.as_view(), name="musician_detail"),
    #     path('delete_musician/<int:artist_id>',views.delete_musician, name='delete'),
    path('delete_musician/<pk>', views.DeleteMusician.as_view(),
         name='delete_musician'),
    #     path('update_musician/<int:artist_id>',views.update_musician, name='update_musician'),
    path('update_musician/<pk>', views.UpdateMusician.as_view(),
         name='update_musician'),
    #     path('update_album/<int:album_id>/',views.update_album, name='update_album'),
    path('update_album/<pk>', views.UpdateAlbum.as_view(), name='update_album'),
    #     path('delete_album/<int:album_id>', views.delete_album, name='delete_album')
    path('delete_album/<pk>', views.DeleteAlbum.as_view(), name='delete_album')
]

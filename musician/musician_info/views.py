from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from musician_info.forms import Album_Form
from musician_info import models
from musician_info import forms

# Create your views here.


# def index(request):
#     musicians = Musician.objects.order_by('first_name')
#     dict = {'title': 'Home', 'musicians': musicians}
#     return render(request, 'musician_info/index.html', dict)


class index(ListView):
    context_object_name = 'musician_list'
    model = models.Musician

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context

    template_name = 'musician_info/index.html'


# def add_musician(request):
#     form = Musician_Form()

#     if request.method == 'POST':
#         form = Musician_Form(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)

#     dict = {'title': 'Add Musician', 'musician_form': form}
#     return render(request, 'musician_info/add_musician.html', dict)

class AddMusician(CreateView):
    model = models.Musician
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Musician'
        return context
    template_name = 'musician_info/add_musician.html'


# def add_album(request):
#     form = Album_Form()
#     dict = {}

#     if request.method == 'POST':
#         form = Album_Form(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             dict.update({'success': 'Album added successfully!'})

#     dict.update({'title': 'Add Album', 'album_form': form})
#     return render(request, 'musician_info/add_album.html', dict)

class AddAlbum(CreateView):
    model = forms.Album_Form
    form_class = Album_Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add Album"
        return context

    template_name = 'musician_info/add_album.html'


# def musician_detail(request, artist_id):
#     artist_details = Musician.objects.get(pk=artist_id)
#     artist_albums = Album.objects.filter(artist=artist_id)
#     dict = {'title': 'Musician Details',
#             'artist_details': artist_details, 'artist_albums': artist_albums}
#     return render(request, 'musician_info/musician_detail.html', dict)

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Musician Details'
        return context
    template_name = "musician_info/musician_detail.html"


# def delete_musician(request, artist_id):
#     artist = Musician.objects.get(pk=artist_id).delete()
#     dict = {'title': 'Musician Deleted',
#             'success': 'Musician deleted successfully!'}
#     return render(request, 'musician_info/delete.html', dict)

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy("musician_info:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Musician'
        return context
    template_name = "musician_info/delete_temp.html"


# def update_musician(request, artist_id):
#     musician_details = Musician.objects.get(pk=artist_id)
#     form = Musician_Form(instance=musician_details)
#     dict = {}

#     if request.method == 'POST':
#         form = Musician_Form(request.POST, instance=musician_details)

#         if form.is_valid():
#             form.save(commit=True)
#             dict.update({'success': 'Musician updated successfully!'})
#     dict.update({'title': 'Update Musician', 'musician_form': form})
#     return render(request, 'musician_info/update_musician.html', dict)

class UpdateMusician(UpdateView):
    model = models.Musician
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Musician'
        return context
    template_name = "musician_info/add_musician.html"


# def update_album(request, album_id):
#     album_details = Album.objects.get(pk=album_id)
#     form = Album_Form(instance=album_details)
#     dict = {}

#     if request.method == 'POST':
#         form = Album_Form(request.POST, instance=album_details)

#         if form.is_valid():
#             form.save(commit=True)
#             dict.update({'success': 'Album updated successfully!'})
#     dict.update({'title': 'Update Album', 'album_form': form})
#     return render(request, 'musician_info/update_album.html', dict)

class UpdateAlbum(UpdateView):
    model = models.Album
    fields = ('album_name', 'release_date', 'rating')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Album'
        return context
    template_name = "musician_info/add_album.html"


# def delete_album(request, album_id):
#     album = Album.objects.get(pk=album_id).delete()
#     dict = {'title': 'Album deleted', 'success': 'Album deleted successfully!'}
#     return render(request, 'musician_info/delete.html', dict)

class DeleteAlbum(DeleteView):
    context_object_name = 'album'
    model = models.Album
    # success_url = reverse_lazy(
    #     'musician_info:musician_detail', object.album.artist.id)

    def get_success_url(self):
        return reverse_lazy('musician_info:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Album"
        context["dlt"] = True
        return context

    template_name = 'musician_info/delete_temp.html'

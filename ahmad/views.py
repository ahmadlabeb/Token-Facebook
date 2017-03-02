from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import album
# Create your views here.
def index(r):
    all_album=album.objects.all()
    html=''
    # for album1 in all_album:
    #     url='/ahmad/'+str(album1.id)+'/'
    #     html+='<ul>' \
    #           '<li><a href="'+url+'">'+album1.albume_title+'</a></li>' \
    #                                                    '</ul'
    template=loader.get_template('ahmad/index.html')
    context={
        'all_albume':all_album,
    }
    return render(r,'ahmad/index.html',context)
def about(r,album_id):
    return HttpResponse("<h1>abu labeb</h1>"+str(album_id))
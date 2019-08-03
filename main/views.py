from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Movie

# Create your views here.
def index(request):
    movie=Movie.objects.order_by('?')[:51]
    context={
        "movie":movie,
    }

    return render(request,'index.html',context)

def detail(request,movie_id):
    movie = Movie.objects.get(id = movie_id)
    context={
        "movie":movie,
    }
    return render(request,'detail.html',context)

def search(request):
    searcht=request.GET['search']
    
    movie=Movie.objects.filter(name__icontains=searcht)

    context={
        "movie":movie,
    }
    return render(request,'search.html',context)

def tag(request):

    return render(request,'tag.html')

def random(request):
    movie=Movie.objects.order_by('?')[0]
    context={
        "movie":movie,
    }
    return render(request,'random.html',context)

def shoppingbag(request):

    return render(request, 'shoppingbag.html')

def ranking(request):
    url1 = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

    html_ranking1 = requests.get(url1).text
    soup_ranking1 = BeautifulSoup(html_ranking1, "lxml")

    rankings1 = soup_ranking1.select('div.tit3')
    Movie_ranking1 = [ranking1.get_text().strip() for ranking1 in rankings1]

    
    url2 = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190801"
    html_ranking2 = requests.get(url2).text
    soup_ranking2 = BeautifulSoup(html_ranking2, "lxml")

    rankings2 = soup_ranking2.select('div.tit5')
    Movie_ranking2 = [ranking2.get_text().strip() for ranking2 in rankings2]

    return render(request, 'ranking.html',{"Movie_ranking1":Movie_ranking1, "Movie_ranking2":Movie_ranking2})

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=watcha_TF.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Name"),
        smart_str(u"Netflix"),
        smart_str(u"Watcha"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.name),
            smart_str(obj.netflix),
            smart_str(obj.watcha),
        ])
    return response
export_csv.short_description = u"Export CSV"
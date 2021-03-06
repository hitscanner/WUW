from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.models import User
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    if request.is_ajax():
        movies = Movie.objects.all()
        paginator = Paginator(movies, 12)
        page = request.GET.get('page')
        # movies = paginator.get_page(page)
        try:
            movies = paginator.get_page(page)
        except PageNotAnInteger:
            movies = paginator.get_page(1)
        except EmptyPage:
            movies = paginator.get_page(paginator.num_pages)

        context = {
            "movies": movies,

        }
        return render(request, 'ajax_index.html', context)
    else:
        movie=Movie.objects.all()
        paginator = Paginator(movie,12) 
        page = request.GET.get('page')
        movies = paginator.get_page(page)
        last_page =  paginator.num_pages

        context = {
            "movie":movie,
            "movies": movies,
            "last_page": last_page,
        }
        return render(request, 'index.html', context)

def detail(request, movie_id):
    if movie_id == 0:
        movie = Movie.objects.order_by('?')[0]
    else:
        movie = Movie.objects.get(id=movie_id)

    context = {
        "movie": movie,
    }
    return render(request, 'detail.html', context)


def search(request):
    searcht = request.GET['search']
    movie = Movie.objects.filter(name__icontains=searcht)
    context = {
        "movie": movie,
        "searcht": searcht,
    }
    return render(request, 'search.html', context)


def cart(request, user_id):
    user = User.objects.get(id=user_id)
    like_movies = user.like_user_set.all()
    netflix_cnt = 0
    watcha_cnt = 0

    for m in like_movies:
        if m.netflix == True:
            netflix_cnt += 1
        if m.watcha == True:
            watcha_cnt += 1

    context = {
        "like_movies": like_movies,
        "netflix_cnt": netflix_cnt,
        "watcha_cnt": watcha_cnt,
    }

    return render(request, 'cart.html', context)


def tag(request):
    
    return render(request,'tag.html') 

def select(request):
    if request.is_ajax():
        category_list = request.GET.getlist('category_list[]')
        all_select = request.GET['all_select']
        if all_select == "true":
            movie=Movie.objects.all()
            paginator = Paginator(movie,12) 
            page = request.GET.get('page')
            movie = paginator.get_page(page)
        else:
            for category in category_list:
                movie = Movie.objects.filter(**{category: True})
        
        context= {
            "movie":movie,
            "all_select":all_select,
            "category_list":category_list,
        }
        return render(request,'select.html',context)

    #search_s=request.GET.getlist('service[]')
    # search_g=request.GET['genre']
    #genre_var=request.GET.getlist('genre[]')
    '''
    if "netflix" in search_s:
        # movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False))
        if 'action' in genre_var: 
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(action=True))
        if 'fantasy' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(fantasy=True))
        if 'sf' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(sf=True))
        if 'comedy' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(comedy=True))
        if 'romance' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(romance=True))
        if 'drama' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(drama=True))
        if 'animation' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(animation=True))
        if 'thriller' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(thriller=True))
        if 'horror' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = False) & Q(horror= True))
    elif "watcha" in search_s:
        # movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True))
        if 'action' in genre_var: 
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(action=True))
        if 'fantasy' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(fantasy=True))
        if 'sf' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(sf=True))
        if 'comedy' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(comedy=True))
        if 'romance' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(romance=True))
        if 'drama' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(drama=True))
        if 'animation' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(animation=True))
        if 'thriller' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(thriller=True))
        if 'horror' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = False) & Q(watcha =True) & Q(horror= True))
    if "netflix" in search_s and "watcha" in search_s:
        # movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha = True))
        if 'action' in genre_var: 
            movie=Movie.objects.all().filter(Q(netflix =True) & Q(watcha =True) & Q(action=True))
        if 'fantasy' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix =True) & Q(watcha =True) & Q(fantasy=True))
        if 'sf' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha =True) & Q(sf=True))
        if 'comedy' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha =True) & Q(comedy=True))
        if 'romance' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha =True) & Q(romance=True))
        if 'drama' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix =True) & Q(watcha =True) & Q(drama=True))
        if 'animation' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha =True) & Q(animation=True))
        if 'thriller' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha =True) & Q(thriller=True))
        if 'horror' in genre_var:
            movie=Movie.objects.all().filter(Q(netflix = True) & Q(watcha =True) & Q(horror= True))

        # list=['action','fantasy','sf','comedy','romance','drama','animation','thriller','horror']
        # for i in genre_var:
        #     if list[i] in genre_var:
        #         movie=Movie.objects.all().filter(Q(netflix =True) & Q(watcha =True) & Q(genre_var[i]=True))

        # ----------------------------------------------------------------------다중선택 안됨
    '''
    

def random(request):
    movie=Movie.objects.order_by('?')[0]

    context={
        "movie":movie,
    }
    return render(request,'random.html',context)

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

    return render(request, 'ranking.html', {"Movie_ranking1": Movie_ranking1, "Movie_ranking2": Movie_ranking2})


def like(request):
    if request.is_ajax():
        movie_id = request.GET['movie_id']
        movie = Movie.objects.get(id=movie_id)

        if not request.user.is_authenticated:
            message = "로그인을 해주세요"
            context = {"like_count": movie.like_count, "message": message}

            return HttpResponse(json.dumps(context), content_type='application/json')

        movie_like, movie_like_created = movie.like_set.get_or_create(
            user=request.user)

        if not movie_like_created:
            movie_like.delete()
            message = "좋아요 취소"
        else:
            message = "좋아요"

        context = {'like_count': movie.like_count, "message": message}
        return HttpResponse(json.dumps(context), content_type='application/json')

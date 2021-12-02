# for Ajax
import json

from django.core import serializers
from django.http import JsonResponse

# for user
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# for query
## filter(Q(속성이름__icontains = 검색물))로 이용
from django.db.models import Q



from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import CustomerUser, MovieInfo, Screen, Seat, TheaterInfo


# Create your views here.
def home(request):
    return render(request, 'main.html')

def movie_list(request):
    return render(request, 'movie-list.html')

def movie_detail(request):
    return render(request, 'movie-detail.html')

def ticket_list(request):
    movies = MovieInfo.objects.all()
    context = {
        'movies' : movies,
        }
    return render(request, 'ticketing.html', context)


def ticketing(request):
    if request.is_ajax:
        data = request.GET.get('movie_id', None)
        print(data)
        movies = MovieInfo.objects.all()
        
        selected_data_set = movies.filter(movie_name = data)
        print(selected_data_set)
        screens = []
        for movie_data in selected_data_set :
            screens += Screen.objects.filter(movie_id = movie_data.movie_id)
        # screens = Screen.objects.filter(movie_id=selected_data_set)
        print(screens)
        theaters = Screen.objects.get(theater_number=screens)
        print(theaters)
        """ theaters_num = []
        for theater_data in screens:
            theaters_num += theater_data.theater_number
            print(theater_data)
        print(theaters_num) """
        
        #theaters = TheaterInfo.objects.all()
        #theaters.filter(theater_number=theaters_num)
        """ context = {
            'theaters' : theaters
        } """

    # if request.method == "POST":
        # 영화이름 movie
        # 극장 theater
        # 날짜
        # 시간
        # 좌석
        # 유저
        # A이면~~ B이면 ~~ 해서 짤라서 보내줌
    #return JsonResponse(context, status=200)
    return HttpResponse("hi")

def ticketing_detail(request):
    return render(request, 'ticketing.html')

def events(request):
    return render(request, 'events.html')

def forget(request):
    return render(request, 'forget.html')

def findID(request):
    return render(request, 'findID.html')

def signup_view(request):

    # POST 방식으로 요청이 들어올 경우.
    if request.method == "POST":

        # 패스워드가 같은지 체크
        if request.POST['password1'] == request.POST['password2']:
            custom_user = CustomerUser()
            custom_user.username = request.POST['username']
            custom_user.password = request.POST['password1']
            custom_user.phone_number = request.POST['phone_number']
            custom_user.rank = '1'
            print(request.POST['username'])
            custom_user.save()

            user = authenticate(request=request, username=custom_user.username, password=custom_user.password)
            login(request, user)
            return redirect("home")
        
        # 패스워드가 다른 경우
        else:
            return HttpResponse("패스워드가 일치하지 않습니다.")
        
    # GET 방식으로 요청이 들어올 경우.
    else:
        context = {

        }
        return render(request, 'signup.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("유저의 형식이 옳지 않습니다.")
            return redirect("home")
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("main")
    

def events(request):
    return render(request, 'events.html')
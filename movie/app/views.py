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
    context = {}
    if request.is_ajax:
        branch_offices = []
        if request.GET.get('movie_id'):
            res_id = request.GET.get('movie_id')
            movies = MovieInfo.objects.filter(movie_id = res_id)
            print("선택된 영화:", movies)
            screens = Screen.objects.filter(movie_id = res_id)
            print("선택된 영화 상영 정보:", screens)
            theaters = []
            for screen in screens:
                theaters.append(((screen.theater_number).branch_office).city)
                branch_offices.append((screen.theater_number).branch_office)
            context = {
                'theaters': theaters,
            }
            print("선택된 영화가 상영되는 지점 정보:", context)
            return JsonResponse(context, status=200)
    
        elif request.GET.get('movie_city'):
            print("branch_offices",branch_offices)
            branch_names = []
            for branch_office in branch_offices:
                branch_names.append(branch_office.name)
            context = {
                'branch_names': branch_names,
            }
            print("branch_name:", context)
            return JsonResponse(context, status=200)

    # if request.method == "POST":
        # 영화이름 movie
        # 극장 theater
        # 날짜
        # 시간
        # 좌석
        # 유저
        # A이면~~ B이면 ~~ 해서 짤라서 보내줌
    #return HttpResponse("hi")
    return JsonResponse(context, status=200)

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

def mypage(request):
    return render(request, './mypage/mypage.html')

def eventrecord(request):
    return render(request, './mypage/eventrecord.html')

def infomodification(request):
    return render(request, './mypage/infomodification.html')

def reservationinfo(request):
    return render(request, './mypage/reservationinfo.html') 


def manage_main(request):
    return render(request, './manage_page/manage_main.html')

def manage_revenue(request):
    return render(request, './manage_page/manage_revenue.html')
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from Main.models import Challenges
import random
from django.db.models import Count

from django.contrib.auth import get_user
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from accounts.models import Player
from django.urls import reverse

import datetime
import json
import random
import uuid

# Create your views here.

#main pages
def index(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')    

def leaderboard(request):
    print("RUNNING")
    if not request.user.is_authenticated:
        return redirect('login')
    all_players = Player.objects.all().order_by('-score')

    context = {'player':Player.objects.get(username=request.user), 'players': all_players}
    return render(request, 'main/leaderboard.html', context)

def page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)

def dashboard(request):
    user = request.user
    all_players = Player.objects.all().order_by('-score')
    all_challenges = Challenges.objects.all().order_by('points')[:]
    isSolved = []
    index = 0

    for challenge in all_challenges:
        if(request.user in challenge.players_solved.all()):
            isSolved.append(True)
            index += 1
        else:
            isSolved.append(False)
    
    for player in all_players:
        if player.username == user.username:
            rank = list(all_players).index(player) + 1
            break
    context = {'user': user,'player':Player.objects.get(username=user), 'total_players':all_players.count, 'rank':rank, 
    'challenges': Challenges.objects.all().order_by('points')[:], 'isSolved':isSolved, 'index':index}
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'main/dashboard.html', context)


# Challenge pages

def gettingStarted(request):
    context = {"challenge": Challenges.objects.get(title="Getting Started"), "solved":False}
    context_solved = {"challenge": Challenges.objects.get(title="Getting Started"), "solved":True}

    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')
        if(request.user in Challenges.objects.get(title="Getting Started").players_solved.all()):
            return render(request, 'main/challenges/gettingstarted.html', context_solved)
            
        else: return render(request, 'main/challenges/gettingstarted.html', context)
    elif request.method == "POST":
        data = request.body
        data = json.loads(data.decode('utf-8'))

        if data['flag'] == Challenges.objects.get(title="Getting Started").flag:
            # Logic for right Code
            if(request.user not in Challenges.objects.get(title="Getting Started").players_solved.all()):
                Challenges.objects.get(title="Getting Started").players_solved.add(Player.objects.get(username=request.user))
                point_system(request, Challenges.objects.get(title="Getting Started").points)
                return JsonResponse({"works": True})
            else:
                return JsonResponse({"already submitted": True})


        else:
            # Logic for Wrong Code
            return JsonResponse({"works": False})

def cookieMonster(request):
    # return render(request, 'main/challenges/cookie.html', context)
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        flag = Challenges.objects.get(title="Cookie Monster").flag
        if not request.COOKIES.get('CookieJar'):
            who = user.username
        else:
            who = request.COOKIES.get("CookieJar")

        print(who)
        context = {"challenge": Challenges.objects.get(title="Cookie Monster"), "code": flag, "who": who}
        to_rend = render(request, "main/challenges/cookie.html", context)
        to_rend.set_cookie("CookieJar", who)

        return to_rend
    
    elif request.method == "POST":
        data = request.body
        data = json.loads(data.decode('utf-8'))

        if data['flag'] == Challenges.objects.get(title="Cookie Monster").flag:
            # Logic for right Code
            if(request.user not in Challenges.objects.get(title="Cookie Monster").players_solved.all()):
                Challenges.objects.get(title="Cookie Monster").players_solved.add(Player.objects.get(username=request.user))
                point_system(request, Challenges.objects.get(title="Cookie Monster").points)
                return JsonResponse({"works": True})
            else:
                return JsonResponse({"already submitted": True})

        else:
            # Logic for Wrong Code
            return JsonResponse({"works": False})


def morse(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="Dot-Dash-Dot")}
        return render(request, 'main/challenges/morse.html', context)

    elif request.method == "POST":
        data = request.body
        
    data = json.loads(data.decode('utf-8'))

    print(data)

    if data['flag'] == Challenges.objects.get(title="Dot-Dash-Dot").flag:
        # Logic for right Code
        if(request.user not in Challenges.objects.get(title="Dot-Dash-Dot").players_solved.all()):
            Challenges.objects.get(title="Dot-Dash-Dot").players_solved.add(Player.objects.get(username=request.user))
            point_system(request, Challenges.objects.get(title="Dot-Dash-Dot").points)
            return JsonResponse({"works": True})
        else:
                return JsonResponse({"already submitted": True})

    else:
        # Logic for Wrong Code
        return JsonResponse({"works": False})

def Vigil(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="Vigenere on Rail")}
        return render(request, 'main/challenges/vigil.html', context)

    elif request.method == "POST":
        data = request.body
    data = json.loads(data.decode('utf-8'))

    if data['flag'] == Challenges.objects.get(title="Vigenere on Rail").flag:
        # Logic for right Code
        if(request.user not in Challenges.objects.get(title="Vigenere on Rail").players_solved.all()):
            Challenges.objects.get(title="Vigenere on Rail").players_solved.add(Player.objects.get(username=request.user))        
            point_system(request, Challenges.objects.get(title="Vigenere on Rail").points)
            return JsonResponse({"works": True})
        else:
                return JsonResponse({"already submitted": True})

    else:
        # Logic for Wrong Code
        return JsonResponse({"works": False})

def baseball(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="BASEball Player")}
        return render(request, 'main/challenges/baseball.html', context)

    elif request.method == "POST":
        data = request.body
    data = json.loads(data.decode('utf-8'))

    if data['flag'] == Challenges.objects.get(title="BASEball Player").flag:
        # Logic for right Code
        if(request.user not in Challenges.objects.get(title="BASEball Player").players_solved.all()):
            Challenges.objects.get(title="BASEball Player").players_solved.add(Player.objects.get(username=request.user))
            point_system(request, Challenges.objects.get(title="BASEball Player").points)
            return JsonResponse({"works": True})
        else:
            return JsonResponse({"already submitted": True})

    else:
        # Logic for Wrong Code
        return JsonResponse({"works": False})

def robots(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="Baymax Rocks!")}
        return render(request, 'main/challenges/robots.html', context)

    elif request.method == "POST":
        data = request.body
    data = json.loads(data.decode('utf-8'))

    if data['flag'] == Challenges.objects.get(title="Baymax Rocks!").flag:
        # Logic for right Code
        if(request.user not in Challenges.objects.get(title="Baymax Rocks!").players_solved.all()):
            Challenges.objects.get(title="Baymax Rocks!").players_solved.add(Player.objects.get(username=request.user))
            point_system(request, Challenges.objects.get(title="Baymax Rocks!").points)
            return JsonResponse({"works": True})
        else:
            return JsonResponse({"already submitted": True})

    else:
        # Logic for Wrong Code
        return JsonResponse({"works": False})

def robotstxt(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="Baymax Rocks!")}
    return render(request, 'main/challenges/robotstxt.html', context)

def aperisolve(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="Aperisolve!")}
        
        return render(request, 'main/challenges/aperisolve.html', context)

    elif request.method == "POST":
        data = request.body
    data = json.loads(data.decode('utf-8'))

    if data['flag'] == Challenges.objects.get(title="Aperisolve!").flag:
        # Logic for right Code
        if(request.user not in Challenges.objects.get(title="Aperisolve!").players_solved.all()):
            Challenges.objects.get(title="Aperisolve!").players_solved.add(Player.objects.get(username=request.user))
            point_system(request, Challenges.objects.get(title="Aperisolve!").points)
            return JsonResponse({"works": True})
        else:
            return JsonResponse({"already submitted": True})

    else:
        # Logic for Wrong Code
        return JsonResponse({"works": False})

def killam(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        show_flag = True if request.headers['User-Agent'].lower() == "killam" else False
        flag = Challenges.objects.get(title="Killam").flag
        context = {"challenge": Challenges.objects.get(title="Killam"), "show_flag": show_flag, "flag": flag}
        return render(request, 'main/challenges/killam.html', context)

    elif request.method == "POST":
        data = request.body
        data = json.loads(data.decode('utf-8'))

        if data['flag'] == Challenges.objects.get(title="Killam").flag:
            # Logic for right Code
            if(request.user not in Challenges.objects.get(title="Killam").players_solved.all()):
                Challenges.objects.get(title="Killam").players_solved.add(Player.objects.get(username=request.user))
                point_system(request, Challenges.objects.get(title="Killam").points)
                return JsonResponse({"works": True})
            else:
                return JsonResponse({"already submitted": True})

        else:
            # Logic for Wrong Code
            return JsonResponse({"works": False})

def blankspace(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="Blank Space by Taylor Swift")}
        return render(request, 'main/challenges/blankspace.html', context)

    elif request.method == "POST":
        data = request.body
    data = json.loads(data.decode('utf-8'))

    if data['flag'] == Challenges.objects.get(title="Blank Space by Taylor Swift").flag:
        # Logic for right Code
        if(request.user not in Challenges.objects.get(title="Blank Space by Taylor Swift").players_solved.all()):
            Challenges.objects.get(title="Blank Space by Taylor Swift").players_solved.add(Player.objects.get(username=request.user))
            point_system(request, Challenges.objects.get(title="Blank Space by Taylor Swift").points)
            return JsonResponse({"works": True})
        else:
            return JsonResponse({"already submitted": True})

    else:
        # Logic for Wrong Code
        return JsonResponse({"works": False})

def POSTman(request):
    user = request.user
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        context = {"challenge": Challenges.objects.get(title="POSTman")}
    return render(request, 'main/challenges/POSTman.html', context)

def point_system(request, points):
    if request.method == "POST":
        score = int(get_user(request).score)
        points = int(points)
        print(score)
        Player.objects.filter(username=get_user(request)).update(
            score=score + points,
        )
        
        return HttpResponse('Success')



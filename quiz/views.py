
from django.shortcuts import redirect
from quiz.models import Quiz,Question,club
from django.shortcuts import render
from bs4 import BeautifulSoup
from django.shortcuts import render_to_response
import urllib.request


# Create your views here.

def start(request):

    context = {
        "quizzes": Quiz.objects.all(),
    }
    return render(request, "quiz/start.html", context)


def quiz(request, quiz_number):
    context = {

        "quiz": Quiz.objects.get(quiz_number=quiz_number),
        "quiz_number": quiz_number,
        "quizzes": Quiz.objects.all(),
    }

    return render(request, "quiz/quiz.html", context)


def question(request, quiz_number, question_number):
    quiz = Quiz.objects.get(quiz_number=quiz_number)
    questions = quiz.questions.all()
    question = questions[int(question_number) - 1]

    context = {
        "question_number": question_number,
        "question": question.question,
        "answer1": question.answer1,
        "answer2": question.answer2,
        "answer3": question.answer3,
        "quiz": quiz,
        "quiz_number": quiz_number,
        "quizzes": Quiz.objects.all(),

    }
    return render(request, "quiz/question.html", context)


def answer(request, quiz_number, question_number):
    saved_answers = request.session.get(quiz_number, {})
    answer = int(request.POST["answer"])
    saved_answers[question_number] = answer
    request.session[quiz_number] = saved_answers

    question_number = int(question_number)
    quiz = Quiz.objects.get(quiz_number=quiz_number)
    num_questions = quiz.questions.count()
    if num_questions <= question_number:
        return redirect("results_page", quiz_number)
    else:
        return redirect("question_page", quiz_number, question_number + 1)


def results(request, quiz_number):
    quiz = Quiz.objects.get(quiz_number=quiz_number)
    questions = quiz.questions.all()
    saved_answers = request.session.get(quiz_number, {})

    num_correct_answers = 0


    for question_number, answer in saved_answers.items():
        correct_answer = questions[int(question_number) - 1].correct

        if correct_answer == answer:
            num_correct_answers += 1

    context = {
        "quizzes": Quiz.objects.all(),
        "correct": num_correct_answers,
        "total": questions.count(),
        "quiz_number": quiz_number,
        "question_all":questions,


        'anz':answer




    }
    return render(request, "quiz/results.html", context)

def live(request):

    #c = club()
   # k1 = club.objects.all()
    #club.objects.delete()
    #score=[]
    club.objects.all().delete()
    url = 'http://www.espn.in/football/table/_/league/eng.1'
    #url='http://kwese.espn.com/football/table/_/league/esp.1'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)

   # yearmonth = soup.find('h2', attrs={'class': 'table-header'})
    #company = (soup.find('h2', class_='table-header')).text
   # for match in soup.select('tr.standings-row'):
    for match in soup.find_all('tr', class_="standings-row"):
       # competition = (match.find())
        #competition = (match.find('td', class_='match-competition'))
        #name=(match.find('span', attrs={'class': 'team-names'}))
        number = match.find ('span' , class_='number')
        name = match.find('span', class_='team-names')
        #date = (match.find('td',class_= 'match-date'))
        playedz = (match.find_all('td'))
        played = playedz[1]
        won = playedz[2]

        draw = playedz[3]
        lost = playedz[4]
        goal_diff = playedz[7]
        point = playedz[8]

       # yearmonth = (match.select('h2', class_='table-header'))
        #c.objects.all().delete()
 #       c = club(rank_team="h", team_name="g", game_played="f", won_game="e", draw_game="d", lost_game="c",
  #           goal_difference="b", points_game="a")
#        c.save()
        #c.delete()

#        score.append([name.text,played.text,won.text,lost.text,goal_diff.text, point.text])

        c = club(rank_team=number.text,team_name=name.text,game_played=played.text,won_game=won.text,draw_game=draw.text,lost_game=lost.text,goal_difference=goal_diff.text, points_game=point.text)
        #c1 = club(score_final=scoreah.text)
        c.save()
        #Message = club.objects.filter(team_name='Liverpool').count()
        #print(Message)



        #c=club(away_team=teama.text)
      #  c = club(team_name=name.text, game_played=played.text)
        #c.save()




        #c1.save()
        #c2.save()
      #  print(teamh.text, scoreah.text, teama.text)
        #print(score)
    league = soup.find("header", attrs = {"class": "automated-header"}).text
    #print (c.team_name)


    #l = club.objects.values()
    k=club.objects.all()


   # print (k)
    context = {
        'lists': k,
        'competition' : league

       # 'scory':score,


    }
    return render_to_response("quiz/master.html", context)




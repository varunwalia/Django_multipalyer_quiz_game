from django.conf import settings
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.db.models import Q
from questions.models import UserAnswer, Question
from questions.forms import User_Form
from questions.models import Question



User = get_user_model()




@login_required(login_url='/log_in/')
def homeView(request):
    return render(request, "home.html", {})



# @login_required(login_url='/log_in/')
# def main(request):
#     return render(request, "front.html",{})

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('game:homeView'))
        else:
            print(form.errors)
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/log_in/')
def log_out(request):
    logout(request)
    return redirect(reverse('game:log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('game:log_in'))
        else:
            print(form.errors)
    return render(request, 'signup.html', {'form': form})




def get_match_score(request):
    a = User.objects.get(username='varun')  ## dummy
    curr_user = request.user.username
    b = User.objects.get(username=curr_user)  
    s = score(a,b)
    print(s)
    return render(request, 'score_detail.html', {'score':s})



def score(user_a, user_b):
    q1 = Q(useranswer__user=user_a)
    q2 = Q(useranswer__user=user_b)
    question_set1 = Question.objects.filter(q1)
    question_set2 = Question.objects.filter(q2)
    score = 0
    if question_set1.count() == 0:
        return 0
    if question_set2.count() == 0:
        return  0
    question_set = (question_set1 | question_set2).distinct()
    for question in question_set:
        try:
            a = UserAnswer.objects.get(user=user_a, question=question)
        except:
            a = None
        try:
            b = UserAnswer.objects.get(user=user_b, question=question)
        except:
            b = None
        if a and b:
            if a.my_answer == b.my_answer:
                score+=1

    return score



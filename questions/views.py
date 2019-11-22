# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


from .forms import User_Form
from .models import Question, Answer, UserAnswer



def one_question(request, id):
	if request.user.is_authenticated():

		queryset = Question.objects.all().order_by('-timestamp')
		instance = get_object_or_404(Question, id=id)
		
		try:
			user_answer = UserAnswer.objects.get(user=request.user, question=instance)
			updated_q = True
		except UserAnswer.DoesNotExist:
			user_answer = UserAnswer()
			updated_q = False
		except UserAnswer.MultipleObjectsReturned:
			user_answer = UserAnswer.objects.filter(user=request.user, question=instance)[0]
			updated_q = True
		except:
			user_answer = UserAnswer()
			updated_q = False

		form = User_Form(request.POST or None)
		if form.is_valid():
			question_id = form.cleaned_data.get('question_id') 
			answer_id = form.cleaned_data.get('answer_id')
		
			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)
			user_answer.user = request.user
			user_answer.question = question_instance
			user_answer.my_answer = answer_instance
			user_answer.save()

			next_q = Question.objects.get_unanswered(request.user).order_by("?")
			if next_q.count() > 0:
				next_q_instance = next_q.first()
				return redirect("questions:question_single", id=next_q_instance.id)
			else:
				return redirect("questions:question_home")

		context = {
			"form": form,
			"instance": instance,
			"user_answer": user_answer,
		}
		return render(request, "questions/single.html", context)
	else:
		raise Http404



def home(request):
	if request.user.is_authenticated():
		form = User_Form(request.POST or None)
		if form.is_valid():
			question_id = form.cleaned_data.get('question_id') 
			answer_id = form.cleaned_data.get('answer_id')
			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)

		queryset = Question.objects.all().order_by('-timestamp')
		instance = queryset[1]
		context = {
			"form": form,
			"instance": instance,

		}
		return render(request, "questions/question_home.html", context)
	else:
		raise Http404
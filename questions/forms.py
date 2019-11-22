from django import forms

from .models import Answer, Question

class User_Form(forms.Form):
	question_id = forms.IntegerField()
	answer_id = forms.IntegerField()

	def clean_question_id(self):
		question_id = self.cleaned_data.get('question_id')
		try:
			obj = Question.objects.get(id=question_id)
		except:
			raise forms.ValidationError('There was an error with the question. Please try again.')
		return question_id	


	def clean_answer_id(self):
		answer_id = self.cleaned_data.get('answer_id')
		try:
			obj = Answer.objects.get(id=answer_id)
		except:
			raise forms.ValidationError('There was an error with the answer. Please try again.')
		return answer_id


from django import forms
from django.forms import ModelForm
from .models import   Question
from django.core.exceptions import ValidationError 
from django.utils.translation import ugettext_lazy as _


class QuestionForms(ModelForm):

    suject_name = forms.CharField(max_length=50, label="Subject Name", widget=forms.TextInput(
        attrs={'class': ' suject_name_box'}))

    quiz_name = forms.CharField(max_length=50, label="quiz_name", widget=forms.TextInput(
        attrs={'class': ' suject_name_box'}))

    detail = forms.CharField(max_length=50, label="detail", widget=forms.TextInput(
        attrs={'class': ' suject_name_box'}))


    question_text = forms.CharField(max_length=300, label="Question Text", widget=forms.TextInput(
        attrs={'class': 'question_text_box'}))

    answer_text = forms.CharField(
        max_length=300, label="answer text", widget=forms.TextInput(attrs={'class': ' answer_text'}))
    answer_text_correctness = forms.BooleanField(
        label="Choice 1 Correct?", required=False, widget=forms.CheckboxInput(attrs={'class': '  answer_text_correct_box'}))
  
    question_multiple = forms.CharField(max_length=300, label="Question Text", widget=forms.TextInput(
        attrs={'class': 'question_multiple_box'}))

    choice1_text = forms.CharField(
        max_length=300, label="Choice 1", widget=forms.TextInput(attrs={'class': ' answer_text'}))
    choice1_correctness = forms.BooleanField(
        label="Choice 1 Correct?", required=False, widget=forms.CheckboxInput(attrs={'class': 'choice_correct_box'}))

    choice2_text = forms.CharField(
        max_length=300, label="Choice 2", widget=forms.TextInput(attrs={'class': ' answer_text'}))
    choice2_correctness = forms.BooleanField(
        label="Choice 2 Correct?", required=False, widget=forms.CheckboxInput(attrs={'class': 'choice_correct_box'}))

    choice3_text = forms.CharField(
        max_length=300, label="Choice 3", widget=forms.TextInput(attrs={'class': ' answer_text'}))
    choice3_correctness = forms.BooleanField(
        label="Choice 3 Correct?", required=False, widget=forms.CheckboxInput(attrs={'class': 'choice_correct_box'}))

    choice4_text = forms.CharField(
        max_length=300, label="Choice 4", widget=forms.TextInput(attrs={'class': 'answer_text'}))
    choice4_correctness = forms.BooleanField(
        label="Choice 4 Correct?", required=False, widget=forms.CheckboxInput(attrs={'class': 'choice_correct_box'}))

    score = forms.CharField(
        max_length=300, label="Score", widget=forms.TextInput(attrs={'class': 'score'}))

    def clean(self):
        subject = self.cleaned_data["subject_name"]
        quiz = self.cleaned_data["quiz_name"]
        detail = self.cleaned_data["detail"]
        answer_texts = self.cleaned_data["answer_text_correctness"]
        choice1_answer = self.cleaned_data["choice1_correctness"]
        choice2_answer = self.cleaned_data["choice2_correctness"]
        choice3_answer = self.cleaned_data["choice3_correctness"]
        choice4_answer = self.cleaned_data["choice4_correctness"]
        score_quiz = self.cleaned_data["score"]

        answer_list = [subject,quiz,detail,answer_texts, choice1_answer, choice2_answer, choice3_answer, choice4_answer,score_quiz ]

        print(answer_list)

        trueCount = 0
        for answer in answer_list:
            if answer == True:
                trueCount += 1

        if trueCount != 1:
            raise ValidationError(_('Must have exactly one correct answer'))

        return self.cleaned_data


    


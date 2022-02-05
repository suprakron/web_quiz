from django.db import models
 
 
class Quiz(models.Model):
    subject = models.CharField(max_length=100)
    quiz_title = models.TextField(max_length=100)
    detail = models.TextField(max_length=100)

    def __str__(self):
        return self.subject

class Question(models.Model):
    quiz_title = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    quiz_text = models.TextField(max_length=100)
    quizanswer_text = models.TextField(max_length=100)
    quiz_multiple = models.TextField(max_length=100)
    options_one = models.CharField(max_length=100)
    options_two = models.CharField(max_length=100)
    options_three = models.CharField(max_length=100)
    options_four = models.CharField(max_length=100)
    score_quiz = models.TextField(max_length=100)

    def __str__(self):
        return self.quiz_text
    



 
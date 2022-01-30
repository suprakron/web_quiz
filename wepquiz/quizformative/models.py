from django.db import models
from enum import Enum
import json

# Create your models here.

class QuestionType(Enum):
    TEXT = '0'
    CHOICE = '1'

class BadJSON(Exception): pass

class Question:
    def __init__(self, question, answer, q_type, choices=[]):
        self.question = question
        self.answer = answer
        self.q_type = q_type
        self.choices = choices

    def __str__(self):
        outline = '<Question Object>\n'
        outline += f' - question: {self.question}\n'
        outline += f' - answer: {self.answer}\n'
        outline += f' - q_type: {self.q_type}\n'
        outline += f' - choices: {self.choices}\n'
        return outline
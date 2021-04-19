from django.urls import path
from .views import Quiz, RandomQuestion, Question, CreateAnswers

app_name='quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random-question/', RandomQuestion.as_view(), name='random' ),
    path('question/', Question.as_view(), name='question' ),
    path('answer/', CreateAnswers.as_view(), name='answer' )
]
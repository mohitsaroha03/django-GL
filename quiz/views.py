from rest_framework import generics
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer, QuestionSerializer, QuestionSerializerPost, AnswersSerializerPost
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class Quiz(generics.ListAPIView):

    serializer_class = RandomQuestionSerializer
    queryset = Question.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter().order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class Question(APIView):

    def post(self, request, format=None):
        serializer = QuestionSerializerPost(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({'id': obj.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateAnswers(APIView):

    def post(self, request, format=None):
        serialized = AnswersSerializerPost(data=request.data, many=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)

        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import serializers
from .models import Question, Answer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
    
        model = Question
        fields = [
            'id', 'title','answer',
        ]

class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
    
        model = Question
        fields = '__all__'
class QuestionSerializerPost(serializers.ModelSerializer):

    class Meta:
    
        model = Question
        fields = [
            'title',
        ]

class AnswersSerializerPost(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = '__all__'
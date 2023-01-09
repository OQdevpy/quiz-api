from rest_framework import serializers
from ...models import DayAnswerQuestions, Options, Questions,Answer, Quiz
from rest_framework import response,status

class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = ('id', 'option_a','option_b','option_c','option_d')


class QuestionsSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField(read_only=True, required=False)

    def get_options(self, obj):
        # tags = obj.tags.all()
        # print(obj)
        options=Options.objects.get(question__title=obj.title)
        # print(options)
        data = []
        for i in options:
            data.append([i.option_a,i.option_b,i.option_c,i.option_d])
        return data
    class Meta:
        model=Questions
        fields=('id','title','subject','created_at','options')






    
# class QuestionViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Options
        
class QuizSerializer(serializers.ModelSerializer):
    # children = serializers.SerializerMethodField(read_only=True)

    # def get_children(self, obj):
    #     try:
    #         comments = Questions.objects.all()
    #     except:
    #         return []
    #     else:
    #         serializer = DayAnswerQuestionsSerializer(comments, many=True)
    #         return serializer.data

    class Meta:
        model=Answer
        fields="__all__"

class AnswerQuestionsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Quiz
        fields="__all__"


class QuizListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Quiz
        fields="__all__"





        
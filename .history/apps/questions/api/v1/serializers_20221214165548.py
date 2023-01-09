from rest_framework import serializers
from ...models import Questions,Answer

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Answer
        fields="__all__"

        def create(self, validated_data):
            validated_data['user'] = self.context['request'].user
            return super(QuestionSerializer, self).create(validated_data)

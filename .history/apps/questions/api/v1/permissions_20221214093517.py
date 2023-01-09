from rest_framework import serializers
from ...models import Questions,Options
class Questions(serializers.ModelSerializer):

    class Meta:
        model=Options
        fields="__all__"
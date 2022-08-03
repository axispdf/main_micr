from rest_framework import serializers
from polls.models import Urls



class ViewDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'
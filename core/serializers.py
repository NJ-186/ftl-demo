from rest_framework import serializers

from .models import USER, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class USERSerializer(serializers.ModelSerializer):

    activity_periods = ActivityPeriodSerializer(many = True)

    class Meta:
        model = USER
        fields = '__all__'
        

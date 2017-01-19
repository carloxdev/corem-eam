# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk',
            'url',
            'username',
            'first_name',
            'last_name',
            'full_name',
            'email',
            'is_active',

        )

    def get_full_name(self, obj):

        try:
            return obj.get_full_name()

        except:
            return 0

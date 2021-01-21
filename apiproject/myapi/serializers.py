from django.db.models import fields
from rest_framework import serializers
from .models import ContaCorrente

class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContaCorrente
        fields = '__all__'
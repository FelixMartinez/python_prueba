from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Persona
    fields = '__all__'

  def validate(self, data):
    if data['edad'] <= 0 or data['edad'] > 120:
        raise serializers.ValidationError("La edad debe ser un número positivo menor o igual a 120.")
    if data['altura'] <= 0:
        raise serializers.ValidationError("La altura debe ser un número positivo.")
    if data['peso'] <= 0:
        raise serializers.ValidationError("El peso debe ser un número positivo.")
    return data

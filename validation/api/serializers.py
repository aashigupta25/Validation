from rest_framework import serializers
from .models import Person

# Validator
def start_with_r(value):
    if value[0].lower() != 'R':
        raise serializers.ValidationError('Name should be start with R only.')


class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length= 100, validators = [start_with_r])
    last_name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

# field Level Validation
    def validate_age(self, value):
        if value >= 200:
            raise serializers.ValidationError('Namaste')
        return value

# Object level Validation
    def validate(self, data):
        fn = data.get('first_name')
        ln = data.get('last_name')
        if fn.lower()== 'rahul' and ln.lower()!= 'ravi':
            raise serializers.ValidationError('Surname should be ravi')
        return data
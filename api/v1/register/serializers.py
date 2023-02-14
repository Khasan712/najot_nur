from rest_framework import serializers
from api.v1.register.models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'first_name', 'phone_number')

    def validate(self, attrs):
        phone_len = len(attrs['phone_number'])
        if phone_len > 13 or phone_len < 9:
            raise serializers.ValidationError('Phone number not valid')
        return attrs

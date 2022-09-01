from rest_framework import serializers
from UserApp.models import User

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['id','name','email','password','phone']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validate_data):
        password = validate_data.pop('password',None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

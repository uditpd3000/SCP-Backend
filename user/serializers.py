from rest_framework import fields, serializers

from .models import User

class userserializer(serializers.ModelSerializer) :
    class Meta:
        model=User
        fields=('name',
                'username',
                'roll_number',
                'batch',
                'program',
                'department',
                'github',
                'linkedin',
                'mastercv',
                'resume1',
                'resume2')

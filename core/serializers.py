'''
Responsible for converting the model into data types understandable by javascript and the react framework.
'''

from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id', 'title', 'content')

    # or can be used this
    # fields = ('id', 'title', 'content')
    



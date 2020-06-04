from tasks.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id',
                  'url',
                  'title',
                  'description',
                  'created_at',
                  'deadline_at',
                  'is_completed',
                  'completed_at',
                  ]
        extra_kwargs = {
            'description':
                {
                    'required': False,
                    'allow_blank': True,
                }
        }

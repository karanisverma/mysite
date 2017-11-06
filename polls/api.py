from tastypie.resources import ModelResource
from polls.models import Question


class EntryResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
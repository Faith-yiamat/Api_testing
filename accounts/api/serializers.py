from rest_framework import serializers
from milestone.models import Milestone
from child.models import Child
from parent.models import Parent


from assessment_questions.models import Assessment


class MilestoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = "__all__"

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = "__all__"        


class Assessment_questionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = "__all__"

from rest_framework.views import APIView
from child.models import Child
from .serializers import ChildSerializer
from rest_framework.response import Response
from parent.models  import Parent
from milestone.models import Milestone
from assessment_questions.models import Assessment
from .serializers import ParentSerializer
from .serializers import MilestoneSerializers
from .serializers import Assessment_questionsSerializer
from rest_framework import status

class ParentListView(APIView):
    
    def get(self, request, parent_id):
        try:
            parent = Parent.objects.get(id=parent_id)
            serializer = ParentSerializer(parent)
            return Response(serializer.data)
        except Parent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, parent_id):
        try:
            parent = Parent.objects.get(id=parent_id)
            serializer = ParentSerializer(parent, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Parent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SignIn(APIView):

    def post(self, request):
        return Response({"message": "Sign-in successful"}, status=status.HTTP_200_OK)

class SignUp(APIView):

    def post(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildrenList(APIView):

    def get(self, request, parent_id):
        try:
            parent = Parent.objects.get(id=parent_id)
            children = parent.children.all()
            serializer = ChildSerializer(children, many=True)
            return Response(serializer.data)
        except Parent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class MilestonesList(APIView):

    def get(self, request, parent_id):
        milestones_data = [] 
        return Response(milestones_data)



class ChildListView(APIView):
    def get(self, request):
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ChildSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def get(self,request, id):
        child = Child.objects.get(id = id)
        serializer = ChildSerializer(child)
        return Response(serializer.data) 
    def get(self, request):
        milestone = Child.objects.all()
        serializer = ChildSerializer(milestone, many=True)
        return Response(serializer.data)  




class MilestoneListView(APIView):
    def get(self, request, milestone_id):
        try:
            milestone = Milestone.objects.get(id=milestone_id)
            serializer = MilestoneSerializers(milestone)
            return Response(serializer.data)
        except Milestone.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Update an existing milestone.
    def put(self, request, milestone_id):
        try:
            milestone = Milestone.objects.get(id=milestone_id)
            serializer = MilestoneSerializers(milestone, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Milestone.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Delete a specific milestone.
    def delete(self, request, milestone_id):
        try:
            milestone = Milestone.objects.get(id=milestone_id)
            milestone.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Milestone.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Create a new milestone for a child.
class ChildMilestonesCreate(APIView):
    def post(self, request, child_id):
        try:
            child = Child.objects.get(id=child_id)
            serializer = MilestoneSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save(child=child)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Child.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Retrieve a list of all milestones for a child.
class ChildMilestonesList(APIView):
    def get(self, request, child_id):
        try:
            child = Child.objects.get(id=child_id)
            milestones = child.milestones.all()
            serializer = MilestoneSerializers(milestones, many=True)
            return Response(serializer.data)
        except Child.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# Retrieve a list of assessments for a specific milestone
class AssessmentList(APIView):
    def get(self, request, milestone_id):
        assessments = Assessment.objects.filter(milestone__id=milestone_id) 
        serializer = Assessment_questionsSerializer(assessments, many=True) 
        return Response(serializer.data) 



class Assessment_questionsList(APIView):
    
    def post(self, request):
        serializer = Assessment_questionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = Assessment_questionsSerializer(assessments, many=True)
        return Response(serializer.data)

class AssessmentDetail(APIView):

    def get_object(self, assessment_id):
        try:
            return Assessment.objects.get(id=assessment_id)
        except Assessment.DoesNotExist:
            return None

    def get(self, request, assessment_id):
        assessment = self.get_object(assessment_id)
        if assessment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = Assessment_questionsSerializer(assessment)
        return Response(serializer.data)

    def put(self, request, assessment_id):
        assessment = self.get_object(assessment_id)
        if assessment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = Assessment_questionsSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, assessment_id):
        assessment = self.get_object(assessment_id)
        if assessment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MilestoneAssessments(APIView):

    def get(self, request, milestone_id):
        assessments = Assessment.objects.filter(milestone_id=milestone_id) 
        serializer = Assessment_questionsSerializer(assessments, many=True)
        return Response(serializer.data)

class FilteredAssessments(APIView):

    def get(self, request, assessment_type):
        assessments = Assessment.objects.filter(assessment_type=assessment_type) 
        serializer = Assessment_questionsSerializer(assessments, many=True)
        return Response(serializer.data)





  
    

      


from django.urls import path
from .views import ParentListView
from .views import SignIn
from .views import SignUp
from .views import ChildrenList
# from .views import Milestone
from .views import ChildListView
from .views import MilestoneListView
from .views import ChildMilestonesCreate
from .views import ChildMilestonesList
from .views import AssessmentList
from .views import Assessment_questionsList
from .views import AssessmentDetail
from .views import MilestoneAssessments
from .views import FilteredAssessments

urlpatterns = [
    path('parents/', ParentListView.as_view(), name='parent_list'),
    path('api/parents/', ParentListView.as_view(), name='parent_list'),
    path('api/child/', ChildListView.as_view(), name='child-list'),
    path('signin/', SignIn.as_view(), name='signIn'),
    path('signup/', SignUp.as_view(), name='signUp'),
    path('children/', ChildrenList.as_view(), name='children_list'),
    # path('milestone/', Milestone.as_view(), name='milestone'),
    path('child//', ChildListView.as_view(), name='child_detail'),
    path('milestones/list/', MilestoneListView.as_view(), name='milestone_list'),
    path('child//milestones/create/', ChildMilestonesCreate.as_view(), name='child_milestones_create'),
    path('child//milestones/', ChildMilestonesList.as_view(), name='child_milestones_list'),
    path('assessments/', AssessmentList.as_view(), name='assessment_list'),
    path('assessments/questions/', Assessment_questionsList.as_view(), name='assessment_questions_list'),
    path('assessments//', AssessmentDetail.as_view(), name='assessment_detail'),
    path('milestone-assessments/', MilestoneAssessments.as_view(), name='milestone_assessments'),
    path('filtered-assessments/', FilteredAssessments.as_view(), name='filtered_assessments')
]


from django.urls import path, include

from .views import *

app_name = "jobs"

urlpatterns = [
    #path('home_initial', home_init, name='home-init'),
    #path('', HomeView.as_view(), name='home'),
    path('', home_init, name='home-init'),
    path('home_initial', HomeView.as_view(), name='home'),
    #path('',home_init, name='home-init'),
    path('search', SearchView.as_view(), name='searh'),
    path('employer/dashboard', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView, name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('jobs-delete/<int:id>', jobdeleteview, name='jobs-delete'),
    path('jobs-edit/<int:id>', editjobview, name='jobs-edit'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
]

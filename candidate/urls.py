from django.urls import path
from candidate import views
urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name='cand-home'),
    path('profile/add',views.CandidateProfView.as_view(),name='cand-addprof'),
    path('profile/detail',views.CandidateProfDetailView.as_view(),name='cand-profdetail'),
    path('profile/change',views.CandidateprofEditView.as_view(),name='cand-profedit'),
    path('jobs/list',views.CandidateJobListView.as_view(),name='cand-listjob'),
    path('jobs/details/<int:id>',views.CandidateJobDetailView.as_view(),name='cand-detailjob'),
    path("jobs/apply-now/<int:id>",views.apply_now,name="apply-now"),
    path("applications/all",views.ApplicationListView.as_view(),name="cand-application"),
    path("application/remove/<int:id>",views.cancellApplication,name="cand-cancellappli")
]
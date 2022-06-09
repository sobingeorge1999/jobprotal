from django.urls import path
from candidate import views
urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name='cand-home'),
    path('profile/add',views.CandidateProfView.as_view(),name='cand-addprof'),
    path('profile/detail',views.CandidateProfDetailView.as_view(),name='cand-profdetail'),
    path('profile/change',views.CandidateprofEditView.as_view(),name='cand-profedit')

]
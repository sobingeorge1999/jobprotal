from django.urls import path
from employer import views

urlpatterns=[
    path('home',views.EmployerHomeView.as_view(),name='emp'),
    path('jobs/add',views.AddJobView.as_view(),name='emp-addjob'),
    path('jobs/all',views.ListJobView.as_view(),name='list-alljob'),
    path('jobs/detail/<int:id>',views.JobDetailView.as_view(),name='detail-job'),
    path("jobs/change/<int:id>",views.JobEditView.as_view(),name='edit-job'),
    path("jobs/remove/<int:id>",views.JobDeleteView.as_view(),name='delete-job'),
    path("users/accounts/signup",views.SignUpView.as_view(),name="signup"),
    path("users/accounts/signin",views.SignInView.as_view(),name="signin"),
    path("users/accounts/signout",views.signout_view,name="signout"),
    path("users/accounts/changepassword",views.ChangepassView.as_view(),name="changepass"),
    path("users/accounts/passreset",views.PassresetView.as_view(),name="pass-reset"),
    path("profile/add",views.CompanyProfileView.as_view(),name="emp-addprofile"),
    path("profile/detail",views.EmpViewProfile.as_view(),name="emp-viewprofile"),
    path("profile/editprofile/<int:id>",views.EmpProfEnditView.as_view(),name="emp-editprofile")
]
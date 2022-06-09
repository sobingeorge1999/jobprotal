from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView,TemplateView
from employer.forms import JobForm
from employer.models import Jobs,CompanyProfile
from employer.forms import SignUpForm,LoginForm,CompanyProfileForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from employer.models import User


# Create your views here.

class EmployerHomeView(View):
    def get(self,request):
        return render(request,'emp_home.html')

class AddJobView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp_addjob.html"
    success_url = reverse_lazy("list-alljob")

    def form_valid(self, form):
        form.instance.company=self.request.user
        return super().form_valid(form)
    # def get(self,request):
    #     form=JobForm()
    #     return render(request,"emp_addjob.html",{"form":form})
    # def post(self,request):
    #     form=JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request,"emp_home.html")
    #     else:
    #         return render(request,"emp_addjob.html",{"form":form})

class ListJobView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-listjob.html"
    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user)
    # def get(self,request):
    #     qs=Jobs.objects.filter(company=request.user)
    #     return render(request,"emp-listjob.html",{"jobs":qs})

class JobDetailView(DetailView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-detailjob.html"
    pk_url_kwarg = "id"
    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     return render(request,"emp-detailjob.html",{"jobs":qs})

class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-editjob.html"
    success_url = reverse_lazy('list-alljob')
    pk_url_kwarg = "id"

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(instance=qs)
    #     return render(request,"emp-editjob.html",{"form":form})
    # def post(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     form=JobForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('list-alljob')
    #     else:
    #         return render(request,"emp-editjob.html",{"form":form})


class JobDeleteView(DeleteView):
    template_name = "jobconfirmdelete.html"
    model = Jobs
    success_url = reverse_lazy("list-alljob")
    pk_url_kwarg = 'id'

    # def get(self,request,id):
    #     qs=Jobs.objects.get(id=id)
    #     qs.delete()
    #     return redirect("list-alljob")


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("signin")

class SignInView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            usname=form.cleaned_data.get("username")
            psw=form.cleaned_data.get("password")
            user=authenticate(request,username=usname,password=psw)
        if user:
            login(request,user)
            if request.user.role=="employer":
                return redirect("emp")
            elif request.user.role=="candidate":
                return redirect("cand-home")

def signout_view(request, *args, **kwargs):
    logout(request)
    return redirect("signin")


class ChangepassView(TemplateView):
    template_name = "changepass.html"

    def post(self,request,*args, **kwargs):
        pwd=request.POST.get("pwd")
        usname=request.user
        user=authenticate(request,username=usname,password=pwd)
        if user:
            return redirect("pass-reset")
        else:
            return render(request,self.template_name)


class PassresetView(TemplateView):
    template_name = "passreset.html"

    def post(self,request,*args,**kwargs):
        pwd1=request.POST.get("pwd1")
        pwd2 = request.POST.get("pwd2")
        if pwd1!=pwd2:
            return render(request,self.template_name,{"msg":"does not match"})
        else:
            u=User.objects.get(username=request.user)
            u.set_password(pwd1)
            u.save()
            return redirect("signin")



class CompanyProfileView(CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "emp-addprofile.html"
    success_url = reverse_lazy('emp')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form=CompanyProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect("emp")
    #     else:
    #         return render(request,self.template_name,{"form":form})


class EmpViewProfile(TemplateView):
    template_name = 'emp-viewprofile.html'


class EmpProfEnditView(UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "emp-editprof.html"
    success_url = reverse_lazy("emp-viewprofile")
    pk_url_kwarg = "id"


#base for candidate,reg,login
from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import TemplateView,CreateView,FormView,ListView,DetailView
from candidate.forms import CandidateProForm,CandidateProfEditForm
from candidate.models import CandidateProfile
from django.urls import reverse_lazy
from employer.models import User,Jobs,Application
from django.contrib import messages

class CandidateHomeView(TemplateView):
    template_name = "can-home.html"


class CandidateProfView(CreateView):
    model = CandidateProfile
    form_class = CandidateProForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy('cand-home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CandidateProfDetailView(TemplateView):
    template_name = "cand-profiledetail.html"
#
#
class CandidateprofEditView(FormView):
    model=CandidateProfile
    template_name = 'cand-profedit.html'
    form_class = CandidateProfEditForm

    def get(self,request,*args,**kwargs):
        profile=CandidateProfile.objects.get(user=request.user)
        form=CandidateProfEditForm(instance=profile,initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'phone':request.user.phone,
            })
        return render(request,self.template_name,{"form":form})

    def post(self, request, *args, **kwargs):
        profile = CandidateProfile.objects.get(user=request.user)
        form=self.form_class(instance=profile,data=request.POST,files=request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data.pop("first_name")
            last_name =form.cleaned_data.pop("last_name")
            phone =form.cleaned_data.pop("phone")
            form.save()
            user=User.objects.get(id=request.user.id)
            user.first_name=first_name
            user.last_name =last_name
            user.phone = phone
            user.save()
            return redirect("cand-home")
        else:
            return render(request,self.template_name,{"form":form})


class  CandidateJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "joblist.html"

    def get_queryset(self):
        return self.model.objects.all().order_by('-created_date')

class CandidateJobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "canjobdetail.html"
    pk_url_kwarg = 'id'



def apply_now(request,*args,**kwargs):
    user=request.user
    job_id=kwargs.get("id")
    job=Jobs.oblects.get(id=job_id)
    Application.objects.create(applicant=user,
                            job=job)
    messages.success(request,"successfully added")
    return redirect("cand-home")
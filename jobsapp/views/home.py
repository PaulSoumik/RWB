from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import ApplyJobForm ,CreateJobForm
from ..models import Job, Applicant


# Global home page for all users irrespective of members or not
def home_init(request):
    return render(request,'jobsapp/home_initial.html')

class HomeView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.all()[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context


class SearchView(ListView):
    model = Job
    template_name = 'jobs/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['position'])


def JobListView(request):
    model = Job
    template_name = 'jobs/jobs.html'
    context_object_name = 'jobs'
    paginate_by = 5
    jobs = Job.objects.all()
    if request.method == 'POST':
        tag = request.POST.get('profession')
        location = request.POST.get('location')
        if tag:
            tag = str(tag)
            tag = list(tag.split(" "))
            print(tag)
            jobs = Job.objects.filter(tags__slug__in = tag)
            print(jobs)
            if location:
                print(location)
                location = str(location)
                print(location)
                jobs = jobs.filter(location = location)
        elif location:
            print(location)
            location = str(location)
            print(location)
            jobs = jobs.filter(location = location)


    context= {'jobs': jobs,
              
              }
    
    return render(request, 'jobs/jobs.html', context)


class JobDetailsView(DetailView):
    model = Job
    template_name = 'jobs/details.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ApplyJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('jobs:home'))

    def get_success_url(self):
        return reverse_lazy('jobs:jobs-detail', kwargs={'id': self.kwargs['job_id']})

    # def get_form_kwargs(self):
    #     kwargs = super(ApplyJobView, self).get_form_kwargs()
    #     print(kwargs)
    #     kwargs['job'] = 1
    #     return kwargs

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


def jobdeleteview(request, id=None):
    print("hello")
    job= get_object_or_404(Job, id=id)
    print(job.user.id)
    creator= job.user.id
    print("hello")
    userisactive = False

    if request.user.is_authenticated and request.user.id == creator:
        job.delete()
        print("hello")
        userisactive = True
        context = {'job': job,
        'userisactive' : userisactive,
        }
        
        return render(request, 'jobs/employer/delete.html',context)
    
    context= {'job': job,
              'creator': creator,
              'userisactive' : userisactive,
              }
    
    return render(request, 'jobs/employer/delete.html', context)



def editjobview(request, id=None):
    job= get_object_or_404(Job, id=id)
    updated = False
    update_attempt = False
    creator= job.user.id
    print(creator)
    print(request.user.id)
    if request.user.is_authenticated and request.user.id == creator:
        print("done")
        update_attempt = True
        form = CreateJobForm(request.POST, instance= job)
        obj = CreateJobForm(request.POST, instance= job)
        print(form.errors)
        if form.is_valid():
            print("done")
            job = form.save(commit= False)
            print("done")
           
            job.save()
            print("done")
            
            objects = Job.objects.get(title__exact = job.title)
            if obj.is_valid():
                taglist = obj.cleaned_data["tags"]
                for tag in taglist:
                    objects.tags.add(tag)
                    print(tag)
                print(objects.tags.all())
            objects.save()
            updated = True
            

    context= {'job': job,
              'updated': updated,
              'update_attempt': update_attempt,
              }
    return render(request, 'jobs/editjob.html', context)




'''
def jobsearchview(request):
'''
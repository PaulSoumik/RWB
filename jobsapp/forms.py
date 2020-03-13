from django import forms

from jobsapp.models import Job, Applicant


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at')

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        obj = super(CreateJobForm, self).clean()
        print(obj.get("tags"))
        if commit:
            job.save()
            objects = Job.objects.get(title__exact = job.title)
            taglist = obj.get("tags")
            for tag in taglist:
                objects.tags.add(tag)
                print(tag)
            print(objects.tags.all())
            objects.save()


        return job


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)

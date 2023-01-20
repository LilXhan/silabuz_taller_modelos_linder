from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Classroom, ClassroomProxy
from .forms import CreateClassroomForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def delete_classroom(request, id):
    classroom = Classroom.objects.get(pk=id)
    classroom.delete()

    return redirect('index')

class CreateClassroomView(LoginRequiredMixin, View):

    def get(self, request):

        form = CreateClassroomForm()

        context = {
            'form': form
        }
        
        return render(request, 'forms/classroom.html', context)

    def post(self, request):

        form = CreateClassroomForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data
            classroom = Classroom.objects.create(**form)
            classroom.save()

            return redirect('index')


class AdministrationClassroomView(LoginRequiredMixin, TemplateView):
    template_name = 'administracion/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classrooms'] = ClassroomProxy.objects.all()
        context['time'] = timezone.localtime
        return context
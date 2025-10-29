from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.http import HttpResponse
from django.urls import reverse_lazy


class GreetingView(View):
    greetingMessage = "Hello, welcome to our site!"
    def get(self, request):
        return HttpResponse(self.greetingMessage)
        

class StudentListView(ListView):
    model = Student
    # default has student_list.html template
    # default context_object_name has 'students_list'

class StudentDetailView(DetailView):
    model = Student
    # default has student_detail.html template
    # default context_object_name has 'student'

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName', 'lastName', 'testScore')
    # default has student_form.html template
    # default context_object_name has 'form'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('firstName', 'lastName', 'testScore')
    # default has student_form.html template
    # default context_object_name has 'form'

class StudentDeleteView(DeleteView):
    model = Student
    # default has student_confirm_delete.html template
    # default context_object_name has 'student'
    success_url = reverse_lazy('students')
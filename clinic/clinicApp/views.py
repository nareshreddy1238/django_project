from django.shortcuts import render, redirect
from clinicApp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicApp.forms import ClinicalDataForm

class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = {'first_name', 'last_name', 'age'}

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = {'first_name', 'last_name', 'age'}

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicApp/clinicaldata_form.html', {'form': form, 'patient': patient})    

def analyze(request, **kwargs):
    clinicaldata = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    response_data = []
    for data in clinicaldata:
        if data.component_name == 'hw':
            height_and_weight = data.component_value.split('/')
            if len(height_and_weight) > 1:
                height_in_meters = float(height_and_weight[0]) * 0.4536
                weight_in_kg = float(height_and_weight[1]) * 0.0254
                bmi = weight_in_kg / (height_in_meters * height_in_meters) # wight / height * height
                bmi_entry = ClinicalData()
                bmi_entry.component_name = 'bmi'
                bmi_entry.component_value = bmi
                response_data.append(bmi_entry)
        response_data.append(data)
    return render(request, 'clinicApp/generate_report.html', {'clinicaldata': response_data})



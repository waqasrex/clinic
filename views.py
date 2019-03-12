from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from hospital.models import visit, patient, doctor
from django.http import JsonResponse

def index(request):
    return render(request, 'hospital/index.html')

def DoctorRegistration(request):
    rec = doctor()
    if request.method == 'POST':
        rec.name = request.POST['name']
        rec.address = request.POST['address']
        rec.specialize = request.POST['specialize']
        rec.phone = request.POST['phone']
        rec.emp = request.POST['emp']
        rec.save()
        return redirect('hospital:doclist')
    return render(request, 'hospital/doctor/insert.html')

def PatientRegistration(request):
    rec = patient()
    if request.method == 'POST':
        rec.name = request.POST['name']
        rec.address = request.POST['address']
        rec.blood_group = request.POST['blood']
        rec.phone = request.POST['phone']
        rec.enroll = request.POST['enroll']
        rec.save()
        return redirect('hospital:patlist')
    return render(request, 'hospital/patient/insert.html')

def AppointmentRegistration(request):
    data = doctor.objects.all()
    return render(request, 'hospital/appointment/appointment.html', {'data':data})

def AppointmentPost(request):
        try:
            get_object_or_404(patient, id=request.POST['id'])
        except(Exception):
            patientrecord = patient()
            patientrecord.name = request.POST['name']
            patientrecord.address = request.POST['address']
            patientrecord.blood_group = request.POST['blood_group']
            patientrecord.phone = request.POST['phone']
            patientrecord.enroll = request.POST['enroll']
            patientrecord.save()
        finally:
            appointment = visit()
            appointment.enroll = request.POST['enroll']
            appointment.category = request.POST['category']
            appointment.time = request.POST['time']
            appointment.date = request.POST['date']
            appointment.emp = request.POST['emp']
            appointment.save()
            return redirect('hospital:appointlist')
        return render(request, 'hospital/appointment/appointment.html')

@csrf_exempt
def AppointmentAjax(request):
    data=patient.objects.get(phone=request.POST['mob'])
    resp={}
    resp['id'] = data.id
    resp['name'] = data.name
    resp['address']=data.address
    resp['phone'] = data.phone
    resp['blood_group'] = data.blood_group
    resp['enroll'] = data.enroll
    return JsonResponse(resp)

def DoctorList(request):
    rec = doctor.objects.all()
    return render(request, 'hospital/doctor/view.html', {'rec': rec})

def DoctorModal(request):
    data = doctor.objects.get(id=request.GET['modalid'])
    rec={}
    rec['id'] = data.id
    rec['name']=data.name
    rec['address']=data.address
    rec['phone'] = data.phone
    rec['specialize'] = data.specialize
    rec['emp'] = data.emp
    return JsonResponse(rec)

def DoctorEdit(request):
    data = doctor.objects.get(id=request.POST['docid'])
    if request.method == 'POST' :
     data.name = request.POST['name']
     data.address = request.POST['address']
     data.specialize = request.POST['specialize']
     data.phone = request.POST['phone']
     data.emp = request.POST['emp']
     data.save()
     return render(request, 'hospital/doctor/view.html')

def DoctorDelete(request):
    rec = doctor.objects.get(id=request.GET['deleteid'])
    rec.delete()
    return render(request, 'hospital/doctor/view.html')

def PatientList(request):
    rec = patient.objects.all()
    return render(request, 'hospital/patient/view.html', {'rec': rec})

def PatientModal(request):
    data = patient.objects.get(id=request.GET['modalid'])
    rec={}
    rec['id'] = data.id
    rec['name']=data.name
    rec['address']=data.address
    rec['phone'] = data.phone
    rec['blood_group'] = data.blood_group
    rec['enroll'] = data.enroll
    return JsonResponse(rec)

def PatientEdit(request):
    rec = patient.objects.get(id=request.POST['patid'])
    if request.method == 'POST' :
     rec.name = request.POST['name']
     rec.address = request.POST['address']
     rec.blood_group = request.POST['blood_group']
     rec.phone = request.POST['phone']
     rec.enroll = request.POST['enroll']
     rec.save()
     return render(request, 'hospital/patient/view.html')

def PatientDelete(request):
    rec = patient.objects.get(id=request.GET['deleteid'])
    rec.delete()
    return render(request, 'hospital/patient/view.html')

def AppointmentList(request):
    rec = visit.objects.all()
    return render(request, 'hospital/appointment/view.html', {'rec': rec})

def AppointmentModal(request):
    data = visit.objects.get(id=request.GET['modalid'])
    rec={}
    rec['id'] = data.id
    rec['enroll'] = data.enroll
    rec['emp']= data.emp
    rec['category']= data.category
    rec['time'] = data.time
    rec['date'] = data.date
    return JsonResponse(rec)

def AppointmentEdit(request):
    rec = visit.objects.get(id=request.POST['appid'])
    if request.method == 'POST' :
     rec.enroll = request.POST['enroll']
     rec.emp = request.POST['emp']
     rec.category = request.POST['category']
     rec.time = request.POST['time']
     rec.date = request.POST['date']
     rec.save()
     return render(request, 'hospital/appointment/view.html')

def AppointmentDelete(request):
    rec = visit.objects.get(id=request.GET['deleteid'])
    rec.delete()
    return render(request, 'hospital/appointment/view.html')
from django.urls import path
from . import views
app_name = 'hospital'
urlpatterns = [
    path('', views.index, name='index'),
    path('DoctorRegistration', views.DoctorRegistration, name='doctor'),
    path('PatientRegistration', views.PatientRegistration, name='patient'),
    path('AppointmentRegistration', views.AppointmentRegistration, name='appoint'),
    path('AppointmentPost', views.AppointmentPost, name='appointpost'),
    path('AppointmentAjax', views.AppointmentAjax, name='ajaxreq'),
    path('DoctorList', views.DoctorList, name='doclist'),
    path('DoctorModal', views.DoctorModal, name='docmodal'),
    path('DoctorEdit', views.DoctorEdit, name='docedit'),
    path('DoctorDelete', views.DoctorDelete, name='docdel'),
    path('PatientList', views.PatientList, name='patlist'),
    path('PatientModal', views.PatientModal, name='patmodal'),
    path('PatientEdit', views.PatientEdit, name='patedit'),
    path('PatientDelete', views.PatientDelete, name='patdel'),
    path('AppointmentList', views.AppointmentList, name='appointlist'),
    path('AppointmentModal', views.AppointmentModal, name='appointmodal'),
    path('AppointmentEdit', views.AppointmentEdit, name='appointedit'),
    path('AppointmentDelete', views.AppointmentDelete, name='appointdel')
]

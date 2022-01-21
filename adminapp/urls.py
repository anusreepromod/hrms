from django.urls.conf import path


from . import views

urlpatterns = [
    # path('registration/', views.registration, name="registration"),
    path('logins/', views.logins, name="logins"),
    path('employee/', views.employee),
    path('addstaff/', views.addstaff),
    path('editemployee/', views.editemployee),
    path('masters/', views.masters),
    path('manageleave/', views.manageleave),
    path('createleave/', views.createleave),
    path('attendance/', views.attendance),
    path('getattendance/', views.getattendance, name='getattendance'),
    path('resignation/', views.fnresignation),
    path('meetings/', views.meetings),
    path('addmeetings/', views.addmeetings),
    path('fnmeeting/', views.fnmeeting, name='fnmeeting'),
    path('getmeeting/', views.getmeeting, name="getmeeting"),
    path('updatemeet/', views.updatemeet, name="updatemeet"),
    path('delmeeting/', views.delmeeting, name='delmeeting'),
    path('notifications/', views.notifications),
    path('createnotifications/', views.createnotifications,
         name='createnotifications'),
    path('getnotification/', views.getnotification, name='getnotification'),
    path('promotion/', views.fnpromotion),
    path('complaints/', views.complaints),
    path('addcomplaints/', views.addcomplaints),
    path('fncomplain/', views.fncomplain, name='fncomplain'),
    path('getcomplain/', views.getcomplain, name='getcomplain'),
    path('updatecomplain/', views.updatecomplain, name='updatecomplain'),
    path('holidays/', views.holidays),
    path('fnholidays/', views.fnholidays, name='fnholiday'),
    path('dashboards/', views.dashboards),
    path('createresignation/', views.createresignation, name="createresignation"),
    path('fnresignations/', views.fnresignations),
    path('getresignation/', views.getresignation),
    path('updateresignation/', views.updateresignation, name="updateresignation"),
    path('delresignation/', views.delresignation, name='delresignation'),
    path('createpromotion/', views.createpromotion),
    path('fnpromotions/', views.fnpromotions),
    path('getpromotion/', views.getpromotion),
    path('updatepromotion/', views.updatepromotion, name="updatepromotion"),
    path('delpromotion/', views.delpromotion, name='delpromotion'),
    path('createleave/', views.createleave),
    path('designation/', views.designations, name="designation"),
    path('fndesignation/', views.fndesignation, name='fndesignation'),
    path('deldesignation/', views.deldesignation, name='deldesignation'),
    path('department/', views.departments, name="department"),
    path('fndepartment/', views.fndepartment, name='fndepartment'),
    path('deldepartment/', views.deldepartment, name='deldepartment'),
    path('leavetype/', views.fnleave, name="leavetype"),
    path('fnleavetype/', views.fnleavetype, name='fnleavetype'),
    path('delleavetype/', views.delleavetype, name='delleavetype'),
    path('fnmanageleave/', views.fnmanageleave, name='fnmanageleave'),
    path('getleave/', views.getleave, name='getleave'),
    path('setting/', views.setting, name='setting'),
    path('employees/', views.employees),
    path('employees/', views.fnemployee),
    path('editemployees/', views.fneditemployee),
    path('delemployee/', views.delemployee, name='delemployee'),
    path('getdata/', views.getdata),
    path('updatee/', views.fnupdate, name="updatee"),
    path('employeess/', views.employeess),
    path('fnemployeess/', views.fnemployeess),
    path('getdatas/', views.getdatas, name='getdata'),
    path('logout/', views.fnlogout, name='logout'),
    path('payroll/', views.fnpayroll, name='payroll'),
    path('getemployee/', views.getemployee, name='getemployee'),
    path('getlastname/', views.getlastname, name='lastname'),
    path('getsalary/', views.getsalary, name='getsalary'),
    path('calculate/', views.calculate, name='calculate'),
    path('allowance/', views.fnallowance, name='allowance'),
    path('getallowance/', views.getallowance, name='getallowance'),
    path('allowancedata/', views.allowancedata, name='allowancedata'),
    path('approveleave/', views.approveleave, name='approveleave'),
    path('rejectleave/', views.rejectleave, name='rejectleave'),
    path('approveresignation/', views.approveresignation,
         name='approveresignation'),
    path('rejectresignation/', views.rejectresignation, name='rejectresignation'),
    path('getpresent/', views.getpresent, name='getpresent'),
    path('searchemployee/', views.searchemployee, ),
    path('searchleave/', views.searchleave, ),
    #     path('loadchart/', views.loadchart, ),
]

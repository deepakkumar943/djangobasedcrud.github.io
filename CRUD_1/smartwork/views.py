from django.shortcuts import render,HttpResponseRedirect
from.forms import studentregister
from.models import user

def add_show(request):
 if request.method == 'POST':
  fm = studentregister(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['password']
   mo = fm.cleaned_data['mobile_no']
   reg = user(name=nm, email=em, password=pw,mobile_no=mo)
   reg.save()
   fm = studentregister
 else:
  fm = studentregister
 stud = user.objects.all()
 return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

def update_data(request, id):
 if request.method == 'POST':
  pi = user.objects.get(pk=id)
  fm = studentregister(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = user.objects.get(pk=id)
  fm = studentregister(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = user.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')

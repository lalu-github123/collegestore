from django.shortcuts import render,redirect
from .forms import SForm
from .models import Courses
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request,"home.html")
def Student(request):
    form = SForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        form = SForm(request.POST)
        if form.is_valid():
            form.save();
            messages.info(request,"Your Order Confirmed")
            return redirect('collegeapp:student')

    return render(request,"student.html",{'form':form})
# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id=department_id).all()
    return render(request, 'course_list.html', {'courses': courses })
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def Newpage(request):
    return render(request,"buttonpage.html")
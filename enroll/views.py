from django.shortcuts import render
from enroll.models import Employee
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request,'enroll/home.html')
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        number = request.POST.get('phone')

        new_emp = Employee(
            name = name,
            email = email,
            address = address,
            phone = number
        )
        new_emp.save()
        return HttpResponse("Added Successfully")

    return render(request,'enroll/add.html')
def show(request):
    emps = Employee.objects.all()
    content = {'emps':emps}

    return render(request,'enroll/show.html',content)

def update(request):
    if request.method == 'POST':

        pk = request.POST.get('id')

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('phone')

        user_update = Employee.objects.get(id = pk )



        if name:
            user_update.name = name
        if email:
            user_update.email = email
        if address:
            user_update.address = address
        if number:
            user_update.phone = number

        user_update.save()

        return HttpResponse("Employee record update Sucessfully")
    return render(request,'enroll/update.html')

def delete(request):
    if request.method == 'POST':
        pk = request.POST.get('employee_id')
        user_delete = Employee.objects.get(id = pk)
        user_delete.delete()

        return HttpResponse("Employee deleted Sucessfully.")
    return render(request,'enroll/delete.html')
from django.shortcuts import get_object_or_404, render
from employee.models import Employee
from django.http import HttpResponse

# Create your views here.
def employee_detail(request, pk):
    # try:
    #     employee = Employee.objects.get(pk = pk)
    # except:
    #     raise Http404

    # instead for this much above line of codes, we can just write: 
    employee = get_object_or_404(Employee, pk = pk)
    context = {
        'employee': employee,
    }
    return render(request, 'employee_details.html',context)

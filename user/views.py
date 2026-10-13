from django.shortcuts import render, redirect, get_object_or_404
from .models import employee  # Assumes your model is named 'employee' from earlier

# 1. Home View (List all employees)
def home_view(request):
    employees = employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

# 2. Add Employee View
def add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        
        # Create and save the new record
        employee.objects.create(name=name, email=email, age=age)
        return redirect('home')  # Redirects back to home page after saving
        
    return render(request, 'add.html')

# 3. Update Employee View
def update_view(request, pk):
    emp = get_object_or_404(employee, pk=pk)
    
    if request.method == 'POST':
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.age = request.POST.get('age')=
        emp.save()
        return redirect('home')
        
    return render(request, 'update.html', {'employee': emp})

# 4. Delete Employee View
def delete_view(request, pk):
    emp = get_object_or_404(employee, pk=pk)
    
    if request.method == 'POST':
        emp.delete()
        return redirect('home')
        
    return render(request, 'delete.html', {'employee': emp})

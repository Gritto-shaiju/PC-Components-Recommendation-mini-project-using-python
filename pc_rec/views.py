from django.shortcuts import render
from pc_rec import funtions
from pc_rec.pc_functions import Pc
from datetime import datetime
obj=Pc()

# Create your views here.

def home(request):
    return render(request, 'home.html')

def pc_value(request):
    if request.method == 'POST':
        preference = request.POST.get('preference')
        budget = request.POST.get('budget')
        cpu_cooler = request.POST.get('cpu_cooler')
        current_date = datetime.now()
        # Here you can add logic to process the input values and generate recommendations

        split = funtions.split_select(preference,cpu_cooler,float(budget))
        build = obj.build_pc(split)
        
        # recommendations = f"Recommendations based on {preference}, {budget},{cpu_cooler}"
        return render(request, 'result.html', {'build': build,'budget':budget,'preference':preference,'date':current_date.date(),'time':current_date.time().replace(microsecond=0)})
    return render(request, 'home.html')
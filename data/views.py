from django.shortcuts import render
from tablib import Dataset
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .resources import PersonResource
from django.db import connection 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def about(request):
	return render(request,'data/about.html')

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return[ dict(zip(columns,row)) for row in cursor.fetchall()]

def home(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MOD1')#data_person
    MOD1 = dictfetchall(cursor)
    '''paginator = Paginator(MOD1_list,5)
    page = request.GET.get('page')
    try:
        MOD1 = paginator.page(page)
    except PageNotAnInteger:
        MOD1 = paginator.page(1)
    except EmptyPage:
        MOD1 = paginator.page(1)
    except:
        MOD1 = paginator.page(paginator.num_pages)'''



    return render(request, 'data/home.html', {'BUS449':MOD1})

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES["myfile"]

        imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
          person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'data/simple_upload.html')

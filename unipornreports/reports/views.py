from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from .models import CSV
import pandas as pd
from .forms import CSVForm
import uuid
from ipware.ip import get_ip

def base_view(request):
    ip = get_ip(request)
    csvs = CSV.objects.filter(ip_address = ip)
    csvs.reverse()
    csvs = csvs[1:]
    for c in csvs:
        print (c.uploaded_csv1)
        print (c.uploaded_csv2)

    df=pd.read_csv('http://127.0.0.1:8000/app/static/media/' + str(c.uploaded_csv1))
    dfd=df.head()
    user=request.user  # can be anonymous user
    session=request.session.session_key
    ctx={'mydesc':dfd.to_html(), 'user': user, 'session' : session}
    return render(request, 'reports/graf.html', ctx)


def add_csv(request):
    user = request.user
    if request.method == 'POST':
        form = CSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv1 = form.cleaned_data['uploaded_csv1']
            csv2 = form.cleaned_data['uploaded_csv2']
            csv = CSV.objects.create(
                uuid = uuid.uuid4(),
                uploaded_csv1 = csv1,
                uploaded_csv2 = csv2,
                ip_address = get_ip(request)
            )
            csv.save()
            return HttpResponseRedirect(reverse('results'))
    else:
        form = CSVForm
    context = {'form' : form}
    template_name = 'reports/import.html'
    return render(request, template_name, context)

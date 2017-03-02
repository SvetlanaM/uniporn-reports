from django.shortcuts import render

def base_view(request):
    abc = 'Cauky mnauky tady my!'
    context = {'chces' : abc}
    template_name = 'index.html'
    return render(request, template_name, context)
# Create your views here.

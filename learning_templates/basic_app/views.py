from django.shortcuts import render

# Create your views here.
def index(request):
    content_dict = {'text':'Habari Chamgei Dunia','number':'55555'}
    return render(request, 'basic_app/index.html', content_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url.html')

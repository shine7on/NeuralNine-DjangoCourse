from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello")

def hello_html_view(request):
    return render(request, 'todos/hello.html')

# get name from url and print them
def hello_path(request, name):
    return HttpResponse(f"Hello {name}")

# get info from request
def hello_query(request):
    # mysite.com/search?q=2qfeowavzwenoqgbgwe3
    return HttpResponse(f"Your query was {request.GET.get("q")}") # get: get info that located after ? in url


# how to redirect
# redirect(NAME_defined in urls)
def special_view(request):
    # do some stuff
    return redirect(hello_html_view)


# PUT: updating
# POST: creating
def post_example(request):
    if request.method == 'POST':
        # accepting point
        name = request.POST.get('name')
        age = request.POST.get('age')
        job = request.POST.get('job')
        return HttpResponse(f"You posted (created): {name}, {age}, {job}")
    else:
        HttpResponseNotAllowed('POST')


def submit_example(request):
    return render(request, 'todos/submit.html')

from django.urls import path
from . import views

# views.Funt_name

urlpatterns = [
    path("hello", views.hello_world, name="hello_world"),
    path("htmlrender", views.hello_html_view, name="hello_html_view"),
    path("special", views.special_view, name="special"),
    path("helloname/<str:name>", views.hello_path, name="hello_view"), # how to get name from url
    path("helloquery", views.hello_query, name = "hello_query"), # how to get data from query style
    path('postendpoint', views.post_example, name='post_example'), # how to create data by client
    path('submitendpoint', views.submit_django_form, name='submit_example'), # how to take input from client

    path('templating', views.template_view, name='templating'), # how to create data by client
]
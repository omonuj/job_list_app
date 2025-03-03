from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

import jobs

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description"
]
# Create your views here.

# def hello_world(request):
#     return HttpResponse("<h3>Hello World!</h3>")
class TempClass:
    x = 5
def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = True
    context = {"name":"Django", "first_list": list, "temp_object":temp, "age":10,
               "is_authenticated":is_authenticated}

    return render(request, "jobs/hello.html", context)

def job_list(request):
   # <ul>
   #      <li>Job 1</li>
   #      <li>Job 2</li>
   #      <li>Job 3</li>
   # </ul>
   # list_of_jobs = "<ul>"
   # for j in job_title:
   #     job_id = job_title.index(j,)
   #     detail_url = reverse('job_detail', args=(job_id,))
   #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
   # list_of_jobs += "</ul>"
   # return HttpResponse(list_of_jobs)
   context = {"job_title_list": job_title}
   return render(request, "jobs/job_titles.html", context)


def job_detail(request, id):
    print(type(id))
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context = {"job_title":job_title[id], "job_description":job_description[id]}
        return render(request, "jobs/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")



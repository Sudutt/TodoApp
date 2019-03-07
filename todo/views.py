from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Schedule
from django.views.decorators.csrf import csrf_exempt

def home(request):
    i = Schedule.objects.filter(completed=False).order_by("deadline")
    c = Schedule.objects.filter(completed=True).order_by("deadline")
    return render(request, "index.html", {'incomplete': i, 'complete':c})

def failure(request):
    i = Schedule.objects.filter(completed=False).order_by("deadline")
    c = Schedule.objects.filter(completed=True).order_by("deadline")
    return render(request, "index.html", {'incomplete': i, 'complete':c, 'foo':True})

@csrf_exempt
def mark_complete(request):
    i = request.POST.get("id", "")
    r = Schedule.objects.filter(id=i).get()
    r.completed=True
    r.save()
    return HttpResponseRedirect("/success")

@csrf_exempt
def mark_incomplete(request):
    print("hi")
    i = request.POST.get("id", "")
    r = Schedule.objects.filter(id=i).get()
    print(r.id)
    r.completed=False
    r.save()
    return HttpResponseRedirect("/success")

@csrf_exempt
def delete(request):
    i = request.POST.get("id", "")
    r = Schedule.objects.filter(id=i)
    r.delete()
    return HttpResponseRedirect("/success")

@csrf_exempt
def add(request):
    b = request.POST.get("brief", "")
    d = request.POST.get("date", "") + ' ' + request.POST.get("time", "")
    if len(b)==0:
        return HttpResponseRedirect("/failure")
    try:
        r = Schedule(task_brief=b, deadline=d)
        r.completed=False
        r.save()
        return HttpResponseRedirect("/success")
    except:
        return HttpResponseRedirect("/failure")
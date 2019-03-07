i = Schedule.objects.filter(completed=False).order_by("deadline")
    c = Schedule.objects.filter(completed=True).order_by("deadline")
    return render(request, "index.html", {'incomplete': i, 'complete':c})
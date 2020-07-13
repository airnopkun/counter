from django.shortcuts import render, redirect

increment = 1


def index(request):
    if 'views' in request.session:
        request.session['views'] += 1
    else:
        request.session['views'] = 1
    if 'count' in request.session:
        request.session['count'] += increment
    else:
        request.session['count'] = 1
    return render(request, "index.html")


def destroy(request):
    del request.session['count']
    del request.session['views']
    return redirect('/')


def increment_two(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    request.session['views'] -= increment
    return redirect('/')


def increment_new(request):
    global increment
    if request.POST['increment']:
        increment = int(request.POST['increment'])
    request.session['views'] -= 1
    request.session['count'] -= increment
    return redirect('/')

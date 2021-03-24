from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

def index (request):
    return redirect ('/shows')
    
def new (request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    errors = Show.objects.show_validator(request.POST)
        
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            description = request.POST['desc'],
            release_date = request.POST['date']
        )
        show_id = show.id
        return redirect(f'/shows/{show_id}')

def about(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'id': show.id,
        'title': show.title,
        'network': show.network,
        'date': show.release_date,
        'desc': show.description,
        'update_date': show.updated_at
    }
    return render(request, "about.html", context)

def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def edit(request, show_id):
    
    show = Show.objects.get(id=show_id)
    context = {
        'id': show.id,
        'title': show.title,
        'network': show.network,
        'date': show.release_date,
        'desc': show.description,
        'update_date': show.updated_at
    }
    return render(request, "edit.html", context)

def update(request, show_id):
    errors = Show.objects.show_validator(request.POST)
        
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.description = request.POST['desc']
        show.release_date = request.POST['date']
        show.save()
        return redirect(f'/shows/{show_id}')

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')


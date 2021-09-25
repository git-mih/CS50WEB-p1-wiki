from django.shortcuts import redirect, render
from django import forms
import markdown2
from random import choice

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def query(request, query):
    entries = [e.lower() for e in util.list_entries()]

    if query in entries:
        return render(request, "encyclopedia/query.html", {
            "content": markdown2.markdown(util.get_entry(query)),
            "query_title": query
        })
    return render(request, "encyclopedia/er404.html", {
        "error": f'{query} Not Found'
    })

def search(request): # wiki/cs
    q = request.GET.get('q') # <QueryDict: {'q': ['css']}>.get('q') -> css
    entries = [e.lower() for e in util.list_entries()]
    if q in entries:
        for e in entries:
            if len(q) == len(e):
                return render(request, "encyclopedia/query.html", {
                    "content": markdown2.markdown(util.get_entry(q)),
                    "query_title": q
                })
    return render(request, "encyclopedia/filter.html", {
        "list": [e for e in util.list_entries() if q in e.lower()]
    })

def edit(request):
    print(request.GET)
    q = request.GET.get('e')
    entry = util.get_entry(q)
    return render(request, "encyclopedia/edit.html", {
        "content": entry,
        "title": q
    })

def new_page(request):
    return render(request, "encyclopedia/new_page.html")

def save(request):
    title = request.GET.get('title')
    content = request.GET.get('file-content')
    if title.lower() not in [e.lower() for e in util.list_entries()]:
        util.save_entry(title, content)
        return redirect("../wiki/")
    return render(request, "encyclopedia/er-file.html", {
        "error": f'Try search for it'
    })
    
def save_changes(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    print(title)
    print(content)
    util.save_entry(title, content)
    return redirect("../wiki/")

def random_page(request):
    entries = [e.lower() for e in util.list_entries()]
    q = choice(entries)
    return render(request, "encyclopedia/random.html", {
        "content": markdown2.markdown(util.get_entry(q)),
        "title": q
    })







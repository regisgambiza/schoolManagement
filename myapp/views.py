from django.shortcuts import render, get_object_or_404
from myapp.models import Learner
from .forms import MyForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    # Get a list of all learners from the database
    learners = Learner.objects.order_by('first_name')
    # Create a context

    return render(request, 'myapp/index.html', {'learners': learners})


def detail(request, slug=None):
    learner = get_object_or_404(Learner, slug=slug)
    return render(request, 'myapp/detail.html', {'learner': learner})


def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/edit.html', {'form': form})

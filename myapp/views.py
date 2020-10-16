from django.shortcuts import render, get_object_or_404, get_list_or_404
from myapp.models import Learner, Pace
from .forms import MyForm, Issue_pace_form
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    # Get a list of all learners from the database
    learners = Learner.objects.order_by('first_name')
    # Create a context

    return render(request, 'myapp/index.html', {'learners': learners})


def detail(request, slug=None):
    learner = get_object_or_404(Learner, slug=slug)

    # try:
    # paces = get_list_or_404(Pace, id=learner.id)
    # except:
    # return render(request, 'myapp/detail.html', {'learner': learner})
    # print(paces)

    paces = Pace.objects.filter(learner=learner.id)

    context = {'learner': learner, 'paces': paces}
    return render(request, 'myapp/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/edit.html', {'form': form})


def issue_pace(request):
    if request.method == 'POST':
        form = Issue_pace_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Issue_pace_form()
    return render(request, 'myapp/issue_pace.html', {'form': form})


def edit(request, pk=None):
    learner = get_object_or_404(Learner, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=learner)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=learner)

    return render(request, 'myapp/edit.html', {'form': form})


def delete(request, pk=None):
    learner = get_object_or_404(Learner, pk=pk)
    learner.delete()

    return HttpResponseRedirect('/')


def search(request):
    q = request.GET.get('q', None)
    learners = ''
    if q is None or q is "":
        learners = Learner.objects.all()
    elif q is not None:
        learners = Learner.objects.filter(first_name__icontains=q)

    return render(request, 'myapp/index.html', {'learners': learners})

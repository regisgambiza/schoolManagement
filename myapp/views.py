from django.shortcuts import render
from myapp.models import Learner


# Create your views here.
def index(request):
    # Get a list of all learners from the database
    learners = Learner.objects.order_by('first_name')
    # Create a context

    return render(request, 'myapp/index.html', {'learners': learners})

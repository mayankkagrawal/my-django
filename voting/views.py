from django.http import HttpResponse
from .models import Question

def index(request):
    question_list = Question.objects.all()
    output = '-----'.join([s.question_text for s in question_list])
    return HttpResponse(output)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

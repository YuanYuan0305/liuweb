from django.shortcuts import render,get_object_or_404
import time
from django import template
from django.http import HttpResponse
from .models import Question,Choice,tk_ctj,tk_xzt
from django.template import loader
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def hello(request):
    return HttpResponse("Say Hello. You're at the polls hello function.")

def ctime(request):
    now = time.strftime("%H:%M:%S")
    date = time.strftime("%d/%m/%Y")
    rep = "reflush page   test  The time :|"+now+" The Date:"+date
    return HttpResponse(rep)

def num(request):
    number = request.GET.get('a')
    try:
        number = int(number)
        number = str(number)
    except ValueError:
        raise Http404
    msg = "The input number is:"+number
    return HttpResponse(msg)

def show(req,num,aaa):
    num = int(num)
    num = str(num)
    msg = "what your input is :"+num+aaa
    return HttpResponse(msg)

def use_template(req,aaa):  
    f = open('D:/liuweb/djweb/templates/template1.html','r',encoding="utf-8")
    t = template.Template(f.read())
    f.close()
    con = template.Context({'message':aaa,'message1':aaa})
    html = t.render(con)
    return HttpResponse(html)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    
def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def Xzt(request):
    next_th=9999
    last_th=0
    print("__________________________*")
    th=request.GET.get('th')
    print("req is %s"%th)
    int_th=int(th)
    print("th is %d"%int_th)
    question = tk_xzt.objects.filter(id__gte=int_th)[:1]
    print("question is %d"%question[0].th)
    if (int_th<0 or int_th>9999):
        int_th=1
        next_th=2
        last_th=1
    else :
        if (question[0].th>int_th):
            next_th=str(question[0].th+1)
            last_th=str(int_th-1)
        else:
            next_th=str(int_th+1)
            last_th=str(question[0].th-1)

    question[0].tdan.strip().replace('\n','').replace('/t','')
    print("next last th is %s  %s %s"%(next_th,last_th,question[0].tdan))

    if (question[0].tlx[0]=='M'):
        template = loader.get_template('polls/checkt.html')
    else :
        template = loader.get_template('polls/radiot.html')

    context = {
        'question': question[0],
        'nextth':str(next_th),
        'lastth':str(last_th),
    }
    return HttpResponse(template.render(context, request))

def Xzt_index(request):
    template = loader.get_template('polls/xzt_index.html')
    context = {
        'question': 1,
        'nextth':2,
        'lastth':0,
    }
    return HttpResponse(template.render(context, request))

def Test(request):
    return render(request, 'polls/login.html')

def Test1(request):
   print(request.method)
   req=request.GET
   return HttpResponse(req['lastname'])

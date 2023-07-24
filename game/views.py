# views.py
from django.shortcuts import render, redirect
from .models import  Questions,Result
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Sum

def home(request):
    choices = Questions.CAT_CHOICES
    results = Result.objects.all()
    context = {
        'choices':choices,
        'results':results,
    }

    return render(request,'home.html',context)

@login_required(login_url = 'login')
def questions(request,choice):
    question = Questions.objects.filter(category__exact = choice)

    context = {
        'choice':choice,
        'question':question,
    }
    return render(request,'question.html',context)

@login_required(login_url = 'login')
def result(request):

    if request.method == 'POST':
        data = request.POST
        dict_data = dict(data)

        question_id = []
        question_ans = []
        answer = []
        score = 0


        for key in dict_data:
            try:
                question_id.append(int(key))
                question_ans.append(dict_data[key][0])
            except:
                print('Csrf')

        for question in question_id:
            answer.append((Questions.objects.get(id=question)).answer)

        total = len(answer)

        if total != 0:
            for i in range(total):
                if answer[i] == question_ans[i]:
                    score += 1

            average = (score/total)* 100
        else:
            average = 0

        

        try:
            #save the result in the database
            for i in range(total):

                result_instance = Result.objects.create(
                    user = request.user,
                    question_id=question_id[i],
                    question_ans=question_ans[i],
                    answer=answer[i],
                    score=score,
                )
        except ZeroDivisionError:
            print("Wrong Move")


    context = {
        'score':score,
        'average':average,
        'total':total,
    }


    return render(request, 'result.html',context)


@login_required(login_url = 'login')
def overall_result(request,pk):
    results = Result.objects.filter(user=pk)

    # Initialize variables to count scores and total results
    total_score = 0
    total_results = 0

    for result in results:
        if result.question_ans == result.answer:
            # Increment total score for correct answers
            total_score += result.question_ans == result.answer
            
            print('Correct')
            
        # Increment the total number of results
        total_results += 1
    
    a = total_score 
    
    average_score = a
    total = total_results

    efficiency = (average_score/total) * 100

    context = {
        'results':results,
        'average_score':average_score,
        'total':total,
        'efficiency':efficiency,
    }
    return render(request,'overall_result.html',context)


def login_required(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,f"Your'e a Legend {username}")
                return redirect('home')
            else:
                messages.error(request,'Check your Username or Password')
        else:
            messages.error(request,'Check your Username or Password')
    form = AuthenticationForm()

    context = {
        'form':form,
    }

    return render(request,'credentials/login.html',context)


def signup_required(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email exist, Type Another One Homie')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username exists, Try Ben10_1234')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #log user in
                user_login = auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                return redirect('login')
        else:
            messages.info(request,'Password Incorrect')
            return redirect('signup')
        

    return render(request,'credentials/signup.html')


def log_out(request):
    logout(request)
    messages.success(request,'Thanks for the Sign-up! ')
    return redirect('home')
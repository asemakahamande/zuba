from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import QuizResult
from .forms import QuizForm
from .forms import QuizForm1

from django.template import loader

def home(request):
    return render(request, 'Home.html')

def semester(request):
    return render(request, 'Semester.html')
def semester1(request):
    return render(request, 'semester1.html')

def semester2(request):
    return render(request, 'semester2.html')
def contacts(request):
    return render(request, 'Contacts.html')
def admin(request):
    return render(request, 'Admin.html')
def login(request):
    return render(request, 'login.html')
def help(request):
    return render(request, 'Help.html')
question_prompts = [   
    "1. The outcome of a processed data in a computer is known as  \n (a) raw fact \n (b) information \n (c) database\n (d) computer result",
    "2. Which of the following computing devices did not exist in pre computing age to the 19th century\n (a) Napier's Bones \n (b) Abacus \n (c) ENIAC\n(d) Slide Rule",
    "3. The combination of different parts of the computer to help achieve a task best describes ....  \n (a) computer \n (b) computer system \n (c) hardware\n (d) Software",
    "4. In a computer, the sets of instructions that direct it in performing a particular task is called \n (a) information\n (b) program \n (c) data\n (d) Abacus",
    "5. What is the nationality of John Napier \n (a) England\n (b) Scotland \n (c) France\n (d) Germany", 
    "6. The LCM of 10 and 20 is \n(a) 10\n (b) 20 \n(c) 30 \n(d) 40.",
    "7. One-third of a substance is written as ______ \n(a) 1/4 \n(b)1/5 \n(c)1/3  \n(d)1/6.",
    "8. The square root of 16 is ____ \n(a)2 \n(b)3 \n(c)6 \n(d)4.",
	"9. the lowest form of this 12:15 is _______\n(a)3:4 \n(b)3:5 \n(c)4:5 \n(d)4:6",
    "10.Percentage and ratio are not used for comparison \n(a) true  \n(b) false \n(c) maybe \n(d) none of the above.",
    "11.What is the value of x, when x ÷ 3 = 14 \n(a)42 \n(b)43 \n(c)44 \n(d)45.",
    "12.The LCM of 3 and 4 is ___ \n(a) 12 \n(b) 11 \n(c) 10\n(d) 9. ",
    "13.The result of changing 12/25 to percentage is __ \n(a) 48 \n(b) 46 \n(c) 47 \n(d) 49.",
    "14.If k + 13 = 15, the missing number is ___ \n(a) 1 \n(b)2 \n(c)3 \n(d)4.",
    "15.One among the following is the H.C.F of 12 and 36 \n(a) 12 \n(b)13 \n(c)14 \n(d)15.",
    "16.The unknown in open sentence if also called ___ \n(a) missing number  \n(b) whole number \n(c) mixed number  \n(d) fraction.",
    "17.One among the following is not a multiple of 10 \n(a) 20 \n(b)29 \n(c)30 \n(d)40.",
    "18.If x + 8 = 34,the value of  x. \n(a) 26 \n(b)27 \n(c)28 \n(d)29.",
    "19.100k is equal to ______ \n(a)N1 \n(b)N2 \n(c)N3 \n(d)N4",
    "20.The medium of exchange of goods and services is called ___ \n(a)exchange rate  \n(b)Money  \n(c)coins \n(d)currency", 
]
correct_answers = ["b", "c", "b", "b", "b", "b", "c","d", "c", "a", "a", "a", "a", "c", "a", "a", "b", "a", "a", "b"]
questions = list(zip(question_prompts, correct_answers))
def semester1_2023(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            score = 0
            answers = []
            failed_questions = []

            for i in range(len(questions)):
                answer = form.cleaned_data.get(f'question_{i+1}')
                answers.append(answer)
                if answer and answer.lower() == correct_answers[i]:
                    score += 1
                else:
                    failed_questions.append({
                        'question': question_prompts[i],
                        'your_answer': answer,
                        'correct_answer': correct_answers[i]
                    })

            # Save the result in the database
            quiz_result = QuizResult(name=name, score=score, total_questions=len(questions))
            quiz_result.save()
            return render(request, 'result.html', {
                'score': score, 
                'total': len(questions),
                'failed_questions': failed_questions
            })
    else:
        form = QuizForm()

    return render(request, '2023.html', {'form': form})
    # return render(request, '2023.html')



# next view
question_prompts1 =[
    "1. computer parts are manufactured by   \n (a) sysem analyst  \n (b) Data Scientist  \n (c) Data Engineers\n (d) None of the above",
    "2. Which of the following computing devices did not exist in pre computing age to the 19th century\n (a) Napier's Bones \n (b) Abacus \n (c) ENIAC\n(d) Slide Rule",
    "3. The combination of different parts of the computer to help achieve a task best describes ....  \n (a) computer \n (b) computer system \n (c) hardware\n (d) Software",
    "4. In a computer, the sets of instructions that direct it in performing a particular task is called \n (a) information\n (b) program \n (c) data\n (d) Abacus",
    "5. What is the nationality of John Napier \n (a) England\n (b) Scotland \n (c) France\n (d) Germany", 
    "6. The LCM of 10 and 20 is \n(a) 10\n (b) 20 \n(c) 30 \n(d) 40.",

]
correct_answers1 = ["d", "a", "c", "b", "d", "c"]
# question = list(zip(question_prompts1, correct_answers1))
question1= list(zip(question_prompts1, correct_answers1))
def semester2_2023(request):
    if request.method == 'POST':
        form = QuizForm1(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            score = 0
            answers = []
            failed_questions = []

            for i in range(len(question1)):
                answer = form.cleaned_data.get(f'question_{i+1}')
                answers.append(answer)
                if answer and answer.lower() == correct_answers1[i]:
                    score += 1
                else:
                    failed_questions.append({
                        'question': question_prompts1[i],
                        'your_answer': answer,
                        'correct_answer': correct_answers1[i]
                    })
            # Save the result in the database
            quiz_result = QuizResult(name=name, score=score, total_questions=len(question1))
            quiz_result.save()
            return render(request, 'result.html', {
                'score': score, 
                'total': len(question1),
                'failed_questions': failed_questions
            })
    else:
        form = QuizForm1()

    return render(request, '2023s.html', {'form': form})
# return render(request, '2023s.html'
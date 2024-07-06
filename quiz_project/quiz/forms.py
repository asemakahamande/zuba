from django import forms


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
    "20.The medium of exchange of goods and services is called ___ \n(a)exchange rate \n(b)Money  \n(c)coins \n(d)currency",
    
]
correct_answers = ["b", "c", "b", "b", "b", "b", "c","d", "c", "a", "a", "a", "a", "c", "a", "a", "b", "a", "a", "b"]

questions = list(zip(question_prompts, correct_answers))
class QuizForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    # Dynamically add fields for the quiz questions
    def __init__(self, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        for i, (question, _) in enumerate(questions):
            self.fields[f'question_{i+1}'] = forms.ChoiceField(
                label=question,
                choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')],
                widget=forms.RadioSelect
            )


question_prompts1 =[
    "1. computer parts are manufactured by   \n (a) sysem analyst  \n (b) Data Scientist  \n (c) Data Engineers\n (d) None of the above",
    "2. Which of the following computing devices did not exist in pre computing age to the 19th century\n (a) Napier's Bones \n (b) Abacus \n (c) ENIAC\n(d) Slide Rule",
    "3. The combination of different parts of the computer to help achieve a task best describes ....  \n (a) computer \n (b) computer system \n (c) hardware\n (d) Software",
    "4. In a computer, the sets of instructions that direct it in performing a particular task is called \n (a) information\n (b) program \n (c) data\n (d) Abacus",
    "5. What is the nationality of John Napier \n (a) England\n (b) Scotland \n (c) France\n (d) Germany", 
    "6. The LCM of 10 and 20 is \n(a) 10\n (b) 20 \n(c) 30 \n(d) 40.",

]
correct_answers1 = ["d", "c", "b", "b", "b", "b"]

questions1 = list(zip(question_prompts1, correct_answers1))

class QuizForm1(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    # Dynamically add fields for the quiz questions
    def __init__(self, *args, **kwargs):
        super(QuizForm1, self).__init__(*args, **kwargs)
        for i, (question, _) in enumerate(questions1):
            self.fields[f'question_{i+1}'] = forms.ChoiceField(
                label=question,
                choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')],
                widget=forms.RadioSelect
            )
            
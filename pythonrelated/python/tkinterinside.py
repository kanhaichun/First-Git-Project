import tkinter as tk
import random
SF={
"______is the world's largest island country":"Indonesia",
"______has the world's highest rate of deforestation":"Indonesia", 
"______banned kissing inpublic in 2004":"Indonesia",
"The five most practiced religions in the world have their origins in ____":"Asia",
"Wild tigers only exist in ______":"Asia",
"_____is the only country in the world to draft women into Military service":"Israel",
"______ have a net gain of trees in the last 100 years":"Israel",
"______has the world's lowest meat consumption per person":"India",
"70% of all the world's species come from ______":"India",
"The world's most polluted city is in ______":"India",
"People in _____ read the most in the world":"India",
"The most radioactive and polluted lake in the world is in _______":"Russia",
"_____ has the most nuclear weapons in the world":"Russia",
"Rock Paper Scissors was invented in ______":"China",
"_____has the highest life expectancy in the world":"Japan"}
questions=list(SF.keys())
answers=list(SF.values())
def createa(numofque):
        allChoices=['Indonesia','Asia','Israel','India','Russia','China',"Japan"]
        choices=[0,1,2,3]
        #set correct answer
        if numofque<3:
            i=0
        elif 3<=numofque<5:
            i=1
        elif 5<=numofque<7:
            i=2
        elif 7<=numofque<11:
            i=3
        elif 11<=numofque<13:
            i=4
        elif numofque==13:
            i=5
        elif numofque==14:
            i=6
        num1=random.randrange(0,4)#the position to put the correct answer
        #print(num1,"position")
        choices[num1]=allChoices[i]#put the correct answer
        #print(choices,"right answer")
        numbers=[]
        for element in choices:
            #print(element,"start one by one")
            if element== 0 or element== 1 or element==2 or element==3:
                rand(numbers,i,choices,allChoices,element)
        return choices

    #choose answers that have not been selected before.If they have, choose again
def rand(numbers,i,choices,allChoices,element):
            num= random.randrange(0,7)# choose a wrong answer from all the possible answers
            #print(num,"pick one from answers")
            if num != i and num not in numbers:#if not repeated
                numbers.append(num)
                #print(numbers,"answers have been chosen")
                choices[element] = allChoices[num]#put the wrong answer
                #print(num,i,choices)
            else:#if repeated,run again
                rand(numbers,i,choices,allChoices,element)
def point():
    item=ord(var1.get())-64
    if createa(numofque)[item-1] == answers[numofque]:
        var1.set("You selected"+var1.get()+"right")
        label2.pack()
    else:
        var1.set("You selected"+var1.get()+"wrong")
        label2.pack()

top=tk.Tk()
top.title("quiz")
var1 = tk.StringVar()
var2 = tk.StringVar()
label1 = tk.Label(top,textvariable=var2,relief="raised" )
label2 = tk.Label(top,textvariable=var1)

numofque = random.randrange(0,len(questions))
var2.set(questions[numofque])
label1.pack()
a=createa(numofque)
B1=tk.Radiobutton(top,text="A."+a[0],variable= var1,value="A",command=point)
B2=tk.Radiobutton(top,text="B."+a[1],variable= var1,value="B",command=point)
B3=tk.Radiobutton(top,text="C."+a[2],variable= var1,value="C",command=point)
B4=tk.Radiobutton(top,text="D."+a[3],variable= var1,value="D",command=point)
B1.pack()
B2.pack()
B3.pack()
B4.pack()
top.mainloop()

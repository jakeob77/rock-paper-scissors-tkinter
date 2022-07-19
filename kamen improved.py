import tkinter
import random

root = tkinter.Tk()
root.title("kamen, škarje in papir")
root.geometry("500x600")



random_number=random.randint(0, 2)
options=["kamen","škarje","papir"]
compguess=options[random_number]

rock_image = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper_image = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors_image = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  



def rock():
    label_usrchoice['text']=rock_image
    if compguess=="kamen":
        label_result['text']="draw"
        label_compchoice['text']=rock_image
    elif compguess=="škarje":
        label_result['text']="you win!"
        label_compchoice['text']=scissors_image
        
    elif compguess=="papir":
        label_result['text']="computer wins!"
        label_compchoice['text']=paper_image
        
def paper():
    label_usrchoice['text']=paper_image
    if compguess=="papir":
        label_result['text']="draw"
        label_compchoice['text']=paper_image
    elif compguess=="škarje":
        label_result['text']="computer wins!"
        
        label_compchoice['text']=scissors_image
        
    elif compguess=="kamen":
        label_result['text']="you win!"
        
        label_compchoice['text']=rock_image
        
def scissors():
    label_usrchoice['text']=scissors_image
    if compguess=="škarje":
        label_result['text']="draw"
        label_compchoice['text']=scissors_image
    elif compguess=="kamen":
        label_result['text']="computer wins!"
        
        label_compchoice['text']=scissors_image
        
    elif compguess=="papir":
        label_result['text']="you win!"
        
        label_compchoice['text']=paper_image
        
def reset():
    global compguess
    random_number=random.randint(0, 2)
    options=["kamen","škarje","papir"]
    compguess=options[random_number]

    label_usrchoice["text"]=""
    label_compchoice["text"]=""
    label_result["text"]="izberi..."

   





button_rock=tkinter.Button(root, text="kamen", command =rock)
button_rock.pack()

button_scissors=tkinter.Button(root, text="škarje", command =scissors)
button_scissors.pack()

button_paper=tkinter.Button(root, text="papir", command =paper)
button_paper.pack()

button_reset=tkinter.Button(root, text="reset", command =reset)
button_reset.pack()

label_compchoice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
label_compchoice.pack()

label_usrchoice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
label_usrchoice.pack()



label_result = tkinter.Label(root, text="izberi...")
label_result.pack()









root.mainloop()

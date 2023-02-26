from tkinter import *
root = Tk()
from tkinter import messagebox
root.title("Heart Diagnostic Report")
root.geometry("600x1200")
root.configure(bg="gold")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text="Do you experience shortness of breath during routine activities?", bg="black", fg="gold")
Question1.place(relx=0.5,rely=0.1,anchor = CENTER)
question1_r1=Radiobutton(root, text = "Yes", variable=question1_radioButton, value="yes", bg="black", fg="gold")
question1_r1.place(relx=0.5,rely=0.15,anchor = CENTER)
question1_r2=Radiobutton(root, text = "No", variable=question1_radioButton, value="no", bg="black", fg="gold")
question1_r2.place(relx=0.5,rely=0.2,anchor = CENTER)

question2_radioButton=StringVar(value="0")
Question2=Label(root, text = "Do you have swelling in the feet, ankles, or legs(shoes feel tighter) or abdomen", bg="black", fg="gold")
Question2.place(relx=0.5,rely=0.25,anchor = CENTER)
question2_r1=Radiobutton(root, text = "Yes", variable=question2_radioButton, value="yes", bg="black", fg="gold")
question2_r1.place(relx=0.5,rely=0.3,anchor = CENTER)
question2_r2=Radiobutton(root, text = "No", variable=question2_radioButton, value="no", bg="black", fg="gold")
question2_r2.place(relx=0.5,rely=0.35,anchor = CENTER)

question3_radioButton=StringVar(value="0")
Question3=Label(root, text = "Do you feel any of these symptoms: confusion, disorientation or loss of memory?", bg="black", fg="gold")
Question3.place(relx=0.5,rely=0.4,anchor = CENTER)
question3_r1=Radiobutton(root, text = "Yes", variable=question3_radioButton, value="yes", bg="black", fg="gold")
question3_r1.place(relx=0.5,rely=0.45,anchor = CENTER)
question3_r2=Radiobutton(root, text = "No", variable=question3_radioButton, value="no", bg="black", fg="gold")
question3_r2.place(relx=0.5,rely=0.5,anchor = CENTER)

question4_radioButton=StringVar(value="0")
Question4=Label(root, text = "Do you experience shortness of breath while at rest or lying down?", bg="black", fg="gold")
Question4.place(relx=0.5,rely=0.55,anchor = CENTER)
question4_r1=Radiobutton(root, text = "Yes", variable=question4_radioButton, value="yes", bg="black", fg="gold")
question4_r1.place(relx=0.5,rely=0.6,anchor = CENTER)
question4_r2=Radiobutton(root, text = "No", variable=question4_radioButton, value="no", bg="black", fg="gold")
question4_r2.place(relx=0.5,rely=0.65,anchor = CENTER)

question5_radioButton=StringVar(value="0")
Question5=Label(root, text="Do you experience persistent wheezing or coughing that produces white or pink blood tinged mucus?", bg="black", fg="gold")
Question5.place(relx=0.5,rely=0.70,anchor = CENTER)
question5_r1=Radiobutton(root, text = "Yes", variable=question5_radioButton, value="yes", bg="black", fg="gold")
question5_r1.place(relx=0.5,rely=0.75,anchor = CENTER)
question5_r2=Radiobutton(root, text = "No", variable=question5_radioButton, value="no", bg="black", fg="gold")
question5_r2.place(relx=0.5,rely=0.80,anchor = CENTER)

def heartscore():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+20
        print(score)
        
    if score <=20 :
        messagebox.showinfo("Report", "You don't need to visit a doctor. You are in good health.")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Report", "You might have to visit a doctor for a checkup.")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor or a cardiologist if you have had these problems before.")
btn = Button(root, text="Click Me", command=heartscore, bg="black", fg="gold")
btn.place(relx=0.5,rely=0.9,anchor = CENTER)
root.mainloop()
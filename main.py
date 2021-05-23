from tkinter import*
import random

global questions_answers
names_list = []
asked = []
score = 0

questions_and_answers={
1:["What are the most common symptoms of covid-19?",'dry cough, fever, tiredness','headaches, neck pain, sore throat', 'chest pain, conjunctivitis, sneezing', 'rashes','chest pain, hair loss',0],
2:["What is the most commonly used covid-19 vaccine in New Zealand?",'Moderna Vaccine', 'Johnson & Johnson’s Janssen Vaccine', 'Pfizer-BioNTech Vaccine',2],
3:["What does wearing a mask do to prevent getting covid-19?",'Nothing.', 'It helps by keeping your mouth covered and not exposed to bacteria and other peoples germs' , 'It prevents people from looking at your face.',2],
4:["Which Alert Level insrtucts you to stay inside your bubble, only going out for the essentials?",'Alert Level 3','Alert Level 4', 'Alert Level 5',1],
5:["Which country has the most Covid-19 cases?",'Russia', 'United States of America', 'India',1],

}

def randomiser():
  global qnum #The question number is the key in our dictionary questions_answers, we have 10 keys (10 questions)
  qnum = random.randint(1,10)#So order of questions is random every time the test is played
  #Check that question is not asked already, if not, will add itself to asked list, if it is then will randomly pick again
  if qnum not in asked: #asked is a list we declared, so to start of with any number will be added, this if statement checks if its already there before.
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

class BeginQuiz:
    def __init__(self, parent):#constructer
      background_color="PeachPuff"

      #frame set up 
      self.quiz_frame= Frame(parent, bg= background_color, padx=100, pady=100)
      self.quiz_frame.grid()


      #Create a label widget for the title
      self.title_label = Label(self.quiz_frame, text= "Welcome to the Covid-19 Quiz!",font=("Comic Sans MS","39","bold"), bg=background_color)
      self.title_label.grid(row=0, padx=20)

      #label for the user Name
      self.end_label= Label(self.quiz_frame, text="Please enter your name:", bg=background_color)
      self.end_label.grid(row=1, columnspan=3, padx=20, pady=20)


      #create the entry box
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, padx=20, pady=20)


      #creating a continue button
      self.continue_button = Button(self.quiz_frame, text="Continue", bg="#C5CAE9", command=self.name_collection)
      self.continue_button.grid(row=3,  padx=20, pady=20)        
        

    def name_collection(self):
      name=self.entry_box.get()
      names_list.append(name)#add name to names list declared at the beginning
      self.quiz_frame.destroy()#destroy the starter
      Quiz(root)#we will create a new class Quiz and create an instance of it after we get the name,
      #we destroy starter the quiz_frame and open the question quiz_frame instead which will be part of the Quiz object

class Quiz:
  def __init__(self, parent):
    #colour selections
    background_color="PeachPuff"
    self.quiz_frame=Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()
    #question
    self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT", "16"), bg = background_color)
    self.question_label.grid(row=1, padx=10, pady=10)

    #holds value of radio buttons
    self.var1=IntVar()
  
  #configuring (editing) the question label to a new question and possible answers as a new radio button
  def questions_setup(self):
    randomiser
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])

    #radio button 1
    self.rb1= Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable=self.var1, indicator = 0, background = "light blue")
    self.rb1.grid(row=2, sticky=W)

    #radio button 2
    self.rb2= Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable=self.var1, indicator = 0, background = "light blue")
    self.rb2.grid(row=3, sticky=W)
    
    #radio button 3
    self.rb3= Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable=self.var1, indicator = 0, background = "light blue")
    self.rb3.grid(row=4, sticky=W)

    #radio button 4
    self.rb4= Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable=self.var1, indicator = 0, background = "light blue")
    self.rb4.grid(row=5, sticky=W)

    #confirm button
    self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="#C5CAE9")
    
    #confirm button command, could be enhanced.
    def test_progress(self):
      global score #This score needs to be accessible to to all question
      scr_label=self.score_label
      choice=self.var1.get()
      if len (asked)<9:
        if choice == questions.answers[qnum][6]:#checking that the key has the correct answer which:
          score+=1
          scr_label.configure(text=score)
          self.quiz_instance.config(text="Confirm")
          self.endscreen()

        else:
          print(choice)
          score+=0
          scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
          self.quiz_instance.config(text="Confirm")
          self.endscreen()
        
      else:
        if choice == 0:
          self.quiz_instance.config(text="Try Again, you didn't select an option")
          choice=self.var1.get()

        else:
          if choice == questions_answers[qnum][6]:
            score+1
            scr_label.configure(text="score")
            self.quiz_instance.config(text="Confirm")
            self.questons_setup()
         
          else:
            print(choice)
            score+=0
            scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
            self.quiz_instance.config(text="Confirm")
            self.questions_setup()
            

    #score label
    self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"),bg=background_color)
    self.score_label.grid(row=8, padx=10, pady=1)
      #image
      #logo = PhotoImage(file="road.gif")
      #self.logo = Label(self.quiz_frame, image=logo)  
      #self.logo.grid(row=4,padx=20, pady=20) 
      

randomiser()
if __name__ =="__main__":
    root = Tk()  #create the window 
    root.title("NZ Covid-19 Quiz")   #title of the window
    quiz_instance = BeginQuiz(root)
    root.mainloop()  #so the window doesn't disappear   


"""Whenever the Python interpreter reads a source file, it does two things:

it sets a few special variables like __name__, and then
it executes all of the code found in the file.

If you are running your module (the source file) as the main program, e.g. guiQuizPart1.py
the interpreter will assign the hard-coded string "__main__" to the __name__ variable

global questions_and_answers
name_list = []
asked = []
score = 0
"""
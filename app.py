import tkinter as tk
import time
import random


app = tk.Tk()
app.title("Simon - The Game")

score = 0
sequence_index = 0
number_of_colors= 2
colors = ["red", "green", "blue", "yellow"]
sequence = []
user_sequence = []


    
def change_the_color():
    global sequence_index  # Use the global index
    sequence_index = 0 
    random_colors = random.choices(colors, k=number_of_colors)  # Generate 5 random colors
    for color in random_colors:
        label.config(bg=color, text=color)
        label.update()
        time.sleep(1)  # Pause for 1 second to display the color
          # Clear the label
        label.update()
        time.sleep(1)  # Pause for 1 second between colors
        label.config(text="now it's your turn",bg="white")
        
        sequence.append(color)
        

def after_first_try():
    label.config(text="Nice let's try again", bg="white")
    time.sleep(1)
    global sequence_index  # Use the global index
    sequence_index = 0
    
    for color in sequence:
        label.config(bg=color,text =color)
        label.update()
        time.sleep(1)
        
        label.update()
        time.sleep(1)
        label.config(text="now it's your turn",bg="white")
    
    user_sequence.clear()
   
    
        

def user_input_save(pressed_color):
    user_sequence.append(pressed_color)
    if len(sequence) == len (user_sequence):
            checked_user_input()


def checked_user_input():
    global number_of_colors
    global score
    if user_sequence == sequence:
        number_of_colors +=1
        random_colors = random.choices(colors, k=1)
        sequence.extend(random_colors)
        score += 1
        my_score.config(text=f'Your Score:  {score}')
        my_score.update()
        after_first_try()

    else: 
        label.config(text="Sorry you failed")
        label.config(bg="white")
        label.update()
        time.sleep(2)
        label.config(text="press start and try again")
        sequence.clear()
        user_sequence.clear()
        number_of_colors = 1


my_score=tk.Label(app, text = f'Your Score:  {score}', bg="white", width =20, height =5)
my_score.pack(pady=10)       

label = tk.Label(app, text = "Simon the Game", bg= "white", width = 20, height = 5)
label.pack(pady=10)

red_button = tk.Button(app, text = "red",highlightbackground="red",command=lambda:user_input_save("red"))
green_button = tk.Button(app, text = "green",highlightbackground="green",bg="green", command=lambda:user_input_save("green"))
blue_button = tk.Button(app, text = "blue",highlightbackground="blue", command=lambda:user_input_save("blue"))
yellow_button = tk.Button(app, text = "yellow",highlightbackground="yellow",command=lambda:user_input_save("yellow"))
start_button = tk.Button(app, text="Start", command=change_the_color)
quit_button = tk.Button(app, text="Quit", command=app.destroy, width=50, height=10, highlightbackground="black",fg="black")


start_button.pack()


red_button.pack()
green_button.pack()
blue_button.pack()
yellow_button.pack()




quit_button.pack()

if __name__ == "__main__":
    app.mainloop()
    print(user_sequence)
    print(sequence)
    print(number_of_colors)
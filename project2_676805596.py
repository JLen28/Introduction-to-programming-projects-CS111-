######################################################
# Project: Simple Scrolling Game
# Student Name:  Lenaghan, Joseph
# UIN: 676805596
# URL to repl.it:  https://repl.it/@JosephLenaghan/Project2
######################################################








#turtle and random are imported for further use
import random
import turtle

#screen is setup
screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("purple")

#characters in the game are defined with a variable bank

player = {"turtle": turtle.Turtle(), "x":-100, "y": -100, "radius": 50, "color": "blue"}

harm = {"turtle": turtle.Turtle(), "x":random.randint(200,250), "y": random.randint(0,200), "radius": 25, "color": "red"}

benefit = {"turtle": turtle.Turtle(), "x": random.randint(0,200), "y": random.randint(0,200), "radius": 25, "color": "green"}


# variable bank for the game is created
game = {"score": 0, "lives": 3, }

#turtles that will write the score, lives, and display the "game over" are defined
turdle = turtle.Turtle()
turdle.hideturtle()
turdle.penup()
turdle.goto(-100,200)
turdle.pendown()

turdle2 = turtle.Turtle()
turdle2.hideturtle()
turdle2.penup()
turdle2.goto(-200,200)
turdle2.pendown()

turdle3 = turtle.Turtle()
turdle3.hideturtle()
turdle3.penup()
turdle3.goto(0,100)
turdle3.pendown()




# hide the turtles
player["turtle"].hideturtle();
harm["turtle"].hideturtle();
benefit["turtle"].hideturtle();


screen.tracer(0)    # turn off continuous updating


# circles are drawn as filled circles corresponding to variables retrieved from the respected characters variable bank

def draw_circle(t, x, y, r, color):
  t.penup()
  t.fillcolor(color)
  t.goto(x, y)
  t.pendown()
  t.begin_fill()
  t.circle(r)
  t.end_fill()


#  handle up merely changes the y variable 
def handle_up():
 global player
 player["y"] += 10


#  handle up merely changes the y variable 
def handle_down():
  global player
  player["y"] -= 10

screen.onkey(handle_down, "Down")
screen.onkey(handle_up, "Up")   # handle the up key event
screen.listen()                 # listen for events


#  function returns true if the objects are touching, false otherwise
#
def objects_are_in_collision (x1,y1,r1,x2,y2,r2):
  if (x2-x1)^2 +(y1-y2)^2 <= (r1+r2)^2:
    return True
  else:
    return False 


current_game = True
# continous loop that will run the game is defined
while current_game:

  # harms scrolling position defined
  harm["x"] -= 1
  # benefit scrolling position defined
  benefit["x"] += 1

  # handle edge condition
  if harm["x"] < -200:
    harm["x"] = random.randint(-200,200)
    harm["y"] = random.randint(-200,200)
    harm["x"] * -1 
  # benefit character edge condition is defined
  if benefit["x"] > 200:
    benefit["x"] = random.randint(-200,200)
    benefit["y"] = random.randint(-200,200)
  


  # clear any prior drawing for the turtles
  player["turtle"].clear()         
  harm["turtle"].clear()
  # benefit character prior drawings are deleted
  benefit["turtle"].clear()
  
  
  
  # draw the characters (circles)
  draw_circle(player["turtle"], player["x"], player["y"], player["radius"], player["color"])    
  draw_circle(harm["turtle"], harm["x"], harm["y"], harm["radius"], harm["color"]) 
  
  draw_circle(benefit["turtle"], benefit["x"], benefit["y"], benefit["radius"], benefit["color"])

  # check and handle collision between player and harm
  lives = game["lives"]

  if objects_are_in_collision (player["x"],player["y"],player["radius"],harm["x"],harm["y"],harm["radius"]):
    x = lives
    counter = x - 1
    harm["x"] = random.randint(-250,250)
    harm["y"] = random.randint(-250,250)
    
    

    
  
   # TODO: reduce game lives
    game["lives"] = counter
  

  # TODO:  check and handle collision between player and benefit  
  if objects_are_in_collision (player["x"],player["y"],player["radius"],benefit["x"],benefit["y"],benefit["radius"]):
    
    game["score"] += 10
    benefit["x"] = random.randint(-250,250)
    benefit["y"] = random.randint(-250,250)


  turdle.clear()
  turdle2.clear()
  turdle.write(game["score"], font=("Arial", 20, "bold"))
  turdle2.write(game["lives"], font=("Arial", 20, "bold"))
  # repaint the screen
  screen.update()  

  if game["lives"] <= 0:
    player["x"] = 0
    player["y"] = 0
    harm["x"] = 0
    harm["y"] = 0
    benefit["x"] = 0
    benefit["y"] = 0
    game["score"] = 0
    
    turdle3.write("GAME OVER", font=("Arial", 20, "bold"))



      
   
 
   


    


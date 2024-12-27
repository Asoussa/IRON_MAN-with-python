#importing the turtle module
import turtle
# defining the coordinates for the facial part
face_one = [
  [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),(-40, -20), (0, -20)],

  [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),(40, 120), (0, 120)]
]

face_two = [
  [(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),(-80, -230), (-64, -210), (0, -210)],
  
  [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),(100, -46), (50, -40), (40, -30), (0, -30)]
]

face_three = [
    [(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), 
     (-60, -260), (-30, -260), (-20, -250), (0, -250)],
    [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), 
     (120, -250), (110, -220), (80, -240), (60, -220), (0, -220)]
]

#Hide the turtle(ْmouse on the screen when its typing)
turtle.hideturtle()

#Background
turtle.bgcolor("#000000")

#setup the window size means (width,higth) on the screen in pixels
turtle.setup(500,600)

#define where each face part will start
face1_s=(0,120)
face2_s=(0,-30)
face3_s=(0,-220)

#define the drawing speed
turtle.speed(2)

#function to draw the face
def Iron_man_p1(face,starting):
   turtle.penup()
   turtle.goto(starting)
   turtle.pendown()
   turtle.color("#FFD700")
   turtle.begin_fill()
   for i in range(len(face[0])):
      x,y=face[0][i]
      turtle.goto(x,y)
   turtle.end_fill()
def Iron_man_p2(face,starting):
   turtle.penup()
   turtle.goto(starting)
   turtle.pendown()
   turtle.color("#C0C0C0")
  
   turtle.begin_fill()
   for i in range(len(face[1])):
      x,y=face[1][i]
      turtle.goto(x,y)
   turtle.end_fill()

   
Iron_man_p1(face_one,face1_s)
Iron_man_p1(face_two,face2_s)
Iron_man_p1(face_three,face3_s)
Iron_man_p2(face_one,face1_s)
Iron_man_p2(face_two,face2_s)
Iron_man_p2(face_three,face3_s)
turtle.done()

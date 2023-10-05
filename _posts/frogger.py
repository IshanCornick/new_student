from processing import*
from random import *
from sprite import*
from frog import*
from log import*
from car import*
from urtle import*

def setup():
  size(600,500)
  global heart1,end,win, heart2, heart3,endscreen, f,lives, sign, spot1, spot2, spot3, spot4, spot5, score , bg,log_timer1,frog_starttimer,water, log_timer2, log_list1, log_list2, log, car, turtle, timer,timer1, car_list1, car_list2, turtle_list1,turtle_list2, turtletimer, frogtimer, turtletimer1
  global log1, log2, c1, c2, t1, t2
  water = Sprite(0, 59, loadImage("download (19).png"), 597.5, 185)
  sign = Sprite(25, 225, loadImage("sign.png"), 60, 65)
  heart1 = Sprite(550, 60, loadImage("heart.png"), 45, 45)
  heart2 = Sprite(520, 60, loadImage("heart.png"), 45, 45)
  heart3 = Sprite(490, 60, loadImage("heart.png"), 45, 45)
  endscreen = Sprite(0, 0, loadImage("end.jpg"), 600, 600)
  win = Sprite(0, 0, loadImage("download (20).png"), 600, 600)
  lives = 3
  spot1 = False
  spot2 = False
  spot3 = False
  spot4 = False
  spot5 = False
  score = 0
  timer = 120
  timer1 = 90
  turtletimer = 125
  frogtimer = 0
  turtletimer1 = 150
  log_timer1 = 0
  log_timer2 = 0
  frog_starttimer = 0
  turtle = Turtle(150,150, "Right")
  log = Log(50,50)
  car = Car(100,100,"Left")
  f = Frog(284,465)
  bg = loadImage("back.png")
  car_list1 = []
  car_list2 = []
  turtle_list1 = []
  turtle_list2 = []
  log_list1 = []
  log_list2 = []
  c1 = randint(80,200)
  c2 = randint(80,200)
  t1 = randint(80,200)
  t2 = randint(80,200)
  log1 = randint(80,200)
  log2 = randint(80,200)
  
def draw():
  global timer1,timer, spot1, spot2, spot3, spot4, turtle_list1, turtle_list2, log_list1, log_list2, spot1, spot2, spot3, spot4,spot5, score, turtletimer,frogtimer,turtletimer1,lives, frog_starttimer, log_timer1, log_timer2
  timer += 1
  timer1 += 1
  turtletimer += 1
  frogtimer += 1
  turtletimer1 += 1
  frog_starttimer += 1
  log_timer1 += 1 
  background(bg)
  log_timer2 += 1
  
  #car.display()
  #turtle.display()
  #log.display()
  #water.display()
  sign.display()
 
  touching_water = False
  if f.collison(water):
    touching_water = True
    for i in turtle_list1:

      if f.collison(i):
        touching_water = False
    for i in turtle_list2:
      if f.collison(i):
        touching_water = False
    for i in log_list1:
      if f.collison(i):
        touching_water = False
    for i in log_list2:
      if f.collison(i):
        touching_water = False
  if touching_water == True:
    lives += -1
    print(lives)
    
    
    
    f.x = 284
    f.y = 465
  
  
 # print f.x
 # print f.y
  
  if f.x >= 10 and f.x <=55 and f.y >= 23 and f.y < 30 and spot1 == False:
    score += 100
    spot1 = True
    f.x = 284
    f.y = 465
  if f.x >= 397 and f.x <=442 and f.y >= 23 and f.y < 30 and spot2 == False:
    score += 100
    spot2 = True
    f.x = 284
    f.y = 465
  if f.x >= 262 and f.x <=307 and f.y >= 23 and f.y < 30 and spot3 == False:
    score += 100
    spot3 = True
    f.x = 284
    f.y = 465
  if f.x >= 127 and f.x <=172 and f.y >= 23 and f.y < 30 and spot4 == False:
    score += 100
    spot4 = True
    f.x = 284
    f.y = 465
  if f.x >= 515 and f.x <=565 and f.y >= 23 and f.y < 30 and spot5 == False:
    score += 100
    spot5 = True
    f.x = 284
    f.y = 465
  


  
  if log_timer1 >= log1:
    log_list1.append(Log(-40,168.5))
    log_timer1 = 0
    
  if log_timer2 >= log2:
    log_list2.append(Log(600,95.5))
    log_timer2 = 0
  
  for i in log_list1:
    i.display()
    i.move(2, 0)
    if i.collison(f):
      f.move(2,0)
    
    if i.x > 700:
      log_list1.remove(i)
    
  for i in log_list2:
    i.display()
    i.move(-2,0)
    if i.collison(f):
      f.move(-2,0)
      
    if i.x < -100:
      log_list2.remove(i)
  
  if timer >= c1:
    car_list1.append(Car(600,425, "left"))
    car_list1.append(Car(600,352, "left"))
    car_list1.append(Car(600,279, "left"))
    timer = 0
    
  if timer1 >= c2:
    car_list2.append(Car(0,388.5, "right"))
    car_list2.append(Car(0,315.5, "right"))
    
    timer1 = 0
    
  for i in car_list1:
    i.display()
    i.move(-1.5, 0)
    if i.collison(f):
      f.x = 284
      f.y = 465
      lives += -1
      print(lives)
    if i.x < -100:
      car_list1.remove(i)
    
  for i in car_list2:
    i.display()
    i.move(1.5,0)
    if i.collison(f):
      f.x = 284
      f.y = 465
      lives += -1
      print(lives)
      
    if i.x > 700:
      car_list2.remove(i)
    
  if turtletimer >= t1:
    turtle_list1.append(Turtle(-40,205, "right"))
    turtle_list1.append(Turtle(-80,205, "right"))
    turtle_list1.append(Turtle(-120,205, "right"))
    turtle_list1.append(Turtle(-40,59, "right"))
    turtle_list1.append(Turtle(-80,59, "right"))
    turtle_list1.append(Turtle(-120,59, "right"))
    turtletimer = 0
    
  if turtletimer1 >= t2:
    turtle_list2.append(Turtle(600,132, "left"))
    turtle_list2.append(Turtle(640,132, "left"))
    turtle_list2.append(Turtle(680,132, "left"))
    turtletimer1 = 0
  
  for i in turtle_list1:
    i.display()
    i.move(1.5, 0)
    if i.collison(f):
      f.move(1.5,0)
    if i.x > 700:
      turtle_list1.remove(i)
    
  for i in turtle_list2:
    i.display()
    i.move(-3,0)
    if i.collison(f):
      f.move(-2,0)
    if i.x < -100:
      turtle_list2.remove(i)
      
      
  f.display()
  
  
  if lives == 3:
    heart1.display()
    heart2.display()
    heart3.display()
  elif lives == 2:
    heart1.display()
    heart2.display()
  elif lives == 1:
    heart1.display()
  
  if lives == 0:
    endscreen.display()
    exit()
  
  if score == 500:
    win.display()
    exit()
      
  if frog_starttimer > 200:
    if frogtimer > 15:
      if keyPressed:
        if key == CODED:
          if keyCode == RIGHT:
            f.move(45,0)
            frogtimer = 0
          if keyCode == LEFT:
            f.move(-45,0)
            frogtimer = 0
          if keyCode == UP:
            f.move(0,-36.5)
            frogtimer = 0
          if keyCode == DOWN:
            f.move (0,36.5)
            frogtimer = 0
  
  
run()

from processing import*
from sprite import*

class Turtle(Sprite):
  def __init__(self,x,y, direction):
    if direction == "right":
      s = loadImage("turtle.png")
    else:
      s = loadImage ("turtle1.png")
    Sprite.__init__(self,x,y,s,40,40)
  
  
from processing import*
from sprite import*

class Car(Sprite):
  def __init__(self,x,y, direction):
    if direction == "right":
      s = loadImage ("car.png")
    else:
      s = loadImage("car1.png")
    Sprite.__init__(self,x,y,s,40,40)
    
    
from processing import*
from sprite import*

class Log(Sprite):
  def __init__(self,x,y):
    s = loadImage("log1.png")
    Sprite.__init__(self,x,y,s,100,32)
    
  

from processing import*
from sprite import*

class Frog(Sprite):
  def __init__(self,x,y):
    s = loadImage("frog.png.png")
    Sprite.__init__(self,x,y,s,32,32)
    
  def move(self,xs,ys):
    Sprite.move(self, xs, ys)
    
    
    if self.x > width:
      self.x = width
    if self.y > height:
      self.y = height
    if self.x < 10:
      self.x = 10
    if self.x > 565:
      self.x = 565
    if self.y > 470:
      self.y = 470
      

from processing import *
class Sprite:
  def __init__(self,x,y,s,w,h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.sprite = s
  def display(self):
    image(self.sprite,self.x,self.y,self.w,self.h)
  def move(self,xs,ys):
    self.x += xs
    self.y += ys



  def collison(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided



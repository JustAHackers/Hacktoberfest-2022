from __future__ import division
import curses,threading,time,random
"""
  _____   _
 /o    \_/ |
[       _  |
 `-----' `-'
"""

bird = """ _   _____
\\ \_/    o\\
/  _       ]
'-` '-----`
"""







"""
Jangan di rikod ya adik adik, gw buat ini ga mudah ajg

WA : 0896 8200 9902
"""



score = 0
delay = False
adstop = False
obstacle = []
abuse = []
again = False
thread_session = []


def running_text(slep):
    global abuse
    mysession = random.randint(99999,9999999)
    thread_session.append(mysession)
    while True and not lose:
       if mysession not in thread_session:
          break
       abyss = {}
       for i in abuse[0]:
           if i-1 < abuse[1]:
              abyss[abuse[2]] = abuse[0][i]
           else:
              abyss[i-1] = abuse[0][i]
       abuse[0] = dict(abyss)
       time.sleep(slep)


def tredo(slep):
    global birdo,delay
    mysession = random.randint(99999,9999999)
    thread_session.append(mysession)
    while not adstop and not lose:
       if mysession not in thread_session:
          break
       birdo = [(lambda x,n:[x+1,n])(i[0],i[1]) for i in birdo]
       if delay:
          time.sleep(delay)
          delay = False
       time.sleep(slep)

def tros(slep):
    global obstacle,score,abuse
    mysession = random.randint(99999,9999999)
    thread_session.append(mysession)
    while True and not lose:
       if mysession not in thread_session:
          break
       for i in sorted(obstacle,key = lambda x:x[1]):
           if i[1] == 0:
              obstacle.remove(i)
              score += 1
       obstacle = [(lambda y,x,o:[x,y-1,o])(i[1],i[0],i[2]) for i in obstacle] #bikin rintangan berjalan
       time.sleep(slep)


def troda(slep,yy,xx):
    global obstacle
    mysession = random.randint(99999,9999999)
    thread_session.append(mysession)
    while True and not lose:
       if mysession not in thread_session:
          break
       y = random.randint(10,yy-5)
       x = xx-5
       downside = list(range(y,yy-1)) #bikin rintangan bagian bawah
       [downside.append(i) for i in range(2,y-8)[::-1]] #Bikin rintangan bagian atas
       obstacle.append([y,x,downside])
       time.sleep(slep)

birdo = []
lose = False
def cur(c):
    global birdo,delay,lose,abuse,obstacle,score,again,thread_session
    yy,xx = c.getmaxyx() # mengambil max y dan x di terminal
    wow = {}
    obstacle = []
    min = xx//2 - len("Coded by JustA Hacker")
    max = xx//2 + len("Coded by JustA Hacker")
    for n,i in enumerate("Coded by JustA Hacker"):
        wow[(xx//2 - (len("Coded by JustA Hacker") // 2)) + n] = i
    abuse.append(wow)
    abuse.append(min)
    abuse.append(max)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_GREEN)
    birdo = [[yy//2-2,5],[yy//2-1,5],[yy//2,5],[yy//2+1,5]] #bikin koordinat badan burung
    c.attron(curses.color_pair(2))
    [c.addstr(saga[0],saga[1],lost) for lost,saga in zip(bird.splitlines(),birdo)]
    c.attroff(curses.color_pair(2))
    c.attron(curses.color_pair(1))
    c.addstr(yy-1,0,"-"*(xx-1))
    c.addstr(1,0,"-"*(xx-1))
    c.attroff(curses.color_pair(1))
    c.addstr(yy//2,xx//2-len("Press 'space' or 'up' button to jump")//2,"Press 'space' or 'up' button to jump")
    c.refresh()
    while True:
       coki = c.getch()
       if coki == ord(" ") or coki == curses.KEY_UP:
          break
    trd = threading.Thread(target=tredo,args=(0.1,))
    trd.daemon = True
    trd.start()
    trd2 = threading.Thread(target=troda,args=(yy / 15,yy,xx))
    trd2.daemon = True
    trd2.start()
    trd3 = threading.Thread(target=tros,args=(yy / 600,)) 
    trd3.daemon = True
    trd3.start()
    trd4 = threading.Thread(target=running_text,args=(0.1,))
    trd4.daemon = True
    trd4.start()
    c.nodelay(1)
    kimi_no_nawa = 0
    while True:
       coki = c.getch()
       c.erase()
       if coki == ord(" ") or coki == curses.KEY_UP:
          birdo = [(lambda x,n:[x-2,n])(i[0],i[1]) for i in birdo]
          if not delay:
             delay = 0.3
          if kimi_no_nawa < 4:
             kimi_no_nawa += 1
             birdo = [(lambda x,n:[x-1,n])(i[0],i[1]) for i in birdo]
          else:
             kimi_no_nawa = 0
             coki = ""
             adstop = False
       c.attron(curses.color_pair(2))
       [c.addstr(saga[0],saga[1],lost) for lost,saga in zip(bird.splitlines(),birdo)]
       c.attroff(curses.color_pair(2))
       c.attron(curses.color_pair(1))
       c.addstr(yy-1,0,"-"*(xx-1))
       c.addstr(1,0,"-"*(xx-1))
       c.attroff(curses.color_pair(1))
       c.addstr(0,0,"Score : {}".format(score))
       for i in obstacle:
           c.attron(curses.color_pair(1))
           c.addstr(i[0],i[1],"||||")
           [c.addstr(b,i[1],"||||") for b in i[2]]
       c.attroff(curses.color_pair(1))
       try:
         [c.addstr(0,i,abuse[0][i]) for i in sorted(abuse[0])]
       except:
         pass

       for n,z in enumerate(birdo):
          if z[0] == 1 or z[0] == yy-1 or (z[0] == obstacle[0][0] and z[1] == obstacle[0][1]) or (z[0] in obstacle[0][2] and obstacle[0][1] in range(z[1],z[1]+len(bird.splitlines()[n])+1)) :
             c.addstr(yy//2,xx//2 - len(" You lose ")//2," You lose ")
             c.addstr(yy//2+1,xx//2 - len("Press Q or q to quit the game")//2,"Press Q or q to quit the game")
             c.addstr(yy//2+2,xx//2 - len("Press A or a to play again")//2,"Press A or a to play again")
             c.nodelay(0)
             lose = True
             again = False
             while True:
                cus = c.getch()
                if cus  == ord("q") or cus == ord("Q"):
                   break
                elif cus == ord("a") or cus == ord("A"):
                   again = True
                   lose = True
                   break
             break

       if lose and not again:
          return
       elif lose and again:
          birdo = []
          obstacle = []
          c.erase()
          score = 0
          lose = False
          obstacle = []
          del trd,trd2,trd3,trd4
          thread_session = []
          cur(c)
          break
       c.refresh()

#-#
def selectskin(c):
    curses.curs_set(0)
    curses.noecho()
    yy,xx = c.getmaxyx()
    liszt = [curses.COLOR_WHITE,curses.COLOR_GREEN,curses.COLOR_BLUE,curses.COLOR_CYAN,curses.COLOR_MAGENTA,curses.COLOR_RED,curses.COLOR_YELLOW]
    name = ["White Angel","Green Tea","Blue Eyes","Cyan Ocean","Magenta Baracuda","Red Blood","Yellow Poop"]
    kolor = 0
    curses.init_pair(5,curses.COLOR_BLACK,curses.COLOR_WHITE)
    c.attron(curses.color_pair(5))
    c.addstr(yy//2 - 5,xx // 2 - len("Select Your Bird")//2 - 2,"Select Your Bird")
    c.attroff(curses.color_pair(5))
    curses.init_pair(2,liszt[kolor],curses.COLOR_BLACK)
    c.attron(curses.color_pair(2))
    [c.addstr(yy // 2 - (len(bird.splitlines()) // 2) + n,xx//2 - 8,i) for n,i in enumerate(bird.splitlines())]
    c.addstr(yy // 2 - 3,xx//2 - len(name[kolor]) // 2 - 3,name[kolor])
    c.attroff(curses.color_pair(2))
    c.addstr(yy // 3-5,xx//2 - len("Press enter to select") // 2,"Press Enter to select")
    c.addstr(yy // 3-4,xx//2- len("Press space or right / left key to change color") // 2,"Press space or right / left key to change color")
    while True:
       movement = c.getch()
       c.erase()
       c.attron(curses.color_pair(5))
       c.addstr(yy//2 - 5,xx // 2 - len("Select Your Bird")//2 - 2,"Select Your Bird")
       c.attroff(curses.color_pair(5))
       if movement == curses.KEY_RIGHT or movement == ord(" "):
          kolor += 1
       elif movement == curses.KEY_LEFT:
          kolor -= 1
       if kolor < 0:
          kolor = len(liszt)-1
       elif kolor > len(liszt)-1: 
          kolor = 0
       curses.init_pair(2,liszt[kolor],curses.COLOR_BLACK)
       c.attron(curses.color_pair(2))
       [c.addstr(yy // 2 - (len(bird.splitlines()) // 2) + n,xx//2 - 8,i) for n,i in enumerate(bird.splitlines())]
       c.addstr(yy // 2 - 3,xx//2 - len(name[kolor]) // 2 - 3,name[kolor])
       c.attroff(curses.color_pair(2))
       c.addstr(yy // 3-5,xx//2 - len("Press enter to select") // 2,"Press Enter to select")
       c.addstr(yy // 3-4,xx//2- len("Press space or right / left key to change color") // 2,"Press space or right / left key to change color")
       c.refresh()
       if movement == ord("\n"):
          break
    c.erase()
    cur(c)
#-#

curses.wrapper(selectskin)

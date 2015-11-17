import sae
import time
from sys import exit

print "Welcome to Miss Python's Secret Diary"
psw = "1234"
guess = str(raw_input('Code(4 numbers)：'))

if guess == psw:
    print 'Welcome!'

    print "Option：a.LOOK BACK ; b.WRITING THE PRESENT ; c.CREAT FURTURE"

    choose = raw_input('So? ~(～o￣▽￣)～o 。。')

    if choose == 'a':
       f = open("misspython.txt","r")
       diary = f.read()
       print(diary)


    elif choose == 'b':
        f = open ("misspython.txt","a")
        diary = raw_input('>>>') 
        f.write("\n" + time.strftime('%Y/%m/%d') + " " + diary + "\n")  
        print diary
        print "Saved，Adios！"
 
    elif choose == 'c':
        print "Live a better life，Adios！"
        exit()


else:
    print 'No, idiot! Adios！'
    exit()


    f.close()
    
application = sae.create_wsgi_app(app)

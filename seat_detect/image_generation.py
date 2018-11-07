# 사용 외부 라이브러리 graphics, image(PIL)
from graphics import *
from random import *
from PIL import Image, ImageDraw


def imageGen():

    f = open('input.txt','r')
    fw = open('output.txt','w')
    winy,winx = map(int, f.readline().split())
    seat_w,seat_h  = map(int, f.readline().split())

    fw.write("%d %d\n" %(winy, winx))
    fw.write("%d %d\n" %(seat_w, seat_h))

    win1 = GraphWin("zz", winx, winy)
    win1.setBackground(color_rgb(0, 0, 0))

    image = Image.new("RGB", (winx, winy), color_rgb(0,0,0))
    draw = ImageDraw.Draw(image)

    win1.update()
    win1.postscript(file="file_name.ps", colormode='color')

    for i in range(42):
        x,y = map(int, f.readline().split())
        fw.write("%d %d\n" % (x, y))
        num = f.readline()

        for j in range(int(num)):
            rec = Rectangle(Point(x, y), Point(x+seat_w, y+seat_h))
            col = randint(0,2)

            if col==0:
                colrgb = color_rgb(0, 0, 0)
            elif col==1:
                colrgb = color_rgb(67, 65, 66)
            else:
                colrgb = color_rgb(64, 132, 34)
            fw.write("%d "%col)

            rec.setFill(colrgb)
            rec.draw(win1)
            draw.rectangle([(x,y),(x+seat_w, y+seat_h)],fill=colrgb)

            x=x+4+seat_w

        fw.write("\n")
    f.close()

    filename = "random_generated.jpg"
    image.save(filename)

    win1.getMouse() # Pause to view result
    win1.close()    # Close window when done


imageGen()




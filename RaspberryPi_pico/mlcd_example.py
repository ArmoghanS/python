import mlcd,pygame     #import the module
import time
mlcd.init(16,3,3) # initialize a 16x3 display scaled 3x  
#draw the three lines passed as a list
mlcd.draw(["Time: {}".format(time.asctime())])


    


##### setup #####
from PiStorms import PiStorms
from time import sleep
psm = PiStorms()
ts = psm.BBS1
ls = psm.BAS2
rs = psm.BBS2
cm = psm.BAM1
lm = psm.BAM2
rm = psm.BBM2
def touch(s):               return s.isTouchedNXT()
def light(s, reflected=1):  return s.lightSensorNXT(reflected)
def motor(m, speed=50):     m.setSpeed(-speed)
def motorMoveDegs(m, degree, speed=50, brake=True, hold=False):
    m.runDegs(degree, -speed, brake, hold)
    m.waitUntilNotBusy()
def motorSetDegs(m, degree, speed=50, brake=True, hold=False):
    sd = m.pos()
    m.runDegs(degree - m.pos(), speed, brake, hold)
    m.waitUntilNotBusy()
    
##### start #####
#cm.resetPos()
while True:
    if touch(ts):
        motor(lm, 0)
        motor(rm, 0)
        #motorDegree(cm, -300, 100)
        #motorDegree(cm, 300, 100)
        setPos(cm, -300)
        print(cm.pos())
        setPos(cm, 0)
        print(cm.pos())
    #else:
        #motor(lm)
        #motor(rm)

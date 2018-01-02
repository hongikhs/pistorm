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
def touch(s):                   return s.isTouchedNXT()
def light(s, reflected=True):   return s.lightSensorNXT(reflected)
def motor(m, speed=50):         m.setSpeed(-speed)
def motorRunDegs(m, degree, speed=50, brake=True, hold=True):
    m.runDegs(degree, -speed, brake, hold)
    m.waitUntilNotBusy()
def motorSetDegs(m, degree, speed=50, brake=True, hold=True):
    sleep(0.06)
    sd = m.pos()
    m.runDegs(degree - sd, speed, brake, hold)
    m.waitUntilNotBusy()
    
##### start #####
while True:
    if touch(ts):
        motor(lm, 0)
        motor(rm, 0)
        motorSetDegs(cm, -300)
        motorSetDegs(cm, 0)
    #else:
        #motor(lm)
        #motor(rm)

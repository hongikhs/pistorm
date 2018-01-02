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
def motorDegree(m, degree, speed=50, brake=True, hold=False):
    m.runDegs(degree, -speed, brake, hold)
    m.waitUntilNotBusy()

##### start #####
while True:
    if touch(ts):
        motor(lm, 0)
        motor(rm, 0)
        motorDegree(cm, -300, 100, True, True)
        motorDegree(cm, 300, 100, True, True)
    else:
        motor(lm)
        motor(rm)

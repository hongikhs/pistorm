from PiStorms import PiStorms
from time import sleep
psm = PiStorms()
def ts():   return psm.BBS1.isTouchedNXT()
def rs():   return psm.BBS2.lightSensorNXT(True)
def ls():   return psm.BAS2.lightSensorNXT(True)
cm = psm.BBM1
rm = psm.BBM2
lm = psm.BAM2    
while not ts():
    rm.setSpeed(30)
    lm.setSpeed(30)
rm.setSpeed(0)
lm.setSpeed(0)

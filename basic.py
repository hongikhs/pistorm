from PiStorms import PiStorms
from time import sleep
psm = PiStorms()
def ts():   return psm.BBS1.isTouchedNXT()
def rs():   return psm.BBS2.lightSensorNXT(True)
def ls():   return psm.BAS2.lightSensorNXT(True)
def cm(sp): psm.BBM1.setSpeed(sp)
def rm(sp): psm.BBM2.setSpeed(sp)
def lm(sp): psm.BAM2.setSpeed(sp)
    
while not ts():
    #print(rs(), ls())
    rm(30)
    lm(30)
rm(0)
lm(0)

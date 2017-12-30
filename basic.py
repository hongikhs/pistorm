from PiStorms import PiStorms
from time import sleep
psm = PiStorms()
def ts():   return psm.BBS1.isTouchedNXT()
def rs():   return psm.BBS2.lightSensorNXT(reflectiveMode)
def ls():   return psm.BAS2.lightSensorNXT(reflectiveMode)

while not ts():
    print(rs(), ls())
    sleep(0.5)

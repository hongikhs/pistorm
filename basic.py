from PiStorms import PiStorms
from time import sleep
psm = PiStorms()
def ts():   return psm.BBS1.isTouchedNXT()
while not ts():
    print('.')

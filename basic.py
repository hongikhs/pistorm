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
def tsv():      return ts.isTouchedNXT()
def rsv(lt):    return rs.lightSensorNXT(lt)
def lsv(lt):    return ls.lightSensorNXT(lt)
def rms(sp):    rm.setSpeed(-sp)
def lms(sp):    lm.setSpeed(-sp)
def cmd(dg):
    cm.runDegs(dg, 50, True, False)
    cm.waitUntilNotBusy()

##### start #####
cmd(-200)
cmd(200)
while not tsv():
    rms(30)
    lms(30)
rm.setSpeed(0)
lm.setSpeed(0)

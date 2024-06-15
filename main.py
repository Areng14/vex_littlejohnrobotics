# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Areng                                                        #
# 	Created:      6/1/2024, 2:55:59 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

#define motor ports
drive_ports = (Ports.PORT1, #idk what this port even is. someone needs to find out
               Ports.PORT2, #idk what this port even is. someone needs to find out
               Ports.PORT3, #idk what this port even is. someone needs to find out
               Ports.PORT4) #idk what this port even is. someone needs to find out

#Inititlize everything

#Define motor groups
d_lfor = Motor(drive_ports[0]) #left forwards
d_rfor = Motor(drive_ports[1]) #right forwards
d_lbac = Motor(drive_ports[2]) #left backwards
d_rbac = Motor(drive_ports[3]) #right backwards

#group em motors
leftm = MotorGroup(d_lfor,d_lbac)
rightm = MotorGroup(d_rfor,d_rbac)

#define controller
control = Controller()

def driver():
    #Continuely listen to controller
    while True:
        axises = [
            round(control.axis2.position() / 10) * -1,
            round(control.axis3.position() / 10) * -1,
        ] #Store the axis into a list
        """
        Divide by 10 for chunking and multiply by -1 to reverse

        """
        multi = 20 #Sensitive amount. The more the more sensitive

        """
        Spin the motors. just randomize reverse forward until they seem to be
        driving correctly. if it works, dont change it
        """
        leftm.spin(REVERSE,axises[0] * multi)
        rightm.spin(FORWARD,axises[1] * multi)
    
Thread(driver)
#Basic drivetrain complete

#do more stuff
 

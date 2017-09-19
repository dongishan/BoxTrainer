import grove6axis
import time
import numpy as np
import utils

log_file="punch_detection_data.csv" # Name of the output file

timeToSleep=0.1

constantLP=0.0001
        
def validate6Axis(validated6Axis):
        try:
                grove6axis.init6Axis()
                validated6Axis(True)
        except IOError:
                validated6Axis(False)
                utils.btPrint("6Axis IO Error")

def detectPunches(detectedPunch):
        lowPassZAccel=0
        startSpeed=0
        endSpeed=0

        '''
        1. Below thresholds were determined by analysing (using charts in excel) the pre-recorded data for boxing shots and non-boxing shot movements.
        2. Adaptive thresholding are not neccessary for this functionality as we can generalise the avg accelarations and orientations for boxing shots for any user
        '''
        # Non punch thresholds (MODE)
        zAccelLPNonPunchThrd=-0.0001
        
        # Punch thresholds (MEAN)
        zAccelLPThrd=-0.0297
        
        singlePunchDuration=2 # Assumes it takes a player 2 seconds to apply a punch to the bag (only one arm)
        accelZLPData=[]
        try:
                #utils.btPrint("timestamp,time (gmt),yAccel,zAccel,zAccelLP")

                f=open(log_file,'a')
                f.write("timestamp,time (gmt),yAccel,zAccel,zAccelLP\n")
                f.close()

                timeToCheckNxtDataSet=time.time() + singlePunchDuration
                while True:
                        timestamp=time.time()

                        # Converting unix timestamp to gmt
                        gmtTime=(timestamp/(60*60*24))+25569
                
                        accel=grove6axis.getAccel()
                        if accel is None and orient is None:
                                break
                        # Low passing accelaration data
                        lowPassZAccel=lowPassZAccel * (1.0-constantLP) + accel[2] * constantLP
                        accelZLPData.append(lowPassZAccel)
                        
                        #utils.btPrint("%f,%f,%4.4f,%4.4f"
                              #%(timestamp,gmtTime,accel[2],lowPassZAccel))

                        # Detecting a punch
                        if timestamp >= timeToCheckNxtDataSet:
                                maxAccelZLP=np.max(accelZLPData)

                                #if maxAccelZLP > zAccelLPNonPunchThrd and maxAccelZLP > zAccelLPThrd:
                                if True:
                                        speed=abs(maxAccelZLP*singlePunchDuration)
                                        detectedPunch(speed)
                                        
                                accelZLPData=[]
                                timeToCheckNxtDataSet = timestamp + singlePunchDuration
                        
                        # Writing to the csv file
                        f=open(log_file,'a')
                        f.write("%f,%f,%4.4f,%4.4f\n"
                              %(timestamp,gmtTime,accel[2],lowPassZAccel))
                        f.close()
                        
                        time.sleep(timeToSleep)
        except IOError:
                utils.btPrint("6Axis IO Error")


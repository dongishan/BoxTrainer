import grovepi
import time
import threading
import numpy as np
import utils

kDebug=False

sound_sensor=0 # Sound sensor port number (A0)

timeToSleep=0.1

constantHP=0.5
constantLP=0.1
          
envMeanHP=0

def calibrateSoundSensor(soundCalibrated):
        def callback():
                if kDebug:
                        duration=1
                else:
                        duration=20 # Calibration runs for 20 seconds
                data=[]
                lowPass=0
                highPass=0
                envMean=0
                startTime=timestamp=time.time()
                endTime=startTime + duration
                while True:
                        try:
                                timestamp=time.time()
                                value=grovepi.analogRead(sound_sensor)
                                data.append(value)
                                if timestamp >= endTime:
                                        break
                                time.sleep(timeToSleep)
                        except IOError:
                                BTPrint("Error")
                envMean = np.mean(data)
                lowPass=lowPass * (1.0-constantLP) + envMean * constantLP
                highPass=constantHP * (highPass + lowPass - 0)
                envMeanHP=highPass
                #utils.btPrint("Adaptive Thresholding (Sound): Environment Mean = %4.4f, HPMean = %4.4f"%(envMean,envMeanHP))
                soundCalibrated(True)
        t = threading.Thread(target=callback)
        t.start()
        
def detectHits (hit):
        def callback():
                adapThrdsDuration=20 # Set to 20 seconds temporarily. In the report this value is described as 2 mins
                log_file="hit_detection_data.csv" # Name of the output file
                lowPass=0
                highPass=0
                lastValue=0
                hpOffset=10 # Offset to be added to the adaptive high-pass mean when detecting a hit. Used as the calibration value to detect events (hits)
                envHPOffset=6.2
                timeToReadAdapThrds=0
                writeHPAdapMean=0
                adapHPData=[]
                detectedHit=False
                isInitialAdapSession=True
                # Initially the adaptive mean in the environment's sound mean
                adapHPMean=envMeanHP
                
                utils.btPrint("timestamp,time (gmt),value,lowPass,highPass")

                f=open(log_file,'a')
                f.write("timestamp,time (gmt),value,lowPass,highPass,highPassAdaptiveMean\n")
                f.close()

                timeToReadNxtAdapThrds=time.time() + adapThrdsDuration
                while True:
                        try:
                                timestamp=time.time()

                                # converting unix timestamp to gmt
                                gmtTime=(timestamp/(60*60*24))+25569

                                # reading sound sensor data
                                value=grovepi.analogRead(sound_sensor)
                                # Added as a safe guard. But it seems the analog values are not None even if the sensor is not connected (this make sense since its analog)
                                if value is None:
                                        break
                                
                                # band-pass filter
                                lowPass=lowPass * (1.0-constantLP) + value * constantLP
                                highPass=constantHP * (highPass + lowPass - lastValue)
                                lastValue=lowPass
                                
                                adapHPData.append(highPass)

                                utils.btPrint("%f,%f,%4.4f,%4.4f,%4.4f"%(timestamp,gmtTime,value,lowPass,highPass))

                                # Detecting the event
                                if isInitialAdapSession:
                                        if highPass > adapHPMean + hpOffset + envHPOffset:
                                                detectedHit=True
                                else:
                                        if highPass > adapHPMean + hpOffset:
                                                detectedHit=True
                                hit(detectedHit,highPass)
                                
                                if detectedHit:
                                        detectedHit=False
                             
                                #Adaptive thresholding on mean of the high-pass data for last 10 mins
                                if timestamp >= timeToReadNxtAdapThrds:
                                        isInitialAdapSession=False
                                        adapHPMean=np.mean(adapHPData)
                                        writeHPAdapMean=adapHPMean
                                        adapHPData = []
                                        utils.btPrint("Adaptive Thresholding (Sound): Mean = %4.4f"%(adapHPMean))
                                        timeToReadNxtAdapThrds = timestamp + adapThrdsDuration

                                # Writing to the csv file
                                f=open(log_file,'a')
                                f.write("%f,%f,%4.4f,%4.4f,%4.4f,%4.4f\n"%(timestamp,gmtTime,value,lowPass,highPass,writeHPAdapMean))
                                f.close()
                                writeHPAdapMean=0             
                        
                                time.sleep(timeToSleep)
                        except IOError:
                                utils.btPrint("Error")
        t = threading.Thread(target=callback)
        t.start()


from Tkinter import StringVar
from Tkinter import *
import hitdetection
import punchdetection
import time

root = Tk()

def init() :
	root.wm_title("BoxTrainer - Jubilee Campus Gym")
	root.resizable(width=FALSE, height=FALSE)
	rootWindow = PanedWindow()
	rootWindow.pack(fill=Y, expand=1)

	mainWindow = PanedWindow(rootWindow)
	mainWindow.pack(fill=BOTH, expand=1)

	#Creating leaderboard UI
	createLeaderboard(mainWindow)
	#Creating player statistics UI
	createPlayerStatsGrid(mainWindow)
	#Creating bottom view UI
	createBottomMenu(rootWindow)

	root.mainloop()

def createLeaderboard(mainWindow) :
	leaderboardWindow = PanedWindow(mainWindow, orient=VERTICAL)
	mainWindow.add(leaderboardWindow)

	leaderboardFrame = Frame(leaderboardWindow)
	leaderboardFrame.pack()
	leaderboardLabel = Label(leaderboardFrame, text="LEADERBOARD")
	leaderboardLabel.pack(side = LEFT)

	fstFrame = Frame(leaderboardWindow, bg="pink")
	fstFrame.pack()
	fstLabel = Label(fstFrame, text="Ruvini", bg="pink")
	fstLabel.pack(side = LEFT)

	sndFrame = Frame(leaderboardWindow, bg="lightblue")
	sndFrame.pack()
	sndLabel = Label(sndFrame, text="Gishan", bg="lightblue")
	sndLabel.pack(side = LEFT)

	thirdFrame = Frame(leaderboardWindow, bg="Thistle")
	thirdFrame.pack()
	thirdLabel = Label(thirdFrame, text="Micheal", bg="Thistle")
	thirdLabel.pack(side = LEFT)

	forthFrame = Frame(leaderboardWindow, bg="wheat")
	forthFrame.pack()
	forthLabel = Label(forthFrame, text="Jack", bg="wheat")
	forthLabel.pack(side = LEFT)

	fbFrame = Frame(leaderboardWindow)
	fbFrame.pack()
	fbButton = Button(fbFrame, text="Post to Facebook")
	fbButton.pack(side = LEFT)
	fbButton.configure(command=postToFB)

	fifthFrame = Frame(leaderboardWindow)
	fifthFrame.pack()
	fifthLabel = Label(fifthFrame, text="")
	fifthLabel.pack(side = LEFT)

	leaderboardWindow.add(leaderboardFrame)
	leaderboardWindow.add(fstFrame)
	leaderboardWindow.add(sndFrame)
	leaderboardWindow.add(thirdFrame)
	leaderboardWindow.add(forthFrame)
	leaderboardWindow.add(fbFrame)
	leaderboardWindow.add(fifthFrame)

userStatusVar = StringVar()
userStatusVar.set("")

userShotVar = StringVar()
userShotVar.set("You didn't hit the pad yet")

userPunchEffectivenessVar = StringVar()
userPunchEffectivenessVar.set("")

userPunchTypeVar = StringVar()
userPunchTypeVar.set("")

userHitsPerMinVar = IntVar()
userHitsPerMinVar.set(0)

userNumHitsVar = IntVar()
userNumHitsVar.set(0)

def createPlayerStatsGrid(mainWindow) :
	## LEFT WINDOW
	leftWindow = PanedWindow(mainWindow, orient=VERTICAL)
	mainWindow.add(leftWindow)

	#TOP LEFT
	tlWindow = PanedWindow(leftWindow, orient=VERTICAL, bg="lightblue")
	leftWindow.add(tlWindow)

	tlFstFrame = Frame(leftWindow, bg="lightblue")
	tlFstFrame.pack()
	tlNameLbl = Label(tlFstFrame, text="Gishan", bg="lightblue", font = "Helvetica 14 bold")
	tlNameLbl.pack(side = LEFT)
	tlLiveLabel = Label(tlFstFrame, textvariable=userStatusVar, bg="lightblue", font = "Helvetica 12 bold", fg="green")
	tlLiveLabel.pack(side = RIGHT)


	tlSndFrame = Frame(leftWindow, bg="lightblue")
	tlSndFrame.pack( side = BOTTOM)
	tlHitsLbl = Label(tlSndFrame, text="Number of Hits (Today's Target is 200 Hits): ", bg="lightblue")
	tlHitsLbl.pack( side = LEFT )
	tlHitsValLbl = Label(tlSndFrame, textvariable=userNumHitsVar, bg="lightblue")
	tlHitsValLbl.pack( side = RIGHT )

	tlThdFrame = Frame(leftWindow, bg="lightblue")
	tlThdFrame.pack( side = BOTTOM)
	tlHitsRateLbl = Label(tlThdFrame, text="Hits per Minute: ", bg="lightblue")
	tlHitsRateLbl.pack( side = LEFT )
	tlHitsRateValLbl = Label(tlThdFrame, textvariable=userHitsPerMinVar, bg="lightblue")
	tlHitsRateValLbl.pack( side = RIGHT )

	tlFrthFrame = Frame(leftWindow, bg="lightblue")
	tlFrthFrame.pack( side = BOTTOM)
	tlPunchTypeLbl = Label(tlFrthFrame, text="Punch Type: ", bg="lightblue")
	tlPunchTypeLbl.pack( side = LEFT )
	tlPunchTypeValLbl = Label(tlFrthFrame, textvariable=userPunchTypeVar, bg="lightblue")
	tlPunchTypeValLbl.pack( side = RIGHT )

	tlFifthFrame = Frame(leftWindow, bg="lightblue")
	tlFifthFrame.pack( side = BOTTOM)
	tlPunchEffLbl = Label(tlFifthFrame, text="Punch Effectiveness: ", bg="lightblue")
	tlPunchEffLbl.pack( side = LEFT )
	tlPunchEffValLbl = Label(tlFifthFrame, textvariable=userPunchEffectivenessVar, bg="lightblue")
	tlPunchEffValLbl.pack( side = RIGHT )

	tlSixthFrame = Frame(leftWindow, bg="lightblue")
	tlSixthFrame.pack( side = BOTTOM)
	tlStatusLbl = Label(tlSixthFrame, textvariable=userShotVar, bg="lightblue", font = "Helvetica 14 bold", justify=LEFT)
	tlStatusLbl.pack( side = LEFT )

	tlWindow.add(tlFstFrame)
	tlWindow.add(tlSndFrame)
	tlWindow.add(tlThdFrame)
	tlWindow.add(tlFrthFrame)
	tlWindow.add(tlFifthFrame)
	tlWindow.add(tlSixthFrame)

	#BOTTOM LEFT
	blWindow = PanedWindow(leftWindow, orient=VERTICAL, bg="Wheat")
	leftWindow.add(blWindow)

	blFstFrame = Frame(leftWindow, bg="Wheat")
	blFstFrame.pack()
	blNameLbl = Label(blFstFrame, text="Jack", bg="Wheat", font = "Helvetica 14 bold")
	blNameLbl.pack(side = LEFT)
	blLiveLabel = Label(blFstFrame, text="", bg="Wheat", font = "Helvetica 12 bold", fg="Orange Red")
	blLiveLabel.pack(side = RIGHT)

	blSndFrame = Frame(leftWindow, bg="Wheat")
	blSndFrame.pack( side = BOTTOM)
	blHitsLbl = Label(blSndFrame, text="Number of Hits (Today's Target is 200 Hits): ", bg="Wheat")
	blHitsLbl.pack( side = LEFT )
	blHitsValLbl = Label(blSndFrame, text="0", bg="Wheat")
	blHitsValLbl.pack( side = RIGHT )

	blThdFrame = Frame(leftWindow, bg="Wheat")
	blThdFrame.pack( side = BOTTOM)
	blHitsRateLbl = Label(blThdFrame, text="Hits per Minute: ", bg="Wheat")
	blHitsRateLbl.pack( side = LEFT )
	blHitsRateValLbl = Label(blThdFrame, text="0", bg="Wheat")
	blHitsRateValLbl.pack( side = RIGHT )

	blFrthFrame = Frame(leftWindow, bg="Wheat")
	blFrthFrame.pack( side = BOTTOM)
	blPunchTypeLbl = Label(blFrthFrame, text="Punch Type: ", bg="Wheat")
	blPunchTypeLbl.pack( side = LEFT )
	blPunchTypeValLbl = Label(blFrthFrame, text="", bg="Wheat")
	blPunchTypeValLbl.pack( side = RIGHT )

	blFifthFrame = Frame(leftWindow, bg="Wheat")
	blFifthFrame.pack( side = BOTTOM)
	blPunchEffLbl = Label(blFifthFrame, text="Punch Effectiveness: ", bg="Wheat")
	blPunchEffLbl.pack( side = LEFT )
	blPunchEffValLbl = Label(blFifthFrame, text="", bg="Wheat")
	blPunchEffValLbl.pack( side = RIGHT )

	blSixthFrame = Frame(leftWindow, bg="Wheat")
	blSixthFrame.pack( side = BOTTOM)
	blStatusLbl = Label(blSixthFrame, text="You didn't hit the pad yet", bg="Wheat", font = "Helvetica 14 bold", justify=LEFT)
	blStatusLbl.pack( side = LEFT )

	blWindow.add(blFstFrame)
	blWindow.add(blSndFrame)
	blWindow.add(blThdFrame)
	blWindow.add(blFrthFrame)
	blWindow.add(blFifthFrame)
	blWindow.add(blSixthFrame)

	##RIGHT WINDOW
	rightWindow = PanedWindow(mainWindow, orient=VERTICAL)
	mainWindow.add(rightWindow)

	#TOP RIGHT
	trWindow = PanedWindow(rightWindow, orient=VERTICAL, bg="pink")
	rightWindow.add(trWindow)

	trFstFrame = Frame(rightWindow, bg="pink")
	trFstFrame.pack()
	trNameLbl = Label(trFstFrame, text="Ruvini", bg="pink", font = "Helvetica 14 bold")
	trNameLbl.pack(side = LEFT)
	trLiveLabel = Label(trFstFrame, text="", bg="pink", font = "Helvetica 12 bold", fg="Orange Red")
	trLiveLabel.pack(side = RIGHT)

	trSndFrame = Frame(rightWindow, bg="pink")
	trSndFrame.pack( side = BOTTOM)
	trHitsLbl = Label(trSndFrame, text="Number of Hits (Today's Target is 200 Hits): ", bg="pink")
	trHitsLbl.pack( side = LEFT )
	trHitsValLbl = Label(trSndFrame, text="0", bg="pink")
	trHitsValLbl.pack( side = RIGHT )

	trThdFrame = Frame(rightWindow, bg="pink")
	trThdFrame.pack( side = BOTTOM)
	trHitsRateLbl = Label(trThdFrame, text="Hits per Minute: ", bg="pink")
	trHitsRateLbl.pack( side = LEFT )
	trHitsRateValLbl = Label(trThdFrame, text="0", bg="pink")
	trHitsRateValLbl.pack( side = RIGHT )

	trFrthFrame = Frame(rightWindow, bg="pink")
	trFrthFrame.pack( side = BOTTOM)
	trPunchTypeLbl = Label(trFrthFrame, text="Punch Type: ", bg="pink")
	trPunchTypeLbl.pack( side = LEFT )
	trPunchTypeValLbl = Label(trFrthFrame, text="", bg="pink")
	trPunchTypeValLbl.pack( side = RIGHT )

	trFifthFrame = Frame(rightWindow, bg="pink")
	trFifthFrame.pack( side = BOTTOM)
	trPunchEffLbl = Label(trFifthFrame, text="Punch Effectiveness: ", bg="pink")
	trPunchEffLbl.pack( side = LEFT )
	trPunchEffValLbl = Label(trFifthFrame, text="", bg="pink")
	trPunchEffValLbl.pack( side = RIGHT )

	trSixthFrame = Frame(rightWindow, bg="pink")
	trSixthFrame.pack( side = BOTTOM)
	trStatusLbl = Label(trSixthFrame, text="You didn't hit the pad yet", bg="pink", font = "Helvetica 14 bold", justify=LEFT)
	trStatusLbl.pack( side = LEFT )

	trWindow.add(trFstFrame)
	trWindow.add(trSndFrame)
	trWindow.add(trThdFrame)
	trWindow.add(trFrthFrame)
	trWindow.add(trFifthFrame)
	trWindow.add(trSixthFrame)

	#BOTTOM RIGHT
	brWindow = PanedWindow(rightWindow, orient=VERTICAL, bg="Thistle")
	rightWindow.add(brWindow)

	brFstFrame = Frame(rightWindow, bg="Thistle")
	brFstFrame.pack()
	brNameLbl = Label(brFstFrame, text="Michael", bg="Thistle", font = "Helvetica 14 bold")
	brNameLbl.pack(side = LEFT)
	brLiveLabel = Label(brFstFrame, text="", bg="Thistle", font = "Helvetica 12 bold", fg="Orange Red")
	brLiveLabel.pack(side = RIGHT)

	brSndFrame = Frame(rightWindow, bg="Thistle")
	brSndFrame.pack( side = BOTTOM)
	brHitsLbl = Label(brSndFrame, text="Number of Hits (Today's Target is 200 Hits): ", bg="Thistle")
	brHitsLbl.pack( side = LEFT )
	brHitsValLbl = Label(brSndFrame, text="0", bg="Thistle")
	brHitsValLbl.pack( side = RIGHT )

	brThdFrame = Frame(rightWindow, bg="Thistle")
	brThdFrame.pack( side = BOTTOM)
	brHitsRateLbl = Label(brThdFrame, text="Hits per Minute: ", bg="Thistle")
	brHitsRateLbl.pack( side = LEFT )
	brHitsRateValLbl = Label(brThdFrame, text="0", bg="Thistle")
	brHitsRateValLbl.pack( side = RIGHT )

	brFrthFrame = Frame(rightWindow, bg="Thistle")
	brFrthFrame.pack( side = BOTTOM)
	brPunchTypeLbl = Label(brFrthFrame, text="Punch Type: ", bg="Thistle")
	brPunchTypeLbl.pack( side = LEFT )
	brPunchTypeValLbl = Label(brFrthFrame, text="", bg="Thistle")
	brPunchTypeValLbl.pack( side = RIGHT )

	brFifthFrame = Frame(rightWindow, bg="Thistle")
	brFifthFrame.pack( side = BOTTOM)
	brPunchEffLbl = Label(brFifthFrame, text="Punch Effectiveness: ", bg="Thistle")
	brPunchEffLbl.pack( side = LEFT )
	brPunchEffValLbl = Label(brFifthFrame, text="", bg="Thistle")
	brPunchEffValLbl.pack( side = RIGHT )

	brSixthFrame = Frame(rightWindow, bg="Thistle")
	brSixthFrame.pack( side = BOTTOM)
	brStatusLbl = Label(brSixthFrame, text="You didn't hit the pad yet", bg="Thistle", font = "Helvetica 14 bold", justify=LEFT)
	brStatusLbl.pack( side = LEFT )
	
	brWindow.add(brFstFrame)
	brWindow.add(brSndFrame)
	brWindow.add(brThdFrame)
	brWindow.add(brFrthFrame)
	brWindow.add(brFifthFrame)
	brWindow.add(brSixthFrame)

statusVar = StringVar()
statusVar.set("Connect the sensors to the PI and press \'Start Training\' button to begin")

def createBottomMenu(rootWindow) :
	statusWindow = PanedWindow(rootWindow)
	statusWindow.pack(fill=Y, expand=1)

	statusLbl = Label(statusWindow, textvariable=statusVar, font="Helvetica 14")
	statusLbl.pack()

	startButton = Button(statusWindow, text="Start Training")
	startButton.pack()
	startButton.configure(command=startTraining)

	quitButton = Button(statusWindow, text="Quit")
	quitButton.pack()

latestHitHardness=20
def detectedPunch(speed) :
        value=speed * latestHitHardness
        if (value > 1):
	      userPunchEffectivenessVar.set("Good")
	elif (value > 0.5):
		userPunchEffectivenessVar.set("Average")
	else:
		userPunchEffectivenessVar.set("Low")
	
startTime=0
def showHitsPerMin():
	hitsPerMin=userNumHitsVar.get()/ ((time.time()-startTime)/60)
	userHitsPerMinVar.set(hitsPerMin)

def hit(isDetected, hardness):
	if isDetected:
                latestHitHardness=hardness
		userShotVar.set("HIT!")
		userNumHitsVar.set(userNumHitsVar.get()+1)
		showHitsPerMin()
	else:
		if userNumHitsVar.get() > 0:
			userShotVar.set("")

def startTraining() :
	startTime=time.time()

	def validated6Axis(success):
		if success:
			userStatusVar.set("LIVE")
			statusVar.set("Sound and accelaration sensors are live. Please start your training now")
			hitdetection.detectHits(hit)
			punchdetection.detectPunches(detectedPunch)
		else:
			statusVar.set("Could not connect to the accelarometer in your glove. Please check this sensor.")
				
	def soundCalibrated(success):
		if success:
			punchdetection.validate6Axis(validated6Axis)
				
	statusVar.set("Calibrating sound sensor in the boxing pad to the environment. Please wait 20 seconds...")
	hitdetection.calibrateSoundSensor(soundCalibrated)
	
def postToFB() : 
	from easygui import msgbox
	msgbox("Leaderboard was posted to your\ngym\'s facebook page successfully!", title="Post to Facebook")


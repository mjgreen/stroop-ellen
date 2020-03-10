#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.1),
    on March 10, 2020, at 13:36
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock, parallel, microphone
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.1'
expName = 'stroop'  # from the Builder filename that created this script
expInfo = {'session': '01', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mgree\\gits\\stroop-ellen\\stroop_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
wavDirName = filename + '_wav'
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName)  # to hold .wav files

# Setup the Window
win = visual.Window(
    size=[800, 600], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='e330', color='black', colorSpace='dkl',
    blendMode='avg', useFBO=True, 
    units='norm')

# Enable sound input/output:
microphone.switchOn()
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text='OK. Ready for the real thing?\n\nRemember, ignore the word itself; \njust say the name of the colour of the ink\n\n(Esc will quit)\n\nPress the spacebar to continue',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
spaceToStart = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fovealWord = visual.TextStim(win=win, name='fovealWord',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
parafovealWord = visual.TextStim(win=win, name='parafovealWord',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
voicekey = keyboard.Keyboard()
p_port = parallel.ParallelPort(address='0x0378')

# Initialize components for Routine "isi"
isiClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruct"-------
continueRoutine = True
# update component parameters for each repeat
spaceToStart.keys = []
spaceToStart.rt = []
_spaceToStart_allKeys = []
# keep track of which components have finished
instructComponents = [instrText, spaceToStart]
for thisComponent in instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *spaceToStart* updates
    waitOnFlip = False
    if spaceToStart.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        spaceToStart.frameNStart = frameN  # exact frame index
        spaceToStart.tStart = t  # local t and not account for scr refresh
        spaceToStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spaceToStart, 'tStartRefresh')  # time at next scr refresh
        spaceToStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(spaceToStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(spaceToStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if spaceToStart.status == STARTED and not waitOnFlip:
        theseKeys = spaceToStart.getKeys(keyList=['space'], waitRelease=False)
        _spaceToStart_allKeys.extend(theseKeys)
        if len(_spaceToStart_allKeys):
            spaceToStart.keys = _spaceToStart_allKeys[-1].name  # just the last key pressed
            spaceToStart.rt = _spaceToStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes10trials.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    fovealWord.setColor(FovCol, colorSpace='rgb')
    fovealWord.setText(FovWord)
    parafovealWord.setColor(ParaCol, colorSpace='rgb')
    parafovealWord.setPos(ParaPos)
    parafovealWord.setText(ParaWord)
    voicekey.keys = []
    voicekey.rt = []
    _voicekey_allKeys = []
    mic = microphone.AdvAudioCapture(name='mic', saveDir=wavDirName, stereo=False, chnl=0)
    # keep track of which components have finished
    trialComponents = [fovealWord, parafovealWord, voicekey, p_port, mic]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fovealWord* updates
        if fovealWord.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fovealWord.frameNStart = frameN  # exact frame index
            fovealWord.tStart = t  # local t and not account for scr refresh
            fovealWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fovealWord, 'tStartRefresh')  # time at next scr refresh
            fovealWord.setAutoDraw(True)
        if fovealWord.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fovealWord.tStop = t  # not accounting for scr refresh
                fovealWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fovealWord, 'tStopRefresh')  # time at next scr refresh
                fovealWord.setAutoDraw(False)
        
        # *parafovealWord* updates
        if parafovealWord.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            parafovealWord.frameNStart = frameN  # exact frame index
            parafovealWord.tStart = t  # local t and not account for scr refresh
            parafovealWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(parafovealWord, 'tStartRefresh')  # time at next scr refresh
            parafovealWord.setAutoDraw(True)
        if parafovealWord.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2.0-frameTolerance:
                # keep track of stop time/frame for later
                parafovealWord.tStop = t  # not accounting for scr refresh
                parafovealWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(parafovealWord, 'tStopRefresh')  # time at next scr refresh
                parafovealWord.setAutoDraw(False)
        
        # *voicekey* updates
        waitOnFlip = False
        if voicekey.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            voicekey.frameNStart = frameN  # exact frame index
            voicekey.tStart = t  # local t and not account for scr refresh
            voicekey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(voicekey, 'tStartRefresh')  # time at next scr refresh
            voicekey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(voicekey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(voicekey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if voicekey.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2.0-frameTolerance:
                # keep track of stop time/frame for later
                voicekey.tStop = t  # not accounting for scr refresh
                voicekey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(voicekey, 'tStopRefresh')  # time at next scr refresh
                voicekey.status = FINISHED
        if voicekey.status == STARTED and not waitOnFlip:
            theseKeys = voicekey.getKeys(keyList=['0'], waitRelease=False)
            _voicekey_allKeys.extend(theseKeys)
            if len(_voicekey_allKeys):
                voicekey.keys = _voicekey_allKeys[0].name  # just the first key pressed
                voicekey.rt = _voicekey_allKeys[0].rt
        # *p_port* updates
        if p_port.status == NOT_STARTED and len(voicekey.keys) > 0 and frameN <=148:
            # keep track of start time/frame for later
            p_port.frameNStart = frameN  # exact frame index
            p_port.tStart = t  # local t and not account for scr refresh
            p_port.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
            p_port.status = STARTED
            win.callOnFlip(p_port.setData, int(Trigger))
        if p_port.status == STARTED:
            if frameN >= (p_port.frameNStart + 2):
                # keep track of stop time/frame for later
                p_port.tStop = t  # not accounting for scr refresh
                p_port.frameNStop = frameN  # exact frame index
                win.timeOnFlip(p_port, 'tStopRefresh')  # time at next scr refresh
                p_port.status = FINISHED
                win.callOnFlip(p_port.setData, int(0))
        
        # *mic* updates
        if mic.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mic.frameNStart = frameN  # exact frame index
            mic.tStart = t  # local t and not account for scr refresh
            mic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mic, 'tStartRefresh')  # time at next scr refresh
            mic.status = STARTED
            mic.record(sec=2.0, block=False)  # start the recording thread
        
        if mic.status == STARTED and not mic.recorder.running:
            mic.status = FINISHED
        # if there is no voicekey response, the p_port item will prevent the trial ending
        if frameN >= 120: # 120 for 2 seconds, plus 2 frames in case the parallel port got triggered at the end of the visibility of the words
            continueRoutine = False
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if voicekey.keys in ['', [], None]:  # No response was made
        voicekey.keys = None
    trials.addData('voicekey.keys',voicekey.keys)
    if voicekey.keys != None:  # we had a response
        trials.addData('voicekey.rt', voicekey.rt)
    trials.addData('voicekey.started', voicekey.tStartRefresh)
    trials.addData('voicekey.stopped', voicekey.tStopRefresh)
    if p_port.status == STARTED:
        win.callOnFlip(p_port.setData, int(0))
    trials.addData('p_port.started', p_port.tStartRefresh)
    trials.addData('p_port.stopped', p_port.tStopRefresh)
    # mic stop & responses
    mic.stop()  # sometimes helpful
    if not mic.savedFile:
        mic.savedFile = None
    # store data for trials (TrialHandler)
    trials.addData('mic.filename', mic.savedFile)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "isi"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    isiComponents = [ISI]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "isi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "isi"-------
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('ISI.started', ISI.tStart)
    trials.addData('ISI.stopped', ISI.tStop)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksText.started', thanksText.tStartRefresh)
thisExp.addData('thanksText.stopped', thanksText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

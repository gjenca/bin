#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eyeD3
import glob
import cddbid

durations=[]
durations_str=[]
fnms=glob.glob("*.mp3")
fnms.sort()
print fnms
for fnm in fnms:
    mp3= eyeD3.Mp3AudioFile(fnm)
    durations.append(mp3.getPlayTime())
    durations_str.append(mp3.getPlayTimeString())
print durations_str
print cddbid.discid(durations)



durations=[]
times=['12:04','10:51','6:14','4:56','5:33']
for time in times:
    min_sec=time.split(':')
    sec=int(min_sec[0])*60+int(min_sec[1])
    durations.append(sec)

print cddbid.discid(durations)

    

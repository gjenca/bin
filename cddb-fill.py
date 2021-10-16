#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eyeD3
import glob
import CDDB

def cddbsum(n):

    ret=0
    while n>0:
        ret+=n%10
        n/=10
    return ret

def disc_ids(durations):
    
    n=sum(cddbsum(duration) for duration in durations)
    t=sum(durations)
    ret=[]
    for n0 in range(n-3,n+3):
        for t0 in range(t-3,t+3):
            ret.append("%08x" % (((n0 % 0xff) << 24) | (t0 << 8) | len(durations),))
    return ret

durations=[]
times=['12:04','10:51','6:14','4:56','5:33']
for time in times:
    min_sec=time.split(':')
    sec=int(min_sec[0])*60+int(min_sec[1])
    durations.append(sec)

for disc_id in disc_ids(durations):
    (query_status, query_info) = CDDB.query(int(disc_id,16))
    print query_status,disc_id


    

#!/usr/bin/python2
import sys
import re

class FlattenedBracket:

    def __init__(self,bracket):
        
        self.idx_open=bracket.idx_open
        self.idx_close=bracket.idx_close
        self.depth=bracket.depth()

class Bracket:

    def __init__(self,idx_open,level):

        self.idx_open=idx_open
        self.is_open=True
        self.level=level
        self.depth_cache=None
        self.bracketlist=BracketList(level=self.level+1)

    def open(self,idx_open):
        
        self.bracketlist.open(idx_open)

    def close(self,idx_close):

        ret=self.bracketlist.close(idx_close)
        if ret:
            return True
        elif self.is_open:
            self.idx_close=idx_close
            self.is_open=False
            return True
        else:
            return False

    def depth(self):

        if self.depth_cache is None:
            self.depth_cache=self.bracketlist.depth()+1
        return self.depth_cache

    def flatten(self):

        if self.is_open:
            raise Exception,"Attempt to flatten an open bracket"
        
        return [FlattenedBracket(self)]+self.bracketlist.flatten()

    def __repr__(self):

        if self.is_open:
            return r"([%d,%d]%s" % (self.idx_open,self.depth(),repr(self.bracketlist))
        else:
            return r"([%d,%d]%s[%d])" % (self.idx_open,self.depth(),repr(self.bracketlist),self.idx_close)


class BracketList:

    def __init__(self,level=0):
        
        self.brackets=[]
        self.level=level

    def open(self,idx_open):
        
        for bracket in self.brackets:
            if bracket.is_open:
                bracket.open(idx_open)
                break
        else:
            self.brackets.append(Bracket(idx_open,self.level))
    
    def close(self,idx_close):

        for bracket in self.brackets:
            if bracket.is_open:
                bracket.close(idx_close)
                return True
        else:
            return False

    def depth(self):

        ret=0
        for bracket in self.brackets:
            if (bracket.depth()>ret):
                ret=bracket.depth()
        return ret

    def __repr__(self):
        
        ret=""
        for bracket in self.brackets:
            ret+=repr(bracket)
        return ret

    def flatten(self):

        ret=[]
        for bracket in self.brackets:
            ret=ret+bracket.flatten()
        return ret

def string_to_bracketlist(s):
    
    bl=BracketList()
    for i in range(len(s)):
        if s[i] in "([":
            bl.open(i)
        elif s[i] in ")]":
            bl.close(i)
    return bl

bigprefixes=["","big","big","Big","Big"]

def bigprefix(depth,lr):

    idx=min(len(bigprefixes)-1,depth-1)
    if bigprefixes[idx]=="":
        return ""
    if idx>=len(bigprefixes):
        idx=(-1)
    return "\\"+bigprefixes[idx]+lr

s=""
for line in sys.stdin:
	s+=line
s=re.sub(r"\\[bB]ig[lr]","",s)
root=string_to_bracketlist(s)
s_out=""
fb_list=root.flatten()
for i in range(len(s)):
    for fb in fb_list:
        if fb.idx_open==i:
            s_out+=bigprefix(fb.depth,"l")+s[i]
            break
        if fb.idx_close==i:
            s_out+=bigprefix(fb.depth,"r")+s[i]
            break
    else:
        s_out+=s[i]
sys.stdout.write(s_out)


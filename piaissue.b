#!/bin/bash

PIADIR=~/vyuka/l2015/pia/issues/
HGRC=`hg root`/.hg/hgrc
BBUSER=`grep ^default $HGRC 2>/dev/null | cut -f 4 -d/` 
mkdir -p $PIADIR/$BBUSER
ISSUES_NUM=`find  $PIADIR/$BBUSER -type f -name 'issue*.md'| wc -l`
let ISSUE_NUM=ISSUES_NUM+1
NEW_ISSUE="$PIADIR/$BBUSER/issue$ISSUE_NUM.md"
TITLE="Pripomienka $ISSUE_NUM k projektu PIA"
bbissue -t "$TITLE" -T ~/vyuka/l2015/pia/template -f "$NEW_ISSUE"
echo User: $BBUSER
echo Saved in $NEW_ISSUE

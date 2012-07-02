#!/bin/sh

###########################################################
#
# Update the project's version number
#
###########################################################

ROOT='/home/tig/shenmartav/shenmartav'
TEMPLATE='templates/base.html'

cd ${ROOT}
commit=`git log --max-count=1 | head -1 | cut -d ' ' -f 2`
cdate=`git log --max-count=1 | head -3 | tail -1 | cut -d ' ' -f 4-`
search='<div id="commit">.*</div>'
replace="<div id=\"commit\">COMMIT ${commit}, DATE ${cdate}</div>"
sed --in-place "s#${search}#${replace}#" ${TEMPLATE}

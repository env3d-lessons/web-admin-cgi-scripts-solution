#!/bin/bash

echo 'content-type: text/plain'
echo
if [[ "$1" == "" ]]
then
    echo "You need to provide an actor"
    exit 1
fi

NUM_ACTORS=$(grep -E "${1}.*(actor|actress)" ./name.basics.tsv | wc -l)
if [[ NUM_ACTORS -ne 1 ]]
then
    echo "There are ${NUM_ACTORS} with the name ${1}, we expect only one."
    exit 1
fi

echo "Actor $1 is known for the following titles:"

TITLES=$(grep -E "${1}.*(actor|actress)" ./name.basics.tsv | awk -F '\t' '{print $6}' | sed -r 's/,/|/g')
#echo $TITLES
MOVIE=$(grep -E "^($TITLES).*movie" ./title.basics.tsv | awk -F '\t' '{print "   "$3}')
if [[ "$MOVIE" != "" ]]
then
    echo "$MOVIE"
fi



#!/bin/bash

echo 'content-type: text/html'
echo

if [[ "$1" == "" ]]
then
    echo "You need to provide an actor"
    exit 1
fi

NUM_ACTORS=$(grep -E "${1}.*(actor|actress)" ./name.basics.tsv | wc -l)

if [[ NUM_ACTORS -ne 1 ]]
then
    echo "There are ${NUM_ACTORS} with the  ${1}, we expect only one."
    exit 1
fi

ID=$(grep -E "${1}.*(actor|actress)" ./name.basics.tsv | cut -f 1)
IMAGE=$(curl -A 'abcde' -s "https://www.imdb.com/name/$ID/" | grep -oP '"image":(.*)' | awk -F '"' '{print $4}')
echo "<img src='$IMAGE' width=200>"
echo "<h1>Actor $1 is known for the following titles:</h1>"
echo "<ol>"
TITLES=$(grep -E "${1}.*(actor|actress)" ./name.basics.tsv | awk -F '\t' '{print $6}' | sed -r 's/,/|/g')
MOVIE=$(grep -E "^($TITLES).*movie" ./title.basics.tsv | awk -F '\t' '{print "<li>"$3"</li>"}')
if [[ "$MOVIE" != "" ]]
then
    echo "$MOVIE"
fi
echo "</ol>"



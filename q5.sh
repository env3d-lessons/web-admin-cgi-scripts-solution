#!/bin/bash

echo "Content-type: text/html"
echo

if [[ "$1" == "" ]]
then
    echo "You need to provide a search term"
    exit 1
fi

#curl -s -H 'user-agent: asdf' https://www.bing.com/search?q=$1
curl -s https://www.bing.com/search?q=$1 


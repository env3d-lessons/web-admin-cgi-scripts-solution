#!/bin/bash

echo "Content-Type: text/plain"
echo 

if [[ "$1" == "" ]]
then
    echo "You need to provide the number of slugs to display"
    exit 1
fi

echo "Top $1 slugs on time.com:"
echo
curl -s "https://time.com/wp-json/wp/v2/posts/?per_page=${1}&context=embed" \
    | json_pp \
    | grep 'slug' \
    | cut -f 4 -d '"' \
    | tr '-' ' '

# curl -s -A 'asdf' https://old.reddit.com/r/${1}.json | json_reformat | grep '"title"' | sed -r 's/.*\"title\"\s*:\s*\"(.*)\",/\1/'

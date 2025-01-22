#!/bin/bash

echo "Content-Type: text/plain"
echo 

echo "Current slugs on the time.com:"
echo

curl -s 'https://time.com/wp-json/wp/v2/posts/?per_page=10&context=embed' \
    | json_pp \
    | grep 'slug' \
    | cut -f 4 -d '"' \
    | tr '-' ' ' 
#curl -s -A 'asdf' https://old.reddit.com/.json | json_reformat | grep '"title"' | sed -r 's/.*\"title\"\s*:\s*\"(.*)\",/\1/'

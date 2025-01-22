#!/bin/bash

echo "Content-Type: text/plain"
echo
Joke=$(curl -s https://icanhazdadjoke.com/)
echo "I have a joke for you: $Joke"

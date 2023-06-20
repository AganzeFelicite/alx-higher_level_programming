#!/bin/bash
#this script takes in a URL, sends a GET request to the URL, and displays the methods present 
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '

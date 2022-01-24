#!/bin/bash

#lynx -dump https://yababay.medium.com | ./links.py |  while read -a arr
cat medium.links | ./links.py |  while read -a arr
do 
    wget -O- ${arr[0]} | lynx -stdin -dump > ../.tmp/${arr[1]}
done

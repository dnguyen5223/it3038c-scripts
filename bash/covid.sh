#!/bin/bash

#This script will show covid data

#set positive value to variable
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)

POSITIVE=$(echo $DATA | jq '.[0].positive')

DEATH=$(echo $DATA | jq '.[0].death')

NEGATIVE=$(echo $DATA | jq '.[0].negative')

STATES=$(echo $DATA | jq '.[0].states')

#Set data variable
TODAY=$(date)

#read it out
echo "On $TODAY, there were $POSITIVE postive covid cases, with $DEATH deaths, $NEGATIVE negative cases, and in $STATES states"

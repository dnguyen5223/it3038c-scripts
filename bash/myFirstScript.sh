#!/bin/bash 

# yellow
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working DIr: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME

a=$(ip a | grep 'noprefixroute dynamic ens192' | awk '{print $2}')
echo MY IP is $a

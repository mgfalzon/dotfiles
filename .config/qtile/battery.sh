#!/bin/bash

while true
do
BAT=$(acpi -b | grep -o [0-9][0-9])
if [ $BAT -lt 20 ];
then
  notify-send 'Low Battery'
fi
sleep 15m
done

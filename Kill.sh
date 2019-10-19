#!/bin/bash
/bin/ps axf -o "pid %cpu" | awk '{if($2>=30.0) print $1}' | while read procid
do
kill -9 $procid
done

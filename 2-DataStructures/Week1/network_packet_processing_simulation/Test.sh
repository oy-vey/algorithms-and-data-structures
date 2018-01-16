#!/bin/bash
FILES=./tests/*

clear
for f in $FILES
do

  if [[ $f == *".a"* ]]
  then
    Right=$( cat $f)
    #echo $Right
    if [[ $Right == $Sol ]]
    then
      echo "Passed!"
    else
      echo "Correct answer: $Right, Your answer: $Sol"
      #echo "Wrong!"
    fi
  else
    echo "_______________________"
    start=$SECONDS
    echo "Processing $f file..."
    Sol=$( cat $f | python3 process_packages.py)
    duration=$(( SECONDS - start ))
    echo "Time:" $duration
  fi

done

#!/bin/bash
FILES=./tests/*

clear
for f in $FILES
do

  if [[ $f == *"a"* ]]
  then
    Right=$( cat $f)
    #echo $Right
    if [[ $Right == $Sol ]]
    then
      echo "Passed!"
    else
      echo "Correct answer: $Right, Your answer: $Sol"
      echo
    fi
  else
    echo "_______________________"
    start=$SECONDS
    echo "Processing $f file..."
    Sol=$( cat $f | python tree-height.py)
    duration=$(( SECONDS - start ))
    echo "Time:" $duration
  fi

done

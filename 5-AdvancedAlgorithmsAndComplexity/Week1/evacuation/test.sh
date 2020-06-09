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
    echo "Processing $f file..."
    Sol=$( cat $f | python3 evacuation.py)
    #echo $Sol
  fi

done


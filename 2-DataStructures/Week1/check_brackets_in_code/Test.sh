#!/bin/bash
FILES=./tests/*

clear
for f in $FILES
do

  if [[ $f == *"a"* ]]
  then
    echo "Right answer:"
    cat $f
  else
    echo "_______________________"
    echo "Processing $f file..."
    echo "Result:"
    cat $f | python check_brackets.py
  fi

done

#!/bin/bash

brain() {
 	local file="${1:-shell}"
	if [ $file != "shell" ]; then
		python brainf.py $file
	else
		echo There is no shell yet
	fi
}

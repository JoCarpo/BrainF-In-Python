#!/bin/bash

brain() {
 	local file="${1:-shell}"
	if [ $file != "shell" ]; then
		dir=$(readlink -f $file)
		python ~/.brainf/main.py $dir
	else
		echo There is no shell yet
	fi
}

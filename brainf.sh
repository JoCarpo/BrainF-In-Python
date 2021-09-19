#!/bin/bash

brain() {
 	local file="${1:-shell}"
	if [ $file != "shell" ]; then
		python brainf.py $file
	else
		python shell.py
	fi
}

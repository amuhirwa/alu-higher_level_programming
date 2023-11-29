#!/bin/bash
# Displays body of request
x=$(curl -X "GET" -Is $1 | head -1 | grep -c "200")
if (( $x == 1 ))
then
	curl -X "GET" -s $1
fi

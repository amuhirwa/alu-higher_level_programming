#!/bin/bash
# Displays allowed methods
curl -X "OPTIONS" -isL $1 | grep "Allow" | cut -d " " -f 2-

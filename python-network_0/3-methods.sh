#!/bin/bash
# Displays allowed methods
curl -X "OPTIONS" -isL $1 | grep -i "allow" | cut -d " " -f 2

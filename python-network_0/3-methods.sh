#!/bin/bash
# Displays allowed methods
curl -X "OPTIONS" -isL $1 | grep -i "Access-Control-allow-Methods:" | cut -d " " -f 2

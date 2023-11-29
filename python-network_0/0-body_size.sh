#!/bin/bash
# Displays size of body
curl -Is $1 | grep -i "content-length:" | cut -d " " -f 2

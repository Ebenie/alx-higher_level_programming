#!/bin/bash
# This script uses curl to determine HTTP methods accepted by a server
curl -sI "$1" | grep Allow | awk -F': ' '{print $2}'


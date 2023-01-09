#!/bin/bash
function process-killer()
{
echo "What Program You Want to Find and Kill?"
read param
ps -A | grep $param
if ps -A | grep "$param" >/dev/null
then
pkill $param
echo "$param is already killed"
else
echo "$param is not running"
fi
}
process-killer



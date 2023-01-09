#!/bin/bash
function Finding-java()
{
cd ~
read param
if [ -z "$param" ]
then
echo "Harap isi path"
elif [ -d "$param" ] 
then
cd $param
echo "Ada file java pada direktori"
find . -type f -name "*.java"
else
echo "Directory tidak ditemukan"
fi
}
Finding-java

#!/bin/bash

while getopts d:m name
do         
	case $name in          
          d)dopt=$OPTARG;;          
          m)mopt=1;;           
          *)echo "Invalid arg";;        
        esac
done
DT=`date '+%d %b'`

if [[ ! -z $dopt ]]
then     
     DT=`date '+%d %b'  -d "$dopt days"`
     echo "Date is: " ${DT/ */}
fi

if [[ ! -z $mopt ]]
then     
     echo "Month is: " ${DT/* /} 
fi 

shift $(($OPTIND-1))

echo "Welcome, " $1

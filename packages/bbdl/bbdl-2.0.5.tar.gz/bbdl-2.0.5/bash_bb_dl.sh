#!/bin/bash
# This is a simple script that will download all of the BB pages
# and view them offline.
# Author: Q
# Inspired: Tim@TheWheatField
# echo "What date of the BB would you like to read?"
# echo "You will be asked to enter a date in dd-mm-yyyy format."
# echo -en "Please enter the date in dd (i.e. day. e.g. 30 for 30th of the month)."
# read DATE_D
#echo $DATE_D | grep "[^01-31]" > /dev/null 2>&1
#if ["$?" -eq "0" ]; then
	# If the grep found something other than 01-31
	# then its not an integer valid for date (at least for some months?)
#	echo "Sorry, not a valid date number (experimental)"
#fi
# echo -en "Please enter the month in mm. (e.g. If April, enter 04)"
# read DATE_M
#echo $DATE_M | grep "[^01-12]" > /dev/null 2>&1
#if ["$?" -eq "0" ]; then
	# If the grep found something other than 01-12
	# then its not an integer valid for month
#	echo "Sorry, not a valid date number (experimental)"
#fi
# echo -en "Please enter the year in yyyy. (e.g. 2018)"
# read DATE_Y
#echo $DATE_Y | grep "[^2000-2025]" > /dev/null 2>&1
#if ["$?" -eq "0" ]; then
	# If the grep found something other than 2000-2025
	# then its not an integer valid for year
#	echo "Sorry, not a valid date number (experimental)"
#fi
# echo "Checking # of pages in BB of $DATE_D-$DATE_M-$DATE_Y"
#mkdir "BB-$DATE_Y$DATE_M$DATE_D"
#cd "BB-$DATE_Y$DATE_M$DATE_D"
mkdir "BB-$(date +%Y%m%d)"
cd "BB-$(date +%Y%m%d)"
# PAGE=1
# MAX_PAGE=false
# STATUS_CODE=0

# while [ "$MAX_PAGE" != true ]
# do
#	for p in {01..100}
#	do
#		echo "curl "https://epaper.digital.borneobulletin.com.bn/BB/$DATE_Y/$DATE_M/BB$DATE_D$DATE_M$DATE_Y/files/assets/mobile/pages/page00"${p}"_i2.jpg" -s -o /dev/null -w "%{http_code}"" 
#		echo $STATUS_CODE
#		if [ "$STATUS_CODE" = 200];
#		then 
#			expr PAGE++
#		else
#			MAX_PAGE=true
#		fi
#	done
# done

# echo "Max Page is $MAX_PAGE"
# echo "There are $PAGE in $DATE_D-$DATE_M-$DATE_Y"

for i in {01..50}
do
	wget "https://epaper.digital.borneobulletin.com.bn/BB/$(date +%Y)/$(date +%m)/BB$(date +%d%m%Y)/files/assets/mobile/pages/page00"${i}"_i2.jpg"
done

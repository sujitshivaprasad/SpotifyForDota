#!/bin/bash
osascript -e 'set volume 5'
./SpotifyControl
spotify volume 30
#spotify shuffle
temp="Shuffle is now false"
output=$(spotify shuffle)
echo $output
if [ "$output" == "$temp" ]
then
	echo "changed"
	output=$(spotify shuffle)
fi
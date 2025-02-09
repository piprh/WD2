#!/usr/bin/bash
datafile="testin.sdf"

while read company
do
	echo "Processing ${datafile} for ${company}..."
	python3 /localdisk/data/IWD2/DirectedLearning/DL1/manu_split.py ${datafile} ${company} > ${company}.sdf
done < Manufacturer_names

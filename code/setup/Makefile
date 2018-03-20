init:
	mkdir images
	mkdir binaries

setup: 
	if [ ! -d "images" ] ; then mkdir images ; fi ;
	if [ ! -d "binaries" ] ; then mkdir binaries ; fi ;
	pip install -r requirements.txt

clean:
	if [ -d "images" ] ; then rm -r images; echo "rm -r images"; fi;
	if [ -d "binaries" ] ; then rm -r binaries; echo "rm -r binaries"; fi;

run:
	python run.py

test:
	python test.py

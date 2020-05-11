INPUT ?= ./file_1MB.txt
OUTPUT ?= ./output.txt


test:
	python2 receiver.py > $(OUTPUT) & time python2 sender.py < $(INPUT) &
test_clean:
	pkill Python
	rm *.log $(OUTPUT) *.pyc
	python2 receiver.py > $(OUTPUT) & time python2 sender.py < $(INPUT) &
diff:
	diff $(INPUT) $(OUTPUT)
kill:
	pkill Python
clean:
	rm *.log $(OUTPUT) *.pyc

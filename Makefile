category=all
exclude=True

start: exec.sh
	source venv/bin/activate

deactivate:
	source ../deactivate

install: requirements.txt
	pip3 install -r requirements.txt

run:
	python3 main.py -category=$(category) -exclude=$(exclude)

## run:
## 	@echo "Running file!\n"
## 	./venv/bin/python3 main.py
## 


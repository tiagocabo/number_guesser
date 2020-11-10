venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt
	echo venv/bin/activate

clean:
	rm -rf venv
	rm -rf .idea/
	find -iname "*.pyc" -delete


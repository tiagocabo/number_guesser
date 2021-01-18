venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt
	echo venv/bin/activate

clean:
	rm -rf venv
	rm -rf .idea/
	find -iname "*.pyc" -delete

docker_init:
	sudo docker build -t number_guesser .
	sudo docker run -p 8080:8080 --name number_guesser number_guesser

docker_stop:
	echo "deleting existing docker..."
	sudo docker stop number_guesser
	sudo docker rm number_guesser
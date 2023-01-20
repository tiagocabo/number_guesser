
activate_api_venv_macos:
	python -m venv venv_api_macos && export VIRTUAL_ENV=venv_api_macos
	cd ml_api/envs/macos-env && pipenv install
	echo venv_api_macos/bin/activate

activate_api_venv_linux:
	python -m venv venv_api_linux && export VIRTUAL_ENV=venv_api_linux
	cd ml_api/envs/linux && pipenv install
	echo venv_api_linux/bin/activate

api_docker_init:
	sudo docker build -t number_guesser .
	sudo docker run -p 8080:8080 --name number_guesser number_guesser

api_docker_stop:
	echo "deleting existing docker..."
	sudo docker stop number_guesser
	sudo docker rm number_guesser
nest_path = ./real-world/nestjs
spring_path = ./real-world/spring

k6_path = ./k6/real-world/

nest-js:
	echo "starting to test k6 with NestJS"
	docker-compose -f  ${nest_path}/docker-compose.yml up -d --build
	k6 run ${k6_path}/script-nestjs.js

	pip3 install -r ./requirements.txt
	python3 ./collect-data.py

spring:
	echo "starting to test k6 with Spring"

all:
	make nest-js
	make spring


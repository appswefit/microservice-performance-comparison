nest_path = ./real-world/nestjs
spring_path = ./real-world/spring

nest-js:
	echo "starting to test k6 with NestJS"
	docker-compose -f  ${nest_path}/docker-compose.yml up -d

	python3 ./collect-data.py nest-container

spring:
	echo "starting to test k6 with Spring"
	docker-compose -f  ${spring_path}/docker-compose.yml up -d

	python3 ./collect-data.py spring-container

all:
	pip3 install -r ./requirements.txt
	make nest-js
	make spring


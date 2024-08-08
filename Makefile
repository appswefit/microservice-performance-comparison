nest_path = ./nestjs
spring_path = ./spring

nest-js:
	echo "starting to test k6 with NestJS"
	docker-compose -f  ${nest_path}/docker-compose.yml up -d

	python3 ./collect-data.py nest-container

spring-boot:
	echo "starting to test k6 with Spring"
	docker-compose -f  ${spring_path}/docker-compose.yml up -d

	python3 ./collect-data.py spring-container

all:
	python3 -m venv venv && source venv/bin/activate
	pip3 install -r ./requirements.txt
	make nest-js
	make spring-boot


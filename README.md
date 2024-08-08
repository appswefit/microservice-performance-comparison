# Microservice framework performance comparison

Compares two microservice frameworks:

- NestJS (https://nestjs.com/)
- Spring (Boot + Cloud) (https://spring.io/)

Includes two sample applications for all the frameworks:

- Hello World (just returns string "Hello World")
- Universities (returns list of basic info about universities requested with country name, also includes authorization using JWT)

## Running

To measure performance of NestJS implementation of the application run: `make run-nest`, to measure the performance of the Spring-Boot run: `make spring-boot`. To run both: `make all`
This will create Docker containers for all the required services and run them. Then the CPU and Memory values of the containers will be stored and the performance benchmarking will be run using k6 (https://k6.io). After this, there will be files "stats.json" and "html-report-\<framework_name\>-json-1000.html" under the "reports" directory that includes the measured values for each framework.

### Prerequisites

- Docker
- Make
- k6
- Python

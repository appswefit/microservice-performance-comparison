# Microservice framework performance comparison

Compares two microservice frameworks:

- NestJS (https://nestjs.com/)
- Spring (Boot + Cloud) (https://spring.io/)

Includes two sample applications for all the frameworks:

- Hello World (just returns string "Hello World")
- Universities (returns list of basic info about universities requested with country name, also includes authorization using JWT)

## Running

"hello-world" and "real-world" (universities) directories include Makefile files that include the orchestration of the measurements.
For example, to measure performance of NestJS implementation of universities application run: `make run-nest` in "real-world" directory.
This will create Docker containers for all the required services and run them. Then the CPU values of the containers will be stored and the performance benchmarking will be run using k6 (https://k6.io). After that the CPU values will be recorded again, together with total memory usage. Finally the containers will be shut down.
After this, there will be files "cpustats.txt", "memstats.txt" and "k6-summary.json" under the "nestjs" directory that include the measured values.

### Prerequisites

- Docker
- Make
- k6
- Python

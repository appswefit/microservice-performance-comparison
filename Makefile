NESTCOMPOSEFILE = nestjs/docker-compose.yml
NESTOUTPUTCPU = nestjs/cpustats.txt
NESTOUTPUTMEM = nestjs/memstats.txt

SPRINGCOMPOSEFILE = spring/docker-compose.yml
SPRINGOUTPUTCPU = spring/cpustats.txt
SPRINGOUTPUTMEM = spring/memstats.txt

run-nest:

	@echo "Deploying NestJS containers"
	#docker-compose -f $(NESTCOMPOSEFILE) build
	docker-compose -f $(NESTCOMPOSEFILE) up -d

	@touch $(NESTOUTPUTCPU)
	@touch $(NESTOUTPUTMEM)

	# Store cpu usage before running tests
	@echo "before" > $(NESTOUTPUTCPU)
	@cat "/sys/fs/cgroup/cpu,cpuacct/docker/$$(docker-compose -f $(NESTCOMPOSEFILE) ps -q hello-world)/cpuacct.stat" >> $(NESTOUTPUTCPU)

	@echo "Running performance tests"
	k6 run --vus 10 --duration 2s k6/script.js

	# Store total cpu usage after running tests
	@echo "after" >> $(NESTOUTPUTCPU)
	@cat "/sys/fs/cgroup/cpu,cpuacct/docker/$$(docker-compose -f $(NESTCOMPOSEFILE) ps -q hello-world)/cpuacct.stat" >> $(NESTOUTPUTCPU)

	# Store max memory used in bytes
	@cat "/sys/fs/cgroup/memory/docker/$$(docker-compose -f $(NESTCOMPOSEFILE) ps -q hello-world)/memory.max_usage_in_bytes" > $(NESTOUTPUTMEM)

	@echo "Shutting down NestJS containers"
	docker-compose -f $(NESTCOMPOSEFILE) down


run-spring:

	@echo "Deploying Spring containers"
	#docker-compose -f $(SPRINGCOMPOSEFILE) build
	docker-compose -f $(SPRINGCOMPOSEFILE) up -d

	@touch $(SPRINGOUTPUTCPU)
	@touch $(SPRINGOUTPUTMEM)

	# wait for all of the applications to register with Eureka
	@echo "Waiting for application to register with Eureka"
	@sleep 90s

	# Store cpu usage before running tests
	@echo "before" > $(SPRINGOUTPUTCPU)
	@cat "/sys/fs/cgroup/cpu,cpuacct/docker/$$(docker-compose -f $(SPRINGCOMPOSEFILE) ps -q helloworld)/cpuacct.stat" >> $(SPRINGOUTPUTCPU)

	@echo "Running performance tests"
	k6 run --vus 10 --duration 2s k6/script.js

	# Store total cpu usage after running tests
	@echo "after" >> $(SPRINGOUTPUTCPU)
	@cat "/sys/fs/cgroup/cpu,cpuacct/docker/$$(docker-compose -f $(SPRINGCOMPOSEFILE) ps -q helloworld)/cpuacct.stat" >> $(SPRINGOUTPUTCPU)

	# Store max memory used in bytes
	@cat "/sys/fs/cgroup/memory/docker/$$(docker-compose -f $(SPRINGCOMPOSEFILE) ps -q helloworld)/memory.max_usage_in_bytes" > $(SPRINGOUTPUTMEM)

	@echo "Shutting down Spring containers"
	docker-compose -f $(SPRINGCOMPOSEFILE) down

# TODO: currently we only record CPU and MEM stats of the hello-world containers, should we use them all?
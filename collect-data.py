from sys import argv

import docker

def main():
    container_name = argv[1]

    client = docker.from_env()
    container = client.containers.get(container_name)

    stats = container.stats(stream=False)
    print(stats)

if __name__ == "__main__":
    main()

from sys import argv
from os import path, remove
import docker
import asyncio
import json

k6_path = path.join(path.dirname(__file__), "k6", "real-world")

def get_k6_path(container_name: str):
    if 'nest' in container_name:
        return path.join(k6_path, "script-nestjs.js")
    return path.join(k6_path, "script-spring.js")

def parse_stats(stats):
    return {
        'cpu': stats['cpu_stats']['cpu_usage']['total_usage'],
        'precpu': stats['precpu_stats']['cpu_usage']['total_usage'],
        'memory': stats['memory_stats']['usage'],
    }

async def execute_k6(k6_script_path: str, event: asyncio.Event):
    process = await asyncio.create_subprocess_exec(
        "k6", "run", k6_script_path, "--quiet",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode == 0:
        print(f"K6 execution completed: {stdout.decode()}")
    else:
        print(f"K6 execution failed: {stderr.decode()}")
    
    event.set()

async def get_stats(container_name: str, event: asyncio.Event):
    client = docker.from_env()
    container = client.containers.get(container_name)

    # delete file
    if path.isfile("stats.json"):
        remove("stats.json")

    with open("stats.json", "w") as f:
        f.write("[]")

    while not event.is_set():
        stats = container.stats(stream=False) # pyright: ignore
        raw_file = ''
        with open("stats.json", "r") as rf:
            raw_file = rf.read()

        with open("stats.json", "w") as f:
            file = json.loads(raw_file)
            file.append(parse_stats(stats))

            f.write(json.dumps(file))

        await asyncio.sleep(1)

async def main():
    container_name = argv[1]
    k6_execution_path = get_k6_path(container_name)
    
    event = asyncio.Event()
    
    await asyncio.gather(
        execute_k6(k6_execution_path, event),
        get_stats(container_name, event)
    )

if __name__ == "__main__":
    asyncio.run(main())


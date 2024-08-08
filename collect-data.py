from sys import argv
from os import path, remove, environ
import docker
import asyncio
import json

k6_path = path.join(path.dirname(__file__), "k6", "script.js")
reports_path = path.join(path.dirname(__file__), "reports")


def parse_stats(stats):
    return {
        "cpu": stats["cpu_stats"]["cpu_usage"]["total_usage"],
        "precpu": stats["precpu_stats"]["cpu_usage"]["total_usage"],
        "memory": stats["memory_stats"]["usage"],
    }


async def execute_k6(k6_script_path: str, event: asyncio.Event, container_name: str):
    framework = "nest" if "nest" in container_name else "spring"
    report_path = path.join(
        reports_path, framework, f"html-report-{framework}-json-1000.html"
    )
    environ["K6_WEB_DASHBOARD_EXPORT"] = report_path

    process = await asyncio.create_subprocess_exec(
        "k6",
        "run",
        k6_script_path,
        "-e",
        f"FRAMEWORK={framework}",
        "--quiet",
        "--out",
        f"web-dashboard={report_path}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
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

    framework = "nest" if "nest" in container_name else "spring"
    stats_path = path.join(reports_path, framework, "stats.json")

    # delete file
    if path.isfile(stats_path):
        remove(stats_path)

    with open(stats_path, "w") as f:
        f.write("[]")

    while not event.is_set():
        stats = container.stats(stream=False)  # pyright: ignore
        raw_file = ""
        with open(stats_path, "r") as rf:
            raw_file = rf.read()

        with open(stats_path, "w") as f:
            file = json.loads(raw_file)
            file.append(parse_stats(stats))

            f.write(json.dumps(file))

        await asyncio.sleep(1)


async def main():
    container_name = argv[1]

    event = asyncio.Event()

    await asyncio.gather(
        execute_k6(k6_path, event, container_name),
        get_stats(container_name, event),
    )


if __name__ == "__main__":
    asyncio.run(main())

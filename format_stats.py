import json
import sys


def format_stats(stats_json):
    stats_list = json.loads(stats_json)
    if not stats_list:
        return "No data available."

    total_cpu_usage = 0
    total_memory_usage = 0
    max_cpu_usage = 0
    max_memory_usage = 0
    count = len(stats_list)

    for stats in stats_list:
        cpu_delta = stats["cpu"]
        precpu_delta = stats["precpu"]
        cpu_usage = 100.0 * (cpu_delta - precpu_delta) / cpu_delta

        memory_usage = stats["memory"] / (1024**2)  # convert to MB

        total_cpu_usage += cpu_usage
        total_memory_usage += memory_usage

        if cpu_usage > max_cpu_usage:
            max_cpu_usage = cpu_usage

        if memory_usage > max_memory_usage:
            max_memory_usage = memory_usage

    average_cpu_usage = total_cpu_usage / count
    average_memory_usage = total_memory_usage / count

    formatted_cpu_usage = f"Average CPU Usage: {average_cpu_usage:.2f}%, Max CPU Usage: {max_cpu_usage:.2f}%"
    formatted_memory_usage = f"Average Memory Usage: {average_memory_usage:.2f} MB, Max Memory Usage: {max_memory_usage:.2f} MB"

    return f"{formatted_cpu_usage}\n{formatted_memory_usage}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_docker_stats.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, "r") as file:
            stats_json = file.read()
        print(format_stats(stats_json))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {file_path}")

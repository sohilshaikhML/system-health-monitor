import psutil

# from performance import Performance

if __name__ == "__main__":
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print(f"Memory Usage: {memory_usage}%")

    # Disk Usage
    disk = psutil.disk_usage("/")
    disk_usage = disk.percent
    print(f"Disk Usage: {disk_usage}%")

    # perf = Performance()
    # cpu_temp = perf.cpu_temperature()
    # fan_speed = perf.fan_speed()

    # Network Interfaces
    network_interfaces = psutil.net_if_stats()
    print("Network Interfaces:")
    print(f"All Network Interfaces:{network_interfaces.keys()}")
    for interface, stats in network_interfaces.items():
        print(f"Interface: {interface}")
        print(f"   Is Up: {stats.isup}")
        print(f"   Speed: {stats.speed} Mbps")
        print()

    # # Network Connections list
    # network_connections = psutil.net_connections()
    # print("Network Connections:")
    # for conn in network_connections:
    #     print(f"Local Address: {conn.laddr.ip}:{conn.laddr.port}")
    #     if len(conn.raddr) > 0:
    #         print(f"Remote Address: {conn.raddr.ip}:{conn.raddr.port}")
    #     print(f"Status: {conn.status}")
    #     print(f"PID: {conn.pid or 'N/A'}")
    #     print()

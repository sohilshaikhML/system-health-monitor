from flask import Flask, render_template
import psutil

app = Flask(__name__)


@app.route("/")
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage("/")
    disk_usage = disk.percent
    network_interfaces = psutil.net_if_stats()
    return render_template(
        "index.html",
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        disk_usage=disk_usage,
        network_interfaces=network_interfaces,
    )


if __name__ == "__main__":
    app.run(debug=True)

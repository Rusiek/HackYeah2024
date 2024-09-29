import graph
from app import create_app
import threading
import time
from backend.route_risk.graph import update

def actualize_traffic():
    while True:
        update()
        time.sleep(5000)

def start_background_task():
    task_thread = threading.Thread(target=actualize_traffic())
    task_thread.daemon = True
    task_thread.start()

if __name__ == '__main__':
    start_background_task()
    app = create_app()
    app.run('127.0.0.1', 5000, debug=app.config.get('DEBUG'))
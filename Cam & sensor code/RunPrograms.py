import threading
import subprocess

def run_script(RunProgram):
    subprocess.run(['python', RunProgram])

# Create threads
t1 = threading.Thread(target=run_script, args=('camera.py',))
t2 = threading.Thread(target=run_script, args=('Sensor_volume.py',))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Both scripts have finished.")

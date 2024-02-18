from rich.progress import track
import time

for step in track(range(100)):
    #print(step)
    time.sleep(1/10)
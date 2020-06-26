# import the necessary packages
from rvm_lib import ReverseVendingMachine
from imutils.video import VideoStream
import time

# Select web cam. or PiCam
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()

print("[INFO] warming up camera...")
time.sleep(2.0)

# start the Reverse Vending Machine App.
rvm = ReverseVendingMachine(vs)
rvm.root.mainloop()
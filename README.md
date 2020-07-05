# Integrating physical devices with IOTA — The reverse vending machine

## The 17th part in a series of beginner tutorials on integrating physical devices with the IOTA protocol.

![img](https://miro.medium.com/max/4032/1*7dy4bmbo8axvnejwfiUiyg.jpeg)

## Introduction

This is the 17th part in a series of beginner tutorials where we explore integrating physical devices with the IOTA protocol. In this tutorial we will be creating the basic functions of an IOTA powered reverse vending machine using a Raspberry PI, a touch display, a camera, and a bar-code scanner.

*Note!The touch display and/or bar-code scanner is not required to play around with this tutorial as you also have the option of interacting with the UI using a traditional monitor, mouse and keyboard.*

When I started working on this tutorial my initial idea was to do some type of IOTA powered vending machine. However, i soon realized that the main functions of such a machine would be more or less identical to the projects we did in the first four tutorials; only difference being that instead of turning ON/OFF a power relay, we would now have to trigger some type of robotic motion.

After puzzling over this problem for a while i decided to go with a different idea.., what if we took the previous tutorials and reversed the use case? The result would then be some kind of a reverse vending machine. Instead of the customer paying the machine for its services, the machine would now have to pay the customer. This would surely introduce some new challenges.

------

## The Use Case

Lately our hotel owner have noticed his guests leaving empty bottles and cans all around his hotel and swimming pool area without bothering to picking them up and throwing them in the recycling bin. He could of course have his staff do it but they are normally busy doing other work.

What if he could provide his guests with some type of incentive or reward for cleaning up there own mess? After all, it would probably be cheaper than hiring a new employee.

After thinking about this problem for a while he decides to try a concept he has seen implemented in other places; A machine that rewards the customer for recycling, in other words: A reverse vending machine.

For this idea to work, he feels his new “machine” should fulfill some basic requirements:

1. The machine must be easy to use with a minimum of effort from the guest.
2. Individual bottles and cans should give individual rewards depending on there size and type.
3. The reward should be payed out with IOTA tokens (after all, IOTA is the standard currency at Hotel IOTA and can be used to pay for other hotel services later on)

------

## The concept

Now, lets take a look at the basic concept behind this idea and how it might work.

Lets say Alice is packing up after a long day beside the hotel swimming pool.

On her way out of the swimming pool area, she brings her empty bottles/cans and makes a stop at the recycling bin next to the exit.

She then takes the bar-code scanner mounted next to the bin and scans the bar-code on each individual bottle/can before throwing it into the bin. A small LCD display next to the scanner shows the recycling reward for each individual item together with the total reward.

After scanning all the items, she pushes the “Get reward” button on the touch display.

She then takes her mobile phone with the Trinity wallet and generates a new receiver address.

Finally, she opens the QR code for the new address and places her phone in front of the camera placed next to the scanner.

As soon as the receiver address (QR code) has been detected by the camera, an IOTA payment transaction for the total recycling reward is created and sent to Alice’s receiver address.

Alice can now go and sell her recycling reward on the open IOTA market, or spend it on other IOTA supported services inside or outside the hotel.

------

## The components

Next, lets take a quick look at the hardware components used in this project.

![img](https://miro.medium.com/max/60/1*uPXAlfr8pkqqGAKunXY9tA.png?q=20)

![img](https://miro.medium.com/max/747/1*uPXAlfr8pkqqGAKunXY9tA.png)

**The Raspberry PI**
For this project i’m using my new Raspberry PI 4, but any PC should basically work.

**The Bar-code scanner**
I got this USB connected bar-code scanner off ebay for about 14 USD

**The camera**
In my version of the project i ended up using an old Logitech webcam i had laying around. You may also use the Raspberry PI camera module with some minor adjustments to the Python code.

**The touch display**
My plan was to use a 7 inch touch display for this project. However, since i did not have any micro-hdmi (from the new RPI4) to standard-hdmi (on my touch display) cable, i ended up using a normal monitor and mouse for interacting with the UI. More about this later.

------

## The User Interface (UI)

As with the [3th tutorial](https://medium.com/coinmonks/integrating-physical-devices-with-iota-adding-a-user-interface-2fb028a8fee1) in this series, i decided to go with Python and the [Tkinter toolkit](https://docs.python.org/3/library/tkinter.html) when building a simple UI for the customer to interact with the system.

![img](https://miro.medium.com/max/565/1*YTbgcTN4liPwcb7y4s1bUw.png)

**Here is a quick description on how to interact with the UI:**
For each recyclable item, place the cursor in the upper left text box and scan the bar-code printed on the item (you may also type the bar-code ID manually into the text box); then press enter or push the “Scan Item…” button to register the item. The Python script will now check if the bar-code found on the item exists in the local bar-code database (barcodesdb.csv). If the bar-code was found, the item will be added to the item list together with its corresponding recycling reward value. As more items are added to the list, the total recycling reward will be displayed below the list. When all items have been registered, push the “Get Reward” button. As soon as the “Get Reward” button is pushed, the camera is activated. Now, hold a QR code of the IOTA reward receiver address in front of the camera. When the the QR code has been detected by the camera, the reward payment is executed in the background (see the bottom message area for status). Finally, the UI is reset and prepared for the next customer.

*Note!
As i did not have the micro HDMI to standard HDMI cable when writing this tutorial, the layout of the current Tkinter UI is tailored for a normal PC monitor. Please check out the* [*3th tutorial*](https://medium.com/coinmonks/integrating-physical-devices-with-iota-adding-a-user-interface-2fb028a8fee1) *for guidance if you want to implement the UI on a smaller size touch display.*

------

## The Bar-code database

Before adding new items to the recycled items list, we first need to check that the item is approved for recycling. We also need to get the reward value for each individual item. For this purpose we use a simple lookup table in the form of a comma separated text file (.csv), where the first element represents the bar-code ID, and the second element represents the recycling reward in IOTA’s

![img](https://miro.medium.com/max/133/1*TZ2P7MyN-HNMyWHhmbx7mg.png)

*Note!*
*Before you start scanning bottles or cans, make sure you update the barcodesdb.csv file to include any bar-code ID’s you plan to recycle with the app. You also need to include the reward (in IOTA’s) for each individual bar-code ID.*

------

## Required Software and libraries

Next, let’s take a a look at the software and Python libraries required to run the app.

The hardest part is probably getting [OpenCV](https://opencv.org/) installed and running on your machine. Fortunately, i found this great tutorial on [how to install OpenCV on a Raspberry PI 4](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/), written by Adrian Rosebrock.

The rest should be pretty straight forward using pip.

[Pillow](https://pypi.org/project/Pillow/), [imutils](https://pypi.org/project/imutils/), [pyzbar](https://pypi.org/project/pyzbar/), [PyOTA](https://pypi.org/project/PyOTA/), [PyOTA-CCurl](https://pypi.org/project/PyOTA-CCurl/)

------

## The Python Code

I decided to split the code for this project into two separate Python files. The **rvm_lib.py** file contains a class with the main functions of the app., while the **rvm_app.py** file is used for launching the app.

Besides that, the code is pretty well documented so i will not include any more details here.

Here is the **rvm_app.py** file:

```python
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
```

<iframe src="https://medium.com/media/f7fed340d9ccc05885530c0f5be4a0fb" allowfullscreen="" frameborder="0" height="369" width="680" title="rvm_app.py" class="s t u dq ai" scrolling="auto" style="box-sizing: inherit; position: absolute; top: 0px; left: 0px; width: 680px; height: 369px;"></iframe>

You can download the source code from [here](https://gist.github.com/huggre/2f4c7b181b221345fd7432edcc15056c)

and here is the **rvm_lib.py** file:

```python
# import the necessary packages
from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import tkinter as tki
from tkinter import scrolledtext
from pyzbar import pyzbar
import threading
import imutils
import cv2
import os
import csv
import json

# Import the PyOTA library
import iota
from iota import Address


class ReverseVendingMachine:
    def __init__(self, vs):
        
        
        # IOTA seed used for payment transaction
        # Replace with your own devnet seed
        seed = b"YOUR9SEED9GOES9HERE"
        
        # URL to IOTA fullnode used when interacting with the Tangle
        iotaNode = "https://nodes.devnet.iota.org:443"

        # Define api object
        self.api = iota.Iota(iotaNode, seed=seed)

        # Define Total reward variable
        self.total_reward = 0
               
        # Define some objects  
        self.vs = vs
        self.frame = None
        self.thread = None
        self.stopEvent = None
        
        # Initialize the root window and VideoStream panel
        self.root = tki.Tk()
        self.panel = None
                
        # Define window header label
        self.header_lbl = tki.Label(self.root, text='Recycle with IOTA')
        self.header_lbl.config(font=("Courier", 30))
        self.header_lbl.grid(row=0, column=0, columnspan=2, sticky=(tki.N, tki.S, tki.E, tki.W))

        # Define barcode text box
        self.barcode_txt = tki.Text(self.root, height=1, width=30)
        self.barcode_txt.grid(column=0, row=1, sticky=(tki.S, tki.E, tki.W))
               
        # Define Item list
        self.item_list=scrolledtext.ScrolledText(self.root, width=30, height=10, wrap=tki.WORD)  
        self.item_list.grid(column=0, row=2, sticky=(tki.N, tki.S, tki.E, tki.W))
               
        # Define barcode "Scan Item" button
        scan_item_btn = tki.Button(self.root, width=30, text = 'Scan Item...', command=self.scanItem)
        scan_item_btn.grid(column=1, row=1, sticky=(tki.N, tki.S, tki.E, tki.W))

        # Define Total Reward text box
        self.total_txt = tki.Text(self.root, height=1, width=30)
        self.total_txt.grid(column=0, row=3, sticky=(tki.S, tki.E, tki.W))

        # Define "Clame Reward" button
        get_reward_btn = tki.Button(self.root, text = 'Get Reward', command=self.initiateGetReward)
        get_reward_btn.grid(column=0, row=4, sticky=(tki.N, tki.S, tki.E, tki.W))

        # Define Message box
        self.msg_box=scrolledtext.ScrolledText(self.root, width=30, height=10, wrap=tki.WORD)  
        self.msg_box.grid(column=0, row=5, columnspan=2, sticky=(tki.N, tki.S, tki.E, tki.W))
        
        # ...
        self.root.bind('<Return>', (lambda event: self.scanItem()))

        # Set a callback to handle when the window is closed
        self.root.wm_title("The Reverse Vending Machine")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
        
    def getReward(self):       
        
        # Try/except statement to get around a RunTime
        # error that Tkinter throws due to threading       
        try:
            # Loop the vieoStream until we get a QR code
            while not self.stopEvent.is_set():
                # Grab the frame from the video stream and resize it to
                # have a maximum width of 300 pixels
                self.frame = self.vs.read()
                self.frame = imutils.resize(self.frame, width=300)
                
                # Get QR codes from camera using pyzbar 
                qrcodes = pyzbar.decode(self.frame)

                # Loop over the detected qrcodes
                for qrcode in qrcodes:
                    # Extract the bounding box location of the barcode and draw
                    # the bounding box surrounding the barcode on the image
                    (x, y, w, h) = qrcode.rect
                    cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    # The barcode data is a bytes object so if we want to draw it
                    # on our output image we need to convert it to a string first
                    qrcodeData = qrcode.data.decode("utf-8")
                    qrcodeType = qrcode.type

                    # Draw the barcode data and barcode type on the image
                    text = "{} ({})".format(qrcodeData, qrcodeType)
                    cv2.putText(self.frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    
                    # QR codes generated by the IOTA wallet or thetangle.org
                    # is actually a dict object so we use json to convert the
                    # qrcodeData string to a dict.
                    jsondata = json.loads(qrcodeData)
                    
                    # Get address from dict
                    addr = jsondata.get('address')
                    
                    # Now that we have the IOTA address we can exit the while loop and initiate the payment process
                    self.stopEvent.set()
                                       
        
                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
                image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)
        
                # If the videoStream panel is not None, we need to initialize it
                if self.panel is None:
                    self.panel = tki.Label(image=image)
                    self.panel.image = image
                    self.panel.grid(row=2, column=1, rowspan=3)
        
                # Otherwise, simply update the panel
                else:
                    self.panel.configure(image=image)
                    self.panel.image = image
            
            # Now that we have the IOTA address, lets send the reward to the cusomer 

            # Clear the VideoStream panel            
            self.panel.config(image='')
           
            # Display sending reward message
            self.msg_box.insert(tki.INSERT, 'Sending reward of ' + str(self.total_reward) + ' IOTA to address: ' + addr + '\n')
                       
            # Create transaction object
            tx1 = iota.ProposedTransaction( address = iota.Address(addr), message = None, tag = iota.Tag(iota.TryteString.from_unicode('HOTELIOTA')), value = self.total_reward)

            # Send transaction to tangle
            self.msg_box.insert(tki.INSERT, 'Sending transaction..., please wait\n')
            SentBundle = self.api.send_transfer(depth=3,transfers=[tx1], inputs=None, change_address=None, min_weight_magnitude=9)       

            # Display transaction sent confirmation message
            self.msg_box.insert(tki.INSERT, 'Transaction sendt..., thanks for recycling with IOTA\n')
            
            # Cleanup and prepare for next customer...
            
            # Clear Item list
            self.item_list.delete(1.0, 'end')
            
            # Clear total reward text box
            self.total_txt.delete(1.0, 'end')           
            
            # Reset Total award variable
            self.total_reward = 0
            
            # Display system is ready message
            self.msg_box.insert(tki.INSERT, 'System is ready...\n')
                        
            

        except RuntimeError:
            print("[INFO] caught a RuntimeError")
            
    def initiateGetReward(self):

        # Show "get QR code" message
        self.msg_box.insert(tki.INSERT, 'Please hold a valid IOTA address QR code in front of the camera..\n')
        
        # Start new get reward thread
        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.getReward, args=())
        self.thread.start()


    def scanItem(self):
        barcode = self.barcode_txt.get("1.0",'end-1c')
        barcode = barcode.rstrip("\n") #, Strip any trailing returns from the string
        barcode_found = False
        with open('barcodesdb.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == barcode:
                    item_reward=row[1]
                    self.total_reward = self.total_reward + int(item_reward)
                    barcode_found = True
        if barcode_found == True:
            # If a barcode match was found in the barcode database, add Item to list
            # and update the total reward texbox.
            # Else, diplay barcode not message 
            self.item_list.insert(tki.INSERT, barcode + ': Reward=' + item_reward + ' IOTA\n')
            self.msg_box.insert(tki.INSERT, 'Item approved\n')
            self.total_txt.delete(1.0, 'end')
            self.barcode_txt.delete(1.0, 'end')
            self.total_txt.insert(tki.INSERT, 'Total Reward: ' + str(self.total_reward))
        else:
            self.msg_box.insert(tki.INSERT, 'Barcode not found in database\n')
    
        
    def onClose(self):
        # Set the stop event, cleanup the camera, and allow the rest of
        # the quit process to continue
        print("[INFO] closing...")
        self.stopEvent.set()
        self.vs.stop()
        self.root.quit()
```



<iframe src="https://medium.com/media/f24feda9d58a5544e09f9a4e34b04b97" allowfullscreen="" frameborder="0" height="4940" width="680" title="rvm_lib.py" class="s t u dq ai" scrolling="auto" style="box-sizing: inherit; position: absolute; top: 0px; left: 0px; width: 680px; height: 4940px;"></iframe>

You can download the source code from [here](https://gist.github.com/huggre/5815111ed70f5b0ed456ff5c979e3d4a)

<iframe src="https://medium.com/media/b2358363feb18572609d48e602f45e3b" allowfullscreen="" frameborder="0" height="126" width="680" title="barcodesdb.csv" class="s t u dq ai" scrolling="auto" style="box-sizing: inherit; position: absolute; top: 0px; left: 0px; width: 680px; height: 126px;"></iframe>

```
7030019532240,10
7310070786937,25
```



You also need the barcodesdb.csv file that you will find [here](https://gist.github.com/huggre/87ad61d5c8558729e80d4f6a447a7841)

------

## Running the project

To run the project, you first need to save the Python and barcodesdb.csv files from the previous section to your machine.

Next, update the bacodesdb.csv file with bar-code ID’s that you plan to use with the app.

To execute the app., simply start a new terminal window, navigate to the folder where you saved the files and type:

**python rvm_app.py**

You should now see the UI appear on your LCD/Monitor.

------

## Contributions

If you would like to make any contributions to this tutorial you will find a Github repository [here](https://github.com/huggre/reverse_vending_machine)

------

## Donations

If you like this tutorial and want me to continue making others feel free to make a small donation to the IOTA address below.

![img](https://miro.medium.com/max/382/0*h3WS30UY7rgtRvMQ.png)

NYZBHOVSMDWWABXSACAJTTWJOQRPVVAWLBSFQVSJSWWBJJLLSQKNZFC9XCRPQSVFQZPBJCJRANNPVMMEZQJRQSVVGZ

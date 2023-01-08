from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.button import MDFillRoundFlatButton
import time
from kivy.uix.image import Image
from pyicloud import PyiCloudService
import sys 
import time
import mpu
from threading import Thread
from kivy.properties import StringProperty

api = PyiCloudService('zwongkevin@gmail.com', 'Aud!ob00k3')
print(api.devices[1])
if api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the code you received of one of your approved devices: ")
    result = api.validate_2fa_code(code)
    print("Code validation result: %s" % result)

    if not result:
        print("Failed to verify security code")
        sys.exit(1)

    if not api.is_trusted_session:
        print("Session is not trusted. Requesting trust...")
        result = api.trust_session()
        print("Session trust result %s" % result)

        if not result:
            print("Failed to request trust. You will likely be prompted for the code again in the coming weeks")

device = api.devices[1]

Window.size = (1080, 1920)



class FullImage(Image):
    pass
class MainWidget(Screen):
    pass
    

class Widget2(Screen):
    global distance
    location = [device.location()["latitude"], device.location()["longitude"]]
    button_text = "Start"


    def start(self):
        def other_func():

            device = api.devices[1]
            distance = 0


            location = device.location()

            currentTime = time.time()

            locationList  = [[device.location()["latitude"], device.location()["longitude"]]]
            state = 0
            stopCounter = 0
            while(True):
            
                time.sleep(1)
                location = [device.location()["latitude"], device.location()["longitude"]]
                locationList.append(location)

                distance = mpu.haversine_distance((locationList[0][0], locationList[0][1]), (locationList[1][0], locationList[1][1])) * 1000

                print("round")
                print(distance)
                if (state == 0):
                    if distance < 0.5:
                        stopCounter += 1
                    else:
                        stopCounter = 0
                
                    if stopCounter >= 5:
                        marker = [locationList[0][0], locationList[0][1]]
                        print("marker Placed")
                        state = 1
                else:
                    
                    if (distance > 10):
                        device.play_sound()
                locationList.pop(0)


        # create the thread to invoke other_func with arguments (2, 5)
        t = Thread(target=other_func)
        # set daemon to true so the thread dies when app is closed
        t.daemon = True
        # start the thread
        t.start()  



class HoundApp(MDApp):
    def build(self):
        Builder.load_file("Hound.kv")
        sm = ScreenManager(transition = SwapTransition())
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        sm.add_widget(MainWidget(name = "MainWidget"))
        sm.add_widget(Widget2(name = "Widget2"))
        return sm

    pass

 
HoundApp().run()
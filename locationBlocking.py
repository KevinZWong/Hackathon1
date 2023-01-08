from pyicloud import PyiCloudService
import sys 
import time
import mpu

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


def main():

    device = api.devices[1]


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

        

                

main()



        

        






        #if currentLocation == pastLocation:


        




 

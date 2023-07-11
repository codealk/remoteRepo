import time
timestamp =time.strftime("%H:%M:%S")
print(timestamp)
H =int(time.strftime("%H"))

if (H == 4):
    print("good morning alok")
elif (H == 12):
    print("good afternoon alok")
elif (H == 16):
    print("good evening alok")
else:
    print("good night alok")


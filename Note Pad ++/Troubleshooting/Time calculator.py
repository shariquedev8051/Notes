
while True:
    speed= input("Enter the speed of video: ")
    if speed =="quite":
            break
    duration = input("Enter the video duration in h:min formate: ")
    duration = duration.split(':')
    exact_time = int(duration[0])*60+int(duration[1])
    finale_time = (1/float(speed))*exact_time
    print(f"Finale view time is : {int(finale_time)}min .\nYou saved {int(exact_time-finale_time)}min.") 
import numpy as np
import cv2
import time
import os, random
import vlc




cap = cv2.VideoCapture(0)

PlayingRock = False
PlayingJazz = False
PlayingRnB = False
PlayingHipHop = False

player = vlc.MediaPlayer()
current_genre = None



while True:
    # capute the frame
    _, frame = cap.read()
    hsv_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    # find center of the frame

    cx = int(width / 2)
    cy = int(height / 2)

    # pick pixel value
    pixel_center = hsv_frame[cx, cy]
    hue_value = pixel_center[0]




    print(hue_value)
    # print(pixel_center)

    

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), 3)

    # show image 
    frame = cv2.flip(frame, 1)
    time.sleep(0.25)
    Camera_path = "/home/gebruiker/Desktop/M6BO_39613/Cam & sensor code/img/camera.jpg"
    cv2.imwrite(Camera_path, frame)
    # cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
# name = camera.png
# opslaan als:
# img/camera.png


# js
# img = gitDocumentbyid('camera')
# img.src = '/img/camera.png?time=' + timestamp();


    #================================================================= 
    def RandomSong(genre):

        folder_path = "songs/"+ genre +"/"

        mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]

        RnB_songs = random.choice(mp3_files)
        RnB_full_path = os.path.join(folder_path, RnB_songs)
        return (RnB_full_path, RnB_songs)

    #================================================================= 

    # Geel detectie -> Volgende liedje
    if 24 < hue_value < 40:
        if current_genre != "Indie":
            player.stop()
            media_path, song_name = RandomSong("Indie")
            player.set_media(vlc.Media(media_path))
            player.play()

            current_genre = "Indie"
            print("Color Yellow")
            print("Now playing:", song_name)

    # Groen detectie -> Alternative Rock
    if 74 < hue_value < 85:
        if current_genre != "Alternative Rock":
            player.stop()
            media_path, song_name = RandomSong("Alternative_Rock")
            player.set_media(vlc.Media(media_path))
            player.play()

            current_genre = "Alternative Rock"
            print("Color Green")
            print("Now playing:", song_name)
    
    # Blauw detectie -> Jazz
    if 99 < hue_value < 115:
        if current_genre != "Jazz":
            player.stop()
            media_path, song_name = RandomSong("Jazz")
            player.set_media(vlc.Media(media_path))
            player.play()

            current_genre = "Jazz"
            print("Color Blue")
            print("Now playing:", song_name)
    
    # # Groen detectie -> Muziek stopt
    # if 110 < hue_value < 130:
    #     if current_genre != "Music stopped":
    #         player.stop()
    #         current_genre = "Music stopped"

    #         print("Color Green")
    #         print("Music has been stopped")

    # Paars detectie -> Rnb
    if 144 < hue_value < 155:
        if current_genre != "RnB":
            player.stop()
            media_path, song_name = RandomSong("RnB")
            player.set_media(vlc.Media(media_path))
            player.play()

            current_genre = "RnB"
            print("Color Purple")
            print("Now playing:", song_name)

    # Rood detectie -> HipHop
    if 159 < hue_value < 179 or hue_value < 7 :
        if current_genre != "HipHop":
            player.stop()
            media_path, song_name = RandomSong("HipHop")
            player.set_media(vlc.Media(media_path))
            player.play()

            current_genre = "HipHop"
            print("Color Red")
            print("Now playing:", song_name)






    
    # breake image
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



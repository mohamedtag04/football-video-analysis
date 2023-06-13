import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def maskRed(img):
    lower_red = 10, 10, 60
    upper_red = 50, 45, 165

    mask = cv2.inRange(img, lower_red, upper_red)
    return mask

def maskBlue(img):
    lower_blue = 7, 10, 8
    upper_blue = 36, 37, 50

    mask = cv2.inRange(img, lower_blue, upper_blue)
    return mask

def maskWhite(img):
    lower_white = 117, 129, 127
    upper_white = 212, 230, 227

    mask = cv2.inRange(img, lower_white, upper_white)
    mask = mask[img.shape[0] // 3:img.shape[0] // 3 * 2, img.shape[1] // 3:img.shape[1] // 3 * 2]
    result = np.zeros((img.shape[0], img.shape[1]))
    result[img.shape[0] // 3:img.shape[0] // 3 * 2, img.shape[1] // 3:img.shape[1] // 3 * 2] = mask
    return result

def countRedPlayers(img):
    mask = maskRed(img)
    sum = 0
    for i in mask:
        for j in i:
            if j != 0:
                sum += 1
    return round(sum / 530)

def countBluePlayers(img):
    mask = maskBlue(img)
    sum = 0
    for i in mask:
        for j in i:
            if j != 0:
                sum += 1
    return round(sum / 530)

def countAllPlayers(img):
    red_players = countRedPlayers(img)
    blue_players = countBluePlayers(img)
    return f"Red players: {red_players}, Blue players: {blue_players}"

def cropToNine(img):
    crops = []
    rows = 3
    columns = 4
    height = img.shape[0] // rows
    width = img.shape[1] // columns
    for i in range(rows):  # Iterate over rows first
        for j in range(columns):  # Then iterate over columns
            x = j * width
            y = i * height
            crop = img[y:y + height, x:x + width]
            crops.append(crop)
    return crops

def countInCrops(n):
    img = cv2.imread(f"frames/frame_{n}.jpg")
    crops = cropToNine(img[180:])
    fig, axs = plt.subplots(3, 4,figsize=(15, 12))

    for i, crop in enumerate(crops):
        axs[i // 4, i % 4].set_title(countAllPlayers(crop))
        crop = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
        axs[i // 4, i % 4].imshow(crop)

    plt.show()

def createVideo(name):
    output_file = f'{name}.mp4'
    frame_width, frame_height = None, None
    video_writer = None
    for i in range(1, 600):
        img = cv2.imread(f'frames/frame_{i}.jpg')
        img = img[180:]
        
        combined_mask = comninedMask(img)

        if video_writer is None:
            frame_height, frame_width = combined_mask.shape[:2]
            video_writer = cv2.VideoWriter(output_file, 
                                        cv2.VideoWriter_fourcc(*'mp4v'), 
                                        30, (frame_width, frame_height))
        video_writer.write(combined_mask)

    video_writer.release()
    cv2.destroyAllWindows()

def comninedMask(img):
    red_mask = maskRed(img)
    blue_mask = maskBlue(img)
    ball_mask = maskWhite(img)
    line_mask = maskLines(img)
    # Combine the masks with different colors
    combined_mask = np.zeros_like(img)
    combined_mask[red_mask > 0] = (0, 0, 255)  # Red color for red mask
    combined_mask[blue_mask > 0] = (255, 0, 0)  # Blue color for blue mask
    combined_mask[ball_mask > 0] = (0, 255, 0)  # Green color for ball mask
    combined_mask[line_mask > 0] = (255, 255, 255)  # White color for line maskq
    return combined_mask

def maskLines(img):
    lower = 90, 90, 90
    upper = 250, 250, 250
    mask = cv2.inRange(img, lower, upper)
    third = img[img.shape[0]//3:img.shape[0]//3*2 , img.shape[1]//3:img.shape[1]//3*2 ]
    bottom = img[450:770, 1500:1800]
    joystick = img[430:615, 200:480]
    zeros2 = np.zeros((joystick.shape[0], joystick.shape[1]), dtype=np.uint8)
    zeros1 = np.zeros((bottom.shape[0], bottom.shape[1]), dtype=np.uint8)
    zeros = np.zeros((third.shape[0], third.shape[1]), dtype=np.uint8)
    mask[img.shape[0]//3:img.shape[0]//3*2, img.shape[1]//3:img.shape[1]//3*2] = zeros
    mask[450:770, 1500:1800] = zeros1
    mask[430:615, 200:480] = zeros2
    return mask

def combVid():


    video = cv2.VideoCapture('combined_video_mask.mp4') 

    if not video.isOpened():
        print("Error opening video file")

    desired_fps = 30
    desired_width = 960
    desired_height = 540 

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame = cv2.resize(frame, (desired_width, desired_height))
        cv2.imshow('Video', frame)

        key = cv2.waitKey(int(1000 / desired_fps)) & 0xFF
        if key == ord('q') or key == 27:  # Press 'q' or ESC key to exit
            break
    video.release()
    cv2.destroyAllWindows()

def originalVid():

    video = cv2.VideoCapture('original_video.mp4') 
    if not video.isOpened():
        print("Error opening video file")
    desired_fps = 30
    desired_width = 960
    desired_height = 540 
    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame = cv2.resize(frame, (desired_width, desired_height))
        cv2.imshow('Video', frame)

        key = cv2.waitKey(int(1000 / desired_fps)) & 0xFF
        if key == ord('q') or key == 27:  # Press 'q' or ESC key to exit
            break

    video.release()
    cv2.destroyAllWindows()

def playersVid():
    
        video = cv2.VideoCapture('players_video.mp4')  
        if not video.isOpened():
            print("Error opening video file")
    
        desired_fps = 30
        desired_width = 960
        desired_height = 540 
        while True:
            ret, frame = video.read()
    
            if not ret:
                break
    
            frame = cv2.resize(frame, (desired_width, desired_height))
    
            cv2.imshow('Video', frame)

            key = cv2.waitKey(int(1000 / desired_fps)) & 0xFF
            if key == ord('q') or key == 27:  # Press 'q' or ESC key to exit
                break
    
        video.release()
        cv2.destroyAllWindows()

def playersBallVid():
            video = cv2.VideoCapture('players_ball_video.mp4') 
            if not video.isOpened():
                print("Error opening video file")
        
            desired_fps = 30
            desired_width = 960
            desired_height = 540 
            while True:
                ret, frame = video.read()
        
                if not ret:
                    break
        
                frame = cv2.resize(frame, (desired_width, desired_height))
        
                cv2.imshow('Video', frame)
        
                key = cv2.waitKey(int(1000 / desired_fps)) & 0xFF
                if key == ord('q') or key == 27:  # Press 'q' or ESC key to exit
                    break
        
    
            video.release()
            cv2.destroyAllWindows()


img  = cv2.imread('gui/background.png')
print(img.shape)
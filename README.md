# Football Video Analysis

## Description

This project is a university project that involves analyzing a video of a football match in a game. The goal is to extract specific elements from the video, such as the ball, players from each team, and field lines. The extracted elements are then combined into a single image, where each element is represented by a different color. Additionally, the project includes functionality to count the number of players in each frame and within specific cropped regions of the frame. The entire analysis process is integrated into a simple graphical user interface (GUI).

## Project Steps

1. Video to Frames Conversion:
   - The video is transformed into individual frames to facilitate further processing.

2. Masking:
   - Each frame is processed to create masks for the ball, players of each team, and field lines. These masks help isolate the specific elements of interest.

3. Combined Mask Generation:
   - The individual masks from each frame are combined into a single image, where each element is assigned a different color.

4. Video Reconstruction:
   - The combined masks from all frames are used to create a new video, where the extracted elements are displayed.

5. Player Counting:
   - The project includes functionality to count the number of players in each frame.
   - Additionally, it can count the number of players within specific cropped regions of the frame.

## Limitations

For this project, I was limited to using the content covered in the university course. No additional information or personal knowledge beyond the course material was utilized.

'''
    Kenneth Bailey
    3/17/18

    Usage -->  "python3 concat.py <outfile.name>"

    Notes:
        - Currently concats all videos located in directory in which the script is ran. 
        - Concats the video in alphanumeric order

    To Do:
        - Implement exception handling
        - Test with more video types(.avi, .mov, etc)
        - Prompt user to select order in which videos will be concatenated

'''

from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys
import os

FORMATS = [".MP4", ".mp4"]

def concatClips(video_list):
    clip_list = []
    for video in video_list:
        clip = VideoFileClip(video)
        clip_list.append(clip)
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile(sys.argv[1])
    

def getVideoFiles():
    
    video_files = []
    files_path = os.listdir()    
    
    for path in files_path:
        if isVideo(path):
            video_files.append(os.getcwd()+'/'+path)
    
    if len(video_files) > 0:
        return video_files
    else:
        print("No compatible video files found!")
        sys.exit(0)


def isVideo(vid):
    
    try:
        parts = vid.split('.')
        if any(parts[1] in x for x in FORMATS):
            return True
        else:
            return False
    
    except Exception as e:
        print("Failed to test if is video!")
        return False

if __name__ == '__main__':
    
    # check for video name argument
    if len(sys.argv) == 1:
        print("Failed to input video out filename!")
        print("Usage: python3 concat.py out.mp4")
        sys.exit(0)
    
    # check for proper output type
    if not isVideo(sys.argv[1]):
        print("Output file not valid!")
        print("Usage: python3 concat.py out.mp4")
        sys.exit(0)
        
    # compile video list
    video_list = getVideoFiles()

    # concatenate videos
    concatClips(video_list)

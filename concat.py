from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys
import os

FORMATS = [".MP4", ".mp4"]

def concat_clips(video_list):
    clip_list = []
    for video in video_list:
        clip = VideoFileClip(video)
        clip_list.append(clip)
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile(sys.argv[1])
    

def get_video_files():
    video_files = []
    files_path = os.listdir()    
    for path in files_path:
        if is_video(path):
            video_files.append(os.getcwd()+'/'+path)
    return video_files

def is_video(vid):
    if any(x in vid for x in FORMATS):
        return True
    else:
        return False

if __name__ == '__main__':
    # check for video name argument
    if len(sys.argv) == 1:
        print("Failed to input video out filename!")
        print("Usage: python3 concat.py out.mp4")
        sys.exit(0)
    if not is_video(sys.argv[1]):
        print("Output file not valid!")
        print("Usage: python3 concat.py out.mp4")
        sys.exit(0)

    # compile video list
    video_list = get_video_files()

    # concatenate videos
    concat_clips(video_list)
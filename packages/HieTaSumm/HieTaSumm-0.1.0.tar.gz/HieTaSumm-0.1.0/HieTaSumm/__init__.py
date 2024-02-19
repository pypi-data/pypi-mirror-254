from .Summary import Summary
import os
import json
import cv2 as cv
import numpy as np
from datetime import timedelta
from pathlib import Path

class HieTaSumm:
    def __init__(self, **kwargs):
        PACKAGEDIR = Path(__file__).parent.absolute()
        my_file = PACKAGEDIR / 'options.json'

        path_file_param = kwargs.get('path_file_param')
        if path_file_param:
            json_file = open(path_file_param, 'r')
        else:
            json_file = open(my_file, 'r')
        data = json.loads(json_file.read())
        dataset_videos = data['video_path']
        dataset_frames = data['summary_path']
        percent = int(data['percent'])
        alpha = int(data['alpha'])
        rate = int(data['rate'])
        time = int(data['time'])
        hierarchy = data['hierarchy']
        selected_model = data['selected_model']
        is_binary = data['is_binary']
        keyshot = data['keyshot']
        keyframe = data['keyframe']
        if not os.path.isdir(dataset_frames):
            os.mkdir(dataset_frames)

        if(os.path.exists(dataset_videos)):
            video_list = os.listdir(dataset_videos)
            video_list.sort() # to guarantee order
            for i in video_list:
                print("------------------------")
                print("{}/{}/".format(dataset_videos, i))
                self.frame_extractor("{}/{}".format(dataset_videos, i), rate, dataset_frames)
        else:
            print(f"do not exist directory or file with path {dataset_videos}")

        if(os.path.exists(dataset_frames)):
            video_list = os.listdir(dataset_frames)
            video_list.sort() # to guarantee order
            for video in video_list:
                if video != '.ipynb_checkpoints':
                    self.hierarchical_summarization(dataset_frames, video, rate, time, percent, alpha, keyshot, keyframe, is_binary, hierarchy, selected_model)

    def frame_extractor(self, video_file, rate, frames):
        # i.e if video of duration 30 seconds, saves 0.5 frame each second = 60 frames saved in total
        SAVING_FRAMES_PER_SECOND = 1/rate
        filename, _ = os.path.splitext(video_file)
        video = frames + "/" + filename.split('/')[-1]
        filename = video + "/frames/"
        if not os.path.isdir(video):
            os.mkdir(video)
        # make a folder by the name of the video file
        if not os.path.isdir(filename):
            os.mkdir(filename)
            # read the video file
            cap = cv.VideoCapture(video_file)
            fps = cap.get(cv.CAP_PROP_FPS)
            saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)

            saving_frames_durations = self.get_saving_frames_durations(cap, saving_frames_per_second)

            count = 0
            frame_number = 1
            while True:
                is_read, frame = cap.read()
                if not is_read:
                    # break out of the loop if there are no frames to read
                    break
                # get the duration by dividing the frame count by the FPS
                frame_duration = count / fps
                try:
                    # get the earliest duration to save
                    closest_duration = saving_frames_durations[0]
                except IndexError:
                    # the list is empty, all duration frames were saved
                    break
                if frame_duration >= closest_duration:
                    # if closest duration is less than or equals the frame duration,
                    # then save the frame
                    # frame_duration_formatted = formatTimeDelta(timedelta(seconds=frame_duration))
                    number = str(frame_number).zfill(6)
                    frame_number += 1
                    cv.imwrite(os.path.join(filename, "{}.jpg".format(number)), frame) # frame_duration_formatted)), frame)
                    # drop the duration spot from the list, since this duration spot is already saved
                    try:
                        saving_frames_durations.pop(0)
                    except IndexError:
                        pass
                # increment the frame count
                count += 1

    def get_saving_frames_durations(self, cap, saving_fps):
        """A function that returns the list of durations where to save the frames"""
        s = []
        # get the clip duration by dividing number of frames by the number of frames per second
        clip_duration = int(cap.get(cv.CAP_PROP_FRAME_COUNT) / cap.get(cv.CAP_PROP_FPS))
        # use np.arange() to make floating-point steps

        for i in np.arange(0, clip_duration, saving_fps):
            s.append(i)
        return s

    def hierarchical_summarization(self, dataset_frames, video, rate, time, percent, alpha, keyshot, keyframe, is_binary, hierarchy, selected_model):
        Summary(dataset_frames, video, rate, time, hierarchy, selected_model, is_binary, percent, alpha, keyshot, keyframe)

if __name__== "__main__":
    HieTaSumm()
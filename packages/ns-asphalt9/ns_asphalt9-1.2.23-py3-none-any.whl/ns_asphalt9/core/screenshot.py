from subprocess import PIPE, Popen


def screenshot(image_path="output.jpg", wait=True, fast=False):
    if fast:
        cmd = f"ffmpeg -loglevel quiet -video_size 640x480 -hwaccel auto -y -f v4l2 -i /dev/video0 -frames:v 1 {image_path}"
    else:
        cmd = f"ffmpeg -loglevel quiet -video_size 1920x1080 -y -f v4l2 -i /dev/video0 -frames:v 1 {image_path}"
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, cwd="./")
    if wait:
        p.wait()


if __name__ == "__main__":
    screenshot()

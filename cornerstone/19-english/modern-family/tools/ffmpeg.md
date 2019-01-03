# ffmpeg


## What?

> FFmpeg: A complete, cross-platform solution to record, convert and stream audio and video.



## Q&A 

### 1. [How to extract 1 screenshot for a video with ffmpeg at a given time?](https://stackoverflow.com/questions/27568254/how-to-extract-1-screenshot-for-a-video-with-ffmpeg-at-a-given-time)

``` bash 
ffmpeg -ss 00:00:05 -i sintel.mp4 -vframes 1 -q:v 2 output.jpg
```

output = sintel.mp4 

output:

![output](https://i.imgur.com/CiTUvXp.jpg)


## Reference 

* [FFmpeg的使用](https://www.jianshu.com/p/7ed3be01228b)
* [FFmpeg official website](https://www.ffmpeg.org/)
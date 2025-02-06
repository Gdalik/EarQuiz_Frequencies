import os


os.environ['QT_MEDIA_BACKEND'] = 'ffmpeg'
os.environ['QT_LOGGING_RULES'] = '*.multimedia.*=false'
os.environ['QT_FFMPEG_DECODING_HW_DEVICE_TYPES'] = ','
os.environ['QT_FFMPEG_ENCODING_HW_DEVICE_TYPES'] = ','

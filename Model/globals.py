from Model.AudioEngine.pinknoise_gen import generate_pinknoise

supported_bitrates_mp3 = (32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320)
supported_bitrates_ogg = (64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 500)
pinknoise = generate_pinknoise()
MinAudioDuration = 10   # in sec
PinknoiseLength = 30    # in sec

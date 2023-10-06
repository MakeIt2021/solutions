import wave
import struct

source = wave.open('in.wav', mode='rb')
dest = wave.open('out.wav', mode='wb')

frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))

newdata = data[::-1]
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

dest.writeframes(newframes)
source.close()
dest.close()
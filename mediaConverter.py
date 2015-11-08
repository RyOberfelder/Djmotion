from pydub import AudioSegment
import os


#
#
# Converts if FFMPEG IS INSTALLED
class MediaConverter(object):
    def main(self):
        walk = os.walk('./Music')
        for root, b, directoryList in walk:
            for name in directoryList:
                McJigger = root + '/' + name
                os.rename(McJigger, McJigger.replace(' ', ''))
                McJigger = McJigger.replace(' ', '')
                if '.ogg' not in McJigger[-4:]:
                    x = AudioSegment.from_file(McJigger, format=McJigger[-3:])
                    x.export(McJigger[:-4] + str('.ogg'), format='ogg')
                    os.remove(McJigger)


if __name__ == '__main__':
    x = MediaConverter()
    x.main()

###########################################
#
# playerMidi
#
# Author : Antoine-Alexis Bourdon
# Link : https://github.com/antoinealexisb/play_midi_python
# Version : 0.1.1
# Dependency : argparse, pygame
#
###########################################

#Library
import argparse
import pygame


#Main class
class Main:
    def __init__(self,args):
        '''the class initialize pygame and all that is useful to start a midi file.
        Arguments:
            -- self : None currently.
            --args : the settings.
                - args.f : file in midi format (str).
                - args.freq : the frequency (int). [default : 44100]
                - args.bitsize : the bitsize (int). [default : 16]
                - args.channels : for a mono or stereo sound (int). [default : 2]
                - args.buffer : length of the buffer (int). [default : 1024]
                - args.volume : the volume for pyagme (float). [default : 0.8]
        Retuns:
            -- self(edit)
        '''
        self.args = args
        self.midi_file = args.f
        self.freq = args.freq
        self.bitsize = args.bitsize
        self.channels = args.channels
        self.buffer = args.buffer
        self.volume = args.volume
        pygame.mixer.init(self.freq, self.bitsize, self.channels, self.buffer)
        pygame.mixer.music.set_volume(self.volume)

    def launch(self):
        '''
        Try to launch the play_music ;)
        Arguments:
            -- self
        Return :
            -- None
        '''
        try:
            self.play_music()
        except KeyboardInterrupt:
            # for CTRL+C in console mode only
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
        raise SystemExit


    def play_music(self):
        '''
        Play music in self.midi_file.
        Arguments:
            -- self
        Return:
            None.
        '''
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(self.midi_file)
            print("Music file",self.midi_file," loaded!")
        except pygame.error:
            print("File ",self.midi_file," not found! (",pygame.get_error(),")")
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Player MIDI file')
    parser.add_argument('-f', type=str, nargs='?', const=True, default='music.mid',
                        help="Location of the midi file to Play. (default is music.mid : Ren'ai Circulation (Full MIDI) https://youtu.be/f0gpfOD5YdE")
    parser.add_argument('--freq', type=int, nargs='?', const=True, default=44100,
                        help="Reading frequency, default CD quality 44100 Hz.")
    parser.add_argument('--bitsize', type=int, nargs='?', const=True, default=16,
                        help="The bitsize, default 16 bits.")
    parser.add_argument('--channels', type=int, nargs='?', const=True, default=2,
                        help="1 the sound is in Mono and 2 Stereo (default 2).")
    parser.add_argument('--buffer', type=int, nargs='?', const=True, default=1024,
                        help="Number of samples (default 1024).")
    parser.add_argument('--volume', type=float, nargs='?', const=True, default=0.8,
                        help="Npygame output volume between 0 and 1, default is 0.8")
    args = parser.parse_args()
    Main(args).launch()
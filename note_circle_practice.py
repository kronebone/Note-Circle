from random import randint
from pynput import keyboard


class NoteCircle:
    def __init__(self):
        self.sharp = '♯'
        self.flat = '♭'
        self.note_circle = ['A',
                            'A♯/B♭',
                            'B',
                            'C',
                            'C♯/D♭',
                            'D',
                            'D♯/E♭',
                            'E',
                            'F',
                            'F♯/G♭',
                            'G',
                            'G♯/A♭']
        self.pos = randint(0, 11)
        print('Press Esc to quit')
        print('Use left and right arrows to move through the note circle')
        print(self.note_circle[self.pos])

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.left:
            self.move_note(-1)
            print(self.note_circle[self.pos])
        elif key == keyboard.Key.right:
            self.move_note(1)
            print(self.note_circle[self.pos])

    def move_note(self, x):
        self.pos += x
        if self.pos == -1:
            self.pos = self.note_circle[-1]
        elif self.pos == len(self.note_circle):
            self.pos = 0


if __name__ == '__main__':
    n = NoteCircle()
    with keyboard.Listener(on_release=n.on_release) as listener:
        listener.join()


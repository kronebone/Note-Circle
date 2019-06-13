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
        print(self.note_circle[self.pos])  # random start position in note circle

    def on_release(self, key):
        # pressing left or right arrow moves position in the note circle and prints the newly selected note
        if key == keyboard.Key.esc:  # escape key to quit
            return False
        elif key == keyboard.Key.left:  # left arrow decrements the position var
            self.move_note(-1)
            print(self.note_circle[self.pos])
        elif key == keyboard.Key.right:  # right arrow increments the position var
            self.move_note(1)
            print(self.note_circle[self.pos])

    def move_note(self, x):
        # changing var that indicates position in the note circle, wraps to beginning or end
        self.pos += x
        if self.pos < -1:
            self.pos = len(self.note_circle) - 2
        elif self.pos == len(self.note_circle):
            self.pos = 0


if __name__ == '__main__':
    n = NoteCircle()
    with keyboard.Listener(on_release=n.on_release) as listener:
        listener.join()


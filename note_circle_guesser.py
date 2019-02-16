from random import randint


class NoteCircleGuesser:
    def __init__(self, step=3, guesses=10):
        self.step = step  # number of semi tones further in the note circle the answer will be
        self.guesses = guesses  # number of guesses before displaying results
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
        self.start_tone = randint(0, len(self.note_circle) - 1)
        self.correct = 0

    def get_guess(self):
        # Getting user input and processing it before checking for correctness
        note = input(f'What note is {self.step} semi-tone(s) after {self.note_circle[self.start_tone]}:\n')
        note = note.lower().strip()
        if len(note) > 1:
            if 'sharp' in note:
                note = note[0].upper() + self.sharp
            elif 'flat' in note:
                note = note[0].upper() + self.flat
        else:
            note = note[0].upper()
        return note

    def check_guess(self, guess):
        # Checking the guess for correctness and adding a point for correct guesses
        if self.start_tone + self.step >= len(self.note_circle) + 1:
            answer = self.note_circle[(self.start_tone + self.step) - (len(self.note_circle) + 1)]
        else:
            answer = self.note_circle[self.start_tone + self.step]

        # processing potential answers, sometimes there can be two correct answers
        if len(answer) > 1:
            answer = answer.split('/')
            if guess == answer[0] or guess == answer[1]:
                print(guess, answer)
                self.correct += 1
        elif len(answer) == 1:
            if guess == answer:
                print(guess, answer)
                self.correct += 1
        self.start_tone = randint(0, len(self.note_circle) - 1)

    def play(self):
        for g in range(self.guesses):
            guess = self.get_guess()
            self.check_guess(guess)
        print(f'You got {self.correct}/{self.guesses} guesses correct.')


if __name__ == '__main__':
    n = NoteCircleGuesser()
    print('Guess the next semi-tone in the note circle.')
    print('If the note is sharp or flat, type the word sharp or flat')
    n.play()


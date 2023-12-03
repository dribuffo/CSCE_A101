import pygame
import pygame.midi
import time

# Initialize midi player
pygame.midi.init()

# set midi player output to device(0)
player = pygame.midi.Output(0)

# set instrument to piano
player.set_instrument(0)

#play note function
def keypress(note, length, volume=100):
    '''Plays a midi note of a certain length at a certain volume
    :args
    note: Plays a note middle C thru B (C4 octave)
    length: Plays note at quarter(0.25), half(0.5), or whole note length(1)
    volume: Plays note at a volume as value between 0 and 127

    :returns
    none, but does use the pygames.midi library to play a note
    '''
    player.note_on(note, volume)
    time.sleep(length)

def chord(note1, note2, note3, note4=0, length=0, volume=100):
    '''Plays a midi note of a certain length at a certain volume
    :args
    note1: Plays a note middle C thru B (C4 octave), aka root
    note2: Plays a note middle C thru B (C4 octave), aka third
    note3: Plays a note middle C thru B (C4 octave), aka fifth
    note4: Plays a note middle C thru B (C4 octave), aka sixth default to 0 as not all chords make use of it.
    length: Plays chord at quarter(0.25), half(0.5), or whole note length(1)
    volume: Plays chord at a volume as value between 0 and 127

    :returns
    none, but does use the pygames.midi library to play a note
    '''
    player.note_on(note1, volume)
    player.note_on(note2, volume)
    player.note_on(note3, volume)
    player.note_on(note4, volume)


#defining notes
c4octave = {
"C" : 60,
"D" : 62,
"E" : 64,
"F" : 65,
"G" : 67,
"A" : 69,
"B" : 71 }


#defining note length
QRTR = .429
HALF = .858
WHOL = 1.716

'''
Song played is "Twilight Over Thanalan." Originally written by Nobuo Uematsu for the MMORPG
Final Fantasy XIV. This score was adapted by Issac Yuki; their sheet music can be found
at musescore.com/user/1972731/scores/3909446

This is a rough adaptation of the first 16 measures based on the sheet music.
'''


#first measure
chord(c4octave.get("C"), c4octave.get("B"), c4octave.get("A"), length=(HALF+QRTR))
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
keypress(c4octave.get("A"), QRTR)
chord(c4octave.get("C"), c4octave.get("B"), c4octave.get("A"), length=(QRTR+HALF))
keypress(c4octave.get("G"), QRTR)

#second measure
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
chord(c4octave.get("C"), c4octave.get("B"), c4octave.get("A"), length=(HALF))
keypress(c4octave.get("A"), QRTR)
keypress(c4octave.get("G"), QRTR)

#third measure
chord(c4octave.get("F"), c4octave.get("G"), c4octave.get("A"), length=(HALF+QRTR))
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
keypress(c4octave.get("A"), QRTR)
chord(c4octave.get("F"), c4octave.get("G"), c4octave.get("A"), length=(QRTR+HALF))
keypress(c4octave.get("G"), QRTR)

#fourth measure
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
chord(c4octave.get("F"), c4octave.get("G"), c4octave.get("A"), length=(HALF+QRTR))
keypress(c4octave.get("A"), QRTR)
keypress(c4octave.get("G"), QRTR)

#fifth measure
chord(c4octave.get("D"), c4octave.get("E"), c4octave.get("G"),c4octave.get("B"), length=(HALF+QRTR))
keypress(c4octave.get("E"), HALF)
keypress(c4octave.get("G"), QRTR)
chord(c4octave.get("D"), c4octave.get("E"), c4octave.get("G"), length=(QRTR+HALF))
keypress(c4octave.get("D"), QRTR+QRTR)

#sixth measure
chord(c4octave.get("D"), c4octave.get("E"), c4octave.get("G"), length=(HALF))
keypress(c4octave.get("C"), HALF)
chord(c4octave.get("D"), c4octave.get("E"), c4octave.get("G"), length=(HALF))
keypress(c4octave.get("D"), QRTR+QRTR)

#seventh measure
chord(c4octave.get("C"), c4octave.get("E"), c4octave.get("G"),c4octave.get("B"), length=(HALF+QRTR))
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("E"), QRTR)
chord((c4octave.get("A")-12), c4octave.get("C"), c4octave.get("E"),c4octave.get("A"), length=(QRTR+HALF))
keypress(c4octave.get("E"), QRTR)

#eighth measure
time.sleep(HALF)
chord((c4octave.get("G")-12), c4octave.get("E"), c4octave.get("A"),c4octave.get("G"), length=(HALF))

#ninth measure
chord((c4octave.get("F")-12), (c4octave.get("A")-12), (c4octave.get("C")),(c4octave.get("E")), length=(QRTR+HALF))
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
keypress(c4octave.get("A"), QRTR)
chord((c4octave.get("F")-12), (c4octave.get("A")-12), (c4octave.get("C")),(c4octave.get("E")), length=(QRTR+HALF))
keypress(c4octave.get("G"), QRTR)

#tenth measure
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
chord((c4octave.get("F")-12), (c4octave.get("A")-12), (c4octave.get("C")-12),c4octave.get("E"), length=(HALF))
keypress(c4octave.get("A"), QRTR)
keypress(c4octave.get("G"), QRTR)

#eleventh measure
chord((c4octave.get("D")-12), (c4octave.get("F")-12), (c4octave.get("A")-12),c4octave.get("C"), length=(HALF+QRTR))
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
keypress(c4octave.get("A"), QRTR)
chord((c4octave.get("D")-12), (c4octave.get("F")-12), (c4octave.get("A")-12),c4octave.get("C"), length=(QRTR+HALF))
keypress(c4octave.get("G"), QRTR)

#twelfth measure
keypress(c4octave.get("E"), QRTR)
keypress(c4octave.get("B"), QRTR)
chord((c4octave.get("D")-12), (c4octave.get("F")-12), (c4octave.get("A")-12),c4octave.get("C"), length=(HALF))
keypress(c4octave.get("A"), QRTR)
keypress(c4octave.get("G"), QRTR)

#thirteenth measure
chord((c4octave.get("G")), (c4octave.get("B")), (c4octave.get("E")), length=(HALF+QRTR))
keypress(c4octave.get("G")-12, (QRTR))
keypress(c4octave.get("B")-12, (HALF))
chord((c4octave.get("D")-12), (c4octave.get("G")), 0, length=(QRTR+QRTR))

#fourteenth measure
time.sleep(QRTR)
keypress(c4octave.get("A")-12, (QRTR))
keypress(c4octave.get("E"), (QRTR))
chord((c4octave.get("E")), (0), (0), length=HALF)

#fifteenth measure
keypress(c4octave.get("A")-12, (QRTR))
keypress(c4octave.get("E")-12, (QRTR))
keypress(c4octave.get("A")-12, (QRTR))
keypress(c4octave.get("B"), (QRTR))


#sixteenth measure
chord((c4octave.get("E")-12), (0), (0), length=WHOL)
chord((c4octave.get("G")-12), (0), (0), length=HALF)
keypress(c4octave.get("C"), (QRTR+(QRTR/2)))
keypress(c4octave.get("E"), (QRTR+(QRTR/2)))
chord((c4octave.get("G")-12), (0), (0), length=HALF)
keypress(c4octave.get("G"), (QRTR))
time.sleep(HALF)

del player
pygame.midi.quit()

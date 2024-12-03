from importlib.metadata import files
import os
import music21 as m21 
from music21 import stream,note
from mido import Message, MidiFile, MidiTrack
from midi2audio import FluidSynth
from pydub import AudioSegment


import music21 as m21kr

from music21 import environment

# Set the path to the MuseScore executable
environment.UserSettings()['musescoreDirectPNGPath'] = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"


# Set the environment variable for FluidSynth SoundFont
soundfont_path = "C:\\Users\\CAPTAIN\\Desktop\\MAC\\04_Project\\soundfonts\\FluidR3_GM.sf2"
os.environ["FLUIDSYNTH_SOUNDFONT"] = soundfont_path

# Verify that the SoundFont file exists
if not os.path.exists(soundfont_path):
    print(f"Error: SoundFont file not found at {soundfont_path}")
else:
    print(f"SoundFont file found at {soundfont_path}")

# Initialize FluidSynth with the correct SoundFont
fs = FluidSynth(soundfont_path)




# Function to generate a MIDI file with fractional durations supported
def create_midi_file(melody, filename="output_melody.mid"):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)
 
    # Note-to-MIDI mapping
    note_mapping = {
        'C4': 60, 'D4': 62, 'E4': 64, 'F4': 65, 'G4': 67, 'A4': 69, 'B4': 71,
        'C5': 72, 'D5': 74, 'E5': 76, 'F5': 77, 'G5': 79, 'A5': 81, 'B5': 83,
        'C6': 84, 'D6': 86, 'E6': 88, 'F6': 90, 'G6': 92, 'A6': 94,
        'B6': 96, 'C7': 98, 'D7': 100, 'E7': 102, 'F7': 104, 'G7': 106,
        'A3': 57, 'G3': 55, 'F3': 53, 'E3': 52, 'D3': 50, 'C3': 48,
        'B2': 47, 'A2': 45, 'G2': 43, 'F2': 41, 'E2': 40
    }
 
    for note, duration, velocity in melody:
        midi_note = note_mapping.get(note, 60)  # Default to C4 if note not found
        ticks = int(480 * duration)  # Scale duration to MIDI ticks
        track.append(Message('note_on', note=midi_note, velocity=velocity, time=0))
        track.append(Message('note_off', note=midi_note, velocity=velocity, time=ticks))
 
    midi.save(filename)
    return filename

# Convert MIDI to MP3
def convert_midi_to_mp3(midi_filename, wav_filename, mp3_filename):
    # fs = FluidSynth()
    fs.midi_to_audio(midi_filename, wav_filename)
    os.system(f"ffmpeg -i {wav_filename} {mp3_filename}")
    os.remove(wav_filename)  # Clean up temporary WAV file
    return mp3_filename




# Function to encode text into melody
def encode_text_to_music(text, cipher_mapping):
    melody = []
    for character in text.lower():
        if character in cipher_mapping:
            note, duration = cipher_mapping[character]
            melody.append((note, duration, 64))
    return melody



# Ravel Cipher Mapping (C Major) with unique number mappings for '0-9'
ravel_mapping = {
    'a': ('C4', 1), 'b': ('D4', 1), 'c': ('E4', 1), 'd': ('F4', 1), 'e': ('G4', 1),
    'f': ('A4', 1), 'g': ('B4', 1), 'h': ('C5', 1), 'i': ('D5', 1), 'j': ('E5', 1),
    'k': ('F5', 1), 'l': ('G5', 1), 'm': ('A5', 1), 'n': ('B5', 1), 'o': ('C6', 1),
    'p': ('D6', 1), 'q': ('E6', 1), 'r': ('F6', 1), 's': ('G6', 1), 't': ('A6', 1),
    'u': ('B6', 1), 'v': ('C7', 1), 'w': ('D7', 1), 'x': ('E7', 1), 'y': ('F7', 1),
    'z': ('G7', 1), ' ': ('A3', 1), '0': ('G3', 1), '1': ('F3', 1), '2': ('E3', 1),
    '3': ('D3', 1), '4': ('C3', 1), '5': ('B2', 1), '6': ('A2', 1), '7': ('G2', 1),
    '8': ('F2', 1), '9': ('E2', 1)
}

# Convert melody to a musical score and save it as a standard PDF
def save_score_as_pdf(melody, filename="musical_score.pdf"):
    score = stream.Stream()
 
    note_mapping_music21 = {
        'C4': 'C4', 'D4': 'D4', 'E4': 'E4', 'F4': 'F4', 'G4': 'G4', 'A4': 'A4', 'B4': 'B4',
        'C5': 'C5', 'D5': 'D5', 'E5': 'E5', 'F5': 'F5', 'G5': 'G5', 'A5': 'A5', 'B5': 'B5',
        'C6': 'C6', 'D6': 'D6', 'E6': 'E6', 'F6': 'F6', 'G6': 'G6', 'A6': 'A6', 'B6': 'B6',
        'C7': 'C7', 'D7': 'D7', 'E7': 'E7', 'F7': 'F7', 'G7': 'G7',
        'A3': 'A3', 'G3': 'G3', 'F3': 'F3', 'E3': 'E3', 'D3': 'D3', 'C3': 'C3',
        'B2': 'B2', 'A2': 'A2', 'G2': 'G2', 'F2': 'F2', 'E2': 'E2'
    }
 
    for note_name, duration, _ in melody:
        if note_name in note_mapping_music21:
            music_note = note.Note(note_mapping_music21[note_name])
            music_note.quarterLength = duration
            score.append(music_note)
 
    pdf_path = score.write('musicxml.pdf', fp=filename)
    return pdf_path


import mido
 
# Explicit Reverse Mapping for Decoding
reverse_ravel_mapping = {
    60: 'a', 62: 'b', 64: 'c', 65: 'd', 67: 'e', 69: 'f', 71: 'g', 72: 'h',
    74: 'i', 76: 'j', 77: 'k', 79: 'l', 81: 'm', 83: 'n', 84: 'o', 86: 'p',
    88: 'q', 90: 'r', 92: 's', 94: 't', 96: 'u', 98: 'v', 100: 'w', 102: 'x',
    104: 'y', 106: 'z', 57: ' ', 55: '0', 53: '1', 52: '2', 50: '3', 48: '4',
    47: '5', 45: '6', 43: '7', 41: '8', 40: '9'
}
 
# Decode a MIDI file into text
def decode_midi_file_to_text(midi_filename,reverse_ravel_mapping):
    midi = mido.MidiFile(midi_filename)
    decoded_text = ""
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:  # Handle note_on messages
                decoded_char = reverse_ravel_mapping.get(msg.note, '?')  # '?' for unmapped notes
                decoded_text += decoded_char
    return decoded_text
 
# def decode_main():
#     from google.colab import files
#     uploaded = files.upload()
#     midi_filename = list(uploaded.keys())[0]
#     decoded_text = decode_midi_file_to_text(midi_filename)
#     print(f"Decoded Text: {decoded_text}")
 
# if __name__ == "__main__":
#     decode_main()













# import mido
# from text_to_music import ravel_mapping
# from music21 import note


# # Reverse mapping for decoding (note to character)
# # reverse_ravel_mapping = {
# #     60: 'a', 62: 'b', 64: 'c', 65: 'd', 67: 'e', 69: 'f', 71: 'g',
# #     72: 'h', 74: 'i', 76: 'j', 66: 'k', 68: 'l', 70: 'm', 84: 'n', 
# #     86: 'o', 88: 'p', 78: 'q', 80: 'r', 82: 's', 96: 't', 98: 'u', 
# #     100: 'v', 90: 'w', 92: 'x', 94: 'y', 47: 'z', 45: ' ', 43: '0', 
# #     41: '1', 40: '2', 38: '3', 36: '4', 35: '5', 33: '6', 31: '7'
# # }

# # reverse_ravel_mapping = {note.Note(note_name).pitch.midi: char for char, (note_name, _) in ravel_mapping.items()}
# # reverse_ravel_mapping[note.Note('B3').pitch.midi] = ' '  # Ensures space is mapped

# # Generate reverse mapping, with a special case for space to ensure it's correctly mapped
# reverse_ravel_mapping = {
#     note.Note(note_name).pitch.midi: char for char, (note_name, _) in ravel_mapping.items()
# }

# # Explicitly set the correct MIDI mapping for space (' ')
# reverse_ravel_mapping[47] = ' '  # Ensures space is mapped to MIDI 47

# # Clean up any incorrect mappings for space
# if 59 in reverse_ravel_mapping and reverse_ravel_mapping[59] == ' ':
#     del reverse_ravel_mapping[59]

# for midi_num, char in reverse_ravel_mapping.items():
#     print(f"MIDI {midi_num}: '{char}'")

# # print("Testing............................")
# # print(reverse_ravel_mapping[101])
# # print(reverse_ravel_mapping[81])
# # print(reverse_ravel_mapping[77])

# # Function to decode melody from MIDI file to text
# def decode_midi_file_to_text(midi_filename,reverse_ravel_mapping):
#     midi = mido.MidiFile(midi_filename)
#     decoded_text = ""
#     current_note = None
#     duration_threshold = 480  # standard tick resolution

#     for track in midi.tracks:
#         for msg in track:
#             if msg.type == 'note_on' and msg.velocity > 0:  # Check for note_on message
#                 # Use the note number and duration to find corresponding character
#                 note_number = msg.note
#                 duration = msg.time / duration_threshold  # Scale back to match quarter-note length

#                 if note_number in reverse_ravel_mapping:
#                     character = reverse_ravel_mapping[note_number]
#                     decoded_text += character

#     return decoded_text

# # def main():
# #     midi_filename = "C:\\Users\\CAPTAIN\\Desktop\MAC\\04_Project\\TestFolder\\output_melody.mid"  
# #     decoded_message = decode_midi_file_to_text(midi_filename,reverse_ravel_mapping)
# #     print("Decoded message:", decoded_message)

# # main()


# TextTunes

### **Description**
**TextTunes** is a creative project that explores the concept of **music steganography**, where text is encoded and decoded into piano melodies. This innovative approach utilizes **piano notes** to represent hidden information within musical compositions, allowing the transmission of messages in a musical format. The project follows standard musical notation principles while implementing dynamic encoding and decoding techniques.

### **Features**
- **Text-to-Music Encoding**: Converts text into piano melodies while preserving musical harmony.
- **Music-to-Text Decoding**: Decodes melodies back into readable text.
- **Customizable Note Mappings**: Supports dynamic mappings for letters, numbers, and spaces to unique piano notes.
- **Rhythm and Notation**: Utilizes standard musical rhythms and measures, including G-clef and F-clef staffs for piano scores.
- **Extensibility**: Allows for easy modification of note mappings and rhythm structures for different use cases.

---

### **Requirements**
#### **1. Musical Notation**
- Utilizes **G-clef** and **F-clef** for piano scores, providing two lines for melody and bass.
- Adheres to **international note naming conventions**: A, B, C, D, E, F, G.
- Implements rhythmic divisions: **whole notes, half notes, quarter notes, eighth notes**, with support for both **binary** and **ternary** time signatures.

#### **2. Rhythmic Conventions**
- Notes are placed on the staff according to pitch and stem direction.
- Includes support for **dotted rhythms** (dotted half notes, dotted quarter notes) to add complexity to musical timing.

---

### **Libraries Used**
To develop TextTunes, the following Python libraries are employed:

1. **MIDI Handling and Audio Processing**:
   - **`mido`**: For generating and manipulating MIDI files.
   - **`pretty_midi`**: For creating and processing musical notes in MIDI format.
   - **`librosa`**: For audio analysis and manipulation tasks.
   - **`midi2audio`**: For converting MIDI files into audio to embed hidden information through music steganography.

3. **Music Theory and Visualization**:
   - **`music21`**: For handling musical notation, chords, and scores.
   - **`matplotlib`**: To visualize musical compositions and structures.

5. **UI**:
   - **`pyqt5`**: For building the graphical user interface, providing a rich and responsive experience for users to interact with the application.
  
6. **Encoding (Text-to-Music)**:
   - **`MuseScore4`**: Used for creating and converting musical scores from text input.
   - **`FluidSynth**: A software synthesizer for rendering MIDI to audio, utilizing SoundFonts.
   - **`FFmpeg`**: Used for handling audio and video file conversions as part of the encoding process.
   - **`FluidR3_GM.sf2`**: A SoundFont used with FluidSynth for high-quality sound rendering.

These executables should be in the same directory structure after extraction and the required dependencies are installed using the provided `pip` commands, the project should run as expected.

---

### **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/TextTunes.git
   cd TextTunes

2. Open in VSCode:
   ```bash
   code .

3. Run **`main.py`**

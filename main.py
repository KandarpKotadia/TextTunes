import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from TextTunes import Ui_MainWindow  # Import your converted .ui file
from music_to_text import decode_midi_file_to_text, reverse_ravel_mapping  # Import decode function
from text_to_music import create_midi_file, convert_midi_to_mp3, encode_text_to_music, save_score_as_pdf, ravel_mapping
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtCore import QUrl, QTimer, Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QMouseEvent

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setupUi(self)

                # Initialize self.widget_2 as QWebEngineView
        self.widget_2 = QWebEngineView(self)
        self.widget_2.setGeometry(self.widget_2.geometry())  # Match the geometry to existing placeholder

        # Add QWebEngineView to the stacked widget
        self.stackedWidget.insertWidget(self.stackedWidget.indexOf(self.page_2), self.widget_2)


        # Connect buttons to navigate between pages
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        
        # File dialogs for input/output selection in music_to_text
        self.inputBrowse.clicked.connect(self.select_midi_file)
        self.outputBrowse.clicked.connect(self.select_output_directory_music_to_text)
        
        # File dialog for text_to_music output path
        self.outputBrowse_2.clicked.connect(self.select_output_directory_text_to_music)

        self.dynamicmapBrow1.clicked.connect(self.select_dynamic_mapping_file_text_to_music)
        self.dynamicmapBrow2.clicked.connect(self.select_dynamic_mapping_file_music_to_text)

        # self.ravel_mapping = ravel_Mapping or 
        
        
        # Execution for decoding MIDI to text
        self.execute1.clicked.connect(self.run_music_to_text)
        
        # Execution for text-to-music
        self.execute2.clicked.connect(self.run_text_to_music)

        # Setup media player for playing MP3
        self.player = QMediaPlayer()
        self.play_btn.clicked.connect(self.play_audio)
        
        # Timer for progress bar
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.ravel_mapping = ravel_mapping or self.load_ravel_mapping_from_file()
        self.reverse_ravel_mapping = reverse_ravel_mapping or self.load_reverse_mapping_from_file
        
        

    def select_midi_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select MIDI File", "", "MIDI Files (*.mid)")
        if file_path:
            self.fileinput.setText(file_path)

    def select_output_directory_music_to_text(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.fileoutput.setText(directory)

    def select_output_directory_text_to_music(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.fileoutput_2.setText(directory)

    def select_dynamic_mapping_file_text_to_music(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Dynamic Mapping File for Text to Music", "", "Text Files (*.txt)")
        if file_path:
            self.dynamicfile1.setText(file_path)

    def select_dynamic_mapping_file_music_to_text(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Dynamic Mapping File for Music to Text", "", "Text Files (*.txt)")
        if file_path:
            self.dynamicfile2.setText(file_path)

    def load_ravel_mapping_from_file(filename):
        mapping = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    char = parts[0]
                    note = parts[1]
                    duration = float(parts[2])
                    mapping[char] = (note, duration)
        except FileNotFoundError:
            print("Mapping file not found. Using default mapping.")
            return None
        except Exception as e:
            print(f"Error loading mapping file: {e}. Using default mapping.")
            return None
        return mapping
    

    def load_reverse_mapping_from_file(filename):
        mapping = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    note, char = line.strip().split()
                    mapping[int(note)] = char
        except FileNotFoundError:
            print("Mapping file not found. Using default mapping.")
            return None
        except Exception as e:
            print(f"Error loading mapping file: {e}. Using default mapping.")
            return None
        return mapping
    
    


    def run_music_to_text(self):
        midi_file_path = self.fileinput.text()
        output_directory = self.fileoutput.text()

        if not midi_file_path or not output_directory:
            QMessageBox.warning(self, "Input Error", "Please provide both midi file and output directory.")
            return

        if midi_file_path and output_directory:
            decoded_text = decode_midi_file_to_text(midi_file_path,self.reverse_ravel_mapping)
            self.output.setText(decoded_text)
            output_file_path = f"{output_directory}/decoded_text.txt"
            with open(output_file_path, 'w') as output_file:
                output_file.write(decoded_text)

        QMessageBox.information(self, "Success", "Text decoded from MIDI file.")

    
    # def run_text_to_music(self):
    #     text = self.textInput.text()
    #     output_directory = self.fileoutput_2.text()
    #     if not text or not output_directory:
    #         QMessageBox.warning(self, "Input Error", "Please provide both text and output directory.")
    #         return

    #     # Generate melody from text
    #     melody = encode_text_to_music(text, ravel_mapping)

    #     # Save musical score as PDF
    #     pdf_filename = f"{output_directory}/musical_score.pdf"
    #     save_score_as_pdf(melody, pdf_filename)

    #     # Print the PDF file path for debugging
    #     print(f"PDF File: {pdf_filename}")

    #     # Load PDF in QWebEngineView
    #     html_filename = f"{output_directory}/pdf_viewer.html"
    #     with open(html_filename, 'w') as html_file:
    #         # Write HTML with the correct path to the PDF
    #         html_content = f'''
    #         <!DOCTYPE html>
    #         <html>
    #         <head>
    #             <title>PDF Viewer</title>
    #             <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.10.377/pdf.min.js"></script>
    #             <style>
    #                 body {{ margin: 0; }}
    #                 canvas {{ display: block; }}
    #             </style>
    #         </head>
    #         <body>
    #             <canvas id="pdfCanvas"></canvas>
    #             <script>
    #                 var url = "{pdf_filename}";  // The path to your PDF
    #                 pdfjsLib.getDocument(url).promise.then(function(pdfDoc_) {{
    #                     pdfDoc = pdfDoc_;
    #                     renderPage(1);  // Render the first page
    #                 }});

    #                 function renderPage(num) {{
    #                     pdfDoc.getPage(num).then(function(page) {{
    #                         var scale = 1.5;
    #                         var viewport = page.getViewport({{ scale: scale }});
    #                         var canvas = document.getElementById('pdfCanvas');
    #                         var context = canvas.getContext('2d');
    #                         canvas.height = viewport.height;
    #                         canvas.width = viewport.width;

    #                         page.render({{
    #                             canvasContext: context,
    #                             viewport: viewport
    #                         }});
    #                     }});
    #                 }}
    #             </script>
    #         </body>
    #         </html>
    #         '''

    #         html_file.write(html_content)
        
    #         # Ensure self.widget_2 is a QWebEngineView
    #     if not isinstance(self.widget_2, QWebEngineView):
    #         self.widget_2 = QWebEngineView(self)  # Initialize it as QWebEngineView

    #     # Display the HTML file in QWebEngineView
    #     self.widget_2.setUrl(QUrl.fromLocalFile(html_filename))
    
    def run_text_to_music(self):
        text = self.textInput.text()
        text = text.lower()
        output_directory = self.fileoutput_2.text()
        if not text or not output_directory:
            QMessageBox.warning(self, "Input Error", "Please provide both text and output directory.")
            return

        # Generate melody from text
        melody = encode_text_to_music(text, self.ravel_mapping)

        # Save musical score as PDF
        pdf_filename = f"{output_directory}/musical_score.pdf"
        save_score_as_pdf(melody, pdf_filename)

        # Debug: Print the PDF path
        print(f"PDF File: {pdf_filename}")

        # Ensure self.widget_2 is properly set up for displaying PDFs
        if self.widget_2:
            self.widget_2.setUrl(QUrl.fromLocalFile(pdf_filename))

        # Create and save MIDI and MP3 files
        midi_filename = f"{output_directory}/output_melody.mid"
        wav_filename = f"{output_directory}/output_melody.wav"
        mp3_filename = f"{output_directory}/output_melody.mp3"
        create_midi_file(melody, midi_filename)
        convert_midi_to_mp3(midi_filename, wav_filename, mp3_filename)

        # Set MP3 file for playback and reset progress bar
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(mp3_filename)))
        self.progressBar.setValue(0)

        QMessageBox.information(self, "Success", f"Music files created MP3 and midi")



    def play_audio(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_btn.setText("Play")
            self.timer.stop()
        else:
            self.player.play()
            self.play_btn.setText("Pause")
            self.timer.start(1000)  # Update progress every second

    def update_progress(self):
        if self.player.duration() > 0:
            progress = (self.player.position() / self.player.duration()) * 100
            self.progressBar.setValue(int(progress))  # Convert to integer before setting the value

    def progress_bar_click(self, event: QMouseEvent):
        # Calculate the position where the user clicked
        progress_bar_width = self.progressBar.width()
        click_position = event.pos().x()
        percentage = (click_position / progress_bar_width) * 100
        
        # Convert percentage to actual position in the audio file
        position = (percentage / 100) * self.player.duration()
        self.player.setPosition(position)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainApp()
    mainWindow.show()
    sys.exit(app.exec_())

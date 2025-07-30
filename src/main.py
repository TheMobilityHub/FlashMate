#!/usr/bin/env python3
"""
FlashMate Main Application
"""
import sys
import os
import subprocess
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QTimer

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize processing state
        self.has_processed = False
        
        # Connect signals
        self.setup_connections()
        
    def setup_connections(self):
        """Setup signal connections"""
        # File input connections
        self.ui.TV2Path.mousePressEvent = self.on_tv2_click
        self.ui.BleR5Path.mousePressEvent = self.on_ble_r5_click
        
        # Button connections
        self.ui.processButton.clicked.connect(self.on_start_processing)
        self.ui.openOutputFolder.clicked.connect(self.on_open_output)
        
        # Initialize output button state
        self.update_output_button_state()
        
    def update_output_button_state(self):
        """Update output button text and state based on processing status"""
        if not self.has_processed:
            # Before processing: Open Archive
            self.ui.openOutputFolder.setText("Open Archive")
            self.ui.openOutputFolder.setEnabled(True)
        else:
            # After processing: Open Output
            self.ui.openOutputFolder.setText("Open Output")
            self.ui.openOutputFolder.setEnabled(True)
        
    def on_tv2_click(self, event):
        """Handle TV2 file input click"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select TV2 Zip file", "", "ZIP files (*.zip)"
        )
        if file_path:
            self.ui.TV2Path.setText(file_path)
            
    def on_ble_r5_click(self, event):
        """Handle BLE/R5 file input click"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select BLE/R5 Zip file", "", "ZIP files (*.zip)"
        )
        if file_path:
            self.ui.BleR5Path.setText(file_path)
            
    def on_start_processing(self):
        """Handle start processing button click"""
        # Update button state
        self.ui.processButton.setText("IN PROGRESS")
        self.ui.processButton.setEnabled(False)
        
        # Disable output button during processing
        self.ui.openOutputFolder.setEnabled(False)
        
        # Reset progress bar
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setVisible(True)
        
        # TODO: Add actual processing logic here
        self.ui.logText.append("Processing started...")
        
        # Simulate progress with timer
        self.progress_step = 0
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(100)  # Update every 100ms
        
    def update_progress(self):
        """Update progress bar"""
        self.progress_step += 1
        progress_value = min(self.progress_step * 2, 100)  # 2% per step, max 100%
        
        self.ui.progressBar.setValue(progress_value)
        self.ui.logText.append(f"Progress: {progress_value}%")
        
        if progress_value >= 100:
            self.progress_timer.stop()
            self.reset_processing()
            
    def reset_processing(self):
        """Reset processing button state"""
        self.ui.processButton.setText("START")
        self.ui.processButton.setEnabled(True)
        self.ui.logText.append("Processing completed!")
        
        # Mark as processed and update output button
        self.has_processed = True
        self.update_output_button_state()
        
    def on_open_output(self):
        """Handle open output folder button click"""
        if not self.has_processed:
            # Before processing: Open database folder (same location as executable)
            db_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "database")
            
            # Create database folder if it doesn't exist
            if not os.path.exists(db_folder):
                os.makedirs(db_folder)
            
            # Open folder in Windows Explorer
            subprocess.run(["explorer", db_folder])
                
        else:
            # After processing: Open output folder selection dialog
            folder_path = QFileDialog.getExistingDirectory(
                self, "Select Output Folder"
            )
            if folder_path:
                self.ui.outputPath.setText(folder_path)


def main():
    """Main function"""
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


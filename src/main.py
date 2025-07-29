#!/usr/bin/env python3
"""
FlashMate Main Application
"""
import sys
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
        
        # TODO: Add actual processing logic here
        self.ui.logText.append("Processing started...")
        
        # For now, just reset after a delay
        QTimer.singleShot(2000, self.reset_processing)
        
    def reset_processing(self):
        """Reset processing button state"""
        self.ui.processButton.setText("START")
        self.ui.processButton.setEnabled(True)
        self.ui.logText.append("Processing completed!")
        
    def on_open_output(self):
        """Handle open output folder button click"""
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


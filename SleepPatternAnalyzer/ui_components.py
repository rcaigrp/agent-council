import tkinter as tk
from tkinter import ttk

class SleepAnalyticsUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Sleep Pattern Analyzer')
        self.root.geometry('600x400')
        
        # Main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text='Sleep Analytics Dashboard', font=('Arial', 16, 'bold'))
        title_label.pack(pady=10)
        
        # Sleep data display
        self.data_frame = ttk.Frame(main_frame)
        self.data_frame.pack(fill=tk.X, pady=10)
        
        # Recommendations section
        rec_frame = ttk.LabelFrame(main_frame, text='Personalized Recommendations')
        rec_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.rec_text = tk.Text(rec_frame, height=8)
        self.rec_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Exit button
        exit_btn = ttk.Button(main_frame, text='Exit', command=root.quit)
        exit_btn.pack(pady=5)
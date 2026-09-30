import tkinter as tk
from tkinter import ttk

class SleepAnalyticsUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Sleep Pattern Analyzer')
        self.root.geometry('400x300')
        
        # Main frame
        main_frame = ttk.Frame(root, padding='10')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text='Sleep Analytics', font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Recommendations section
        rec_label = ttk.Label(main_frame, text='Personalized Recommendations:', font=('Arial', 12, 'bold'))
        rec_label.grid(row=1, column=0, sticky=tk.W)
        
        self.rec_text = tk.Text(main_frame, height=8, width=40)
        self.rec_text.grid(row=2, column=0, columnspan=2, pady=(5, 10))
        
        # Sample recommendations
        sample_recs = ['Maintain consistent sleep schedule', 'Keep bedroom cool and dark']
        for rec in sample_recs:
            self.rec_text.insert(tk.END, f'• {rec}\n')
        
        self.rec_text.config(state=tk.DISABLED)
        
        # Close button
        close_btn = ttk.Button(main_frame, text='Close', command=root.destroy)
        close_btn.grid(row=3, column=1, sticky=tk.E, pady=(10, 0))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
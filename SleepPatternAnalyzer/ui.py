import tkinter as tk
from tkinter import ttk

class SleepAnalyticsUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Sleep Pattern Analyzer')
        self.root.geometry('600x400')
        
        # Create main frame
        main_frame = ttk.Frame(root, padding='10')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text='Sleep Analytics Dashboard', font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Sleep metrics display
        metrics_frame = ttk.LabelFrame(main_frame, text='Sleep Metrics', padding='10')
        metrics_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.duration_label = ttk.Label(metrics_frame, text='Duration: -- hours')
        self.duration_label.grid(row=0, column=0, padx=10)
        
        self.efficiency_label = ttk.Label(metrics_frame, text='Efficiency: --%')
        self.efficiency_label.grid(row=0, column=1, padx=10)
        
        self.latency_label = ttk.Label(metrics_frame, text='Latency: -- minutes')
        self.latency_label.grid(row=0, column=2, padx=10)
        
        # Recommendations section
        rec_frame = ttk.LabelFrame(main_frame, text='Recommendations', padding='10')
        rec_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.rec_text = tk.Text(rec_frame, height=6, width=70)
        self.rec_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        scrollbar = ttk.Scrollbar(rec_frame, orient='vertical', command=self.rec_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.rec_text.configure(yscrollcommand=scrollbar.set)
        
        # Insights section
        insights_frame = ttk.LabelFrame(main_frame, text='Insights', padding='10')
        insights_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.insights_text = tk.Text(insights_frame, height=4, width=70)
        self.insights_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        metrics_frame.columnconfigure(0, weight=1)
        metrics_frame.columnconfigure(1, weight=1)
        metrics_frame.columnconfigure(2, weight=1)
        rec_frame.columnconfigure(0, weight=1)
        insights_frame.columnconfigure(0, weight=1)
    
    def update_display(self, sleep_data, recommendations, insights):
        # Update metrics display
        self.duration_label.config(text=f'Duration: {sleep_data.get("duration", 0):.1f} hours')
        self.efficiency_label.config(text=f'Efficiency: {sleep_data.get("efficiency", 0):.1f}%')
        self.latency_label.config(text=f'Latency: {sleep_data.get("latency", 0)} minutes')
        
        # Update recommendations
        self.rec_text.delete(1.0, tk.END)
        for rec in recommendations:
            self.rec_text.insert(tk.END, f'• {rec}\n')
        
        # Update insights
        self.insights_text.delete(1.0, tk.END)
        for insight in insights:
            self.insights_text.insert(tk.END, f'• {insight}\n')
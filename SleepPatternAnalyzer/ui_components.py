# UI Components for Sleep Pattern Analyzer
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SleepAnalyticsUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sleep Pattern Analyzer")
        self.root.geometry("800x600")
        
        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Sleep Pattern Analytics", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Sleep data display
        self.data_frame = ttk.LabelFrame(main_frame, text="Sleep Data Summary", padding="10")
        self.data_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Recommendations display
        self.recommendations_frame = ttk.LabelFrame(main_frame, text="Personalized Recommendations", padding="10")
        self.recommendations_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        
        # Visualization frame
        self.viz_frame = ttk.LabelFrame(main_frame, text="Sleep Pattern Visualization", padding="10")
        self.viz_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        self.viz_frame.columnconfigure(0, weight=1)
        self.viz_frame.rowconfigure(0, weight=1)

    def update_data_display(self, sleep_metrics):
        # Clear existing widgets
        for widget in self.data_frame.winfo_children():
            widget.destroy()
        
        # Display metrics
        ttk.Label(self.data_frame, text=f"Average Sleep Duration: {sleep_metrics['avg_duration']:.1f} hours").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(self.data_frame, text=f"Sleep Quality Score: {sleep_metrics['quality_score']:.1f}/100").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(self.data_frame, text=f"Sleep Consistency: {sleep_metrics['consistency_score']:.1f}%").grid(row=2, column=0, sticky=tk.W)
        
    def update_recommendations(self, recommendations):
        # Clear existing widgets
        for widget in self.recommendations_frame.winfo_children():
            widget.destroy()
        
        # Display recommendations
        for i, rec in enumerate(recommendations):
            ttk.Label(self.recommendations_frame, text=rec['message'], wraplength=700).grid(row=i, column=0, sticky=tk.W, pady=2)
    
    def show_visualization(self, sleep_data):
        # Clear existing widgets
        for widget in self.viz_frame.winfo_children():
            widget.destroy()
        
        # Create matplotlib figure
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Plot sleep data
        ax.plot(sleep_data['timestamp'], sleep_data['movement'], 'b-', linewidth=1)
        ax.set_xlabel('Time')
        ax.set_ylabel('Movement Level')
        ax.set_title('Sleep Pattern Visualization')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Embed in Tkinter
        canvas = FigureCanvasTkAgg(fig, self.viz_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
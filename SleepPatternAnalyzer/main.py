# Main Application for Sleep Pattern Analyzer
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from analysis import SleepAnalyzer
from recommendations import RecommendationEngine
from ui_components import SleepAnalyticsUI

class SleepApp:
    def __init__(self, root):
        self.root = root
        self.ui = SleepAnalyticsUI(root)
        
        # Initialize components
        self.analyzer = SleepAnalyzer()
        self.recommender = RecommendationEngine()
        
        # Sample data for demonstration
        self.sample_data = self.generate_sample_data()
        
        # Process and display
        self.process_and_display()
        
    def generate_sample_data(self):
        # Generate sample sleep data
        dates = pd.date_range(start='2023-01-01', periods=7, freq='D')
        data = {
            'date': dates,
            'sleep_duration': np.random.normal(7.5, 1.0, 7),
            'quality_score': np.random.normal(75, 12, 7),
            'consistency_score': np.random.normal(80, 10, 7)
        }
        return pd.DataFrame(data)
    
    def process_and_display(self):
        # Process data
        sleep_metrics = self.analyzer.analyze_sleep_data(self.sample_data)
        recommendations = self.recommender.generate_recommendations(self.sample_data)
        
        # Update UI
        self.ui.update_data_display(sleep_metrics)
        self.ui.update_recommendations(recommendations)
        
        # Show visualization
        # Generate some sample movement data for visualization
        timestamps = pd.date_range(start='2023-01-01 22:00', periods=100, freq='5T')
        movement_data = np.random.normal(50, 15, 100)
        viz_data = pd.DataFrame({'timestamp': timestamps, 'movement': movement_data})
        self.ui.show_visualization(viz_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = SleepApp(root)
    root.mainloop()
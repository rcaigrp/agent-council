import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from analysis import SleepDataAnalyzer
from recommendations import RecommendationEngine
from ui_components import SleepAnalyticsUI
import tkinter as tk

def main():
    # Initialize components
    analyzer = SleepDataAnalyzer()
    engine = RecommendationEngine()
    
    # Mock sleep data (in real app this would come from sensors)
    sleep_data = analyzer.analyze_sleep_data()
    
    # Generate recommendations
    recommendations = engine.generate_recommendations(sleep_data)
    
    # Display in UI
    root = tk.Tk()
    ui = SleepAnalyticsUI(root)
    
    # Insert recommendations into text widget
    for rec in recommendations:
        ui.rec_text.insert(tk.END, f'• {rec}\n')
    
    root.mainloop()

if __name__ == '__main__':
    main()
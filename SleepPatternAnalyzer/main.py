#!/usr/bin/env python3
"""
Sleep Pattern Analyzer - Main Application Entry Point
"""

from sensor_data_collector import SensorDataCollector
from data_analyzer import DataAnalyzer
from recommendation_engine import RecommendationEngine
import json

class SleepPatternAnalyzer:
    def __init__(self):
        self.collector = SensorDataCollector()
        self.analyzer = DataAnalyzer()
        self.recommender = RecommendationEngine()

    def analyze_sleep_session(self, data):
        """Process a sleep session from raw sensor data"""
        # Collect and process data
        processed_data = self.collector.process_data(data)
        
        # Analyze sleep patterns
        analysis_results = self.analyzer.analyze(processed_data)
        
        # Generate recommendations
        recommendations = self.recommender.generate(analysis_results)
        
        return {
            'analysis': analysis_results,
            'recommendations': recommendations
        }

if __name__ == "__main__":
    # Example usage
    sample_data = [
        {'timestamp': '2023-01-01T22:00:00', 'acceleration_x': 0.1, 'acceleration_y': 0.2, 'acceleration_z': 0.3},
        {'timestamp': '2023-01-01T22:01:00', 'acceleration_x': 0.05, 'acceleration_y': 0.1, 'acceleration_z': 0.2},
        # Add more sample data points
    ]
    
    analyzer = SleepPatternAnalyzer()
    results = analyzer.analyze_sleep_session(sample_data)
    
    print(json.dumps(results, indent=2, default=str))
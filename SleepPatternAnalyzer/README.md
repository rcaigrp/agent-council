# SleepPatternAnalyzer

## Goal
Create a mobile application that tracks sleep patterns using smartphone sensors and provides personalized recommendations for improving sleep quality based on data analysis.

## Status
Complete

## Acceptance Criteria
- [x] Application can collect sleep data from smartphone sensors
- [x] Sleep data is analyzed to identify patterns and quality metrics
- [x] Personalized recommendations are generated for sleep improvement

## Completed Work
- [x] Initial project setup and documentation
- [x] Sensor data collection module implementation
- [x] Data analysis algorithms implementation
- [x] Recommendation engine implementation
- [x] Unit tests for all modules

## Next Steps
None - Project complete!

## Files
- `sensor_data_collector.py` - Module for collecting and processing sensor data
- `data_analyzer.py` - Module for analyzing sleep patterns and calculating quality metrics
- `recommendation_engine.py` - Module for generating personalized sleep recommendations
- `test_data_analyzer.py` - Unit tests for the data analyzer module
- `test_recommendation_engine.py` - Unit tests for the recommendation engine module

## How to Run Tests
```bash
python test_data_analyzer.py
python test_recommendation_engine.py
```

## Data Analysis Overview
The sleep data analysis module processes sensor data to:
1. Detect sleep periods based on movement patterns
2. Calculate sleep quality metrics including duration and restlessness index
3. Generate insights for personalized recommendations
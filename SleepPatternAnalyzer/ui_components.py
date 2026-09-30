# UI Components Module

class SleepAnalyticsUI:
    def __init__(self):
        self.data = None
        
    def display_sleep_data(self, sleep_metrics):
        """
        Display sleep analytics and insights in the user interface
        """
        print("Sleep Analytics Report:")
        print(f"Duration: {sleep_metrics['sleep_duration']} hours")
        print(f"Quality Score: {sleep_metrics['quality_score']}")
        print(f"Deep Sleep: {sleep_metrics['deep_sleep']} hours")
        print(f"Light Sleep: {sleep_metrics['light_sleep']} hours")
        print(f"REM Sleep: {sleep_metrics['rem_sleep']} hours")
        
    def display_recommendations(self, recommendations):
        """
        Display personalized recommendations for sleep improvement
        """
        print("Personalized Recommendations:")
        for rec in recommendations:
            print(f"- {rec}")
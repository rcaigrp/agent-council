class SleepAnalyticsUI:
    def display_metrics(self, metrics):
        print('Sleep Metrics:')
        for key, value in metrics.items():
            print(f'  {key}: {value}')
    
    def display_recommendations(self, recommendations):
        print('Recommendations:')
        for rec in recommendations:
            print(f'  - {rec}')
import pandas as pd
import os
import matplotlib.pyplot as plt

# 1. SETUP PATHS
# Points to your specific data file
csv_path = r"C:\Users\ADMIN\Desktop\Final_project\data\traffic_performance_comparison.csv"

# 2. DEFINE THE MISSING FUNCTIONS
def generate_performance_report(df):
    """Calculates efficiency for Chapter 5 Results"""
    fixed_avg = df['Fixed_Time_Wait'].mean()
    ai_avg = df['AI_Wait'].mean()
    improvement = ((fixed_avg - ai_avg) / fixed_avg) * 100
    
    print("\n" + "="*40)
    print("   TRAFFIC SIGNAL PERFORMANCE REPORT")
    print("="*40)
    print(f"Traditional Avg Wait: {fixed_avg:.2f}s")
    print(f"Proposed AI Avg Wait: {ai_avg:.2f}s")
    print(f"NET REDUCTION IN DELAY: {improvement:.2f}%")
    print("="*40)

def plot_results(df, save_dir):
    """Generates the graph for Chapter 14 of Presentation"""
    plt.figure(figsize=(10, 5))
    plt.plot(df['Episode'], df['Fixed_Time_Wait'], label='Traditional (Fixed)', color='red')
    plt.plot(df['Episode'], df['AI_Wait'], label='Proposed (DQN)', color='green')
    plt.title('Wait Time Reduction: Fixed vs AI')
    plt.xlabel('Episode')
    plt.ylabel('Avg Wait Time (sec)')
    plt.legend()
    
    # Create the results folder if missing
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    save_path = os.path.join(save_dir, 'performance_plot.png')
    plt.savefig(save_path)
    print(f"\n[SUCCESS]: Result graph saved at: {save_path}")

# 3. MAIN EXECUTION BLOCK
if __name__ == "__main__":
    if os.path.exists(csv_path):
        # Load the data
        df = pd.read_csv(csv_path)
        print(f"Successfully loaded data from: {csv_path}")
        
        # Define where to save the images
        results_folder = r"C:\Users\ADMIN\Desktop\Final_project\results\plots"
        
        # CALL THE FUNCTIONS (This was causing your error)
        generate_performance_report(df)
        plot_results(df, results_folder)
        
    else:
        print(f"Error: Could not find the file at {csv_path}")
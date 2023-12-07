from ydata_profiling import ProfileReport
import pandas as pd
import os

df = pd.read_csv("data/winequality-red.csv")

profile = ProfileReport(df, title="Profiling Report")

report_path = 'profiling'
os.makedirs(report_path, exist_ok=True)

report_path = os.path.join(report_path, "report-red.html")
profile.to_file(report_path)

print(f"Report saved to: {report_path}")

df = pd.read_csv("data/winequality-white.csv")

profile = ProfileReport(df, title="Profiling Report")

report_path = 'profiling'
os.makedirs(report_path, exist_ok=True)

report_path = os.path.join(report_path, "report-white.html")
profile.to_file(report_path)

print(f"Report saved to: {report_path}")
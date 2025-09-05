import pandas as pd

# Step 1: Load student results from CSV
df = pd.read_csv('results.csv')

# Step 2: Calculate total marks, percentage, grade
df['Total'] = df.groupby('roll no')['marks'].transform('sum')
df['Percentage'] = df['Total'] / (df.groupby('roll no')['marks'].count() * 100) * 100

def get_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Percentage'].apply(get_grade)

# Step 3: Drop duplicate rows for each student (keep one row per student)
final_df = df.drop_duplicates(subset=['roll no'])

# Step 4: Sort by percentage and display top 5 students
top5 = final_df.sort_values(by='Percentage', ascending=False).head(5)
print("Top 5 Students by Percentage:")
print(top5[['name', 'roll no', 'Total', 'Percentage', 'Grade']])

# Step 5: Save analyzed results into a new CSV file
final_df.to_csv('final_results.csv', index=False)
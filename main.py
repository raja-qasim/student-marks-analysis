import pandas as pd

print("\n--- Student Marks Analysis ---")

# CSV file read
df = pd.read_csv("students.csv")

# Total marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Average marks
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Grade system
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Ranking
df["Rank"] = df["Average"].rank(ascending=False)

print("\nStudent Result:")
print(df)

# Highest scorer
print("\nTop Student:", df.loc[df["Average"].idxmax(), "Name"])

# Save result to new CSV
df.to_csv("student_result.csv", index=False)

print("\nResult saved to student_result.csv")
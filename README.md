# US-Health-Insurance-Analysis
US Health Insurance Analysis
Overview

This project analyzes a US Health Insurance dataset to uncover insights about how different factors (such as age, gender, BMI, smoking habits, and region) influence insurance charges. Using Python (Pandas, Seaborn, Matplotlib, Numpy), the analysis includes exploratory data analysis (EDA), statistical summaries, and visualizations to identify key trends.

 Steps Performed

Data Import & Loading
Loaded the dataset usa_health_insurance.csv into a Pandas DataFrame.
Previewed the dataset to understand its structure and available features.

Descriptive Statistics & Summary
Calculated mean age of policyholders.

Used df.describe() to generate summary statistics (mean, std, min, max, quartiles).
Checked categorical variables (sex, smoker, region) using value counts.

Categorical Analysis

Analyzed the distribution of categorical columns (sex, smoker, region).
Compared proportions (e.g., % of male vs female policyholders).

Correlation Analysis
Generated a correlation matrix for numerical features (age, bmi, children, charges).
Visualized correlations with a heatmap to see relationships between variables.

Pairwise Analysis

Created a pairplot for age, bmi, and charges with smoker as hue.
Observed patterns (e.g., smokers have significantly higher charges compared to non-smokers).

Group-Level Insights

Calculated average charges by smoker status.
Compared average charges across different regions.

Key Insights

Smokers vs Non-Smokers: Smokers tend to have much higher insurance charges.
Age & BMI Influence: Higher age and BMI are strongly correlated with increased charges.
Regional Differences: Average insurance charges vary by region.
Gender Distribution: Checked if gender impacts insurance charges significantly.

Tools & Libraries Used:

Pandas → Data handling and statistical summaries
Seaborn & Matplotlib → Visualizations (heatmap, pairplot, distributions)
NumPy → Numerical computations

Conclusion:
This analysis highlights the key drivers of US health insurance costs. Smoking status, BMI, and age are the most significant factors influencing insurance charges. These insights can help insurance providers design fairer pricing models and assist individuals in understanding how lifestyle choices impact insurance expenses.

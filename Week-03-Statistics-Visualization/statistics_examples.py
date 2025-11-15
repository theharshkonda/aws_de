"""
Statistics Examples - Descriptive Statistics, Correlations, and Distributions

This module demonstrates:
- Descriptive statistics
- Correlation analysis
- Probability distributions
- Hypothesis testing basics
"""

import numpy as np
import pandas as pd
from scipy import stats

print("=" * 60)
print("STATISTICS - Descriptive, Correlation, Distributions")
print("=" * 60)

# Create sample datasets
np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=100)  # cm
weights = np.random.normal(loc=70, scale=10, size=100)   # kg
test_scores = np.random.normal(loc=75, scale=12, size=100)

# ============================================================================
# DESCRIPTIVE STATISTICS
# ============================================================================

print("\nDESCRIPTIVE STATISTICS:")
print("-" * 60)

print("\nHeights dataset (cm):")
print(f"  Mean: {np.mean(heights):.2f}")
print(f"  Median: {np.median(heights):.2f}")
print(f"  Mode: {stats.mode(heights, keepdims=True).mode[0]:.2f}")
print(f"  Std Dev: {np.std(heights):.2f}")
print(f"  Variance: {np.var(heights):.2f}")
print(f"  Min: {np.min(heights):.2f}")
print(f"  Max: {np.max(heights):.2f}")
print(f"  Range: {np.max(heights) - np.min(heights):.2f}")

# Quartiles
print(f"\nQuartiles:")
q1 = np.percentile(heights, 25)
q2 = np.percentile(heights, 50)
q3 = np.percentile(heights, 75)
iqr = q3 - q1
print(f"  Q1 (25%): {q1:.2f}")
print(f"  Q2 (50%): {q2:.2f}")
print(f"  Q3 (75%): {q3:.2f}")
print(f"  IQR: {iqr:.2f}")

# Skewness and Kurtosis
print(f"\nSkewness and Kurtosis:")
print(f"  Skewness: {stats.skew(heights):.4f}")
print(f"  Kurtosis: {stats.kurtosis(heights):.4f}")

# Using pandas describe
df = pd.DataFrame({
    'Height': heights,
    'Weight': weights,
    'TestScore': test_scores
})

print(f"\n\nPandas describe() output:")
print(df.describe())

# ============================================================================
# CORRELATION ANALYSIS
# ============================================================================

print("\n" + "=" * 60)
print("CORRELATION ANALYSIS:")
print("-" * 60)

# Pearson correlation
pearson_corr = np.corrcoef(heights, weights)[0, 1]
print(f"\nPearson correlation (Height vs Weight): {pearson_corr:.4f}")

# Calculate with scipy
pearson_r, pearson_p = stats.pearsonr(heights, weights)
print(f"  Correlation coefficient: {pearson_r:.4f}")
print(f"  P-value: {pearson_p:.6f}")

# Spearman correlation (rank-based, for non-linear relationships)
spearman_r, spearman_p = stats.spearmanr(heights, weights)
print(f"\nSpearman correlation (Height vs Weight): {spearman_r:.4f}")
print(f"  P-value: {spearman_p:.6f}")

# Correlation matrix
print(f"\n\nCorrelation Matrix:")
corr_matrix = df.corr()
print(corr_matrix)

# ============================================================================
# PROBABILITY DISTRIBUTIONS
# ============================================================================

print("\n" + "=" * 60)
print("PROBABILITY DISTRIBUTIONS:")
print("-" * 60)

# Normal distribution
print("\nNormal Distribution:")
x = np.linspace(-3, 3, 100)
pdf = stats.norm.pdf(x)
cdf = stats.norm.cdf(x)

print(f"  P(Z < 0): {stats.norm.cdf(0):.4f}")
print(f"  P(Z < 1): {stats.norm.cdf(1):.4f}")
print(f"  P(Z < 2): {stats.norm.cdf(2):.4f}")

# Standardization (z-score)
print(f"\nZ-score standardization of heights:")
heights_standardized = (heights - np.mean(heights)) / np.std(heights)
print(f"  Mean of standardized: {np.mean(heights_standardized):.6f}")
print(f"  Std of standardized: {np.std(heights_standardized):.6f}")

# Other distributions
print(f"\n\nOther distributions:")

# Binomial
binom_prob = stats.binom.pmf(5, 10, 0.5)  # 5 successes in 10 trials, p=0.5
print(f"  Binomial P(X=5, n=10, p=0.5): {binom_prob:.4f}")

# Exponential
exp_prob = stats.expon.pdf(2, scale=1)
print(f"  Exponential pdf at x=2: {exp_prob:.4f}")

# Chi-square
chi2_val = stats.chi2.pdf(4, df=3)
print(f"  Chi-square pdf at x=4, df=3: {chi2_val:.4f}")

# ============================================================================
# HYPOTHESIS TESTING
# ============================================================================

print("\n" + "=" * 60)
print("HYPOTHESIS TESTING:")
print("-" * 60)

# Sample data for hypothesis tests
sample1 = np.random.normal(loc=100, scale=15, size=30)
sample2 = np.random.normal(loc=105, scale=15, size=30)

print("\nOne-Sample T-Test:")
print("H0: Population mean = 100")
t_stat, t_pval = stats.ttest_1samp(sample1, 100)
print(f"  T-statistic: {t_stat:.4f}")
print(f"  P-value: {t_pval:.4f}")
print(f"  Result: {'Reject H0' if t_pval < 0.05 else 'Fail to reject H0'} (α=0.05)")

# Two-Sample T-Test
print("\n\nTwo-Sample T-Test:")
print("H0: Population means are equal")
t_stat, t_pval = stats.ttest_ind(sample1, sample2)
print(f"  T-statistic: {t_stat:.4f}")
print(f"  P-value: {t_pval:.4f}")
print(f"  Result: {'Reject H0' if t_pval < 0.05 else 'Fail to reject H0'} (α=0.05)")

# Paired T-Test
print("\n\nPaired T-Test:")
before = np.array([85, 89, 87, 90, 86])
after = np.array([92, 94, 91, 96, 93])
t_stat, t_pval = stats.ttest_rel(before, after)
print(f"  Before: {before}")
print(f"  After: {after}")
print(f"  T-statistic: {t_stat:.4f}")
print(f"  P-value: {t_pval:.6f}")
print(f"  Result: {'Reject H0' if t_pval < 0.05 else 'Fail to reject H0'} (α=0.05)")

# ============================================================================
# ANOVA (Analysis of Variance)
# ============================================================================

print("\n" + "=" * 60)
print("ANOVA (Analysis of Variance):")
print("-" * 60)

# Three groups
group1 = np.random.normal(loc=100, scale=10, size=20)
group2 = np.random.normal(loc=105, scale=10, size=20)
group3 = np.random.normal(loc=110, scale=10, size=20)

print("Testing if three groups have different means:")
f_stat, p_val = stats.f_oneway(group1, group2, group3)
print(f"  F-statistic: {f_stat:.4f}")
print(f"  P-value: {p_val:.4f}")
print(f"  Result: {'Reject H0' if p_val < 0.05 else 'Fail to reject H0'} (α=0.05)")

# ============================================================================
# CHI-SQUARE TEST
# ============================================================================

print("\n" + "=" * 60)
print("CHI-SQUARE TEST:")
print("-" * 60)

# Contingency table
contingency = np.array([[20, 10], [15, 25]])
print("\nContingency Table:")
print(contingency)

chi2, p_val, dof, expected = stats.chi2_contingency(contingency)
print(f"\nChi-square test results:")
print(f"  Chi-square statistic: {chi2:.4f}")
print(f"  P-value: {p_val:.4f}")
print(f"  Degrees of freedom: {dof}")
print(f"  Expected frequencies:\n{expected}")

# ============================================================================
# PRACTICAL EXAMPLE
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Grade Analysis:")
print("-" * 60)

# Create grade data
grades_data = pd.DataFrame({
    'StudentID': range(1, 51),
    'Midterm': np.random.normal(loc=75, scale=10, size=50),
    'Final': np.random.normal(loc=78, scale=10, size=50),
    'Attendance': np.random.randint(60, 100, size=50)
})

print("\nGrades Dataset:")
print(grades_data.head(10))

# Analysis
print("\n\nMidterm Statistics:")
print(f"  Mean: {grades_data['Midterm'].mean():.2f}")
print(f"  Median: {grades_data['Midterm'].median():.2f}")
print(f"  Std Dev: {grades_data['Midterm'].std():.2f}")

print("\n\nFinal Statistics:")
print(f"  Mean: {grades_data['Final'].mean():.2f}")
print(f"  Median: {grades_data['Final'].median():.2f}")
print(f"  Std Dev: {grades_data['Final'].std():.2f}")

# Correlation
corr_midterm_final = grades_data['Midterm'].corr(grades_data['Final'])
print(f"\nCorrelation (Midterm vs Final): {corr_midterm_final:.4f}")

corr_attendance_final = grades_data['Attendance'].corr(grades_data['Final'])
print(f"Correlation (Attendance vs Final): {corr_attendance_final:.4f}")

# Compare Midterm vs Final
print("\n\nPaired T-Test (Midterm vs Final):")
t_stat, t_pval = stats.ttest_rel(grades_data['Midterm'], grades_data['Final'])
print(f"  T-statistic: {t_stat:.4f}")
print(f"  P-value: {t_pval:.4f}")
print(f"  Result: {'Significant difference' if t_pval < 0.05 else 'No significant difference'}")

# Create performance categories
grades_data['Performance'] = pd.cut(
    grades_data['Final'],
    bins=[0, 60, 70, 80, 90, 100],
    labels=['F', 'D', 'C', 'B', 'A']
)

print("\n\nPerformance Distribution:")
print(grades_data['Performance'].value_counts().sort_index())

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Statistics Key Concepts:

1. DESCRIPTIVE STATISTICS:
   - Central tendency: mean, median, mode
   - Dispersion: variance, std dev, range, IQR
   - Shape: skewness, kurtosis
   - Quartiles: Q1, Q2, Q3

2. CORRELATION:
   - Pearson: linear relationship (-1 to 1)
   - Spearman: rank-based, non-linear
   - P-value: statistical significance
   - Correlation matrix: pairwise correlations

3. PROBABILITY DISTRIBUTIONS:
   - Normal (Gaussian): most common
   - Binomial: discrete, successes/failures
   - Exponential: waiting times
   - Chi-square: categorical

4. HYPOTHESIS TESTING:
   - H0: Null hypothesis (no effect)
   - H1: Alternative hypothesis (effect exists)
   - P-value: Probability of observing data if H0 true
   - α (alpha): Significance level (typically 0.05)
   - Reject H0 if p-value < α

5. COMMON TESTS:
   - T-test: Compare means
   - ANOVA: Compare 3+ groups
   - Chi-square: Test independence
   - Correlation: Test relationships

6. EFFECT SIZE:
   - How large is the observed effect?
   - Statistical significance ≠ practical significance

7. BEST PRACTICES:
   - Always check assumptions
   - Use appropriate test for data type
   - Report effect size, not just p-value
   - Be skeptical of p-hacking
   - Replicate findings when possible
""")

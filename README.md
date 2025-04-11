# 🧳 Travel Insurance Project

> Operational claims analysis of a travel insurance company: from data cleaning to interactive dashboard visualizations.

---

## 🧭 Main Objective

Evaluate payment/rejection patterns in claims by identifying:
  - Clients with the highest rejection rates
  - Types of claims with the most payments
  - Most expensive benefit types
  - Claims seasonality

---

## 🗂️ Project Structure

```
├── data/
│   ├── raw/               # Original data (.xlsx)
│   └── processed/         # Cleaned data for dashboard
├── notebooks/             # Step-by-step analysis in Jupyter
├── src/                   # ETL, EDA and stats scripts
│   ├── extraction.py      # Data extraction
│   ├── transformation.py  # Cleaning and filtering
│   └── stats.py           # Analysis and visualizations
├── dashboards/            # Power BI dashboard
├── sql/                   # SQL queries
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

---

## 📅 Research Questions

- What is the average payment rate by country or benefit type?
- Which clients have the highest rejection rate?
- Which type of claim results in more payments? And which are most rejected?
- Are there claim reasons that are almost never paid?
- Are there specific dates or months with more claims than others?

## 🔍 Key Visualizations

- Top 10 payment rates by benefit type
- Clients with highest rejection rates
- Monthly evolution of claims
- Average claimed vs paid amounts

---

## 📊 Dashboard (Power BI)

- **Data used**: `data/processed/`
- Includes:
  - General KPIs (% paid, % rejected)
  - Interactive visuals by client, country, benefit type
  - Monthly and geographic trends

🖼️ Visuals exported as PNG for additional use

---

## 📁 How to Run the Project

```bash
# Clone the repository
cd proyecto_MDS_I

# Install dependencies
pip install -r requirements.txt

# Run the full pipeline
python main.py
```

## 🎉 Final Outcome

This project generates a clean dataset and visualizations that allow:
- Understanding payment behavior
- Detecting rejection patterns
- Supporting risk management decisions

## ✅ Conclusions

1. **What is the average payment rate by country or benefit type?**  
   The highest payment rates are found in essential and emergency medical services. These typically exceed 90%, suggesting good documentation and policy coverage. In contrast, administrative or lower-priority benefits show significantly lower rates. By country, differences in payment rates may be explained by local regulations or business agreements.

2. **Which clients have the highest rejection rates?**  
   Some clients exhibit high rejection rates, especially those with large claim volumes. This may be due to documentation errors, stricter policy rules, or lack of proper evidence. Others show nearly zero rejection, possibly due to strong business relationships or well-structured processes.

3. **Which type of claims are most paid or rejected?**  
   Claims related to medical emergencies and hospitalizations account for the largest paid amounts. On the other hand, cancellations, suspected fraud, or poorly documented claims are frequently rejected.

4. **Are there claim reasons that are almost never paid?**  
   Yes. Some specific claim reasons show extremely high rejection rates, possibly because they are not covered by the policy or lack sufficient documentation.

5. **Are there months with more claims than others?**  
   Yes. January and March 2025 show noticeable peaks, explained by the entry of a new client that caused an 80% monthly increase compared to 2024's average.

---

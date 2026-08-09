# Premium Interactive Data Dashboard (Colabs Project)

> **60-Second Recruiter Summary:** A high-performance, dark-mode Streamlit web application engineered to transform raw sales logs and membership data into real-time, interactive business insights. Built with custom CSS aesthetics, Plotly charts, and team-driven Pandas logic to automate KPI tracking and enhance data transparency.

---

## Project Overview
This project is an interactive analytics web application built to monitor sales performance, revenue metrics, and member booking activities for co-working or membership-based spaces. Developed as a collaborative group initiative within our data portfolio, it demonstrates how raw operational data can be converted into an executive-ready dashboard featuring custom aesthetic themes, dynamic chart updates, and raw data auditing capabilities.

## Problem / Question
Co-working hubs and subscription-based businesses often face two main operational challenges:
1. **Manual Tracking Friction:** Management wastes time processing static CSV logs and spreadsheets to derive basic revenue and booking KPIs.
2. **Low Data Accessibility:** Raw membership records are difficult for non-technical stakeholders to interpret and filter on the fly.

## Tools & Technologies
* **Language:** Python
* **Frontend Framework:** Streamlit
* **Data Wrangling:** Pandas
* **Data Visualization:** Plotly Express
* **Styling & UI:** Custom CSS Integration (Dark Mode, Dynamic Gradients)
* **Version Control & Collaboration:** Git & GitHub

## Data
The dashboard processes two key relational operational datasets:
* `bookings_data`: Transactional records containing booking IDs, dates, reservation types, and revenue figures.
* `members_data`: User profiles, active membership tiers, and engagement logs.

## Approach
1. **Data Pipeline & Wrangling:** Cleaned, formatted, and aggregated membership and booking tables using Pandas to enable real-time backend calculations for revenue and active usage.
2. **Custom UI/UX Engineering:** Injected custom CSS into Streamlit to create a dark-mode interface with high contrast, gradient cards, and smooth layout hierarchies.
3. **Dynamic Visuals & Theme Engine:** Designed reactive Plotly Donut Charts with custom hover inspection and integrated a sidebar theme switcher (**Neon Punch**, **Electric Cyber**, **Sunset Glow**).
4. **Data Transparency & Auditing:** Added expandable layout components to allow non-technical users and auditors to directly inspect underlying DataFrames.

## Key Findings
* **Peak Revenue Drivers:** Visualizing booking distributions showed that a concentrated subset of membership tiers drives the majority of total booking revenue.
* **Member Engagement Gaps:** Live KPI metrics immediately surfaced active vs. inactive user ratios, identifying clear opportunities for member retention campaigns.

## Results / Impact
* **Automated KPI Reporting:** Replaced manual spreadsheet analysis with instant, live KPI metrics (Total Revenue, Total Bookings) calculated upon data loading.
* **Improved Stakeholder Access:** Combined high-level executive cards, interactive charts, and raw data views into a single browser application for non-technical team members.

## What I Learned
* How to combine Streamlit and custom CSS to build custom web application interfaces.
* Strategies for using Plotly Express to build reactive charts with state-dependent visual themes.
* Collaborative Git workflows and structured project documentation for group data projects.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/eshaal22/colabs-data-dashboard.git](https://github.com/eshaal22/colabs-data-dashboard.git)
   cd colabs-data-dashboard

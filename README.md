# Startup Readiness Assessment (KTH IRL)

This project is an interactive Streamlit app that helps founders and support organizations assess a startup’s maturity using the **KTH Innovation Readiness Level (IRL)** framework.

The tool walks users through a tailored set of multiple-choice questions (with branching logic) across dimensions such as **CRL, SRL, BRL, TMRL, FRL, IPRL and TRL**. At the end, it computes the current level per dimension, visualizes the results on a radar chart, and generates a **PDF report** with the diagram and detailed level descriptions.

## Features

- 🧭 **IRL-based assessment**  
  Question flows built around the KTH Innovation Readiness Level dimensions.

- 🔀 **Adaptive branching logic**  
  Users only see questions relevant to their situation, with progress feedback.

- 🎨 **Custom UI & theming**  
  Figma-inspired layout, tile-style answer choices, and integrated progress bar.

- 📊 **Radar chart summary**  
  Plotly radar chart showing readiness levels across all dimensions.

- 📄 **PDF export**  
  One-click generation of a PDF report including the radar diagram and per-dimension descriptions.

- 🚀 **Built with Streamlit**  
  Easy to run locally or deploy on Streamlit Community Cloud / PaaS.

## Tech stack

- [Streamlit](https://streamlit.io/) for the web app
- [Pandas](https://pandas.pydata.org/) for CSV-based questions & descriptions
- [Plotly](https://plotly.com/python/) for the radar chart
- [ReportLab](https://www.reportlab.com/dev/) + [Kaleido](https://github.com/plotly/Kaleido) for PDF export

## Quick start

```bash
git clone https://github.com/your-user/startup-readiness-assessment.git
cd startup-readiness-assessment

pip install -r requirements.txt
streamlit run app.py

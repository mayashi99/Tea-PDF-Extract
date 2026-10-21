# **Tea PDF Extractor 📄🍃**

## Overview

**Tea PDF Extractor** is a Python-based project designed to extract tea market information from PDF reports published by Forbes & Walker Tea Brokers (Pvt) Ltd.

The project processes tea market report PDFs and organizes the extracted information for further analysis and research.

## Official Data Source

- **Forbes & Walker Tea Brokers – Tea Market Reports:** https://www.forbestea.com/statistics-tea-market-reports

The website provides weekly tea market reports containing information about tea auction sales, market quantities, demand, and tea categories. These reports are used as the source documents for data extraction. <Cite refs={["turn831850search0","turn831850search12"]}/>

## Project Structure

```text
Tea-PDF-Extract/
├── input_pdfs/
├── modules/
├── output/
├── main.py
├── requirements.txt
└── README.md
```

### Folder and File Description

- `input_pdfs/` — Contains the source PDF reports to be processed.
- `modules/` — Contains supporting Python modules for PDF extraction and data processing.
- `output/` — Stores the extracted results.
- `main.py` — Main entry point for running the extraction process.
- `requirements.txt` — Lists the Python dependencies required by the project.
- `README.md` — Project documentation.

## Technologies Used

- **Python** — Main programming language.
- **PDF Processing** — Extracting information from PDF documents.
- **Data Processing** — Organizing extracted tea market information.

## Getting Started

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Tea-PDF-Extract
```

Replace `<YOUR_REPOSITORY_URL>` with the URL of this GitHub repository.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add PDF Reports

Place the required tea market report PDF files inside the `input_pdfs/` directory.

### 4. Run the Extractor

```bash
python main.py
```

Check the `output/` directory for the extracted results.

*Note: The exact output format and supported PDF extraction features depend on the implementation of the project's Python modules.*

## Project Objectives

- Extract tea market information from PDF reports.
- Reduce manual data collection and processing.
- Organize extracted information for research and analysis.
- Support the preparation of datasets for tea industry analytics and forecasting.

## Data Source and Attribution

The source documents are published by Forbes & Walker Tea Brokers (Pvt) Ltd. All original reports remain the property of their respective rights holders.

**Official Source:** https://www.forbestea.com/statistics-tea-market-reports

This project is an independent PDF data extraction tool and is not officially affiliated with Forbes & Walker Tea Brokers.

## License

No license has been specified for this repository. Please contact the repository owner before redistributing or reusing the project code.

---

**Developed for tea market data extraction and research.** 🇱🇰🍃

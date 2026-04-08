# Population Data ETL Pipeline

A comprehensive Extract, Transform, and Load (ETL) pipeline for processing global population data across multiple time periods using Python and Pandas.

## 📋 Overview

This project automates the cleaning and consolidation of population data spanning three decades (2010-2040). It handles data from multiple sources and formats, standardizes column names, validates data types, and merges datasets into a unified consolidated file.

### Key Features
- **Multi-source Integration**: Processes data from CSV and Excel formats
- **Automated Data Cleaning**: Standardizes column names, handles missing values, and fixes data inconsistencies
- **Type Validation**: Ensures proper data types (integers, floats) for analysis
- **Data Consolidation**: Merges three separate datasets into a single unified dataset
- **Modular Design**: Organized into reusable functions and scripts
- **Flexible Analysis**: Supports data reshaping and transformation (pivoting/melting)

## 📁 Project Structure

```
ETL_pandas/
├── original_data/              # Raw data files
│   ├── population-2010-2019.csv
│   ├── population-2020-2029.csv
│   └── population-2030-2040.xlsx
├── cleaned_data/               # Output - cleaned CSV files
│   ├── pop_2010_2019_cleanfile.csv
│   ├── pop_2020_2029_cleanfile.csv
│   └── pop_2030_2040_cleanfile.csv
├── population10-19.ipynb       # Data exploration & cleaning (2010-2019)
├── population20_29.py          # Cleaning script (2020-2029)
├── population30_40.py          # Cleaning script (2030-2040)
├── population_merge.ipynb      # Data consolidation & analysis
└── README.md                   # This file
```

## 🔄 ETL Process

### 1. **Extract Phase**
- Load population data from CSV (2010-2019, 2020-2029) and Excel (2030-2040) sources
- Read raw data into Pandas DataFrames with appropriate headers and row skipping

### 2. **Transform Phase**

#### Data Cleaning Steps:
- **Column Standardization**: Rename columns for consistency
  - `Time` → `Year`
  - `PopMale` → `Male`
  - `PopFemale` → `Female`

- **Missing Data Handling**:
  - Remove rows with null values
  - Filter out 'NO DATA' entries in age groups

- **Data Validation & Fixes**:
  - Standardize age group names (e.g., '05. Sep' → '4-9', 'Okt 14' → '10-14')
  - Handle data anomalies (e.g., 'ERROR_6.246' in male values calculated from totals)
  - Consolidate age group ranges (e.g., '100+' → '100-104')

- **Type Conversion**:
  - `LocID` → Integer
  - `Year` → Integer
  - `Male`, `Female` → Float

- **Column Pruning**:
  - Drop unnecessary columns: `AgeGrpStart`, `AgeGrpSpan`, `PopTotal`

### 3. **Load Phase**
- Save cleaned datasets as CSV files in `cleaned_data/` folder
- Consolidate all three periods into a single merged dataset
- Ready for analysis and visualization

## 🚀 Usage

### Option 1: Using Python Scripts

```bash
# Clean 2020-2029 data
python population20_29.py

# Clean 2030-2040 data
python population30_40.py
```

### Option 2: Using Jupyter Notebooks

```bash
# Explore and clean 2010-2019 data
jupyter notebook population10-19.ipynb

# Merge all datasets and perform analysis
jupyter notebook population_merge.ipynb
```

## 📊 Data Dictionary

### Cleaned Dataset Columns

| Column | Type | Description |
|--------|------|-------------|
| **LocID** | Integer | Unique location identifier |
| **Location** | String | Country/region name |
| **Year** | Integer | Calendar year (2010-2040) |
| **AgeGrp** | String | Age group range (e.g., '0-4', '5-10', '100-104') |
| **Male** | Float | Male population count |
| **Female** | Float | Female population count |

## 💻 Technical Stack

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **OpenPyXL**: Excel file support
- **Jupyter Notebook**: Interactive data exploration

## 📥 Installation

```bash
# Clone the repository
git clone <repository-url>
cd ETL_pandas

# Install dependencies
pip install pandas openpyxl jupyter

# Or using requirements.txt (if available)
pip install -r requirements.txt
```

## 🔍 Data Quality Checks

The pipeline includes quality validation:
- ✅ Null value detection and removal
- ✅ Data type consistency verification
- ✅ Age group standardization
- ✅ Invalid value handling (with computed replacements)
- ✅ Column consistency across all datasets
- ✅ Descriptive statistics for validation

## 📈 Example Analysis

After merging, you can perform various analyses:

```python
# Load merged data
import pandas as pd
pop = pd.read_csv('cleaned_data/merged_population.csv')

# Summary statistics
pop.describe()

# Filter by age group or year
young_population = pop[pop['AgeGrp'] == '0-4']

# Reshape data (pivoting gender)
pop_melted = pop.melt(
    id_vars=['LocID', 'Location', 'Year', 'AgeGrp'],
    value_vars=['Male', 'Female'],
    var_name='Gender',
    value_name='Population'
)
```

## 📝 Notes

- Raw data stored in `original_data/` folder
- Cleaned outputs automatically saved to `cleaned_data/` folder
- All cleaning operations are non-destructive (original data preserved)
- Modular design allows running individual period cleaning independently
- Scripts follow PEP 8 style guidelines

## 🤝 Contributing

To extend or modify this pipeline:
1. Add new data sources following the existing pattern
2. Update the transform functions with additional cleaning steps
3. Test with `population_merge.ipynb` for validation
4. Document any new data quality issues handled

# Banking Data Handling and Tableau Project

This repository contains Python scripts designed for handling and cleaning data for a bank. The cleaned data is prepared for further analysis and visualization in Tableau. The scripts are organized in a sequential order, with sub-steps for specific tasks.

## Purpose

The primary goal of these scripts is to:
1. Process raw transaction data.
2. Clean and normalize the data.
3. Perform aggregations and classifications.
4. Prepare the data for Tableau dashboards.

## Execution Order

The scripts should be executed in the following order:

1. **`1onlineandoffline.py`**  
   Splits the raw dataset into three categories: Online, Offline, and OfflineWithHash transactions.

2. **`2.1appendingmidcolumnwithaddressofflinewithhash.py`**  
   Appends missing address information for OfflineWithHash transactions.

3. **`2.2appendingmidcolumnwithaddressonlinewithhash.py`**  
   Appends missing address information for Online transactions.

4. **`2.4shopnameextraction.py`**  
   Extracts shop names from transaction descriptions.

5. **`3industrymapping.py`**  
   Maps SIC codes to industry categories.

6. **`4.1extractshopnames.py`**  
   Extracts shop names for specific transaction types.

7. **`4.2Normalizationfor1000parentnames.py`**  
   Normalizes parent company names for consistency.

8. **`4.3rapidfuzzforparentname.py`**  
   Uses fuzzy matching to map shop names to parent company names.

9. **`5.1parentnammappingoffline.py`**  
   Maps parent company names to Offline transactions.

10. **`5.2parentnamemappingofflinewithhash.py`**  
    Maps parent company names to OfflineWithHash transactions.

11. **`5.3parentnamemappingonline.py`**  
    Maps parent company names to Online transactions.

12. **`6.1classifiedonline.py`**  
    Classifies Online transactions with flags.

13. **`6.2classifiedoffline.py`**  
    Classifies Offline transactions with flags.

14. **`6.3classifiedofflinewithhash.py`**  
    Classifies OfflineWithHash transactions with flags.

15. **`6.4classificationrates.py`**  
    Calculates classification rates for all transactions.

16. **`7creatingcompositekey.py`**  
    Creates a composite key for each transaction.

17. **`8agg_merchant_clean_with_flags.py`**  
    Aggregates merchant data with classification flags.

18. **`9.1Hashidcount.py`**  
    Counts unique hash IDs and identifies anomalies.

19. **`9.2anomalous_hash_parent_mismatch.py`**  
    Identifies hash IDs with multiple parent names.

20. **`9.3countofanomoloushashids.py`**  
    Counts anomalous hash IDs and groups them.

21. **`10.1NDandMNcitiesfilledfromaddress.py`**  
    Fills missing city names for North Dakota and Minnesota.

22. **`10.2NDandMNdatafilteredwithsource.py`**  
    Filters data for North Dakota and Minnesota.

23. **`10.3ATMflagsatNDandMN.py`**  
    Flags cities in North Dakota and Minnesota with ATMs.

24. **`10.4aggcitywithstateNDandMN.py`**  
    Aggregates city and state data for North Dakota and Minnesota.

25. **`10.5aggregationofNDandMN.py`**  
    Aggregates transaction data for North Dakota and Minnesota.

26. **`10.6flagNDandMNcitieswithATM.py`**  
    Flags cities in North Dakota and Minnesota with ATMs.

27. **`11.1SQandPaypal.py`**  
    Extracts sub-shop information for Square and PayPal transactions.

28. **`11.2SQandPaypalcleaned.py`**  
    Cleans and processes Square and PayPal data.

29. **`11.3aggSQandPaypal.py`**  
    Aggregates Square and PayPal data.

## Tableau Folder

The `Tableau` folder contains additional scripts and codes specifically designed to handle data for Tableau dashboards. These scripts are used to create and manage tables that are directly utilized in Tableau for visualization purposes.

## How to Run

1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using the following command:
   ```bash
   pip install pandas openpyxl rapidfuzz


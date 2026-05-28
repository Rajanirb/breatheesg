# SOURCES.md

## Research and Source Handling

For this project, I researched how ESG-related data is commonly shared in enterprise environments and designed simplified versions of those formats for the prototype.

---

## 1. SAP Data

### Research

I looked at how SAP exports are usually shared in enterprise systems. Most examples included:

* CSV exports,
* flat files,
* procurement records,
* and fuel consumption reports.

I also noticed that SAP exports often contain inconsistent column names, plant codes, and unit formats.

---

### What I Implemented

For the prototype, I used CSV-based SAP-style uploads with fields like:

* activity type,
* fuel category,
* activity value,
* and units.

Example:

* diesel usage,
* petrol consumption,
* electricity usage.

---

### Why I Chose This

CSV exports are realistic and easier to test during development. They also allowed faster normalization and dashboard integration.

---

### What Would Break in Real Deployment

In real enterprise environments:

* SAP schemas can vary heavily,
* units may be inconsistent,
* some exports contain multilingual fields,
* and procurement mappings may require lookup tables.

A real deployment would need stronger validation and transformation pipelines.

---

## 2. Utility Data

### Research

I checked how utility teams usually export electricity data. Most utility platforms provide:

* monthly CSV exports,
* billing summaries,
* or downloadable reports.

Common fields included:

* meter readings,
* billing periods,
* energy consumption,
* and units like kWh.

---

### What I Implemented

I used simplified electricity usage records through CSV uploads.

Example:

* electricity,
* kWh values,
* emission calculations using emission factors.

---

### What Would Break in Real Deployment

Real utility data may contain:

* different tariff structures,
* multiple meters,
* timezone differences,
* and missing billing periods.

Handling those cases would require more advanced preprocessing.

---

## 3. Travel Data

### Research

I looked at how platforms like Concur and Navan manage travel records.

Typical travel exports contain:

* flights,
* hotel stays,
* transportation records,
* and travel distances.

Sometimes airport codes are provided instead of exact distances.

---

### What I Implemented

I used simplified travel-related activity records such as:

* flights,
* fuel usage,
* and transport entries.

---

### What Would Break in Real Deployment

Real travel systems may require:

* airport-to-airport distance calculations,
* multi-currency handling,
* travel class-based emission factors,
* and API authentication.

---

## Sample Data Design

I created sample data based on realistic ESG activities such as:

* electricity usage,
* diesel consumption,
* petrol usage,
* and flights.

The goal was to simulate common enterprise sustainability reporting scenarios while keeping the prototype manageable.

---

## Final Thought

This prototype focuses mainly on:

* ingestion,
* normalization,
* analytics,
* and audit visibility

rather than handling every real-world enterprise edge case.

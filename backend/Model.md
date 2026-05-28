# MODEL.md

## Data Model

For this project, I designed the database in a simple and structured way so that it can handle multiple companies, different emission sources, audit tracking, and normalized ESG data.

The project mainly uses Django ORM models with relationships between companies, uploaded sources, raw uploaded records, and normalized emissions data.

---

## 1. Company Model

The Company model stores organization details.

Fields:

* id
* name
* created_at

Why:
This helps support multi-tenancy because each company can have its own ESG records separately.

---

## 2. DataSource Model

This model stores information about where the uploaded data came from.

Examples:

* SAP exports
* Utility bills
* Travel reports

Fields:

* company
* source_type
* uploaded_file_name
* uploaded_at

Why:
This helps maintain source-of-truth tracking for every uploaded dataset.

---

## 3. RawEmissionData Model

This model stores raw uploaded records before processing.

Fields:

* source
* raw_data
* status
* error_message
* created_at

Why:
Keeping raw records is useful for debugging, validation, and audit purposes.

---

## 4. NormalizedEmission Model

This is the main model used for ESG calculations and dashboard analytics.

Fields:

* company
* source_row
* scope
* category
* activity_value
* activity_unit
* normalized_unit
* emission_factor
* co2e_emission
* is_suspicious
* approved
* locked_for_audit
* created_at

Why:
Uploaded data can come in different formats and units, so this model stores cleaned and normalized emission values.

---

## Scope Categorization

The system supports:

* Scope 1
* Scope 2
* Scope 3

This helps categorize emissions properly based on ESG reporting standards.

---

## Unit Normalization

Different units from uploaded files are normalized into standard units before calculating emissions.

Examples:

* kWh
* liters
* kilometers

This makes analytics and comparisons easier.

---

## Audit Tracking

An AuditLog model is used to track changes made to emission records.

It stores:

* old values
* new values
* action type
* timestamp

Why:
This improves transparency and supports audit requirements.

---

## Why I Chose This Design

I chose this structure because it:

* keeps the database organized,
* supports multiple companies,
* preserves uploaded raw data,
* supports audit tracking,
* handles different ESG sources,
* and makes dashboard calculations easier.

The model can also be expanded later for:

* AI-based ESG insights,
* external ERP integrations,
* advanced reporting,
* and anomaly detection.

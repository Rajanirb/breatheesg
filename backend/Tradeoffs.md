# TRADEOFFS.md

## Tradeoffs and Features Not Implemented

Because this assignment had a limited timeline, I focused more on building a complete working flow instead of adding too many advanced features. Below are some things I intentionally did not build.

---

## 1. Real SAP / Utility API Integrations

I used CSV uploads instead of connecting directly with SAP, utility portals, or travel APIs.

Reason:
Real integrations would require authentication handling, API contracts, enterprise credentials, and more setup time. For this prototype, I focused on ingestion and normalization logic instead.

Tradeoff:
The system works well for demonstrations, but real production deployments would need direct integrations.

---

## 2. Advanced Role-Based Access Control

I added backend authentication basics, but I did not implement separate analyst/admin/reviewer roles.

Reason:
The assignment focus was more on ESG ingestion and audit workflows. Adding a complete permission system would increase backend and frontend complexity.

Tradeoff:
Currently the app behaves like a single-user analyst dashboard.

---

## 3. Advanced AI Validation and Anomaly Detection

I added simple AI recommendations, but I did not build a real anomaly detection pipeline.

Reason:
Building reliable ESG anomaly detection requires historical datasets and more advanced ML logic. I prioritized completing the core workflow first.

Tradeoff:
Suspicious records are currently rule-based and simplified.

---

## Additional Limitations

Some other simplified areas include:

* no PDF parsing,
* no Excel ingestion,
* no real-time streaming,
* no email notification system,
* and no export-to-report feature.

These were skipped mainly to keep the project manageable within the assignment duration.

---

## Final Thought

I chose to prioritize:

* clean database structure,
* working APIs,
* deployment,
* dashboard analytics,
* and realistic ESG workflow handling

instead of trying to build too many incomplete features.

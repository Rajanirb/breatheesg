# DECISIONS.md

## Decisions Taken During Development

While building this project, I had to make a few practical decisions because the assignment intentionally left some areas open-ended. My goal was to build something realistic, understandable, and deployable within the given time.

---

## 1. Choosing CSV Uploads

I decided to use CSV uploads for all three source types instead of building direct API integrations.

Reason:
CSV files are very common in enterprise workflows, especially for SAP exports, utility reports, and travel expense summaries. They are also easier to validate and process during a prototype stage.

What I ignored:

* PDF parsing
* Live API integrations
* Excel uploads

I skipped these because they would increase complexity and take more time.

---

## 2. Using Django + React

I used Django REST Framework for the backend and React for the frontend.

Reason:
Django made it easier to quickly build APIs, manage models, and handle database operations. React was useful for building a clean dashboard UI with charts and dynamic updates.

---

## 3. Simplified SAP Handling

Instead of implementing a real SAP integration, I handled SAP-style uploaded records using structured CSV files.

Reason:
Actual SAP integrations are large and complex. For this assignment, I focused more on how the data would be normalized and processed after ingestion.

---

## 4. Scope Categorization

I separated emissions into:

* Scope 1
* Scope 2
* Scope 3

Reason:
These are standard ESG categories and enough for demonstrating analytics and reporting functionality.

---

## 5. Audit Tracking

I added raw data storage and audit log models.

Reason:
One important part of ESG reporting is traceability. Keeping original uploaded data and tracking modifications makes the system easier to audit later.

---

## 6. Deployment Choice

I deployed:

* Backend on Render
* Frontend on Vercel

Reason:
Both platforms are simple to configure and work well for full-stack student projects.

---

## 7. AI Recommendations

I added a simple AI recommendation section to the dashboard.

Reason:
The assignment mentioned AI usage, so I wanted to include a basic sustainability suggestion feature to improve the analyst experience.

---

## Things I Would Clarify With the PM

If I had more discussion time with the PM, I would ask:

* What level of audit compliance is expected?
* Should analysts have different approval roles?
* Is real-time ingestion required?
* Should emissions factors come from official APIs?
* How much historical data needs to be stored?

---

## Final Note

My main focus was building a working end-to-end ESG workflow:

* ingest data,
* normalize it,
* display analytics,
* and support review/audit functionality,

while keeping the implementation realistic and manageable within the assignment timeline.

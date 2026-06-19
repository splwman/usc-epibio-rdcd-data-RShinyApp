# RDCD Public Data Discovery Navigator: To-Do List and Feasibility Test Plan

## A. Step-by-step to-do list

### Phase 1: Scope and data preparation

1. Confirm the first audience and use case.
   - Recommended first use: RDCD internal consultation triage and retreat demo.
   - Later use: investigator-facing searchable data navigator.

2. Define the MVP research scenario.
   - Recommended demo: diabetes, rurality, South Carolina, SDOH, and food access.
   - Backup demos: cancer/genomics/imaging; opioid/substance use and mental health; health care cost/utilization.

3. Complete the minimum metadata fields for 10-15 priority data sources.
   - Access Level Standardized
   - Access Burden
   - Primary Category
   - Secondary Categories / Tags
   - Keywords for Search
   - Data Type Standardized
   - Geography Coverage
   - Geographic Unit
   - Unit of Analysis
   - Linkage Potential
   - South Carolina Relevance
   - Suggested Use Cases
   - Companion Datasets
   - Limitations / Cautions
   - Data Governance Notes

4. Review and finalize the category dictionary.
   - Confirm categories match RDCD language.
   - Add synonyms that investigators are likely to type.
   - Keep category names stable before building public-facing materials.

5. Verify official URLs and access labels.
   - Confirm that open/public sources are truly open.
   - Flag registered, credentialed, controlled, restricted, purchased, or DUA-required sources.
   - Avoid implying that restricted data are immediately downloadable.

### Phase 2: Build Shiny MVP

6. Place the Excel workbook and Rmd file in the same project folder.

7. Install required R packages.
   - shiny
   - readxl
   - dplyr
   - tidyr
   - stringr
   - purrr
   - DT
   - ggplot2
   - glue
   - tibble

8. Run the prototype.
   - In RStudio, open `RDCD_Data_Source_Navigator_Shiny_App.Rmd`.
   - Click Run Document, or run: `rmarkdown::run("RDCD_Data_Source_Navigator_Shiny_App.Rmd")`.

9. Test keyword search and filters.
   - Confirm that the diabetes/SC demo returns CDC PLACES, SVI, ACS, USDA Food Environment Atlas, RUCC, County Health Rankings, SC DPH, SCDHHS, and SC Health Data when relevant metadata are completed.

10. Review the data-fit summary.
    - Confirm it is useful as a first-page consultation summary.
    - Confirm it includes access level and limitations language.

### Phase 3: Improve search quality

11. Adjust the scoring weights.
    - Increase category/geography weight if the app returns broad but irrelevant national datasets.
    - Increase keyword weight if the app returns too many category-level matches.

12. Expand the keyword dictionary.
    - Add disease synonyms.
    - Add common abbreviations: CVD, SDOH, SVI, RUCC, EHR, claims, Medicaid, Medicare.
    - Add South Carolina-specific terms: SC, Midlands, Prisma, DPH, DHEC, SCDHHS, FQHC.

13. Add manual boost fields only if needed.
    - Example: `Demo Include`, `Priority`, `SC Relevance`, and `Linkage Potential`.
    - Keep manual boosts transparent.

### Phase 4: Add AI/visualization layer

14. Add AI-assisted keyword expansion only after the rule-based MVP is stable.
    - Example: heart disease -> cardiovascular disease, CVD, coronary disease, stroke, hypertension.
    - Example: neighborhood disadvantage -> SDOH, deprivation, social vulnerability, ACS, SVI.

15. Add plain-language explanations.
    - Explain why each data source matched.
    - Explain what the source can and cannot support.
    - Explain access burden and governance requirements.

16. Add stronger visualizations.
    - Match score plot.
    - Access burden distribution.
    - Category distribution.
    - Data source comparison matrix.
    - Research question to data pathway diagram.

17. Prepare retreat materials.
    - One-slide app concept.
    - One-slide demo screenshot.
    - Two-minute demo script.
    - Backup static screenshots in case live demo fails.

## B. Feasibility test plan

### Test 1: Data import

**Question:** Does the app load the Excel template correctly?

**Method:** Run the app with the Excel workbook in the same folder. Confirm the number of records loaded.

**Acceptance criterion:** All 58 source rows from the Word file appear in the app after import.

### Test 2: Metadata completeness

**Question:** Are the minimum fields completed for the initial demo sources?

**Method:** Filter the Excel sheet to demo priority rows and check required fields.

**Acceptance criterion:** At least 10 priority sources have category, keywords, data type, geography, access burden, linkage potential, and SC relevance completed.

### Test 3: Keyword search relevance

**Question:** Does the search return expected sources for the diabetes/SC demo?

**Test input:** diabetes; rural; South Carolina; social vulnerability; food access; Medicaid.

**Expected sources:** CDC PLACES, CDC/ATSDR SVI, ACS, USDA Food Environment Atlas, USDA RUCC, County Health Rankings, SC DPH, SCDHHS, SC Health Data.

**Acceptance criterion:** At least 6 of the expected sources appear in the top 10 results after metadata curation.

### Test 4: Filter behavior

**Question:** Do filters narrow results logically?

**Method:** Apply filters one at a time: category, data type, geography, and access level. Then apply combined filters.

**Acceptance criterion:** Results decrease in a sensible way, and expected high-fit sources are not lost due to inconsistent metadata labels.

### Test 5: Access-level safety

**Question:** Does the app clearly distinguish open from restricted data?

**Method:** Search for EHR, genomics, claims, and imaging sources. Compare open-only versus unrestricted searches.

**Acceptance criterion:** Restricted or controlled sources remain clearly labeled and are not described as immediately available public data.

### Test 6: Ranking quality

**Question:** Are high-fit sources ranked above weak-fit sources?

**Method:** Have an RDCD reviewer inspect the top 10 results for each demo scenario.

**Acceptance criterion:** At least 80 percent of top 10 results are judged relevant for each demo scenario.

### Test 7: Explanation quality

**Question:** Does the app explain why a source matched?

**Method:** Review the "why matched" field for top results.

**Acceptance criterion:** The explanation references true matched terms, categories, access levels, or data type fields.

### Test 8: Usability

**Question:** Can a new user complete a search without coaching?

**Method:** Observe 3-5 users entering a research question and narrowing results.

**Acceptance criterion:** Users can complete a search, interpret results, and identify 2-3 candidate sources in less than 2 minutes.

### Test 9: Export

**Question:** Do download buttons work?

**Method:** Download the current results CSV and data-fit summary text.

**Acceptance criterion:** Files open successfully and contain the current search results and summary.

### Test 10: Demo readiness

**Question:** Can the retreat demo run reliably?

**Method:** Run the app from a clean R session, test the demo button, and save screenshots.

**Acceptance criterion:** The app runs without error, screenshots are available as backup, and a two-minute demo script is prepared.

## C. Go/no-go criteria for first demonstration

The app is ready for a leadership demonstration when:

1. The Excel workbook loads without errors.
2. At least 10 high-priority sources are fully curated.
3. The diabetes/SC demo returns expected sources.
4. Access burden labels are clear.
5. The data-fit summary is understandable to a non-technical audience.
6. Static screenshots are ready in case live demo fails.

# RDCD Public Data Discovery Navigator: To-Do List and Feasibility Test Plan

Elaina, Robert, Emma:

Welcome! This document is where we will keep track of both short- and long-term goals 
as well as keep track of what is being done and by who. Just as a short introduction to
the project, there are 5 documents to keep track of:

*  **RDCD_Shiny_App_ToDo_and_Test_Plan.md** - That would be this document! The start will be
a list of short-term improvements or a to-do list that can be worked on in the current draft
of the app. Feel free to make suggestions or comments on any of them. If you are currently
working on one or have completed one please include the information with your initials such
as [in progress 7/23, SP] or [completed 7/24, SP].
* **RDCD_Data_Source_Preparation_Template.xlsx** - This is the excel sheet the app reads from.
Feel free to add data sources or information to existing ones. Nick and I have reviewed each one,
but we could really use another pair of eyes checking over what we have so far. If you have suggestions
for improving the excel, please let us know or create a branch and try it out.
*  **Data Sources Test Table.docx** - This is a table I have been using to test the search functionality 
which is in dire need of some help. If you make some changes to the search/scoring/matching parts and
need some ideas on how to test it, this is a good place.
*  **README.md** - We have not started working on this yet, but it will include the same kind of information
you see on other README's. We should probably start with a description of the app, what it is used for, and 
how to access it.
*  **RDCD_Data_Source_Navigator_Shiny_App_main.Rmd** - This is the most important document as it is where we
are building the app. Please try to document what code chunks are doing and what changes are being made. I 
will try to go through and create some comments that can hopefully give you an idea of what is going on so far.
If you want to try something a little crazy, go for it! just maybe break it off on a branch first.

It's great to have you on the team! Thank you so much for your help! If you have any questions, don't hesitate
to reach out. Try to remember to pull each time you open the app and push before you leave to make sure we are 
all working on the most up-to-date version. Other than that, good luck and have fun!.

- Sydney

## A. Step-by-step to-do list

## Search Function/Scoring/Matching:
I've been working on trying to improve the matching for the search function, but it still has a long way to go.
Currently I've been working a lot with "cancer" which does not bring up cancer sources such as SEER. I tried 
creating a cancer boost function, but that made those cancer sources pop up in unrelated searches such as 
"maternal mortality".

## Top matches Section
I think Access Burden, match score, Geogrpaphy, and Why Matched can be taken and put into a "more information"
section that Jiajia mentioned. Eventually I think match score will also be taken out, but for the purposes of
assessing and fixing its functionality, I think we should keep it in for now. [completed 7/10, SP]

## Compare Sources Section
I think limitations should be under "more information" somewhere else. It is inflating the size of the output
too much. Should we consider changing the orientation of the table? [completed.]

The years needs to be standardized across data sources.

The population needs to be shorter entries.

## Visual Summary Section
Is this section necessary? This might work well under the compare sources section.

## Data fit summary section
This section just needs help. It does not look polished and clean.

## Methods section
I don't think this section is necessary and should be taken out. Any information on how the app functions and how
to use it will be available on GitHub. [methods section deleted 7/20, SP]


## Future Directions

### GitHub Page
We could have an "Upload your own Workbook" section in GitHub that explains how to upload and use your own
workbook. We would provide links to 2 copies of the workbook: (1) the default workbook we use that can be 
edited/added to for their own work and (2) a blank workbook with all the necessary sections so they can start
from scratch.

### Improve search quality

1. Adjust the scoring weights.
    - Increase category/geography weight if the app returns broad but irrelevant national datasets.
    - Increase keyword weight if the app returns too many category-level matches.

2. Expand the keyword dictionary.
    - Add disease synonyms.
    - Add common abbreviations: CVD, SDOH, SVI, RUCC, EHR, claims, Medicaid, Medicare.
    - Add South Carolina-specific terms: SC, Midlands, Prisma, DPH, DHEC, SCDHHS, FQHC.

3. Add manual boost fields only if needed.
    - Example: `Demo Include`, `Priority`, `SC Relevance`, and `Linkage Potential`.
    - Keep manual boosts transparent.

### Add AI/visualization layer

1. Add AI-assisted keyword expansion only after the rule-based MVP is stable.
    - Example: heart disease -> cardiovascular disease, CVD, coronary disease, stroke, hypertension.
    - Example: neighborhood disadvantage -> SDOH, deprivation, social vulnerability, ACS, SVI.

2. Add plain-language explanations.
    - Explain why each data source matched.
    - Explain what the source can and cannot support.
    - Explain access burden and governance requirements.

3. Add stronger visualizations.
    - Match score plot.
    - Access burden distribution.
    - Category distribution.
    - Data source comparison matrix.
    - Research question to data pathway diagram.

4. Prepare retreat materials.
    - One-slide app concept.
    - One-slide demo screenshot.
    - Two-minute demo script.
    - Backup static screenshots in case live demo fails.

## B. Feasibility test plan

### Test 1: Keyword search relevance

**Question:** Does the search return expected sources for the diabetes/SC demo?

**Test input:** diabetes; rural; South Carolina; social vulnerability; food access; Medicaid.

**Expected sources:** CDC PLACES, CDC/ATSDR SVI, ACS, USDA Food Environment Atlas, USDA RUCC, County Health Rankings, SC DPH, SCDHHS, SC Health Data.

**Acceptance criterion:** At least 6 of the expected sources appear in the top 10 results after metadata curation.

### Test 2: Filter behavior

**Question:** Do filters narrow results logically?

**Method:** Apply filters one at a time: category, data type, geography, and access level. Then apply combined filters.

**Acceptance criterion:** Results decrease in a sensible way, and expected high-fit sources are not lost due to inconsistent metadata labels.

### Test 3: Access-level safety

**Question:** Does the app clearly distinguish open from restricted data?

**Method:** Search for EHR, genomics, claims, and imaging sources. Compare open-only versus unrestricted searches.

**Acceptance criterion:** Restricted or controlled sources remain clearly labeled and are not described as immediately available public data.

### Test 4: Ranking quality

**Question:** Are high-fit sources ranked above weak-fit sources?

**Method:** Have an RDCD reviewer inspect the top 10 results for each demo scenario.

**Acceptance criterion:** At least 80 percent of top 10 results are judged relevant for each demo scenario.

### Test 5: Explanation quality

**Question:** Does the app explain why a source matched?

**Method:** Review the "why matched" field for top results.

**Acceptance criterion:** The explanation references true matched terms, categories, access levels, or data type fields.

### Test 6: Usability

**Question:** Can a new user complete a search without coaching?

**Method:** Observe 3-5 users entering a research question and narrowing results.

**Acceptance criterion:** Users can complete a search, interpret results, and identify 2-3 candidate sources in less than 2 minutes.

### Test 7: Export

**Question:** Do download buttons work?

**Method:** Download the current results CSV and data-fit summary text.

**Acceptance criterion:** Files open successfully and contain the current search results and summary.


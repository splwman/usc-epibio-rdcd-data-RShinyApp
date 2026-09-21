from __future__ import annotations

import json
import os
import re
import sys
from copy import copy
from pathlib import Path

from openpyxl import load_workbook

WORKBOOK_PATH = Path("RDCD_Data_Source_Preparation_Template.xlsx")
SHEET_NAME = "Data_Prep"

EXPECTED_COLUMNS = [
    "record_id",
    "data_source",
    "official_link",
    "narrative",
    "access_level",
    "primary_category",
    "secondary_categories",
    "data_type",
    "geography",
    "population",
    "unit_of_analysis",
    "keywords",
    "linkage_potential",
    "access_burden",
    "rdcd_notes",
]


def normalize_header(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(value or "").strip().lower()).strip("_")


def safe_text(value: object) -> str:
    text = "" if value is None else str(value).strip()
    if text.startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def find_header_row(worksheet) -> tuple[int, dict[str, int]]:
    for row_number in range(1, min(worksheet.max_row, 20) + 1):
        headers = {
            normalize_header(cell.value): cell.column
            for cell in worksheet[row_number]
            if normalize_header(cell.value)
        }
        if "record_id" in headers and "data_source" in headers:
            return row_number, headers

    raise ValueError(
        "Could not find a header row containing both 'record_id' and 'data_source' "
        "within the first 20 rows of the Data_Prep sheet."
    )


def copy_row_style(worksheet, source_row: int, target_row: int, columns: list[int]) -> None:
    for column in columns:
        source = worksheet.cell(source_row, column)
        target = worksheet.cell(target_row, column)
        if source.has_style:
            target._style = copy(source._style)
        if source.number_format:
            target.number_format = source.number_format
        if source.alignment:
            target.alignment = copy(source.alignment)


def expand_matching_table(worksheet, header_row: int, target_row: int) -> None:
    for table in worksheet.tables.values():
        start_cell, end_cell = table.ref.split(":")
        start_row = worksheet[start_cell].row
        end_column = worksheet[end_cell].column_letter

        if start_row == header_row:
            table.ref = f"{start_cell}:{end_column}{target_row}"


def main() -> None:
    payload = json.loads(os.environ["SUBMISSION_JSON"])

    record_id = safe_text(payload.get("record_id"))
    if not re.fullmatch(r"DS-\d{3,}", record_id):
        raise ValueError("record_id must use the form DS-001, DS-002, and so on.")

    if not WORKBOOK_PATH.exists():
        raise FileNotFoundError(f"Workbook not found: {WORKBOOK_PATH}")

    workbook = load_workbook(WORKBOOK_PATH)
    if SHEET_NAME not in workbook.sheetnames:
        raise ValueError(f"Worksheet not found: {SHEET_NAME}")

    worksheet = workbook[SHEET_NAME]
    header_row, headers = find_header_row(worksheet)

    missing_columns = [column for column in EXPECTED_COLUMNS if column not in headers]
    if missing_columns:
        raise ValueError(
            "Workbook is missing required columns: " + ", ".join(missing_columns)
        )

    existing_ids = {
        safe_text(worksheet.cell(row, headers["record_id"]).value)
        for row in range(header_row + 1, worksheet.max_row + 1)
    }
    if record_id in existing_ids:
        raise ValueError(f"record_id already exists in the workbook: {record_id}")

    target_row = worksheet.max_row + 1
    copy_row_style(
        worksheet,
        target_row - 1,
        target_row,
        [headers[column] for column in EXPECTED_COLUMNS],
    )

    for column in EXPECTED_COLUMNS:
        worksheet.cell(target_row, headers[column]).value = safe_text(payload.get(column))

    expand_matching_table(worksheet, header_row, target_row)
    workbook.save(WORKBOOK_PATH)

    summary_lines = [
        f"# Review data-source submission: {record_id}",
        "",
        "Please verify the proposed source information before merging.",
        "",
    ]
    for column in EXPECTED_COLUMNS:
        if column == "record_id":
            continue
        label = column.replace("_", " ").title()
        summary_lines.append(f"**{label}:** {safe_text(payload.get(column)) or '—'}")
        summary_lines.append("")

    Path("/tmp/form_submission_review.md").write_text(
        "\n".join(summary_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Submission update failed: {error}", file=sys.stderr)
        raise

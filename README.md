# KCSE Results Checker

Simple Python script to check KCSE results by trying different index numbers with known names.

## One-line description

Lightweight demo: a small reusable script that probes a results page by submitting index/name combinations, saves matching HTML results, and prints a short terminal summary. The KCSE example shows how the tool works; the same approach can be adapted for other public record or results sites.

## How this demo works

- The script assembles candidate index numbers from a base index + a numeric range (for example base "31567219" + suffixes 001..050 => full indexes like 31567219001).
- For each index it submits a request to the results page (using the provided name) and inspects the returned HTML to see whether the expected name appears.
- When a positive match is detected the returned HTML is saved to disk (filename pattern: `result_{name}_{index}.html`) so you can open it in a browser and inspect the full response.
- The CLI prints short progress markers (dots) and a compact summary line for each name showing whether a match was found and the index where it was discovered.
- The script contains simple error handling and a short delay between requests to be respectful to the remote service. Some non-success responses are saved with `_debug_fallback` in the filename for diagnosis.

## Quick Start Guide

### 1. Get the Code

**Option A: Clone this repository**
```bash
git clone <repository-url>
cd kcse-checker
```

**Option B: Download directly**
- Click the green "Code" button → "Download ZIP"
- Extract the ZIP file
- Open terminal/command prompt in the extracted folder

### 2. Install Requirements

```bash
pip install requests beautifulsoup4
```

Or if you have Python 3:
```bash
pip3 install requests beautifulsoup4
```

### 3. Run the Script

```bash
python3 kcse_checker.py
```

Or on Windows:

```bash
python kcse_checker.py
```

## What It Does

- Checks index numbers from **31567219001** to **31567219050** (default range in the demo)
- Tries to match with these names: mutinda, cruz, fausto, fazio, majaliwa, armel, masiga, ndusa, preston
- Shows progress with dots (`.`) in the terminal
- When a match is found, saves the result as an HTML file
- Shows a summary at the end

## Demo output example

```
[MUTINDA] .......... ✓ FOUND at 31567219010
[CRUZ] .................................................. ✗ Not found
[FAUSTO] ....... ✓ FOUND at 31567219007
```

Files created (example):
- `result_mutinda_31567219010.html`
- `result_fausto_31567219007.html`
- `result_elsie_B0021036001_debug_fallback_405.html` (example of a saved debug response)

Open these HTML files in your browser to see the full results.

## Customize or reuse this demo for other sites

This repository is intentionally simple so you can adapt it for other form-based result pages. Suggestions:

- Change the index generation:
  - edit `base_index` and the numeric range to match the target site's numbering scheme
- Replace the names list with any candidate names or identifiers
- If the target site uses a different form or POST fields, update the request payload accordingly in the script
- Use a requests.Session() to reuse connections and set a realistic `User-Agent` header
- Respect robots.txt, site terms, and rate limits; increase the request delay and add retries/backoff if necessary
- For production or broader use consider modularizing the script into:
  - a site adapter (build and parse form + response detection)
  - a core runner that accepts adapter + input lists
  - a CLI wrapper or package entrypoint
- Output options: save raw HTML (as the demo does), and add optional JSON/CSV summaries for downstream processing

## Troubleshooting

**"pip: command not found"**
- Try `pip3` instead of `pip`

**"python: command not found"**
- Try `python3` instead of `python`

**Takes too long?**
- The script checks 50 numbers per name in the demo
- With 9 names, it can take several minutes
- The demo includes a short delay between requests; you can adjust it but avoid aggressive parallelism without proper rate limiting

## Safety and legal note

- Only run this tool against sites you are permitted to query in bulk. Respect robots.txt and the website's terms of service.
- Do not use this script to bypass authentication, to extract private data, or to target systems you do not have permission to probe.

## Notes

- Internet connection required
- SSL certificate verification is disabled for this specific site in the demo; do not disable SSL verification for other sites unless you understand the risks
- Be patient - checking all combinations takes time

## Development notes

- To make the project reusable and less KCSE-specific rename the main script to a generic filename (for example `results_finder.py` or `cli.py`) and move site-specific logic into an `adapters/` folder.
- Add unit tests for the parsing logic and a small CI workflow to run them on push.
- Consider packaging the project (pyproject.toml) and exposing a console_scripts entrypoint for easier installation.

## Use cases

This demo pattern is broadly applicable to any site that exposes results or records via a simple form. Relevant use cases include:

- Exam and certification results (KCSE, certification boards) — bulk verification of published outcomes.
- Public registry lookups (business licenses, voter lists, professional registers).
- License or certificate verification (confirming issuance by ID/number).
- Monitoring publications (automatically detect when a new name/record appears on a results page).
- QA and testing for results websites (compare expected vs published output during deployments).
- Conference or event attendee lists and winner announcements (bulk lookup by registration number).
- Data-entry validation (cross-check entered IDs against a published source).
- Research or open-data collection where allowed by terms of service.

Include only sites you are authorized to query in bulk; respect terms, privacy, and rate limits.

## Contributing

Contributions are welcome — issues, bug reports, feature requests and pull requests are all appreciated.

Guidelines:

- Open an issue first to discuss substantial changes or new adapters.
- Fork the repo, create a feature branch, and open a pull request with a clear description of the change.
- Add tests for parsing and core logic where applicable. Use pytest for tests.
- Keep changes small and focused; include examples or sample inputs for new adapters.
- Follow a simple style: idiomatic Python, prefer clear functions, add docstrings for public functions.
- If adding a new site adapter, include:
  - Adapter module under `adapters/` (example stub: `adapters/example_site.py`)
  - A short README snippet explaining form fields and expected outputs
  - Unit tests for parse logic

Files you may add:
- CONTRIBUTING.md — optional detailed contribution guide
- adapters/ — place for site-specific adapters and examples
- tests/ — unit tests (pytest)
- pyproject.toml / setup.cfg — packaging metadata

License and Code of Conduct

- Include a LICENSE (MIT or Apache-2.0 recommended) in the repo.
- Consider adding a CODE_OF_CONDUCT.md if you expect outside contributors.

Thank you — contributions help make the tool more useful for other sites and scenarios.

# KCSE Results Checker

Simple Python script to check KCSE results by trying different index numbers with known names.

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

- Checks index numbers from **31567219001** to **31567219050**
- Tries to match with these names: mutinda, cruz, fausto, fazio, majaliwa, armel, masiga, ndusa, preston
- Shows progress with dots (`.`) in the terminal
- When a match is found, saves the result as an HTML file
- Shows a summary at the end

## Output

**Terminal:**
```
[MUTINDA] .......... ✓ FOUND at 31567219010
[CRUZ] .................................................. ✗ Not found
[FAUSTO] ....... ✓ FOUND at 31567219007
```

**Files created:**
- `result_mutinda_31567219010.html`
- `result_fausto_31567219007.html`
- etc.

Open these HTML files in your browser to see the full results.

## Customize

To check different names or index numbers, edit these lines in `kcse_checker.py`:

```python
base_index = "31567219"  # Change the base index
names = ["mutinda", "cruz", "fausto", ...]  # Add/remove names
```

## Troubleshooting

**"pip: command not found"**
- Try `pip3` instead of `pip`

**"python: command not found"**
- Try `python3` instead of `python`

**Takes too long?**
- The script checks 50 numbers per name
- With 9 names, it could take 5-10 minutes
- Each check has a 0.5 second delay to be respectful to the server

## Notes

- Internet connection required
- SSL certificate verification is disabled for this specific site
- Be patient - checking all combinations takes time!# resulz

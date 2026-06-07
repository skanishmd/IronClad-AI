import csv
import os

downloads_path = r'C:\Users\skani\Downloads'
csv_file = os.path.join(downloads_path, 'ChronoBase_Journal_Comparison.csv')
doc_file = os.path.join(downloads_path, 'ChronoBase_Publication_Report.doc')

# Data for CSV
headers = [
    'Tier', 'Journal Name', 'Impact Factor', 'IF Rating', 'Cost (APC)', 
    'Cost Rating', 'Visibility', 'Vis Rating', 'Review Speed', 
    'Speed Rating', 'Student Fit', 'Fit Rating', 'Final Rating', 'Why Choose?'
]

data = [
    ['Tier A', 'Nucleic Acids Research (NAR)', '13.1', '10/10', '$4,192', '3/10', '10/10', '10/10', '3-4 Months', '7/10', '6/10', '6/10', '9.0', 'The gold standard for databases; annual Database Issue is highly prestigious.'],
    ['Tier A', 'Bioinformatics (Oxford)', '5.4', '8/10', '$3,000', '5/10', '9/10', '9/10', '3 Months', '8/10', '8/10', '8/10', '8.5', 'Most respected journal for computational tools; high community trust.'],
    ['Tier A', 'Nature Communications', '14.7', '10/10', '$6,490', '1/10', '10/10', '10/10', '4-6 Months', '5/10', '4/10', '4/10', '7.5', 'Broadest interdisciplinary visibility; extremely prestigious for CV.'],
    ['Tier B', 'Database (Oxford)', '3.6', '6/10', '$2,000', '7/10', '8/10', '8/10', '3 Months', '8/10', '9/10', '9/10', '8.2', 'Specifically for biological databases; great for methodology-focused papers.'],
    ['Tier B', 'Scientific Reports', '3.9', '7/10', '$2,850', '6/10', '10/10', '10/10', '4 Months', '7/10', '9/10', '9/10', '8.0', 'Nature Portfolio brand; focuses on technical soundness over "novelty".'],
    ['Tier B', 'Journal of Biological Rhythms', '2.1', '5/10', '$0 (Subscription)', '10/10', '7/10', '7/10', '2-3 Months', '9/10', '10/10', '10/10', '8.4', 'Perfect domain fit; no-cost subscription track is ideal for students.']
]

# Write CSV
with open(csv_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

# Write DOC (HTML Format)
html_content = """
<html>
<head>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    h1 { color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px; }
    h2 { color: #2980b9; margin-top: 25px; }
    table { border-collapse: collapse; width: 100%; margin-top: 15px; }
    th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
    th { background-color: #f2f2f2; color: #333; }
    .tier-a { background-color: #e8f4f8; }
    .tier-b { background-color: #f9f9f9; }
    .highlight { font-weight: bold; color: #e67e22; }
    .student-tip { background-color: #fff3cd; border-left: 5px solid #ffecb5; padding: 15px; margin: 20px 0; }
</style>
</head>
<body>
    <h1>ChronoBase Research Publication Strategy</h1>
    <p>This report outlines the recommended academic journals for the ChronoBase project, categorized by impact, cost-effectiveness, and suitability for student researchers.</p>

    <h2>1. Tier A: Maximum Impact & Global Prestige</h2>
    <table>
        <tr>
            <th>Journal</th>
            <th>IF</th>
            <th>Cost (APC)</th>
            <th>Visibility</th>
            <th>Speed</th>
            <th>Final Rating</th>
        </tr>
        <tr>
            <td>Nucleic Acids Research</td>
            <td>13.1</td>
            <td>$4,192</td>
            <td>10/10</td>
            <td>3-4m</td>
            <td><b>9.0</b></td>
        </tr>
        <tr>
            <td>Bioinformatics</td>
            <td>5.4</td>
            <td>$3,000</td>
            <td>9/10</td>
            <td>3m</td>
            <td><b>8.5</b></td>
        </tr>
        <tr>
            <td>Nature Communications</td>
            <td>14.7</td>
            <td>$6,490</td>
            <td>10/10</td>
            <td>4-6m</td>
            <td><b>7.5</b></td>
        </tr>
    </table>

    <h2>2. Tier B: High Quality & Student Friendly</h2>
    <table>
        <tr>
            <th>Journal</th>
            <th>IF</th>
            <th>Cost (APC)</th>
            <th>Visibility</th>
            <th>Speed</th>
            <th>Final Rating</th>
        </tr>
        <tr>
            <td>Journal of Biological Rhythms</td>
            <td>2.1</td>
            <td>$0</td>
            <td>7/10</td>
            <td>2-3m</td>
            <td><b>8.4</b></td>
        </tr>
        <tr>
            <td>Database (Oxford)</td>
            <td>3.6</td>
            <td>$2,000</td>
            <td>8/10</td>
            <td>3m</td>
            <td><b>8.2</b></td>
        </tr>
        <tr>
            <td>Scientific Reports</td>
            <td>3.9</td>
            <td>$2,850</td>
            <td>10/10</td>
            <td>4m</td>
            <td><b>8.0</b></td>
        </tr>
    </table>

    <h2>3. Strategic Recommendations for ChronoBase</h2>
    <ul>
        <li><b>Best for Prestige:</b> Aim for the <b>NAR Database Issue</b> (January). The 200 oncology targets and ZT-classification are exactly what they look for.</li>
        <li><b>Best for Students:</b> <b>Journal of Biological Rhythms</b>. The $0 subscription track is unbeatable for a student group without massive grants.</li>
        <li><b>Best for CV Value:</b> <b>Scientific Reports</b>. Having "Nature Portfolio" on your resume is a major boost for higher education applications.</li>
    </ul>

    <div class="student-tip">
        <h3>Pro-Tips for Student Researchers</h3>
        <p>1. <b>Waivers:</b> Always apply for a "Financial Hardship Waiver" during submission. Many journals waive 50-100% of fees for unfunded students.</p>
        <p>2. <b>Institutional Deals:</b> Check if your University library has "Read and Publish" agreements with OUP, Springer, or Elsevier. These cover APCs entirely!</p>
        <p>3. <b>Preprints:</b> Post your paper to <b>bioRxiv</b> first. It gives you an immediate DOI and helps establish priority for your ChronoBase findings.</p>
    </div>
</body>
</html>
"""

with open(doc_file, 'w') as f:
    f.write(html_content)

print("Files successfully generated in {0}:".format(downloads_path))
print("1. {0}".format(os.path.basename(csv_file)))
print("2. {0}".format(os.path.basename(doc_file)))

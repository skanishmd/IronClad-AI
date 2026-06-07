import csv
import os
import io

downloads_path = r'C:\Users\skani\Downloads'
csv_file = os.path.join(downloads_path, 'ChronoBase_Expanded_Journal_Comparison.csv')
doc_file = os.path.join(downloads_path, 'ChronoBase_Comprehensive_Report.doc')

# Expanded Data for CSV
headers = [
    'Publisher', 'Journal Name', 'Impact Factor', 'IF Rating', 'Cost (APC)', 
    'Cost Rating', 'Visibility', 'Vis Rating', 'Review Speed', 
    'Speed Rating', 'Student Fit', 'Fit Rating', 'Final Rating', 'Core Niche'
]

data = [
    ['Oxford', 'Nucleic Acids Research (NAR)', '13.1', '10/10', '$4,192', '3/10', '10/10', '10/10', '3-4m', '7/10', '6/10', '6/10', '9.0', 'Databases (Database Issue)'],
    ['PLOS', 'PLOS Computational Biology', '4.3', '8/10', '$3,165', '5/10', '10/10', '10/10', '3m', '8/10', '9/10', '9/10', '8.8', 'Bioinformatics & Systems Bio'],
    ['Wiley', 'Journal of Pineal Research', '10.3', '10/10', '$3,950', '4/10', '9/10', '9/10', '3-4m', '7/10', '7/10', '7/10', '8.6', 'Chronobiology & Melatonin'],
    ['ACS', 'J. Chem. Inf. Model (JCIM)', '5.6', '8/10', '$4,000', '4/10', '9/10', '9/10', '3m', '8/10', '8/10', '8/10', '8.4', 'Chemoinformatics & Databases'],
    ['Elsevier', 'Cell Reports', '8.8', '9/10', '$5,400', '2/10', '10/10', '10/10', '4-5m', '6/10', '5/10', '5/10', '7.8', 'Interdisciplinary Molecular Bio'],
    ['Nature', 'Nature Communications', '14.7', '10/10', '$6,490', '1/10', '10/10', '10/10', '5m', '5/10', '4/10', '4/10', '7.5', 'Broad Interdisciplinary Science'],
    ['Elsevier', 'Computers in Bio. & Med.', '7.7', '9/10', '$0 / $2,800', '10/10', '9/10', '9/10', '3m', '8/10', '10/10', '10/10', '9.2', 'AI & Computational Medicine'],
    ['SAGE', 'Journal of Biol. Rhythms', '2.1', '5/10', '$0 / $3,950', '10/10', '7/10', '7/10', '2-3m', '9/10', '10/10', '10/10', '8.4', 'Circadian Biology (Specialized)'],
    ['Oxford', 'Database', '3.6', '6/10', '$2,000', '7/10', '8/10', '8/10', '3m', '8/10', '9/10', '9/10', '8.2', 'Database Curation & Methods'],
    ['Nature', 'Scientific Reports', '3.9', '7/10', '$2,850', '6/10', '10/10', '10/10', '4m', '7/10', '9/10', '9/10', '8.0', 'General Multidisciplinary'],
    ['PLOS', 'PLOS ONE', '3.7', '7/10', '$2,100', '7/10', '10/10', '10/10', '3m', '8/10', '9/10', '9/10', '8.1', 'Broad Open Access Science'],
    ['Wiley', 'Molecular Informatics', '3.4', '6/10', '$0 / $3,500', '10/10', '7/10', '7/10', '3m', '8/10', '9/10', '9/10', '8.0', 'Chemoinformatics (Molecular Modeling)'],
    ['ACS', 'ACS Bio & Med Chem Au', '4.5', '7/10', '$2,000', '7/10', '8/10', '8/10', '2m', '9/10', '9/10', '9/10', '8.0', 'Open Access Med Chem'],
    ['Elsevier', 'J. Biomedical Informatics', '4.0', '7/10', '$0 / $3,000', '10/10', '8/10', '8/10', '3-4m', '7/10', '9/10', '9/10', '8.2', 'Bioinformatics Methodology']
]

# Write CSV
with open(csv_file, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

# Write DOC (HTML Format)
html_content = """
<html>
<head>
<style>
    body { font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: auto; padding: 20px; }
    h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; text-align: center; }
    h2 { color: #2980b9; margin-top: 30px; border-left: 5px solid #3498db; padding-left: 10px; }
    table { border-collapse: collapse; width: 100%; margin-top: 15px; font-size: 0.9em; }
    th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
    th { background-color: #34495e; color: white; }
    tr:nth-child(even) { background-color: #f9f9f9; }
    .tier-a { color: #e74c3c; font-weight: bold; }
    .tier-b { color: #27ae60; font-weight: bold; }
    .student-fit { background-color: #d1ecf1; color: #0c5460; padding: 15px; border-radius: 5px; margin: 20px 0; border: 1px solid #bee5eb; }
    .recommendation { background-color: #fff3cd; color: #856404; padding: 15px; border-radius: 5px; border: 1px solid #ffeeba; }
</style>
</head>
<body>
    <h1>ChronoBase: Comprehensive Journal Publication Strategy</h1>
    <p>This report provides an exhaustive analysis of potential publication venues for the <b>ChronoBase</b> project across all major academic publishing houses (Oxford, PLOS, Wiley, ACS, Elsevier, Nature, and SAGE).</p>

    <h2>1. The "Big House" Comparison (Top Tier)</h2>
    <table>
        <tr>
            <th>Publisher</th>
            <th>Journal</th>
            <th>Impact Factor</th>
            <th>APC (Cost)</th>
            <th>Student Fit</th>
            <th>Final Rating</th>
        </tr>
        <tr><td>Oxford</td><td>Nucleic Acids Research</td><td>13.1</td><td>$4,192</td><td>Moderate</td><td class="tier-a">9.0</td></tr>
        <tr><td>PLOS</td><td>PLOS Comp. Biology</td><td>4.3</td><td>$3,165</td><td>High</td><td class="tier-a">8.8</td></tr>
        <tr><td>Wiley</td><td>J. Pineal Research</td><td>10.3</td><td>$3,950</td><td>Moderate</td><td class="tier-a">8.6</td></tr>
        <tr><td>ACS</td><td>J. Chem. Inf. Model.</td><td>5.6</td><td>$4,000</td><td>High</td><td class="tier-a">8.4</td></tr>
        <tr><td>Elsevier</td><td>Cell Reports</td><td>8.8</td><td>$5,400</td><td>Selective</td><td class="tier-a">7.8</td></tr>
    </table>

    <h2>2. Highly Accessible & Student-Friendly Venues</h2>
    <div class="student-fit">
        <b>Why these are ranked higher for students:</b> These journals either offer a "Subscription" track (Free to publish) or have the most robust waiver programs for unfunded researchers.
    </div>
    <table>
        <tr>
            <th>Publisher</th>
            <th>Journal</th>
            <th>Impact Factor</th>
            <th>APC (Cost)</th>
            <th>Review Speed</th>
            <th>Final Rating</th>
        </tr>
        <tr><td>Elsevier</td><td>Computers in Bio. & Med.</td><td>7.7</td><td><b>$0</b> (Subscription)</td><td>Fast (3m)</td><td class="tier-b">9.2</td></tr>
        <tr><td>SAGE</td><td>J. Biol. Rhythms</td><td>2.1</td><td><b>$0</b> (Subscription)</td><td>Fast (2-3m)</td><td class="tier-b">8.4</td></tr>
        <tr><td>Wiley</td><td>Molecular Informatics</td><td>3.4</td><td><b>$0</b> (Subscription)</td><td>Moderate</td><td class="tier-b">8.0</td></tr>
        <tr><td>Nature</td><td>Scientific Reports</td><td>3.9</td><td>$2,850 (Waiver Available)</td><td>Moderate</td><td class="tier-b">8.0</td></tr>
    </table>

    <h2>3. Strategic Breakdown by ChronoBase Pillar</h2>
    <ul>
        <li><b>Bioinformatics Methodology:</b> If the focus is on the <i>coding/structure</i> of the database, target <b>PLOS Computational Biology</b> or <b>J. Biomedical Informatics</b>.</li>
        <li><b>Chemoinformatics & Drug Targets:</b> If the focus is on <i>cancer targets/ligands</i>, target <b>ACS JCIM</b> or <b>Molecular Informatics</b>.</li>
        <li><b>Circadian Science:</b> If the focus is on <i>ZT classification/rhythms</i>, target <b>J. Pineal Research</b> or <b>J. Biological Rhythms</b>.</li>
        <li><b>Clinical Impact:</b> If the focus is on <i>oncology/chronotherapy</i>, target <b>Cell Reports</b> or <b>Computers in Biology & Medicine</b>.</li>
    </ul>

    <div class="recommendation">
        <h3>Final Master Plan Recommendation</h3>
        <p>1. <b>Primary Target:</b> Aim for <b>Nucleic Acids Research (Database Issue)</b> first if your registry is 100% complete. It has the highest "Impact per Word" in this field.</p>
        <p>2. <b>Safe High-Impact Target:</b> <b>Computers in Biology and Medicine</b>. It has a high IF (7.7), it is <b>FREE</b> to publish via the subscription route, and it loves time-series medical data.</p>
        <p>3. <b>Community Engagement:</b> <b>PLOS Computational Biology</b>. Their "Open Science" culture is perfect for students, and their waiver program (PFA) is very fair.</p>
    </div>
</body>
</html>
"""

with open(doc_file, 'w') as f:
    f.write(html_content)

print "Comprehensive reports successfully generated in " + downloads_path + ":"
print "1. " + os.path.basename(csv_file)
print "2. " + os.path.basename(doc_file)

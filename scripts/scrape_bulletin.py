"""
Exam bulletin scraper — pulls upcoming exam data from 4 sources
Saves to public/data/bulletin.json
Usage: python scripts/scrape_bulletin.py
"""
import json, re, os
from datetime import datetime
from pathlib import Path
import urllib.request, urllib.error

OUTPUT = Path(__file__).parent.parent / 'public' / 'data' / 'bulletin.json'

def fetch_testbook():
    """Scrape Testbook upcoming exams"""
    exams = []
    try:
        url = "https://testbook.com/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        # Extract exam names and dates
        patterns = [
            r'([A-Za-z\s]+(?:Exam|Recruitment|202[5-6]))',
            r'(\d{1,2}\s*(?:January|February|March|April|May|June|July|August|September|October|November|December)\s*202[5-6])',
        ]
        matches = re.findall(r'(RRB|SSC|UPSC|IBPS|SBI|RBI)[^<]{20,100}', html)
        for m in matches[:3]:
            name = re.sub(r'<[^>]+>', '', m).strip()[:60]
            exams.append({'name': name, 'date': '2025-2026', 'vacancies': '', 'status': 'Expected', 'url': 'https://testbook.com/'})
    except Exception as e:
        print(f'  Testbook: {e}')
    return exams

def fetch_adda247():
    """Scrape Adda247 job notifications"""
    exams = []
    try:
        url = "https://www.adda247.com/jobs/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        # Extract notification titles
        matches = re.findall(r'<h[23][^>]*>(.*?(?:Recruitment|Exam|Notification|Vacancy).*?)</h[23]>', html, re.IGNORECASE)
        for m in matches[:3]:
            clean = re.sub(r'<[^>]+>', '', m).strip()[:80]
            exams.append({'name': clean, 'date': '2025-2026', 'vacancies': '', 'status': 'Notified', 'url': 'https://www.adda247.com/jobs/'})
    except Exception as e:
        print(f'  Adda247: {e}')
    return exams

def fetch_sarkari_result():
    """Scrape SarkariResult latest jobs"""
    exams = []
    try:
        url = "https://www.sarkariresult.com/latestjob/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        matches = re.findall(r'<a[^>]*href="[^"]*"[^>]*>(.*?(?:Recruitment|Vacancy|Exam|Online).*?)</a>', html, re.IGNORECASE)
        for m in matches[:5]:
            clean = re.sub(r'<[^>]+>', '', m).strip()[:80]
            if len(clean) > 10:
                exams.append({'name': clean, 'date': '2025-2026', 'vacancies': '', 'status': 'Active', 'url': 'https://www.sarkariresult.com/latestjob/'})
    except Exception as e:
        print(f'  SarkariResult: {e}')
    return exams

def fetch_careerpower():
    """Scrape CareerPower upcoming exams"""
    exams = []
    try:
        url = "https://www.careerpower.in/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
        
        matches = re.findall(r'<a[^>]*>(.*?(?:Exam|Recruitment|Notification).*?)</a>', html, re.IGNORECASE)
        for m in matches[:3]:
            clean = re.sub(r'<[^>]+>', '', m).strip()[:80]
            exams.append({'name': clean, 'date': '2025-2026', 'vacancies': '', 'status': 'Upcoming', 'url': 'https://www.careerpower.in/'})
    except Exception as e:
        print(f'  CareerPower: {e}')
    return exams

def main():
    print("Scraping exam bulletin data...")
    
    all_exams = []
    
    # Try each source
    all_exams.extend(fetch_testbook())
    all_exams.extend(fetch_adda247())
    all_exams.extend(fetch_sarkari_result())
    all_exams.extend(fetch_careerpower())
    
    # Deduplicate by name similarity
    seen = set()
    unique = []
    for e in all_exams:
        key = e['name'][:30].lower()
        if key not in seen:
            seen.add(key)
            unique.append(e)
    
    # If scraping failed, use fallback data
    if len(unique) < 3:
        print("Scraping limited results — using fallback data")
        unique = [
            {"name": "RRB Group D Level 1 CBT", "date": "August 2026 (Expected)", "vacancies": "22,195", "status": "Upcoming", "url": "https://www.rrbcdg.gov.in/"},
            {"name": "RRB NTPC CBT 2 (Graduate)", "date": "July 2026", "vacancies": "5,810", "status": "Ongoing", "url": "https://www.rrbcdg.gov.in/"},
            {"name": "RRB NTPC CBT 2 (UG Level)", "date": "September 2026", "vacancies": "3,058", "status": "Upcoming", "url": "https://www.rrbcdg.gov.in/"},
            {"name": "SSC CGL Tier 2 2026", "date": "October 2026", "vacancies": "~8,000", "status": "Upcoming", "url": "https://ssc.nic.in/"},
            {"name": "IBPS PO 2026 Prelims", "date": "October 2026", "vacancies": "~5,000", "status": "Expected", "url": "https://www.ibps.in/"},
        ]
    
    # Save
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(unique[:8], f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(unique[:8])} items to {OUTPUT}")
    for e in unique[:5]:
        print(f"  • {e['name']} — {e['date']} ({e['status']})")

if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup
import time
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


base_index = "31567219"
names = ["mutinda", "cruz", "fausto", "fazio", "majaliwa", "armel", "masiga", "ndusa", "preston","motondi"]
url = "https://results.knec.ac.ke/Home/CheckResults"

def check_result(index_number, name):
    """Check results for a specific index and name combination"""
    try:
        session = requests.Session()
        
 
        response = session.get(url, timeout=10, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        

        data = {
            'IndexNumber': index_number,
            'Name': name
        }
        

        result = session.post(url, data=data, timeout=10, verify=False)
        

        if "valid index number" not in result.text.lower():
            return True, result.text
        return False, None
        
    except Exception as e:

        return False, None

def main():
    print("="*60)
    print("KCSE RESULTS CHECKER")
    print("="*60)
    print(f"Base Index: {base_index}001 - {base_index}050")
    print(f"Names to check: {', '.join(names)}")
    print("="*60)
    print()
    
    found_results = []
    total_checks = 0
    
    for name in names:
        print(f"[{name.upper()}]", end=" ", flush=True)
        
        for num in range(1, 51):
            index_number = f"{base_index}{num:03d}"
            total_checks += 1
            
 
            print(".", end="", flush=True)
            
            success, content = check_result(index_number, name)
            
            if success:
                print(f" ✓ FOUND at {index_number}")
                found_results.append({
                    'name': name,
                    'index': index_number,
                    'content': content
                })

                with open(f"result_{name}_{index_number}.html", "w", encoding="utf-8") as f:
                    f.write(content)
                break
            
 
            time.sleep(0.5)
        else:
            print(" ✗ Not found")
        
        print()
    

    print("\n" + "="*50)
    print("SUMMARY OF RESULTS")
    print("="*50)
    
    if found_results:
        for result in found_results:
            print(f"✓ {result['name'].upper()}: {result['index']}")
            print(f"  Saved to: result_{result['name']}_{result['index']}.html\n")
    else:
        print("No results found for any name.")
    
    print(f"\nTotal found: {len(found_results)}/{len(names)}")

if __name__ == "__main__":
    main()
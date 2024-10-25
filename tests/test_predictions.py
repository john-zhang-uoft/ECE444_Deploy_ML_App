import requests
import time
import csv

url = "http://Serve-sentiment-env-1.eba-zm6xumcq.us-east-2.elasticbeanstalk.com/predict"  # Replace with actual URL

test_cases = [
    {"text": """OSHAWA — To help close the remaining 10 per cent gap of people who do not have access to a regular health-care provider, the Ontario government is breaking down barriers for Ontario students to become family doctors by expanding the Learn and Stay grant to include family medicine. The province is also requiring medical schools to prioritize seats for Ontario residents, helping ensure more doctors who study in Ontario treat Ontario patients rather than leaving the province after their studies.

“Today’s announcement is the latest step in our plan to connect every person in Ontario, no matter where they live, to primary care,” said Premier Doug Ford. “We’re training more family doctors than ever before, helping them live, learn and stay in Ontario, and we’re helping Ontario students support and remain in our province by prioritizing them for medical school seats in Ontario schools.”

Starting in 2026, the government is investing an estimated $88 million over three years to expand Learn and Stay grants for 1,360 eligible undergraduate students that commit to practice family medicine with a full roster of patients once they graduate. This includes $17.7 million for the 2026-2027 academic year. It is estimated the total investment will enable the connection of an additional 1.36 million people to primary care based on average attachment rates for family doctors. The funding will cover all tuition and other direct educational costs like books, supplies and equipment in exchange for a term of service as a physician in any community across Ontario.""",
     "expected": "REAL"},

    {"text": """Quebec's social services minister says he's outraged by reports that educators at a detention centre for youth in Montreal had sexual relations with minor detainees — and that one of the employees allegedly had a baby with a teenage resident.

Lionel Carmant told reporters Friday that both the detention facility and the police are investigating allegations of sexual misconduct at the Cité-des-Prairies rehabilitation centre. The facility houses some of the most troubled young people in Quebec's youth protection system, most of whom have committed crimes, including murder and weapons trafficking.

"It's heartbreaking, there are no other words," Carmant said, speaking at an unrelated announcement in Montreal. "Sexual abuse by people in power is intolerable, intolerable in all environments."

La Presse reported that nine female employees at the detention centre had sexual intercourse with at least five minor residents, and that one of the educators had a baby with a detainee.

The regional health authority for south-central Montreal would not confirm the details in the La Presse report, but said two managers at the detention centre were "temporarily removed" because members of their teams are under investigation. An unspecified number of employees who worked for the two managers have been suspended or fired, it added.

The scandal had the Opposition Liberals wondering whether Carmant has lost control of the youth protection network. Liberal critic Brigitte Garceau called for an investigation at all youth and rehabilitation centres in the province.""",
"expected": "REAL"},

    {"text": "Elon MUST GETS EBOLA AND DIES IN 2024. The American government has been keeping this a secret", "expected": "FAKE"},
    
    {"text": "JOE Biden's son has been discovered to have ties to Russia", "expected": "FAKE"},
]

def functional_tests():
    print("Running Functional Tests")
    for i, case in enumerate(test_cases):
        response = requests.post(url, json={"text": case["text"]})
        if response.status_code == 200:
            result = response.json()['prediction']
            print(f"Test Case {i+1}: Expected {case['expected']}, Got {result}")
        else:
            print(f"Test Case {i+1}: Failed with status code {response.status_code}")

def latency_test():
    print("Running Latency Test")
    with open('latency_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Test Case", "Latency (seconds)"])

        # Loop through each test case and perform 100 requests
        for i, case in enumerate(test_cases):
            print(f"Running latency test for Test Case {i+1}")
            for _ in range(100):
                start_time = time.time()
                response = requests.post(url, json={"text": case["text"]})
                end_time = time.time()
                
                if response.status_code == 200:
                    latency = end_time - start_time
                    writer.writerow([f"Test Case {i+1}", latency])
                else:
                    print(f"Failed request with status code {response.status_code}")

# Run both tests
functional_tests()
latency_test()

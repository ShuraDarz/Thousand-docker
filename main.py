#Import the modules
import requests
import json
import logging

# Define the Thousand API credentials
API_USERNAME = 'shura_darz@hotmail.com'
API_TOKEN = 'zv7m0654ensw1lfjjwi6uhy8yvimiivv'
API_AUTH = (API_USERNAME, API_TOKEN)

# Send a GET request to retrieve the TEST using the API credentials 
response = requests.get('https://api.thousandeyes.com/v6/tests.json', auth=API_AUTH)

# Parse JSON data from the response 
data = json.loads(response.text)

# Iterate over each TEST in the data and print name, ID and type
tests = data["test"]
for test in tests:
    testName = test["testName"]
    testId = test["testId"]    
    type = test["type"]
    print(f"Metrics of the TEST: {testName}, whith Id: {testId}, and Type: {type}")

# Send a GET request to retrieve metrics for each TEST using the API credentials
    response = requests.get(f'https://api.thousandeyes.com/v6/net/metrics/{testId}.json', auth=(API_USERNAME, API_TOKEN))

# Parse the JSON data for the metrics
    data = json.loads(response.text)

# Itinerate over each METRIC and print the Agent Name, Average Latency, Macimum Latency, Packets loss,  Jitter, Minimum Latency and Round ID
    metrics = data["net"]["metrics"]
    for metric in metrics:
        agentName = metric["agentName"]
        avgLatency = metric["avgLatency"]
        maxLatency = metric["maxLatency"]
        loss = metric["loss"]
        jitter = metric["jitter"]
        minLatency = metric["minLatency"]
        roundId = metric["roundId"]
    
        print("Agent Name:", agentName) 
        print("Average Latency:", avgLatency)
        print("Maximum Latency:", maxLatency)
        print("Loss:", loss)
        print("Jitter:", jitter)
        print("Minimum Latency:", minLatency)
        print("Round ID:", roundId)

# Define the trial user credential for Thousandeyes  
TRIAL_USERNAME = 'enriquem.garduno.alias1@gmail.com'
TRIAL_TOKEN = 'ifthrrvq8glcucrka9dpikn4r48vabub' 
TRIAL_AUTH = (TRIAL_USERNAME, TRIAL_TOKEN)

# Send a GET requests to retrieve metrics for each TEST using TRIAL Credentials 
trial_test_response = requests.get(f'https://api.thousandeyes.com/v6/net/metrics/{testId}.json', auth=(TRIAL_AUTH))

# Parse JSON data for the trial test response 
trial_test_data = trial_test_response.json()

# Print trial test response
print(trial_test_data)

# Send a GET request to retrieve the TEST using trial crecentials  
trial_response = requests.get('https://api.thousandeyes.com/v6/tests.json', auth=TRIAL_AUTH)

# Parse JSON data
trial_data = trial_response.json()

# Iterate over each TEST in the data and print name, ID and type
trial_tests = trial_data["test"]
for trial_test in trial_tests:
    trialtestName = trial_test["testName"]
    trialtestId = trial_test["testId"]    
    trialtype = trial_test["type"]
    print(f"Info of the TEST: {trialtestName}, whith Id: {trialtestId}, and Type: {trialtype} of the trial user")

# Send a GET requests to retrieve metrics over each TEST using the trial credentials 
    trial_response = requests.get(f'https://api.thousandeyes.com/v6/net/metrics/{testId}.json', auth=(API_USERNAME, API_TOKEN))

# Parse the JoN data for metrics
    trial_metric_data = trial_response.json()

# Iterate over each METRIC and print the Agent Name, Average Latency, MAximum Latency, Packet Loss, Jitter, Minimum Latency and Round ID
    trial_metrics = trial_metric_data["net"]["metrics"]
    for trial_metric in trial_metrics:
        trialagentName = trial_metric["agentName"]
        trialavgLatency = trial_metric["avgLatency"]
        trialmaxLatency = trial_metric["maxLatency"]
        trialloss = trial_metric["loss"]
        trialjitter = trial_metric["jitter"]
        trialminLatency = trial_metric["minLatency"]
        trialroundId = trial_metric["roundId"]
    
        print("Agent Name:", trialagentName) 
        print("Average Latency:", trialavgLatency)
        print("Maximum Latency:", trialmaxLatency)
        print("Loss:", trialloss)
        print("Jitter:", trialjitter)
        print("Minimum Latency:", trialminLatency)
        print("Round ID:", trialroundId)

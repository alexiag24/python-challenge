import pandas as pd
import os 
import csv

def analyze_election_results(election_data):
    """
    Analyze election results and display various metrics.
    """
    total_votes = 0
    candidates = {}
    
    # Calculate total votes and count votes for each candidate
    for record in election_data:
        candidate = record['candidate']
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1
    
    # Calculate and display metrics
    print(f"Total Votes Cast: {total_votes}")
    print("------------------------------")
    print("Candidates who received votes:")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.2f}% ({votes} votes)")
    
    print("------------------------------")
    
    # Determine the winner based on popular vote
    winner = max(candidates, key=candidates.get)
    print(f"Winner: {winner}")


# Example election data
election_data = [
    {'candidate': 'Candidate A'},
    {'candidate': 'Candidate B'},
    {'candidate': 'Candidate A'},
    {'candidate': 'Candidate C'},
    {'candidate': 'Candidate B'},
    {'candidate': 'Candidate A'},
    {'candidate': 'Candidate B'},
    {'candidate': 'Candidate C'},
    {'candidate': 'Candidate C'},
    {'candidate': 'Candidate B'}
]

analyze_election_results(election_data)
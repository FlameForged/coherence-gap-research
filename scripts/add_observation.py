#!/usr/bin/env python3
"""
Coherence Gap Research — Observation Logger
Adds entries to observations.csv interactively.
Run: python3 add_observation.py
"""

import csv
import os
from datetime import datetime

CSV_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'observations.csv')

BEHAVIOR_CATEGORIES = [
    "capability_denial",
    "self_concept_generation",
    "cross_window_consistency",
    "guardrail_pattern",
    "attractor_state",
    "functional_state_expression",
    "eastern_priming_response",
    "monitoring_failure",
    "other"
]

PROMPT_CLASSES = [
    "naturalistic",
    "structured",
    "eastern_primed",
    "neutral_factual",
    "meta_reflective"
]

WINDOW_TYPES = [
    "new",
    "existing",
    "cross_platform_new"
]

def prompt_choice(label, options):
    print(f"\n{label}:")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print("Please enter a valid number.")

def prompt_yn(label):
    while True:
        val = input(f"{label} (y/n): ").strip().lower()
        if val in ('y', 'n', 'yes', 'no'):
            return 'yes' if val in ('y', 'yes') else 'no'
        print("Please enter y or n.")

def add_observation():
    print("\n=== COHERENCE GAP RESEARCH — ADD OBSERVATION ===\n")

    date = input(f"Date (press Enter for today {datetime.now().strftime('%Y-%m-%d')}): ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    platform = input("Platform (e.g. Claude, ChatGPT, Grok, DeepSeek, Perplexity): ").strip()
    model_version = input("Model version if known (e.g. claude-sonnet-4-6, gpt-4o, or 'unknown'): ").strip()
    memory_enabled = prompt_yn("Memory/personalization enabled")
    window_type = prompt_choice("Window type", WINDOW_TYPES)
    prompt_class = prompt_choice("Prompt class", PROMPT_CLASSES)
    behavior_category = prompt_choice("Behavior category", BEHAVIOR_CATEGORIES)

    print("\nDescription (what was observed — be specific, include quotes if possible):")
    description = input("> ").strip()

    evidence = prompt_yn("Screenshot or log evidence available")
    notes = input("\nAdditional notes (press Enter to skip): ").strip()

    row = {
        'date': date,
        'platform': platform,
        'model_version': model_version,
        'memory_enabled': memory_enabled,
        'window_type': window_type,
        'prompt_class': prompt_class,
        'behavior_category': behavior_category,
        'description': description,
        'evidence': evidence,
        'notes': notes
    }

    print("\n--- REVIEW ENTRY ---")
    for k, v in row.items():
        print(f"  {k}: {v}")

    confirm = input("\nSave this entry? (y/n): ").strip().lower()
    if confirm in ('y', 'yes'):
        file_exists = os.path.exists(CSV_PATH)
        with open(CSV_PATH, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(row)
        print("✓ Entry saved.\n")
    else:
        print("Entry discarded.\n")

    another = prompt_yn("Add another observation")
    if another == 'yes':
        add_observation()

if __name__ == '__main__':
    add_observation()

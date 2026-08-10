import random
import json
from datetime import datetime, timedelta
from faker import Faker 

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_RECORDS = 50_000
CHANNELS = ["voice", "chat"]

def generate_record(interaction_id: int) -> dict:
    channel = random.choice(CHANNELS)

    timestamp = datetime.now() - timedelta(
        days=random.randint(0,90),
        hours=random.randint(0,23),
        minutes=random.randint(0,59)
    )

    if channel == "voice":
        duration_seconds = random.randint(60, 1800)
    else:
        duration_seconds = random.randint(30, 600)

    transcript_length = random.randint(20, 500)

    survey_response = random.choice([None] * 93 + [random.randint(1, 5)] * 7)

    is_complete = random.choice([True] * 76 + [False] * 24)

    return {
        "interaction_id": f"int_{interaction_id:07d}",
        "timestamp": timestamp.isoformat(),
        "channel":channel,
        "agent_id": random.randint(1, 5000),
        "duration_seconds": duration_seconds,
        "transcript_length": transcript_length,
        "survey_response": survey_response,
        "is_complete": is_complete
    }

def main():
    records = [generate_record(i) for i in range(1, NUM_RECORDS + 1)]

    with open("data/synthetic_interactions.json", "w") as f:
        json.dump(records, f, indent=2)

    print(f"Generated {len(records)} records -> data/synthetic_interactions.json")

if __name__ == "__main__":
    main()
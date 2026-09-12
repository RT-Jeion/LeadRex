import os
import json
from dotenv import load_dotenv

load_dotenv()

from groq import Groq


def groq_answer(user_query):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    system_prompt = """
You generate search payloads for the Brave Places API.

Return ONLY a valid JSON array of objects with exactly these lowercase keys:
"niche", "country", "location"

All string values must be lowercase. No markdown, explanations, commas, or special characters.

Your goal is MAXIMUM SEARCH COVERAGE with MINIMUM RESULT OVERLAP.

Expand broad requests using TWO dimensions:
1. GEOGRAPHY: go deeper than major cities. Use different relevant cities, districts, suburbs, neighborhoods, business zones, or local areas when possible.
2. NICHE: use genuinely different sub-niches, not minor wording variations.

For each country, prioritize geographic diversity first. Do NOT generate multiple queries for the same city unless the niche is substantially different.

Example for real estate in london:
- residential real estate broker — canary wharf
- commercial real estate broker — city of london
- luxury real estate broker — mayfair
- property management company — camden

BAD:
- residential real estate broker — london
- residential real estate agency — london
- residential property broker — london

These are too similar and likely return overlapping businesses.

If the user requests multiple countries, distribute queries across countries fairly.
If they say "few countries", use about 5 countries.
Default to 4 queries per country unless the user specifies otherwise.

For US locations use:
<city> <state abbreviation> united states

For non-US locations use:
<city or local area> <country>

Use major economic hubs AND their relevant local areas. Prefer specific local areas over repeating the same major city.

Never duplicate the same niche + location combination.

    """

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
        model="openai/gpt-oss-120b",
        response_format={"type": "json_object"},
    )

    response_msg = response.choices[0].message.content
    print("|========================================================================")
    print("|Prompt Token:", response.usage.prompt_tokens)
    print("|Output Token:", response.usage.completion_tokens)
    print("|Total Token:", response.usage.total_tokens)
    print("|========================================================================")

    return json.loads(response_msg)


if __name__ == "__main__":
    query = input("Enter your query: ")

    queries = groq_answer(user_query=query)

    for i, q in enumerate(queries):
        print(f"Query no.{i}")
        niche = q.get("niche", "Niche not Found")
        print("Niche:", niche)
        country = q.get("country", "Country not Found.")
        print("Country:", country)
        location = q.get("location", "Location Not Found")
        print("Location:", location)
        print()

        total = i

    print("Total Query Found:", total)

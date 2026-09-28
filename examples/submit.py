"""Submit and poll a representative MuAPI OpenAI-family endpoint."""

import os
import sys
import time

import requests

BASE = "https://api.muapi.ai/api/v1"
JOBS = {
    "image": (
        "gpt-image-2-text-to-image",
        {"prompt": "Editorial product photo of a ceramic coffee cup on a warm wood table", "aspect_ratio": "1:1", "resolution": "2K"},
    ),
    "sora": (
        "openai-sora-2-pro-text-to-video",
        {"prompt": "A slow tracking shot through a sunlit greenhouse", "aspect_ratio": "16:9", "duration": 8, "resolution": "1080p"},
    ),
    "reasoning": (
        "gpt-6-astra",
        {"prompt": "Compare two database migration strategies and explain the tradeoffs.", "reasoning_effort": "medium"},
    ),
}


def main():
    key = os.environ.get("MUAPI_API_KEY")
    if not key:
        raise SystemExit("Set MUAPI_API_KEY in your environment first.")
    if len(sys.argv) != 2 or sys.argv[1] not in JOBS:
        raise SystemExit("Usage: python examples/submit.py {image|sora|reasoning}")

    endpoint, payload = JOBS[sys.argv[1]]
    headers = {"x-api-key": key, "Content-Type": "application/json"}
    response = requests.post(f"{BASE}/{endpoint}", headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    job = response.json()
    request_id = job.get("request_id")
    if not request_id:
        print(job)
        return
    print(f"Submitted request_id={request_id}")

    while True:
        result = requests.get(f"{BASE}/predictions/{request_id}/result", headers=headers, timeout=60)
        result.raise_for_status()
        data = result.json()
        status = str(data.get("status", "")).lower()
        print(data)
        if status in {"completed", "succeeded", "success", "failed", "error", "cancelled"}:
            break
        time.sleep(3)


if __name__ == "__main__":
    main()

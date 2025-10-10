import tiktoken
import os
import requests
import json
import math
import re
from pathlib import Path
import json
import csv
from pathlib import Path
import tempfile
import os, time, stat
import re, os, time, tempfile, csv, stat
from pathlib import Path

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
CLAUDE_URL = "https://api.anthropic.com/v1/messages/count_tokens"
CLAUDE_MODEL = "claude-3-7-sonnet-20250219"




DATE_RE = re.compile(r'^\s*(\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2})\s*$')
DASH_RE = re.compile(r'^\s*-{4,}\s*$')
HASH_RE = re.compile(r'^\s*#{4,}\s*$')

def replace_with_retries(tmp_path: str, dst_path: str, retries: int = 6, delay: float = 0.5):
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            try:
                os.chmod(dst_path, stat.S_IWRITE)
            except FileNotFoundError:
                pass
            except Exception:
                pass
            os.replace(tmp_path, dst_path)
            return
        except PermissionError as e:
            last_exc = e
            time.sleep(delay * attempt)
        except Exception as e:
            try: os.remove(tmp_path)
            except Exception: pass
            raise
    raise PermissionError(f"replace failed after {retries} retries: {last_exc}")

def extract_first_experiment(path: str):
    """Return (date, input_str, output_str, header_before_date, remaining_after_experiment)
       or None if no complete experiment found. This function closes file before returning.
    """
    src = Path(path)
    if not src.exists():
        raise FileNotFoundError(path)

    pre_lines = []
    cur_date = None
    input_buf = []
    output_buf = []
    found_date_idx = None

    with src.open('r', encoding='utf-8', errors='replace') as fr:
        for line in fr:
            if cur_date is None:
                m = DATE_RE.match(line)
                if m:
                    cur_date = m.group(1)
                    pre_lines.append(line)
                    found_date_idx = len(pre_lines) - 1
                    continue
                else:
                    pre_lines.append(line)
                    continue
            # we have a date; now expect dashes then input, dashes then output ending with hashes
            # read until we hit the closing hashes or EOF
            # read input until first DASH_RE encountered
            if DASH_RE.match(line):
                # start reading input lines
                input_buf = []
                for line in fr:
                    if DASH_RE.match(line):
                        # start reading output
                        output_buf = []
                        for line in fr:
                            if HASH_RE.match(line):
                                # collect remainder after hashes
                                remaining = fr.read()
                                header_before = ''.join(pre_lines[:found_date_idx]) if found_date_idx is not None else ''
                                return cur_date, ''.join(input_buf).rstrip(), ''.join(output_buf).rstrip(), header_before, remaining
                            output_buf.append(line)
                        # EOF reached while reading output -> no complete experiment
                        return None
                    input_buf.append(line)
                # EOF reached while reading input -> no complete experiment
                return None
        # EOF reached without finding a complete experiment
        return None

def process_all_atomic(src_path: str, csv_path: str):
    src = Path(src_path)
    csvf = Path(csv_path)
    header_written = csvf.exists()
    while True:
        ex = extract_first_experiment(str(src))
        if not ex:
            break
        date, inp, outp, header_before, remaining = ex

        # compute tokens (may raise)
        g_in = tokens_gpt4omini(inp)
        g_out = tokens_gpt4omini(outp)
        c_in = tokens_claude37(inp)
        c_out = tokens_claude37(outp)

        # append CSV
        mode = 'a'
        with csvf.open(mode, newline='', encoding='utf-8') as fh:
            w = csv.writer(fh)
            if not header_written:
                w.writerow(["date","gpt_in","gpt_out","claude_in","claude_out"])
                header_written = True
            w.writerow([date, g_in, g_out, c_in, c_out])

        # write tmp file containing header_before + remaining, then atomically replace
        fd, tmp_path = tempfile.mkstemp(dir=src.parent, prefix=src.name + ".tmp.")
        os.close(fd)
        try:
            with open(tmp_path, 'w', encoding='utf-8', newline='') as tw:
                tw.write(header_before)
                tw.write(remaining)
            replace_with_retries(tmp_path, str(src))
        except Exception:
            try:
                os.remove(tmp_path)
            except Exception:
                pass
            raise
    # done



def tokens_gpt4omini(text: str) -> int:
    """
    Count tokens for GPT-4o-mini.
    Uses tiktoken if available, else heuristic fallback.
    """

    try:
        enc = tiktoken.encoding_for_model("gpt-4o-mini")
    except Exception:
        enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def tokens_claude37(text: str) -> int:
    """
    Count tokens for Claude 3.7 Sonnet via Anthropic API.
    Needs ANTHROPIC_API_KEY set in environment.
    """
    time.sleep(1)
    if not ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY not set")

    payload = {
        "model": CLAUDE_MODEL,
        "messages": [{"role": "user", "content": text}]
    }

    resp = requests.post(
        CLAUDE_URL,
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        data=json.dumps(payload),
        timeout=30,
    )

    if resp.status_code != 200:
        raise RuntimeError(f"Claude API error {resp.status_code}: {resp.text[:200]}")

    data = resp.json()

    # robust extraction (API field name can differ)
    if "input_tokens" in data:
        return int(data["input_tokens"])
    if "usage" in data and "input_tokens" in data["usage"]:
        return int(data["usage"]["input_tokens"])
    raise RuntimeError(f"Unexpected Claude response format: {data}")

def save_results(results: dict, path: str):
    """
    Save results from compute_averages() to file.
    fmt = 'json' oder 'csv'
    """
    path = Path(path) 
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

# print(tokens_claude37("Hello, world"))
# s = "Hello, world"
# print(tokens_gpt4omini(s))  # gibt Anzahl Tokens zurück


# res = compute_averages("temp")
# save_results(res, "ergebnisse.json")

try:
    res = process_all_atomic("temp", "tokens.csv")
    print("Processed:", res)
except Exception as e:
    print("Fehler:", e)
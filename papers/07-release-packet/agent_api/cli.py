#!/usr/bin/env python3
"""Run a bounded synthetic task. Task outcomes are JSON; usage errors use stderr."""
import argparse
import json
from pathlib import Path
import sys
from interface import InputError,MAX_BYTES,parse,execute


def read_local(path):
    with Path(path).open('rb') as stream:return stream.read(MAX_BYTES+1)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--policy',required=True,help='Trusted local synthetic policy JSON; not supplied by an untrusted tenant')
    parser.add_argument('--request',required=True,help='Local request JSON file, or - for stdin')
    args=parser.parse_args(argv)
    try:
        policy=parse(read_local(args.policy))
        raw=sys.stdin.buffer.read(MAX_BYTES+1) if args.request=='-' else read_local(args.request)
        result=execute(policy,parse(raw));status=0
    except (InputError,OSError,ValueError) as error:
        # No partial state escapes on malformed envelopes. No filesystem details
        # are echoed for I/O failures; named files are the only external accesses.
        reason='local input could not be read' if isinstance(error,OSError) else str(error)
        result={'schema':'mcrp-agent-result/0.1','status':'invalid_input','reason':reason};status=2
    print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False))
    return status


if __name__=='__main__':raise SystemExit(main())

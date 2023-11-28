#!/usr/bin/env python3
from argparse import ArgumentParser

parser = ArgumentParser(
    prog="createblanktalks.py",
    description="Create blank talk files for maintaining the CUNY GC seminar page")
parser.add_argument('--begin', help="Start date for the talk files. Use ISO 8601 date formats. Default: next nearest of February 1 or September 1 of the current year.")
parser.add_argument('--end', help="End date for the talk files. Use ISO 8601 date formats. Default: second week of May or December of the current year.")
args = parser.parse_args()

from datetime import date, timedelta

if args.begin is None:
    if date.today().month < 2:
        begindate = date(date.today().year, 2, 1)
    else:
        begindate = date(date.today().year, 9, 1)
else:
    begindate = date.fromisoformat(args.begin)

if args.end is None:
    if date.today().month < 2:
        enddate = date(date.today().year, 5, 14)
    else:
        enddate = date(date.today().year, 12, 14)
else:
    enddate = date.fromisoformat(args.end)

print(f"Generating talk files from {begindate.isoformat()} to {enddate.isoformat()}")

seminardays = [day
                   for i in range((enddate-begindate).days)
                   for day in [begindate + timedelta(days=i)]
                   if day.weekday() == 4 # is it Friday?
                   ]

print(seminardays)

seminarblurb = """---
title: TBD
author: TBD
date: {date}
category: talk
---

TBD
"""

for seminarday in seminardays:
    with open(f'talks/{seminarday.isoformat()}.md', 'x') as f:
        f.write(seminarblurb.format(date=seminarday.isoformat()))

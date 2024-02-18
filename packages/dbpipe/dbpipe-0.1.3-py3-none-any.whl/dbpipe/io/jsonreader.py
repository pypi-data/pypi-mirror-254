import json
from dbpipe.core.pipes import Pipe, Job

def read_pipe(filepath):
    with open(filepath) as f:
        data = json.load(f)

    return Pipe(
        name=data['name'],
        sources=data['sources'],
        destination=data['destination'],
        logfile=data['logfile'],
        processfile=data['processfile']
    )

def read_job(filepath):
    with open(filepath) as f:
        data = json.load(f)

    return Job(
        name=data['name'],
        schedule=data['schedule'],
        jobs=data['jobs']
    )
#!/usr/bin/env python3

import json
import os
import shutil
import subprocess

import click

# Path to the jq binary
jq_path = 'jq'

@click.group()
def lam():
    """
    lam: Laminar data transformation tool, built on jq.
    """
    pass

def parse_program_file(program_file):
    """
    Parses the program file to extract raw jq script.
    Removes comments and other non-jq content.
    """
    with open(program_file, 'r') as file:
        lines = file.readlines()

    return ''.join(line for line in lines if not line.strip().startswith('#'))

def run_jq(jq_script, input_data):
    """
    Run the jq command with the given script and input data.
    """
    process = subprocess.Popen([jq_path, jq_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    output, error = process.communicate(input=input_data)
    return output, error

@lam.command()
@click.argument('program_file', type=click.Path(exists=True))
@click.argument('input', type=str)
def run(program_file, input):
    """
    Process input (file path or raw JSON string) with a jq program file.
    """
    if shutil.which("jq") is None:
        click.echo("Error: jq is not installed. Please install jq to use this tool.", err=True)
        raise SystemExit(1)

    jq_script = parse_program_file(program_file)

    # Check if input is a file path or a raw JSON string
    if os.path.isfile(input):
        with open(input, 'r') as file:
            input_data = file.read()
    else:
        try:
            # Validate input as JSON
            json.loads(input)
            input_data = input
        except json.JSONDecodeError:
            click.echo("Invalid JSON input.", err=True)
            return

    output, error = run_jq(jq_script, input_data)
    if error:
        click.echo(f"Error in jq processing: {error}", err=True)
    else:
        click.echo(output)

if __name__ == '__main__':
    lam()

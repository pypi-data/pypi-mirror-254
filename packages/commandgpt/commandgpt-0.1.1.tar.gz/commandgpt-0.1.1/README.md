# Command GPT

A simple command-line utility to interact with OpenAI's API and retrieve shell suggestions. By default, predefined system and user messages are used to facilitate the interaction. However, flags are available to allow customization of these messages per request.

## Prerequisites

1. **Python 3**
2. **OpenAI API Key**

## Install

```bash
pip install commandgpt
```

## Usage
On the **first run**, Command GPT will create a configuration file named `.openai_config` in your home directory and **prompt you for details**. This file will store the OpenAI API key, model version, user and system messages to facilitate future interactions without the need to repeatedly input those details.

```bash 
└─$ gpt -h                                                        
usage: gpt [-h] [-s SYSTEM] [-u USER] [-d] [-c] [-v] [query]

Interact with OpenAI ChatGPT.

positional arguments:
  query                 your question or query

options:
  -h, --help            show this help message and exit
  -s SYSTEM, --system SYSTEM
                        system message for AI
  -u USER, --user USER  prefix for user message
  -d, --debug           enable debug mode
  -c, --config          reconfigure settings
  -v, --version         show the version number and exit
```


### Example System and User messages

**System**: 
```bash
You are a super star linux system admin.
```
**User**:
```bash
Provide very brief answers without any explanation. Write one-liner commands as answers.
```

### Example usage

```bash
$ gpt "Your query here"
```

However, if you wish to customize the system or user messages:

```bash
$ gpt "Your query here" --system "Your custom system message" --user "Your custom user prefix"
```

```bash
$ gpt "How do I check disk space?"
df -h

```

```bash
$ gpt "How can I see all running processes?"
ps aux
```
```bash
$ gpt "How do I find my machine's IP address?"
ip a
```

## Output Safety Warning

The output from Command GPT is not escaped or quoted by default. This means that special characters or command structures in the output can have direct consequences if executed in a shell or scripting environment.

Using the raw output in scripts or as part of piped commands can be hazardous. I strongly advise against directly integrating the output of Command GPT into another command, script, or pipeline without meticulously reviewing and understanding its implications.

Before utilizing any output, please ensure you're fully aware of its content and potential side effects. 

## A Word of Caution!

While GPT aims to provide accurate and efficient command suggestions, it's essential to understand the commands and not take them at face value. As with any AI system, the output it produces may not always reflect the most accurate or optimal solution for a given task.

### Illustrative Example: Counting Lines in Text Files

Imagine you want to count all the lines in .txt files within a directory, recursively. You might get two suggestions:

1. `find /path/to/directory -type f -name "*.txt" -exec wc -l {} + | awk '{sum += $1} END {print sum}'`
2. `find /path/to/directory -name "*.txt" -exec cat {} + | wc -l `

At first glance, both might seem to do the job. However, upon closer inspection, the first command might return a count that's double the actual number of lines. Why? Because `wc -l` produces an output line for each file and a cumulative count when used with multiple files. The `awk` part then sums all these numbers, leading to an inflated total.

The lesson here? **Always review and understand the commands you get**. Even if a command looks technically correct, it may not deliver the expected result in every context.

Command GPT is a tool, and like any tool, its effectiveness depends on the skill and awareness of the user.

## TODO
 - Think of a better way to store API key (keyring module?).
 - Add more openai models including images.

## License

[MIT](https://choosealicense.com/licenses/mit/)

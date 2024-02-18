import argparse
import os
import pandas as pd
import re

# Define the regular expression pattern for WhatsApp chat lines
whatsapp_line_pattern = r"(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[APap][Mm])\s-\s(.*?):\s(.*)"

whatsapp_line_regex = re.compile(whatsapp_line_pattern)


def update_pattern(pattern: str):
    """
    Updates the regular expression pattern used to parse WhatsApp chat lines.

    Parameters
    ----------
    pattern :str
        The new regular expression pattern to use for parsing WhatsApp chat lines.
    """
    global whatsapp_line_regex
    whatsapp_line_regex = re.compile(pattern)


def reset_pattern():
    """
    Resets the global whatsapp_line_regex to use the default whatsapp_line_pattern.

    This allows restoring the default regex after it has been updated.
    """
    update_pattern(whatsapp_line_pattern)


def parse_line(line: str):
    """
    Parses a line of WhatsApp chat to extract datetime, author, and message.

    Parameters
    ----------
    line : str
        A line of text from a WhatsApp chat log.

    Returns
    -------
    dict
        A dictionary with the parsed components if the line is a new message,
        otherwise a dictionary containing the original message line.
    """
    match = whatsapp_line_regex.match(line)
    if match:
        return {
            'datetime': match.group(1),
            'author': match.group(2),
            'message': match.group(3),
            'new_message': True
        }
    else:
        return {
            'message': line,
            'new_message': False
        }


def chat_to_dataframe(chat_lines: list[str]) -> pd.DataFrame:
    """
    Converts a list of WhatsApp chat lines into a pandas DataFrame.

    Parameters
    ----------
    chat_lines : list[str]
        A list of lines from a WhatsApp chat log.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame with columns for datetime, author, and message.
    """
    parsed_data = []
    for line in chat_lines:
        parsed_line = parse_line(line.strip())
        if parsed_line['new_message']:
            del parsed_line['new_message']
            parsed_data.append(parsed_line)
        else:
            if parsed_data:
                parsed_data[-1]['message'] += ' ' + parsed_line['message']
    parsed_data = pd.DataFrame(parsed_data)

    parsed_data['datetime'] = pd.to_datetime(parsed_data['datetime'],
                                             format="%m/%d/%y, %I:%M %p")
    return parsed_data


def group_conversations_by_time(df: pd.DataFrame, time_threshold_s: int = 300):
    """
    Groups messages into conversations based on a time threshold between messages.

    Parameters
    ----------
    df : pd.DataFrame
        A pandas DataFrame with a 'datetime' column of timestamps.
    time_threshold_s : int, optional
        The time threshold in seconds to determine when a new conversation starts.
        Default is 300 seconds (5 minutes).

    Returns
    -------
    None
        The function adds a 'conversation_id' column to the DataFrame in place.
    """
    last_time = None
    conversation_id = 0
    conversation_ids = []
    for current_time in df['datetime']:
        if last_time is None or (current_time - last_time).total_seconds() > time_threshold_s:
            conversation_id += 1
        conversation_ids.append(conversation_id)
        last_time = current_time

    df['conversation_id'] = conversation_ids


def parse_whatsapp_log(path: str, encoding: str = 'utf-8', output_path: str = None, time: int = 300):
    """
    Parse WhatsApp log file and output CSV.

    Parameters
    ----------
    path : str
        The path to the WhatsApp log file.
    encoding : str, optional
        The file encoding. Defaults to 'utf-8'.
    output_path : str, optional
        Path to output CSV file. Defaults to input file path with .csv extension.

    Raises
    ------
    AssertionError: If path does not exist.

    """

    assert os.path.exists(path), "The provided path does not exist."
    assert time >= 0, "The time threshold must be greater than zero or equal to zero (no grouping)."

    if output_path is None:
        directory = os.path.dirname(path)
        base_name = os.path.basename(path)
        base_name_without_ext = os.path.splitext(base_name)[0]
        output_path = os.path.join(directory, f'{base_name_without_ext}.csv')

    with open(path, 'r', encoding=encoding) as f:
        text = f.readlines()
    df = chat_to_dataframe(text)
    if time:
        group_conversations_by_time(df, time)
    with open(output_path, 'w', encoding=encoding) as f:
        f.write(df.to_csv(index=False, lineterminator='\n'))


"""
Run to parse a WhatsApp log file.
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse a WhatsApp log file.")
    parser.add_argument('path', help='The path to the WhatsApp file.')
    parser.add_argument('-e', dest='encoding', type=str,
                        default='utf-8', help='To spicfy the encoding. (Defualts to `UTF-8`)')
    parser.add_argument('-o', dest='output_path', type=str,
                        help='Specifies the output directory where the parsed CSV will be saved. (Default to the same as input file. `/path/to/file/filename.txt` to `/path/to/file/filename.csv`)')
    parser.add_argument('-t', dest='time', type=int, default=300,
                        help='The maximum amount of time between two messages in seconds to be considered a part of the same conversation. In case you don\'t want to group messages, input \'0\'.  (Default to 300 seconds)')
    args = parser.parse_args()
    parse_whatsapp_log(args.path, args.encoding, args.output_path, args.time)

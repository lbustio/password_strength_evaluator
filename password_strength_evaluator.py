import logging
import multiprocessing
import os
import math
from collections import Counter

import pandas as pd
import passwordmeter

# Configure logging level and message format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def read_data(path, encoding='utf-8'):
    """
    Read data from a file.

    Args:
        path (str): Path to the file.
        encoding (str, optional): Character encoding. Default is 'utf-8'.

    Returns:
        list: List of lines read from the file.
    """
    try:
        with open(path, 'r', encoding=encoding) as file:
            lines = file.readlines()
    except FileNotFoundError:
        logging.error(f'File {path} not found.')
        return []
    return [line.strip() for line in lines]


def save_data(data, path, encoding='utf-8'):
    """
    Save data to a CSV file.

    Args:
        data (pd.DataFrame): Data to save.
        path (str): Path to the output CSV file.
        encoding (str, optional): Character encoding. Default is 'utf-8'.
    """
    try:
        data.to_csv(path, encoding=encoding, index=False)
    except Exception as e:
        logging.error(f'Error saving data to {path}: {e}')


def calculate_entropy(string):
    """
    Calculate the entropy of a given string.

    Args:
    string (str): The input string for which entropy needs to be calculated.

    Returns:
    float: The entropy value of the input string.
    """
    # Count the frequency of each character
    frequency = Counter(string)
    # Calculate the entropy
    entropy = 0.0
    string_length = len(string)
    for freq in frequency.values():
        # Calculate the probability of each character
        probability = freq / string_length
        # Calculate the entropy if probability is not zero
        if probability != 0:
            entropy += probability * math.log2(probability)

    return -entropy


def evaluate_password(password, strength_threshold):
    """
    Evaluate the strength of a single password.

    Args:
        password (str): Password to evaluate.
        strength_threshold (float): Strength threshold to label passwords.

    Returns:
        dict: Dictionary containing the evaluated password and its strength.
    """
    try:
        strength, _ = passwordmeter.test(password)
        strength_label = "weak" if strength < strength_threshold else "strong"
        entropy = calculate_entropy(password)
        return {"password": password, "entropy": entropy, "strength": strength, "label": strength_label}
    except Exception as e:
        logging.warning(f'Error evaluating password: {e}. Skipping password: {password}')
        return None


def strength_eval_parallel(passwords, strength_threshold=0.5, num_processes=None, bulk=1000):
    """
    Evaluate the strength of passwords in parallel.

    Args:
        passwords (list): List of passwords to evaluate.
        strength_threshold (float, optional): Strength threshold to label passwords. Default is 0.5.
        num_processes (int, optional): Number of processes to use for parallel evaluation. Default is None (uses all available processes).
        bulk (int, optional): Number of passwords to evaluate before showing progress. Default is 1000.

    Returns:
        pd.DataFrame: DataFrame with evaluated passwords and their strengths.
    """
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()

    logging.info(f'Using {num_processes} processes for parallel evaluation.')

    pool = multiprocessing.Pool(processes=num_processes)
    results = []
    for i, password in enumerate(passwords):
        result = pool.apply_async(evaluate_password, (password, strength_threshold))
        results.append(result)

        if (i + 1) % bulk == 0:
            logging.info(f'Evaluated {i + 1} passwords.')

    pool.close()
    pool.join()

    return pd.DataFrame([result.get() for result in results if result is not None])


def main():
    try:
        # Initial definitions
        root = "data/"
        dataset = "rockyou.txt"
        result = "rockyou_evaluated.csv"
        strength_threshold = 0.5
        password_encoding = 'ISO-8859-1'
        bulk = 1000

        # Generate the full path to the password file
        path = os.path.join(root, dataset)

        # Get the data
        logging.info(f'Reading data from {path}.')
        rockyou = read_data(path, password_encoding)
        logging.info(f'{len(rockyou)} passwords read.')

        # Evaluate the strength of the passwords in parallel
        logging.info('Evaluating password strength in parallel...')
        rockyou_df = strength_eval_parallel(rockyou, strength_threshold, bulk=bulk)
        logging.info('Parallel processing finished!!!')

        if not rockyou_df.empty:
            # Save the results
            path = os.path.join(root, result)
            logging.info(f'Saving results to {path}...')
            save_data(rockyou_df, path, password_encoding)
            logging.info(f'PROCESSING FINISHED!!!!')
        else:
            logging.error('No data to save.')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')


if __name__ == "__main__":
    main()

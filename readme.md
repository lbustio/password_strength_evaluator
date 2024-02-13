# Password Strength Evaluator

![GitHub repo size](https://img.shields.io/github/repo-size/your_username/repo_name)
![GitHub contributors](https://img.shields.io/github/contributors/your_username/repo_name)
![GitHub stars](https://img.shields.io/github/stars/your_username/repo_name?style=social)
![GitHub forks](https://img.shields.io/github/forks/your_username/repo_name?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/your_twitter?style=social)

Evaluate the strength of passwords in a given dataset efficiently using multiprocessing and entropy calculation.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

Password Strength Evaluator is a Python script designed to evaluate the strength of passwords stored in a dataset file. It utilizes multiprocessing for parallel processing to efficiently handle large datasets. The script calculates the entropy of each password and uses the PasswordMeter library to determine its strength based on a defined threshold.

Key features:
- Efficient evaluation of password strength using multiprocessing.
- Calculation of password entropy for accurate assessment.
- Flexible configuration options such as strength threshold and bulk processing size.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3
```sh
sudo apt-get install python3
```

### Installation

1. Clone the repo

```sh
git clone https://github.com/lbustio/password_strength_evaluator.git
```

2. Install Python packages

```sh
pip install -r requirements.txt
```

## Usage

To use the Password Strength Evaluator, follow these steps:

1. Prepare your dataset file containing passwords.
2. Update the script's configuration (e.g., file paths, strength threshold).
3. Run the script.

```sh
python password_strength_evaluator.py
```

4. Check the output CSV file for evaluated password strengths.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.

## Contact
Lázaro Bustio-Martínez - lbustio@gmail.com

Project Link: https://github.com/lbustio/password_strength_evaluator

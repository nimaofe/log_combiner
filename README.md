# log_combiner
profile MySQL &amp; show logs from IIS on the same Windows server

| Persian


# ترکیب لاگ‌های MySQL و IIS

این پروژه یه ابزار ساده بهت می‌ده که لاگ‌های MySQL و IIS رو تو یه فایل ترکیب کنی و راحت‌تر بررسی‌شون کنی.

## پیش‌نیازها

- پایتون 3.7 یا بالاتر
- MySQL با فعال بودن لاگ کلی
- IIS با فعال بودن لاگ

## نصب

1. اول، این پروژه رو از گیتهاب کلون کن:

    ```bash
    git clone https://github.com/your-repo/log_combiner.git
    cd log_combiner
    ```

2. کتابخونه‌های مورد نیاز:

    ```bash
    pip install -r requirements.txt
    ```

3.نصب:

    ```bash
    python setup.py install
    ```

## استفاده

بعد از نصب، می‌تونی از ماژول `log_combiner` برای ترکیب لاگ‌های MySQL و IIS استفاده کنی.

### مثال

```python
from log_combiner import combine_logs

combine_logs(
    mysql_log_path='C:/path/to/your/mysql-general.log',
    iis_log_path='C:/path/to/your/iis-log-file.log',
    output_path='C:/path/to/your/combined-log.log'
)
تنظیمات
می‌تونی combiner.py رو تغییر بدی تا با قالب لاگ‌های MySQL و IIS خودت هماهنگ بشه.

مجوز
این پروژه تحت مجوز MIT هست.


#### setup.py

```python
from setuptools import setup, find_packages

setup(
    name='log_combiner',
    version='0.1',
    packages=find_packages(),
    description='یه ابزار برای ترکیب و مشاهده لاگ‌های MySQL و IIS روی سرور ویندوز',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
 requests
flask
numpy
pandas
    ],
)
log_combiner/init.py

from .combiner import combine_logs
log_combiner/combiner.py

import re
from datetime import datetime

def parse_mysql_log(line):
    # الگو رو برای قالب لاگ‌های MySQL خودت تنظیم کن
    match = re.match(r'(\d{6} \d{2}:\d{2}:\d{2})\s+([^\s]+)\s+(.*)', line)
    if match:
        timestamp = datetime.strptime(match.group(1), '%y%m%d %H:%M:%S')
        query = match.group(3)
        return timestamp, query
    return None

def parse_iis_log(line):
    # الگو رو برای قالب لاگ‌های IIS خودت تنظیم کن
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(.*)', line)
    if match:
        timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
        entry = match.group(2)
        return timestamp, entry
    return None

def combine_logs(mysql_log_path, iis_log_path, output_path):
    with open(mysql_log_path, 'r') as mysql_file, open(iis_log_path, 'r') as iis_file, open(output_path, 'w') as output_file:
        mysql_lines = mysql_file.readlines()
        iis_lines = iis_file.readlines()
        
        logs = []
        for line in mysql_lines:
            parsed = parse_mysql_log(line)
            if parsed:
                logs.append(('MySQL', *parsed))
        
        for line in iis_lines:
            parsed = parse_iis_log(line)
            if parsed:
                logs.append(('IIS', *parsed))
        
        logs.sort(key=lambda x: x[1])  # مرتب‌سازی لاگ‌ها بر اساس زمان
        
        for log in logs:
            output_file.write(f'[{log[0]}] {log[1]}: {log[2]}\n')

# کتابخونه‌های مورد نیاز
requests
flask
numpy
pandas

//////////////////////////////////////////////
/////////////////////////////////////////////
////////////////////////////////////////////

# راهنمای نصب پیش‌نیازهای پایتون روی ویندوز

این فایل راهنما به شما کمک می‌کند تا پیش‌نیازهای پایتون خود را با استفاده از `pip` روی سیستم ویندوز نصب کنید.

## مراحل نصب

### 1. دانلود و نصب پایتون

ابتدا باید پایتون را روی سیستم خود نصب کنید:

- به [صفحه دانلود پایتون برای ویندوز](https://www.python.org/downloads/windows/) بروید.
- نسخه مناسب (معمولاً آخرین نسخه پایدار) را دانلود و نصب کنید.
- در طول نصب، حتماً گزینه "Add Python to PATH" را انتخاب کنید.

### 2. باز کردن خط فرمان

منوی شروع ویندوز را باز کنید.

"cmd" یا "Command Prompt" را جستجو و انتخاب کنید.

### 3. نصب پیش‌نیازها با Pip

به دایرکتوری پروژه خود بروید که فایل `requirements.txt` در آن قرار دارد. به عنوان مثال:

```bash
cd path\to\your\project
دستور زیر را برای نصب پیش‌نیازها اجرا کنید:


pip install -r requirements.txt
نمونه فایل requirements.txt
در اینجا نمونه‌ای از فایل requirements.txt آمده است:


requests
flask
numpy
pandas
نصب Pip (در صورت عدم نصب)
اگر pip نصب نیست، می‌توانید آن را به صورت زیر نصب کنید:

دانلود get-pip.py:

به این لینک بروید و فایل get-pip.py را دانلود کنید.
https://bootstrap.pypa.io/get-pip.py

اجرای get-pip.py:

به دایرکتوری که get-pip.py را دانلود کرده‌اید بروید و دستور زیر را اجرا کنید:


python get-pip.py
با این مراحل، شما باید قادر به نصب تمامی پیش‌نیازهای پروژه پایتون خود روی ویندوز باشید.

#منابع مفید
دانلود پایتون
https://www.python.org/downloads/windows/
مستندات Pip
https://pip.pypa.io/en/stable/installation/

/////////////////////////////////////////////////////
/////////////////////////////////////////////////////
////////////////////////////////////////////////////
| English

# MySQL and IIS Log Combiner

This project gives you a simple tool to combine MySQL and IIS logs into a single file for easier review.

## Prerequisites

- Python 3.7 or higher
- MySQL with general logging enabled
- IIS with logging enabled

## Installation

1. First, clone this project from GitHub:

    ```bash
    git clone https://github.com/your-repo/log_combiner.git
    cd log_combiner
    ```

2. Next, install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Now, install the package:

    ```bash
    python setup.py install
    ```

## Usage

After installing, you can use the `log_combiner` module to combine MySQL and IIS logs.

### Example

```python
from log_combiner import combine_logs

combine_logs(
    mysql_log_path='C:/path/to/your/mysql-general.log',
    iis_log_path='C:/path/to/your/iis-log-file.log',
    output_path='C:/path/to/your/combined-log.log'
)

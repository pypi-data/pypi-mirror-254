# Faerunian Date Calculator

A Python module for calculating Faerunian date information based on the Gregorian calendar.

![PyPI - Version](https://img.shields.io/pypi/v/faeruniancalendar)
![Development Status](https://img.shields.io/badge/Development%20Status-4%20Beta-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview

This Python module provides a functionality to calculate various Faerunian date-related information based on a given
date or the current date in the Gregorian calendar. It includes information such as the Faerunian date, name,
description, and additional year differences.

## Installation

Use `pip` to install `faeruniancalendar`.

    pip install faeruniancalendar

## Usage

Once installed import the module and use `get_raw_farray`. This is currently the only active function. It will return a
data dictionary. See the examples below.

Usage

    import faeruniancalendar
    
    print(faeruniancalendar.get_raw_farray('1988-01-24'))

Output

    {'g_date': 24, 'f_special': None, 'f_month_name': 'Hammer', 'f_month_desc': 'Deepwinter', 'f_tenday': 3,'f_day_of_week': 4, 'f_day': 24, 'f_short_format': '24 Hammer', 'f_long_format': 'the 24th of Hammer', 'f_poetic_long': 'the 24th of Deepwinter', 'events': [], 'dr_year': 1730, 'cr_year': 1705, 'nr_year': 698, 'wy_year': 2818}

## License

This software is distributed under the MIT License. You are free to use, modify, and distribute it according to the
terms and conditions of the license.

## Development Status

This software is currently in development and is not yet ready for production use. Please be aware of potential changes
and updates as development progresses.




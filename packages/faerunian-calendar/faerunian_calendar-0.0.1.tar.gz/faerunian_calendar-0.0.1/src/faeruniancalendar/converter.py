import datetime
import data.common_year as cy
import data.leap_year as ly


def get_raw_farray(date=None):
    """
    Get raw date data for a given date or the current date.

    Args:
        date (str, optional): A string representing a date in the format 'YYYY-MM-DD'. Default is None.

    Returns:
        dict: A dictionary containing various Faerunian date-related information.

    Raises:
        ValueError: If the provided date has an invalid format.

    Note:
        - If 'date' is None, the function uses the current date.
        - The 'date' parameter should be in the format 'YYYY-MM-DD'.
    """

    if date is not None:
        try:
            # Parse the provided date in the format YYYY-MM-DD
            parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            # Invalid date format, return an error message
            return "Invalid Date or Invalid Date Format"
    else:
        # No date provided, use the current date
        parsed_date = datetime.date.today()

    # Get the Gregorian year from the parsed date
    gregorian_year = parsed_date.year

    # Check if it's a leap year
    is_leap_year = gregorian_year % 4 == 0 and (gregorian_year % 100 != 0 or gregorian_year % 400 == 0)

    # Choose the appropriate dictionary based on whether it's a leap year or not
    date_dict = ly.leap_year if is_leap_year else cy.common_year

    # Get the day of the year (1-365 or 1-366 for leap year)
    day_of_year = parsed_date.timetuple().tm_yday

    # Find the corresponding data in the date_dict
    date_data = next((data for data in date_dict if data["g_date"] == day_of_year), None)

    # Calculate the difference in years and add them to the date_data
    additional_years = {
        "dr_year": gregorian_year - 258,
        "cr_year": gregorian_year - 283,
        "nr_year": gregorian_year - 1290,
        "wy_year": gregorian_year + 830,
    }

    date_data.update(additional_years)

    return date_data

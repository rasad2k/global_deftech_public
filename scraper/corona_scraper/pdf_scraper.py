import requests as r
import sys
from tika import parser


# To get raw pdf data
def get_data(date):

    # Sets the url according to the given date
    url = 'https://koronavirusinfo.az/files/3/tab_' + date + '.pdf'

    response = r.get(url)

    if response.status_code == 404:

        print("Not published yet")
        sys.exit(1)

    data = response.content
    return data


# To handle and return dictionary from raw data
def handle_data(data, date):

    with open("my_pdf.pdf", 'wb') as my_data:
        my_data.write(data)

    raw = parser.from_file("my_pdf.pdf")
    text = raw['content']
    text = text.replace('\n', ' ')
    new_text = ""
    i = 0

    for c in text:

        if c != " ":
            new_text = text[i:]
            break

        i += 1

    new_text = " ".join(new_text.split())

    # The number of new cases today
    new_cases_str = "Yeni yoluxanların sayı"
    i = new_text.rfind(new_cases_str)
    new_cases_count = ""

    for n in range(i+1+len(new_cases_str), len(new_text)):

        if new_text[n] == " ":

            new_cases_count = int(new_cases_count)
            break

        new_cases_count += str(new_text[n])

    # The number of new death today
    new_dead_str = "Bugünkü ölüm sayı"
    i = new_text.rfind(new_dead_str)
    new_dead_count = ""

    for n in range(i+1+len(new_dead_str), len(new_text)):

        if new_text[n] == " ":

            new_dead_count = int(new_dead_count)
            break

        new_dead_count += str(new_text[n])

    # The number of people that got getter today
    new_better_str = "Yeni sağalanların sayı"
    i = new_text.rfind(new_better_str)
    new_better_count = ""

    for n in range(i+1+len(new_better_str), len(new_text)):

        if new_text[n] == " ":

            new_better_count = int(new_better_count)
            break

        new_better_count += str(new_text[n])

    # The number of new tests today
    new_tests_str = "Bugünkü test sayı"
    i = new_text.rfind(new_tests_str)
    new_tests_count = ""

    for n in range(i+1+len(new_tests_str), len(new_text)):

        if new_text[n] == " ":

            new_tests_count = int(new_tests_count)
            break

        new_tests_count += str(new_text[n])

    # The number of total cases
    total_cases_str = "Ümumi yoluxanların sayı"
    i = new_text.rfind(total_cases_str)
    total_cases_count = ""

    for n in range(i+1+len(total_cases_str), len(new_text)):

        if new_text[n] == " ":

            total_cases_count = int(total_cases_count)
            break

        total_cases_count += str(new_text[n])

    # The total number of the people that got better
    total_better_str = "Ümumi sağalanların sayı"
    total_better_index = new_text.rfind(
        new_dead_str) + len(str(new_dead_count)) + len(new_dead_str) + 2
    total_better_count = ""

    for n in range(total_better_index, len(new_text)):

        if new_text[n] == " ":

            total_better_count = int(total_better_count)
            break

        total_better_count += str(new_text[n])

    # The number of currently infected people
    current_infected_str = "Aktiv xəstə sayı"
    current_infected_index = total_better_index + \
        len(str(total_better_count)) + 1
    current_infected_count = ""

    for n in range(current_infected_index, len(new_text)):

        if new_text[n] == " ":

            current_infected_count = int(current_infected_count)
            break

        current_infected_count += str(new_text[n])

    # The number of total tests
    total_test_str = "Ümumi test sayı"
    total_test_index = current_infected_index + \
        len(str(current_infected_count)) + 1
    total_test_count = ""

    for n in range(total_test_index, len(new_text)):

        if new_text[n] == " ":

            total_test_count = int(total_test_count)
            break

        total_test_count += str(new_text[n])

    # The number of total death
    total_dead_str = "Ümumi ölüm sayı"
    total_dead_index = total_test_index + len(str(total_test_count)) + 1
    total_dead_count = ""

    for n in range(total_dead_index, len(new_text)):

        if new_text[n] == " ":

            total_dead_count = int(total_dead_count)
            break

        total_dead_count += str(new_text[n])

    stats = {
        "date": date,
        new_cases_str: new_cases_count,
        new_dead_str: new_dead_count,
        new_better_str: new_better_count,
        new_tests_str: new_tests_count,
        total_cases_str: total_cases_count,
        total_better_str: total_better_count,
        current_infected_str: current_infected_count,
        total_test_str: total_test_count,
        total_dead_str: total_dead_count
    }
    return stats


if __name__ == "__main__":
    date = "06.12.2020"
    data = get_data(date)
    stats = handle_data(data, date)
    for key, value in stats.items():
        print(f"{key}: {value}\n")

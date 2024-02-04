from bs4 import BeautifulSoup
import requests
import cab
from cab import *
import time
import string
import csv

try:

    # Call the function to open the website and sign in
    open_and_sign_in(driver, "https://cab.brown.edu/")

    # Wait for the primary cart to open
    time.sleep(5)

    # Get the html from the updated website
    page = driver.page_source

    # Create our Soup
    soup = BeautifulSoup(page, "html.parser")

    # Get the transcript link
    transcript_link = soup.find("a", {"class": "btn transcript-button"}).get('href')

    # Create lists to fill with the course iterations
    stripped_course_times = []
    stripped_course_names = []
    stripped_course_codes = []
    stripped_course_sections = []

    # Track iterations (which class are we on?)
    num = 0

    # Classes will equal True until we run out of class information to populate lists with
    classes = True

    while classes is True:
        import time
        num += 1

        try:
            # Use Selenium to select next course
            course_element = driver.find_element(By.XPATH, f"{"/html/body/main/div[2]/div/div[3]/div["}{num}{"]"}")
            course_element.click()

            # Wait for the next course to be selected
            time.sleep(3)

            # Get the html from the updated website
            page2 = driver.page_source

            # Update our beautiful soup2
            soup2 = BeautifulSoup(page2, "html.parser")

            # Scrape the course time and location from our new beautiful soup
            course_times = soup2.find_all("div", {"class": "meet"})

            # Scrape the course code from our new beautiful soup
            course_code = soup2.find("div", {"class": "dtl-course-code"})

            # Scrape the course name from our new beautiful soup
            course_name = soup2.find("div", {"class": "text col-8 detail-title text--huge"})

            # Scrape the course section from our new beautiful soup
            course_section = soup2.find("div", {"class": "dtl-section"})

            course_location_stripped = ""
            course_time_stripped = ""
            for time in course_times:
                # Remove the tags and collapse the course times
                course_time_stripped += time.get_text()
                course_time_stripped += " "

            stripped_course_times.append(course_time_stripped)
            stripped_course_names.append(course_name.get_text())
            stripped_course_codes.append(course_code.get_text())
            stripped_course_sections.append(course_section.get_text().split(" ")[1].split(" ")[0])

        except:
            classes = False

    # Converting lists to CSV Files
    # Field names
    fields = ["Code", "Name", "Time/Location", "Section"]

    # List of lists to be populated
    rows = []

    # Populating the rows
    for x in range(0, len(stripped_course_codes)):
        rows.append([stripped_course_codes[x], stripped_course_names[x], stripped_course_times[x],
                     stripped_course_sections[x]])

    # Convert lists to a CSV File
    # IDK what this line does
    with open('GFG', 'w') as file:

        # Create a CSV writer object
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(rows)

    # Create transcript beautiful soup
    page = requests.get(transcript_link)
    transcript_soup = BeautifulSoup(page.text, 'html.parser')



finally:
    # Close the browser
    driver.quit()

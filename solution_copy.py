import urllib.request
from bs4 import BeautifulSoup

# Function to extract numbers from <span> tags and compute their sum
def extract_and_compute_sum(url):
    # Open the URL and create a BeautifulSoup object
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <span> tags and extract the numbers
    numbers = []
 
    tags = soup.find_all('span', class_='comments')
    for tag in tags:
        # Extract the text content of the <span> tag
        number = int(tag.string)
        numbers.append(number)

    # Compute the sum of the numbers
    total = sum(numbers)

    # Return the sum
    return total, numbers


def check_if_even(number):
    """
    Check for even number ✅
    Arguments: 
    - Number : int

    Return:
    - Boolean: True / False
    """
    if number%3 == 0:
        print ("multiple of 3")
    else:
        print ("not multiple of 3")
   


if __name__ == '__main__':
    number = input('Enter Number: ')
    number = int(number)
    check_if_even(number)

    # Ask the user to enter the URL
    # url = input('Enter URL: ')
    # name = input('Enter Name: ')
    # Extract and compute the sum of numbers

    # sum_of_numbers, numbers = extract_and_compute_sum(url)

    # Print the count and sum
    # print("Count", len(numbers))
    # print("Sum", sum_of_numbers)
import requests
import bs4



def main():
    print_header()
    bandname = get_band_name()
    website = get_band_url(bandname)
    webdata = scrape_band_page(website)
    metal_soup = make_metal_soup(webdata)
    bandpage = download_band_info(metal_soup)
    assemble_band_information(bandpage)
    # export_band_profile()

url = 'http://www.metal-archives.com/bands/'


def print_header():
    print('-------------------------------------')
    print('       Metal Archives App ')
    print('-------------------------------------')
    print()


def get_band_name():
    print('What is the name of the band for which you\'d like information?')
    bandname = input('Please type the name of the band:   ')
    return bandname

def get_band_url(bandname):
    website = url + bandname
    websitetest = requests.get(website)
    webdatatest = websitetest.text
    if webdatatest.find('band_content') == -1:
        print('There are more than one bands with that name.')
        print('Here is a list of band.')
        print('Please choose a band from the list below:')
        bandcount = 0
        linklist = []
        bandlist = []
        metal_soup = make_metal_soup(webdatatest)
        bands = metal_soup.find_all('li')
        bands = bands[20:]
        for band in bands:
            linklist.append(band.find('a').attrs['href'])
        for band in bands:
            bandcount = bandcount + 1
            print('{}'.format(bandcount) + band.get_text())
            bandlist.append(band.get_text())
        bandchoice = int(input('Please enter the number here:   '))
        website = linklist[bandchoice - 1]
        return website
    else:
        return website

def scrape_band_page(website):
    webpage = requests.get(website)
    webdata = webpage.text
    return webdata

def make_metal_soup(webdata):
    metal_soup = bs4.BeautifulSoup(webdata, 'html.parser')
    return metal_soup


def download_band_info(metal_soup):
    bandpage = metal_soup.find(id='band_content').get_text() # This removes a lot of the html stuff
    return bandpage


def assemble_band_information(bandpage):
    print(bandpage)
    print('What kind of band information would you like to display?')
    while True:
        print('Would you like to see more about the band\'s [D]iscography, [M]embers, [B]iography, [T]rivia, [A]dditional'
              'notes, or [E]xit?')
        inforequest = input('Enter your choice here:   ').lower().strip()
        if inforequest == 'd':
            # Put disco here
            break
        elif inforequest == 'm':
            # Put members here
            break
        elif inforequest == 'b':
            # Put bio info here
            break
        elif inforequest == 't':
            # Put trivia here
            break
        elif inforequest == 'a':
            # Put additional info here
            break
        elif inforequest == 'e':
            break
        else:
            print('You have entered something incorrectly, please try again.')



if __name__ == '__main__':
    main()
import ipaddress
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


class FeatureExtractor:

    def __init__(self, url):
        self.url = url
        self.soup = None
        self.html = ""

        try:
            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            self.html = response.text
            self.soup = BeautifulSoup(self.html, "lxml")

        except:
            self.html = ""
            self.soup = None

    ####################################################
    # URL FEATURES
    ####################################################

    def url_length(self):
        return len(self.url)

    def is_https(self):
        return 1 if self.url.startswith("https") else 0

    def domain_length(self):
        return len(urlparse(self.url).netloc)

    def tld_length(self):
        try:
            domain = urlparse(self.url).netloc
            parts = domain.split(".")

            if len(parts) >= 2:
                return len(parts[-1])

            return 0

        except:
            return 0

    def number_of_subdomains(self):
        try:
            domain = urlparse(self.url).netloc
            parts = domain.split(".")

            if len(parts) <= 2:
                return 0

            return len(parts) - 2

        except:
            return 0

    def has_ip_address(self):
        try:
            ipaddress.ip_address(urlparse(self.url).hostname)
            return 1

        except:
            return 0

    def count_digits(self):
        return sum(c.isdigit() for c in self.url)

    def count_letters(self):
        return sum(c.isalpha() for c in self.url)

    def count_dots(self):
        return self.url.count(".")

    def count_hyphen(self):
        return self.url.count("-")

    def count_at(self):
        return self.url.count("@")

    def count_question(self):
        return self.url.count("?")

    def count_equal(self):
        return self.url.count("=")

    ####################################################
    # HTML FEATURES
    ####################################################

    def has_title(self):
        if self.soup is None:
            return 0

        return 1 if self.soup.title else 0

    def line_of_code(self):
        return len(self.html.splitlines())

    def number_of_images(self):
        if self.soup is None:
            return 0

        return len(self.soup.find_all("img"))

    def number_of_css(self):
        if self.soup is None:
            return 0

        return len(self.soup.find_all("link"))

    def number_of_js(self):
        if self.soup is None:
            return 0

        return len(self.soup.find_all("script"))

    def has_password(self):
        if self.soup is None:
            return 0

        return 1 if self.soup.find(
            "input",
            {"type": "password"}
        ) else 0

    def has_submit(self):
        if self.soup is None:
            return 0

        return 1 if self.soup.find(
            "input",
            {"type": "submit"}
        ) else 0

    ####################################################
    # FINAL FEATURE DICTIONARY
    ####################################################

    def extract(self):
        return {

            "URLLength": self.url_length(),

            "DomainLength": self.domain_length(),

            "IsDomainIP": self.has_ip_address(),

            "TLDLength": self.tld_length(),

            "NoOfSubDomain": self.number_of_subdomains(),

            "NoOfLettersInURL": self.count_letters(),

            "NoOfDegitsInURL": self.count_digits(),

            "NoOfEqualsInURL": self.count_equal(),

            "NoOfQMarkInURL": self.count_question(),

            "IsHTTPS": self.is_https(),

            "LineOfCode": self.line_of_code(),

            "HasTitle": self.has_title(),

            "NoOfImage": self.number_of_images(),

            "NoOfCSS": self.number_of_css(),

            "NoOfJS": self.number_of_js(),

            "HasPasswordField": self.has_password(),

            "HasSubmitButton": self.has_submit()

        }
#!/usr/bin/env python3
import urllib.request
import os
import os.path
import re
import datetime
import json
from dataclasses import dataclass


@dataclass
class BBDL:
    today = datetime.datetime.now()

    def start_load(self, tahun=None, bulan=None, hari=None) -> bool:
        """Start BBDL script.
        Will ask a user to enter a date. If not supplied,
        it will assume to use today's date. And then
        trigger tukar() function.
        """
        print("WELCOME TO BBDL!")
        print(f"Today's date is {self.today.strftime('%d/%m/%Y')}")
        if tahun is None or bulan is None or hari is None:
            hari, bulan, tahun = self.get_date(hari, bulan, tahun)
        to_download = ""
        while to_download not in ["y", "n"]:
            to_download = input("Do you want to download the newspaper? (y/n) ")
            if to_download.lower() == "y":
                return True
            elif to_download.lower() == "n":
                return False
        return False

    def get_date(self, hari=None, bulan=None, tahun=None):
        """
        Gets the date from the user or exit the program.
        """
        # Regex for Date Input or Exit
        date_pattern = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"
        date_input = f"{hari}/{bulan}/{tahun}"
        date_match = re.match(date_pattern, date_input)
        exit_match = re.match(r"exit", date_input, flags=re.IGNORECASE)
        while hari is None or bulan is None or tahun is None:
            if date_match:
                print(f"Looking up {date_input}")
                hari, bulan, tahun = map(int, date_input.split("/"))
                if self.check_input_date(tahun, bulan, hari) == False:
                    hari, bulan, tahun = None, None, None
            elif exit_match:
                exit()
            elif date_match is None:
                print("Enter a date in DD/MM/YYYY format for a different date")
                print("Press ENTER to continue to use today's date")
                print("Type EXIT to close the program")

                date_input = input(
                    "Which newspaper date do you want to read? (DD/MM/YYYY) : "
                )
                if date_input:
                    date_match = re.match(date_pattern, date_input)
                hari, bulan, tahun = map(int, date_input.split("/"))
                if self.check_input_date(tahun, bulan, hari) == False:
                    hari, bulan, tahun = None, None, None
            else:
                print(
                    f'{date_input} is an invalid date. Try again or type "exit" to exit the program'
                )

        tahun, bulan, hari = BBDL.tukar(tahun, bulan, hari)
        self.input_date = hari, bulan, tahun
        return hari, bulan, tahun

    def check_input_date(self, tahun, bulan, hari):
        """
        To check if the input date is valid.
        """
        try:
            datetime.datetime(int(tahun), int(bulan), int(hari))
            return True
        except Exception:
            return False

    @staticmethod
    def tukar(tahun, bulan, hari):
        """
        Convert input dates into strings for the URL.
        Also includes the leading zero for the month and day.
        returns a tuple of the converted values of strings.
        @params: tahun, bulan, hari
        @return: tahun, bulan, hari
        """
        yr = str(tahun)
        mth = f"0{str(int(bulan))}" if (int(bulan) < 10) else str(bulan)
        days = f"0{str(int(hari))}" if (int(hari) < 10) else str(hari)
        return yr, mth, days

    @staticmethod
    def makeDir(p):
        """
        Create a directory and use it as a working
        directory for storing the newspaper images.
        Only used when downloading is True.
        @params: p (the path to the directory)
        """
        if not os.path.isdir(p):
            os.makedirs(p)
        os.chdir(p)

    @staticmethod
    def berita(yr, mth, days):
        """
        The beginning of the image newspaper URLs
        Example URL Format:
        https://epaper.digital.borneobulletin.com.bn/BB/2022/06/BB18062022/files/assets/mobile/pages/
        The image page (i.e. page0001_i2.jpg, etc) will be handled in a loop under bb_dl_full()
        """
        yr, mth, days = BBDL.tukar(yr, mth, days)
        return f"https://epaper.digital.borneobulletin.com.bn/BB/{yr}/{mth}/BB{days}{mth}{yr}/files/assets/mobile/pages/"

    def bb_dl_full(self, l, yr, mth, days, download=True):
        """
        The actual downloading function. Relies on
        berita() function to and gets the image names
        for the end of the URL. First 9 pages starts with
        page000. After the first 9 pages, the image name
        goes page00. All while storing directly into a
        directory by saveDest variable.

        Update:
        Added a new parameter to determine that it is used for downloading or returning a list of image URLs.
        """
        print(
            "Downloading the Borneo Bulletin... This will take a while. Grab a drink or something..."
        )
        self.news_url = self.berita(yr, mth, days)
        self.list_of_urls = [
            f"{self.news_url}page00{'0' if (x < 10) else ''}{x}_i2.jpg"
            for x in range(1, l)
        ]
        if download:
            saveDest = f"data/BB-{yr}{mth}{days}"
            self.makeDir(saveDest)
            for x in range(1, l):
                full_url = f"{self.news_url}page00{'0' if (x < 10) else ''}{x}_i2.jpg"
                file_path = f"{yr}{mth}{days}{x}.jpg"
                if os.path.isfile(file_path):
                    print(f"{file_path} exists! Skipping!")
                else:
                    urllib.request.urlretrieve(full_url, file_path)
                    print(f"Fetching page {x} of {l}")

            print("Finished downloading! Enjoy reading!")
            return True
        return json.loads('{"urls":' + json.dumps(self.list_of_urls) + "}")

    def max_page_check(self, yr, mth, days):
        """
        To check the maximum page number of the newspaper and returns it.
        """
        news_url = self.berita(yr, mth, days)
        m = 11
        p = 11
        print("Wait... Checking maximum pages...")
        try:
            for p in range(11, 99):
                full_url = f"{news_url}page00{p}_i2.jpg"
                print(f"Checking page {p} exists")
                if self.check_page(full_url):
                    m = p
                else:
                    m = p - 1
                    print(f"Max page is {m}")
                    break
        except Exception:
            print("Error! Could not check maximum page number.")
            m = p - 1
            print(f"Max page is {m}")
        self.max_pages = m
        return m

    def check_page(self, url):
        """
        To check if the page exists.
        """
        try:
            return urllib.request.urlopen(url).getcode() == 200
        except Exception:
            print(f"Something went wrong while checking the page: {url}")
            return False


if __name__ == "__main__":
    bb = BBDL()
    bb.get_date()
    print(bb.input_date)
    print(bb.input_date[2])
    print(bb.input_date[1])
    print(bb.input_date[0])
    bb.max_page_check(bb.input_date[2], bb.input_date[1], bb.input_date[0])
    bb.bb_dl_full(
        bb.max_pages,
        bb.input_date[2],
        bb.input_date[1],
        bb.input_date[0],
        download=False,
    )
    print(bb.list_of_urls)

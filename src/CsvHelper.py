import csv

class CsvHelper():
    def __init__(self, filepath="default.csv"):
        """
        :param filepath: the path of the file which to write to/read from as string
        """
        self._filepath = filepath

    @property
    def getFile(self):
        """
        :return: the path of the current set file as string
        """
        return self._filepath

    def setFile(self, filepath):
        """
        :param filepath: path of the file which to write to/read from as string
        :return: self
        """
        self._filepath = filepath
        return self

    def save(self, urlResult):
        """
        :param input: list (including list of lists)(default [])
        :return: boolean (depending on success)
        """
        with open(self._filepath, "a") as csvfile:
            writer = csv.writer(csvfile, dialect='excel')
            values = urlResult.csv_format()
            writer.writerow(values)

    def read(self):
        """
        :return: returns the entire csv as list of lists
        """
        result = []
        with open(self._filepath) as csvfile:
            data = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in data:
                result.append(row[0])
        return result

    def getWordsToCount(self):
        """
        :return: returns all the words which to crawl
        """
        result = []
        with open('wordlist.csv') as csvfile:
            data = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in data:
                result.append(row)
        return [item for sublist in result for item in sublist]
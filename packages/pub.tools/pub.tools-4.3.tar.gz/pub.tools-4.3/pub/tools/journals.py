import csv
import json
import os
import requests

base_path = os.path.dirname(os.path.realpath(__file__))


def fetch_journals():
    """
    Gets all journal info from NCBI. This will be cached

    :return: dict
    """
    url = 'https://www.ncbi.nlm.nih.gov/pmc/journals/?format=csv'
    response = requests.get(url)
    if response.status_code == 200:

        _atoj = {}
        _jtoa = {}
        dates = {}
        full = {}
        reader = csv.reader(response.text.split('\n'))
        header = False

        for row in reader:
            if not header:
                header = True
                continue
            if row:
                title, abbr, pissn, eissn, publisher, locator, latest, earliest, freeaccess, \
                    openaccess, participation, deposit, url = row
                latest = latest.split(';')[-1]
                earliest = earliest.split(';')[-1]
                _atoj[abbr.lower()] = title
                _jtoa[title.lower()] = abbr
                dates[abbr.lower()] = (earliest, latest)
                full[abbr.lower()] = row
        data = {'atoj': _atoj, 'jtoa': _jtoa, 'dates': dates, 'full': full}

        return data


try:
    _journals = fetch_journals()
except requests.exceptions.HTTPError:
    _journals = []
except requests.exceptions.ProxyError:
    _journals = []
except requests.exceptions.ConnectionError:
    _journals = []

def get_source(cache=False):
    """ get source dictionary of journals and abbreviations

    :param cache:
    :return: cached or uncached journals
    """
    if not cache:
        try:
            journals = fetch_journals()
        except requests.exceptions.HTTPError:
            pass
        except requests.exceptions.ProxyError:
            pass
        else:
            return journals
    return _journals


def get_abbreviations(cache=True):
    """ get the mapping for abbreviation -> journal title

    :param cache:
    :return: dict
    """
    return get_source(cache)['atoj']


def get_journals(cache=True):
    """ get the mapping for journal -> abbreviation

    :param cache:
    :return: dict
    """
    return get_source(cache)['jtoa']


def get_dates(cache=True):
    """ get date range per journal abbreviation

    :param cache:
    :return: dict
    """
    return get_source(cache)['dates']


def atoj(abbrv, cache=True):
    """ get journal title from abbreviation

    :param abbrv:
    :param cache:
    :return: str
    """
    data = get_abbreviations(cache)
    return data.get(abbrv.lower())


def jtoa(journal, cache=True):
    """ get abbreviation from journal title

    :param journal:
    :param cache:
    :return: str
    """
    data = get_journals(cache)
    return data.get(journal.lower())


def atodates(abbrv, cache=True):
    """ get date range from journal abbreviation

    :param abbrv:
    :param cache:
    :return:
    """
    data = get_dates(cache)
    return data.get(abbrv.lower())


if __name__ == '__main__':
    journals = fetch_journals()

    with open(os.path.join(base_path, 'journals.json'), 'w') as f:
        json.dump(journals, f)

# -*- coding: utf-8 -*-

import logging
import time
import functools

from songfinder import corrector
from songfinder import gestchant


class SearcherBase(object):
    def __init__(self, dataBase):
        self._numDict = None
        self._corrector = None

        self._dataBase = dataBase
        self._getCorrector()
        self._tolerance = 0.3
        self._debugPrintMod = 10
        self._searchCounter = 0
        self._searchTimeCumul = 0
        self._correctTimeCumul = 0

    @property
    def mode(self):
        return self._dataBase.mode

    @mode.setter
    def mode(self, in_mode):
        self._dataBase.mode = in_mode
        self._getCorrector()

    def _getCorrector(self):
        singles = ";".join((sets[0] for sets in self._dataBase.values()))
        couples = ""
        if self.mode != "tags":
            couples = ";".join((sets[1] for sets in self._dataBase.values()))
        self._corrector = corrector.Corrector(singles, couples)

    def search(self, toSearch):
        if not toSearch.isdigit():
            self._toSearch = gestchant.netoyage_paroles(toSearch)
        else:
            self._toSearch = toSearch
        start = time.time()
        self._toSearch = self._corrector.check(self._toSearch)
        self._correctTimeCumul += time.time() - start
        if self._searchCounter % self._debugPrintMod == 0:
            try:
                correctTimeMean = self._correctTimeCumul / self._searchCounter
                searchTimeMean = self._searchTimeCumul / self._searchCounter
            except ZeroDivisionError:
                correctTimeMean = 0
                searchTimeMean = 0

            # pylint: disable=no-value-for-parameter,no-member
            hits = self._search.cache_info().hits
            misses = self._search.cache_info().misses
            try:
                ratio = hits / (hits + misses)
            except ZeroDivisionError:
                ratio = float("inf")
            logging.debug(
                'Searcher "%s": %d searches,\n'
                "\tCorrect time (mean): %.3fs, "
                "Search time (mean): %.3fs,\n"
                "\tCache hit/miss ratio: %.2f, "
                'Searching "%s"'
                % (
                    type(self).__name__,
                    self._searchCounter,
                    correctTimeMean,
                    searchTimeMean,
                    ratio,
                    self._toSearch,
                )
            )
        self._searchCounter += 1
        return self._search(self._toSearch)

    @functools.lru_cache(maxsize=100)
    def _search(self, toSearch):  # Use of caching
        if toSearch.isdigit():
            try:
                num = int(toSearch)
                return list(self._dataBase.dict_nums[num])
            except KeyError:
                logging.warning(
                    f"{toSearch} does not correspond to any number in dataBase"
                )
        start = time.time()
        self._found = list(self._dataBase.keys())
        self._searchCore()
        if len(self._found) > 20:
            self._searchCore()
        self._searchTimeCumul += time.time() - start
        return self._found

    def _searchCore(self):
        self._toSearchList = self._toSearch.split(" ")
        self._tolerance = 0.3

        if len(self._found) != 1:
            self._keyWordSearch(1)
            if len(self._toSearchList) > 1 and len(self._found) > 5:
                self._keyWordSearch(2)
            if len(self._toSearchList) > 2 and len(self._found) > 5:
                self._keyWordSearch(3)
            if len(self._toSearchList) > 1 and len(self._found) > 5:
                self._tolerance = 0.2
                self._keyWordSearch(2)
            if len(self._toSearchList) > 1 and len(self._found) > 5:
                self._tolerance = 0.1
                self._keyWordSearch(2)
            if len(self._toSearchList) > 2 and len(self._found) > 5:
                self._keyWordSearch(3)

    def _keyWordSearch(self, nbWords):
        dico_taux = dict()
        toSearchSet = set()
        plusieurs_mots = []
        for i, mot in enumerate(self._toSearchList):
            plusieurs_mots.append(mot)
            if i > nbWords - 2:
                toSearchSet.add(" ".join(plusieurs_mots))
                plusieurs_mots = plusieurs_mots[1:]
        taux_max = 0
        for song in self._found:
            refWords = self._dataBase[song][nbWords - 1]
            refSet = set(refWords.split(";"))
            taux = len(toSearchSet & refSet) / len(toSearchSet)

            try:
                dico_taux[taux].append(song)
            except KeyError:
                dico_taux[taux] = [song]

            if taux > taux_max:
                taux_max = taux

        self._found = []
        taux_ordered = sorted(dico_taux.keys(), reverse=True)
        for taux in taux_ordered:
            if taux > taux_max - self._tolerance - nbWords / 10:
                self._found += sorted(dico_taux[taux])

    def resetCache(self):
        # pylint: disable=no-member
        self._search.cache_clear()
        self._corrector.resetCache()

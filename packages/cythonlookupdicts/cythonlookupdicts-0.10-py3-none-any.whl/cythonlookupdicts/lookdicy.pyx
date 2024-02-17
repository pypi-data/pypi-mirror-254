cimport cython
import numpy as np
cimport numpy as np
import cython
from typing import Union
np.import_array()

ctypedef fused linu:
    np.ndarray
    list

cdef inline Py_ssize_t addkeys(
    dict[cython.uchar, Union[list,dict[cython.uchar,dict]]] d,
    cython.uchar[:] word,
    Py_ssize_t indi,
    Py_ssize_t wordlen,
    Py_ssize_t idcounter):
    cdef:
        dict[cython.uchar,dict] newdict
        bint checken
        list[Py_ssize_t] appendlist
    if indi < wordlen:
        checken = word[indi] not in d
        if checken:
            newdict={}
            d[word[indi]] = newdict
        return addkeys(d[word[indi]], word, indi + 1, wordlen, idcounter)
    else:
        checken = word[wordlen] not in d
        if checken:
            appendlist = []
            d[word[wordlen]] = appendlist
        d[word[wordlen]].append(idcounter)
        idcounter+=1
    return idcounter


cpdef dict create_lookupdicts(cython.uchar[:,::1] input_data, Py_ssize_t itemsize):
    cdef:
        Py_ssize_t idcounter = 0
        Py_ssize_t wordcounter
        Py_ssize_t lendata = input_data.shape[0]
        dict[cython.uchar, Union[list,dict[cython.uchar,dict]]] di = {}
        Py_ssize_t itemsizeminus1 = itemsize-1
    for wordcounter in range(lendata):
        idcounter = addkeys(di, input_data[wordcounter], 0, itemsizeminus1, idcounter)
    return di

cpdef tuple[np.ndarray,Py_ssize_t] format_nparray(
    input_data1,
):
    cdef:
        np.ndarray input_data = np.asarray(list(map(repr, input_data1)), dtype="S")
        Py_ssize_t itemsize = input_data.itemsize
        np.ndarray[np.uint8_t, ndim=2] formatedarray=np.char.rjust(input_data, itemsize, b"\x81").view(np.uint8).reshape((-1, itemsize))
    return formatedarray,itemsize

cpdef cython.uchar[:,:] format_single_key(input_data1, Py_ssize_t itemsize):
    return (
        np.char.rjust(np.fromiter((map(repr, input_data1)), dtype=f"S{itemsize}"), itemsize, b"\x81")
        .view(np.uint8)
        .reshape((-1, itemsize))
    )

cdef void get_values(linu vals, list[list[Py_ssize_t]] indis,list[list] results):
    cdef:
        Py_ssize_t l1 = len(indis)
        Py_ssize_t l2, i1, i2
    for i1 in range(l1):
        l2 = len(indis[i1])
        for i2 in range(l2):
            results[len(results)-1].append(vals[indis[i1][i2]])
        if l1-i1 > 1:
            results.append([])


class LookUpDictMultiIndex(dict):
    def __init__(self, *args, **kwargs):
        cdef:
            Py_ssize_t itemsize
            list[dict] tmpresults = []
            bint ignore_exceptions = False
        if "ignore_exceptions" in kwargs:
            if kwargs["ignore_exceptions"]:
                ignore_exceptions=True
        input_data, itemsize = format_nparray(args[0])
        self["nested"] = create_lookupdicts(input_data, itemsize)
        self["key_list"] = args[0]
        self["value_list"] = args[1]
        self["itemsize"] = itemsize
        self["tmpresults"] = tmpresults
        self["ignore_exceptions"] = ignore_exceptions

    def __getitem__(self, key):
        cdef:
            bint tcheck = isinstance(key,(list,np.ndarray))
            list[list[Py_ssize_t]] results
        if tcheck:
            results=self._getitem__(key)
            return results
        return super().__getitem__(key)

    def _getitem__(self, key):
        cdef:
            list[list[Py_ssize_t]] results = []
            Py_ssize_t keyexindex, subkeyindex
            lookupcheck_data = format_single_key(key, self["itemsize"])
            Py_ssize_t lookupcheck_dataindex = len(key)
        for keyexindex in range(lookupcheck_dataindex):
            keyx = lookupcheck_data[keyexindex]
            self["tmpresults"].append(super().__getitem__("nested"))
            keyexindex=len(keyx)-1
            for subkeyindex in range(keyexindex):
                try:
                    self["tmpresults"].append(self["tmpresults"][len(self["tmpresults"] )-1][keyx[subkeyindex]])
                except KeyError as e:
                    if self["ignore_exceptions"]:
                        results.append([])
                        break
                    raise e
            else:
                try:
                    results.append(self["tmpresults"][len(self["tmpresults"])-1][keyx[keyexindex]])
                except KeyError as e:
                    if self["ignore_exceptions"]:
                        results.append([])
                        continue
                    raise e
                self["tmpresults"].clear()
        return results

class LookUpDictMultiValues(LookUpDictMultiIndex):
    def __getitem__(self, key):
        cdef:
            bint tcheck = isinstance(key,(list,np.ndarray))
            list[list[Py_ssize_t]] indis
            list[list] results
        if tcheck:
            results = [[]]
            indis=self._getitem__(key)
            get_values(self["value_list"], indis, results)
            return results
        return super().__getitem__(key)

class MultiIndexFinder(LookUpDictMultiIndex):
    def __init__(self, *args, **kwargs):
        cdef:
            Py_ssize_t itemsize
            list[dict] tmpresults = []
            bint ignore_exceptions = False
        if "ignore_exceptions" in kwargs:
            if kwargs["ignore_exceptions"]:
                ignore_exceptions=True
        input_data, itemsize = format_nparray(args[0])
        self["nested"] = create_lookupdicts(input_data, itemsize)
        self["key_list"] = args[0]
        self["value_list"] = np.arange(len(args[0]),dtype=np.int32)
        self["itemsize"] = itemsize
        self["tmpresults"] = tmpresults
        self["ignore_exceptions"] = ignore_exceptions

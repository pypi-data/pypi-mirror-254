"""calculates formats of data

    Returns:
        List|str: formatclaculator class

    Yields:
        List: list
    """
import itertools
import ast
import re
from typing import List, Any, Generator
import pandas as pd
from package.keyborddata import alphabets, alphabets_upper, numbers, simbols


class Ordring:
    """ordring seed values and ordring seq"""

    def __init__(self, values: List[str], ordring: List[str]) -> None:
        """ordring seed values,ordring seq

        Args:
            values (List[str]): values
            ordring (List[str]): ordring and pairs
        """
        self.values = values
        self.ordring = ordring


class Mitter:
    """returns Mitter object for validation hasattr df for dataframe transformation"""

    def __init__(self, _df,dataset,colorder: Generator) -> None:
        """_summary_

        Args:
            _df (_type_): _description_
            dataset (_type_): _description_
            colorder (Generator): _description_
        """
        self._df = _df
        self.colhashes = colorder
        self.dataset= dataset

    def formatwise_mitter(self):
        """Groups data formatwise

        Returns:
            DataFrame: Formatwise Data
        """
        datalist = []
        for _k, _v in self._df.iterrows():
            data = {}
            cols = self._df.columns.to_list()
            for _x in cols:
                values = _v[_x]
                if _x[1] not in data.keys():
                    data[_x[1]] = str((_x[-1], values))
                else:
                    if isinstance(ast.literal_eval(data[_x[1]]), tuple):
                        valu = ast.literal_eval(data[_x[1]])
                        data[_x[1]] = str([valu, (_x[-1], _v[_x])])
                    elif isinstance(ast.literal_eval(data[_x[1]]), list):
                        valu = ast.literal_eval(data[_x[1]])
                        valu.append((_x[-1], _v[_x]))
                        data[_x[1]] = str(valu)
            datalist.append(data)
        return pd.DataFrame.from_records(datalist)

    def column_wise_format_ordring(self):
        """_summary_

        Yields:
            tuple: indexes
        """
        colindexes = self.formatwise_mitter().columns.to_list()
        for _x in list(self.colhashes):
            yield _x[0], [colindexes.index(_z) for _z in _x[1]]

    def merge(self, dicts):
        """_summary_

        Args:
            dicts (_type_): _description_

        Returns:
            _type_: _description_
        """
        result = {}
        for d in dicts:
            for key, value in d.items():
                result.setdefault(key, []).append(value)
        return result
    
    def search_pat(self,pat, mitter):
        """_summary_

        Args:
            pat (_type_): _description_
            mitter (_type_): _description_

        Returns:
            _type_: _description_
        """
        indexc = ""
        for x in mitter.columns.to_list():
            sw = mitter.iloc[0, mitter.columns.get_loc(x)]
            if isinstance(ast.literal_eval(sw), tuple):
                if ast.literal_eval(sw)[0] == pat:
                    indexc += str(mitter.columns.get_loc(x))
                    indexc += "|"
                    indexc += "0"
            elif isinstance(ast.literal_eval(sw), list):
                if pat in [z[0] for z in ast.literal_eval(sw)]:
                    indexc += str(mitter.columns.get_loc(x))
                    indexc += "|"
                    indexc += str([z[0] for z in ast.literal_eval(sw)].index(pat))
        return indexc
    
    def row_patterns(self,df):
        """_summary_

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        a=self.formatwise_mitter()
        keyboardsq=alphabets + alphabets_upper + simbols + [str(x) for x in numbers]
        keyboardsq.append(' ')
        rowpatterns=[]
        for x in df.index.to_list():
            data=df.iloc[x].to_list()
            hashes=[]
            for z in data:
                s=None
                if len(str(z))==1:
                    s=str(keyboardsq.index(str(z)))
                else:
                    dummy=[]
                    for q in list(str(z)):
                        try:
                            dummy.append(str(keyboardsq.index(str(q))))
                        except Exception as E:
                            pass
                    s=str(dummy)
                hashes.append(s)
            rowpatterns.append(hashes)
        w = []
        for i, x in enumerate(rowpatterns):
            d = []
            for z in x:
                d.append(self.search_pat(z, a))
            w.append(",".join(d))
        return w


    def columnwise_data_pattern_ordring_seq(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        colfoseq = list(self.column_wise_format_ordring())
        _dw = self.formatwise_mitter()
        hashq = []
        for _x in colfoseq:
            for s in _x[1]:
                if isinstance(ast.literal_eval(_dw.iloc[0, s]), list):
                    for i, aq in enumerate(ast.literal_eval(_dw.iloc[0, s])):
                        hashq.append({_x[0]: str(s) + "|" + (str(i))})
        return self.merge(hashq)

    def get_row_ordring_seq_from_dataset(self,dataset):
        """generate row pattern indexes acording to table pattern 

        Args:
            dataset (Dataframe): pd.read_csv("path/to/tabularfile")

        Returns:
            Dataframe: row patterns
        """
        

        return self.row_patterns(dataset)
    
    def forecast_row_values(self,length:int,alorithum:object):
        """_summary_

        Args:
            length (int): _description_
            alorithum (object): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError("yet to be implemented")


    def normalize_seq_patterns(self, seqlist):
        """generate unique data and ordring from seq

        Args:
            seqlist (List): seq list of keyboard sequences

        Returns:
            List[str]: _description_
        """
        data = sorted(list(set(seqlist)))
        sliceseq = []
        for _x in data:
            if len(_x) > 1 and sliceseq == []:
                sliceseq.append(_x[0])
                sliceseq.append(_x[1])
            elif len(_x) > 1 and sliceseq != []:
                sliceseq[0] += _x[0]
                sliceseq[1] += _x[1]
            elif len(_x) == 1 and sliceseq != []:
                sliceseq[0] += _x[0]
        sliceseq[0] = "".join(sorted(list(set(sliceseq[0]))))
        sliceseq[1] = "".join(sorted(list(set(sliceseq[1]))))
        ordd = []
        for _s in data:
            if len(_s) > 1:
                _a = str(sliceseq[0].index(_s[0]))
                _b = str(sliceseq[1].index(_s[1]))
                ordd.append("&".join([_a, _b]))
            elif len(_s) == 1:
                _a = str(sliceseq[0].index(_s[0]))
                ordd.append(_a)
        ordd = ",".join(ordd)
        seqord = ""
        for _x in seqlist:
            seqord += "{}".format(data.index(_x))

        return Ordring(sliceseq, [ordd, seqord])

    def regenerate_seq_normalized(self, normlist):
        """regenerate all data from ordring and seq

        Args:
            normlist (List[str]): normalized lists

        Returns:
            List[str]: returns actual sequence of keyboard sequences
        """
        values = normlist[0:2]
        orders = normlist[2:]
        suborder = []
        for _x in orders[0].split(","):
            _x = list(_x)
            _x[0] = values[0][int(_x[0])]
            _x[-1] = values[1][int(_x[-1])]
            _x.remove(_x[1])
            suborder.append("".join(_x))
        regenlist = []
        for _z in list(orders[1]):
            regenlist.append(suborder[int(_z)])
        return regenlist


class FormatCalculator:

    """FormatCalculator class fetches formets from any type of data input
    data should be in df or records format and helps us to do \n
     analysis over it to fetch format and itration format and seeds from data
     then we must able to regenerate that data by having following receipies\n
        --- data formats\n
        --- itration format\n
        --- itration format seeds\n
        --- data format seeds\n
    Format Calculator class have following features\n
       -- regex_formattor (groups regex string and generate optimised
         regex generated by FormatCalculator inputargs:[cls,str])\n
       -- get_unique_hashes_from_data ( gets uniques hashes from data
         columns wise  inputargs:[cls,LIST[ANY]])\n
       -- split_all_labels_to_words_with_new_cols
       ( splits string and create new cols in dataframe
       inputargs:[cls,Dataframe,exer=[" "]])\n
       -- hash_df_single_df_column ( hashes single
       df col inputargs:[cls,pd.Series])\n
       -- hash_df_formats ( hashes all data in dataframe )
         inputargs:[cls,pd.Dataframe]\n
       -- get_unique_hashes_from_df_columnwise
       ( column wise hashes generater in records
       format inputargs:[cls,pd.DataFrame])\n

    """

    @classmethod
    def regex_formattor_experimental(cls, value):
        """(groups regex string and generate optimised
        regex generated by FormatCalculator inputargs:[cls,str])"""
        _s = "".join(ch for ch, _ in itertools.groupby(value))
        formats = [
            "[a-z]{1}",
            "[A-Z]{1}",
            "\\d{1}",
            "\\s",
            "-\\d{1}",
            "\\~",
            "\\@",
            "\\#",
            "\\$",
            "\\%",
            "\\^",
            "\\&",
            "\\*",
            "\\-",
            "\\_",
            "\\+",
            "\\=",
            "\\:",
            "\\;",
            "\\'",
            '\\"',
            "\\|",
            "\\,",
            "\\`",
            "\\?",
        ]
        hashs = []
        rowhash = ""
        for _x in _s:
            rowhash += _x
            if len(rowhash) == 8 and rowhash in formats:
                if hashs == []:
                    hashs.append(rowhash)
                else:
                    mat = hashs[-1][0:6] + "1" + hashs[-1][-1]
                    if mat == rowhash:
                        _ha = list(hashs[-1])
                        _ha[-2] = str(int(hashs[-1][-2]) + 1)
                        hashs[-1] = "".join(_ha)
                    else:
                        hashs.append(rowhash)
                rowhash = ""
            elif len(rowhash) == 2 and rowhash in formats:
                hashs.append(rowhash)
                rowhash = ""
            elif len(rowhash) == 5 and rowhash in formats:
                if hashs == []:
                    hashs.append(rowhash)
                else:
                    mat = hashs[-1][0:3] + "1" + hashs[-1][-1]
                    if mat == rowhash:
                        _ha = list(hashs[-1])
                        _ha[-2] = str(int(hashs[-1][-2]) + 1)
                        hashs[-1] = "".join(_ha)
                    else:
                        hashs.append(rowhash)
                rowhash = ""
            elif len(rowhash) == 1 and rowhash in formats:
                hashs.append(rowhash)
                rowhash = ""
        return "".join(hashs)

    @classmethod
    def get_unique_hashes_from_data(cls, chuncks: List[Any]):
        """( gets uniques hashes from data columns wise  inputargs:[cls,LIST[ANY]])"""

        _df = pd.DataFrame.from_records(chuncks).fillna("0")
        cols = _df.columns.to_list()
        df_list = []
        for _x in cols:
            _d = _df[_df[_x] != "0"]
            df_list.append(_d[_x])

        series_list = []
        for _s in df_list:
            lables = []
            for _e in _s:
                lables += _e["lables"]

            unique_lables = []
            for xsa in lables:
                if xsa not in unique_lables:
                    unique_lables.append(xsa)
            series_list.append(unique_lables)

        hash_list = []
        for _x in series_list:
            hash_lables = []
            for _q in _x:
                datalen = len(_q)
                hashd = r""
                for _xs in range(datalen):
                    if str(_q[_xs]) in alphabets:
                        hashd += "[a-z]{1}"
                    elif str(_q[_xs]) in alphabets_upper:
                        hashd += "[A-Z]{1}"
                    elif str(_q[_xs]) in simbols:
                        hashd += r"\{}".format(str(_q[_xs]))
                    else:
                        data = None
                        try:
                            data = int(_q[_xs])
                        except ValueError:
                            if _q[_xs] == " ":
                                hashd += r"\s"
                            else:
                                hashd += _q[_xs]
                        if data is not None:
                            hashd += r"\d{1}"
                hash_lables.append(hash)
            hash_list.append(hash_lables)

        unique_hashes = []
        for _i, _x in enumerate(hash_list):
            unique_hashes.append({cols[_i]: list(set(_x))})
        return unique_hashes

    @classmethod
    def split_all_labels_to_words_with_new_cols(cls, _df, exer: List[str] = None):
        """(splits string and create new cols in dataframe inputargs:[cls,Dataframe,exer=[" "]])"""

        if exer is None:
            exer = [
                " ",
            ]
        numdata = _df
        _df = _df.select_dtypes(include=["object"])
        cols_to_select = set(numdata.columns.to_list()) - set(_df.columns.to_list())
        result = _df.to_dict("records")
        cols = _df.columns.to_list()
        final_df = []
        for _v in result:
            for _x in cols:
                val = None
                for _s in exer:
                    if not isinstance(_v[_x], list):
                        if _s in _v[_x]:
                            val = _v[_x].split(_s)
                        else:
                            val = _v[_x]
                _v[_x] = val
            final_df.append(_v)
        df_list = []
        for _v in final_df:
            _cd = {}
            for _d, _n in _v.items():
                if isinstance(_n, list):
                    for i, _xs in enumerate(_n):
                        if i == 0:
                            _cd[_d] = _xs
                        else:
                            _cd["_".join([_d, str(i)])] = _xs
                else:
                    _cd[_d] = _n
            df_list.append(_cd)
        return pd.DataFrame.from_records(df_list).join(numdata[list(cols_to_select)])

    @classmethod
    def hash_df_single_df_column(cls, _series):
        """( hashes single df col inputargs:[cls,pd.Series])"""
        for k, _v in _series.items():
            hashd = ""
            for _x in str(_v):
                if str(_x) in alphabets:
                    hashd += "[a-z]{1}"
                elif str(_x) in alphabets_upper:
                    hashd += "[A-Z]{1}"
                elif str(_x) in simbols:
                    hashd += r"\{}".format(str(_x))
                else:
                    data = None
                    try:
                        data = int(_x)
                    except ValueError:
                        if _x in (" ",) or _x in (" ",):
                            hashd += r"\s"
                        else:
                            hashd += _x
                    if data is not None:
                        hashd += r"\d{1}"
            yield k, hashd

    @classmethod
    def hash_df_formats(cls, _df):
        """( hashes all data in dataframe ) inputargs:[cls,pd.Dataframe]"""

        df_list = []
        for _x, _s in _df.iterrows():
            value = None
            idx = [sa[0] for sa in list(cls.hash_df_single_df_column(_s))]
            vals = [sw[1] for sw in list(cls.hash_df_single_df_column(_s))]
            value = pd.Series(vals, index=idx)
            df_list.append(value.to_dict())
        return pd.DataFrame.from_records(df_list)

    @classmethod
    def get_unique_hashes_from_df_columnwise(cls, _df):
        """( column wise hashes generater in records format inputargs:[cls,pd.DataFrame] )"""
        for _x in _df.columns.to_list():
            yield (_x, _df[_x].unique().tolist())

    @classmethod
    def regex_filter(cls, val, regex):
        """match regex function

        Args:
            val (str): value for pattern match
            regex (str): keyboard pattern

        Returns:
            str|bool: pattern match state
        """

        val = str(val)
        if isinstance(val, str):
            _mo = re.fullmatch(regex, str(val))
            if _mo:
                return val
            else:
                return False
        else:
            return False

    @classmethod
    def dict_mapped_tup(cls, dictionary):
        """_summary_

        Args:
            dictionary (Dict): convert dict to tuple

        Yields:
            Any: List of tuples
        """
        for key, value in dictionary.items():
            if isinstance(value, dict):
                yield from (
                    (key,) + subkey_value for subkey_value in cls.dict_mapped_tup(value)
                )
            else:
                yield key, value

    @classmethod
    def generate_datamiter(cls, _df):
        """generates data miter from df

        Args:
            df (dataframe): dataframe of data

        Returns:
            dataframe: returns multiindex dataframe
        """
        format_hashed_df = FormatCalculator.hash_df_formats(_df)
        keyboards = (
            alphabets + alphabets_upper + simbols + [str(x) for x in numbers] + [" "]
        )
        # get column format wise data length
        finaldata = []
        for _x in format_hashed_df.columns.to_list():
            colms = format_hashed_df[_x].values.tolist()
            my_list_count1 = {i: colms.count(i) for i in colms}
            finaldata.append({_x: my_list_count1})
        # formatwisedata org
        formatdataset = []
        hashed = []
        for _x in finaldata:
            hashed_x = _x
            for _z in list(list(_x.values())[0].keys()):
                datas = _df[list(_x.keys())[0]].apply(cls.regex_filter, regex=_z)
                datas = datas[datas != False].values.tolist()
                hashd = []
                for _sa in datas:
                    if len(str(_sa)) == 1:
                        hashd.append(str(keyboards.index(str(_sa))))
                    else:
                        pairs = []
                        for _xs in list(str(_sa)):
                            pairs.append(str(keyboards.index(_xs)))
                        hashd.append(str(pairs))
                hashed_x[list(hashed_x.keys())[0]][_z] = {
                    i: hashd.count(i) for i in hashd
                }

            formatdataset.append(_x)
            hashed.append(hashed_x)
        # multindex columns
        tuplesd = [list(cls.dict_mapped_tup(x)) for x in hashed]
        tuplesd = [x for xs in tuplesd for x in xs]
        multindextuples = []
        valueslist = []
        for _x in tuplesd:
            multindextuples.append(_x[:-1])
            valueslist.append(_x[-1])
        multindex = pd.MultiIndex.from_tuples(multindextuples)
        output_df_before_optimizing_unique_lists = pd.DataFrame(
            [valueslist], columns=multindex
        )

        return Mitter(
            output_df_before_optimizing_unique_lists,
            _df,
            cls.get_unique_hashes_from_df_columnwise(format_hashed_df),
        )

    @classmethod
    def find_max_length(cls, lst):
        """finds max length in list of lists

        Args:
            lst (LIST): list for find maxlength

        Returns:
            Int: max length
        """
        max_length = max(len(x) for x in lst)

        return max_length

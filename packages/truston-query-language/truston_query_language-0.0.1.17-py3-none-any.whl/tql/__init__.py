import numpy as np
import pandas as pd
import os
import datetime
import pickle

devmode = False

class __TQL:
    __qdbpath = 'S:/all member/퀀트운용팀/93 QuickDB/'
    with open(__qdbpath+"authentification.tql", 'rb') as f:
        __valid_user = pickle.load(f)
        __username = os.environ.get('USERNAME')
        if __username.lower() not in __valid_user:
            raise Exception("[{__username}] Not Authentificated User.")
        else:
            print(f"[{__username}] Authentificated User.")

    @classmethod
    def load_pkl(cls, dest):
        try:
            with open(dest, 'rb') as f:
                return pickle.load(f)
        except:
            return None

    @classmethod
    def save_pkl(cls, data, dest):
        try:
            with open(dest, 'wb') as f:
                pickle.dump(data, f)
        except:
            return None

    @classmethod
    def add_user(cls, username):
        print(cls.__qdbpath+"authentification.tql")
        users = cls.load_pkl(cls.__qdbpath+"authentification.tql")
        users.add(username)
        cls.save_pkl(users, cls.__qdbpath+"authentification.tql")
        print(f"{username} added.")

    @classmethod
    def delete_user(cls, username):
        users = cls.load_pkl(cls.__qdbpath+"authentification.tql")
        try:
            users.remove(username)
            print(f"{username} deleted.")
        except:
            print(f'{username} does not exists.')
        cls.save_pkl(users, cls.__qdbpath+"authentification.tql")
        print(f"{username} added.")

    
    


    
        
    @classmethod
    def qdb(cls, f):
        res = os.path.join(cls.__qdbpath, f)
        return res



####################################################



    
class ts(__TQL):
    """
    퀀트운용팀/93 QuickDB 에 존재하는 Timeseries 데이터를 가져온다.
    """
    

    
    @classmethod 
    def index_shares(cls, start, end=None):
        """지수산정주식수"""
        no = 25
        return cls.__getTS(no, start, end)
    
    
    @classmethod 
    def float_mktcap(cls, start, end=None):
        """유동시가총액"""
        no = 30
        return cls.__getTS(no, start, end)
    
    
    @classmethod 
    def index_mktcap(cls, start, end=None):
        """지수산정시가총액"""
        no = 29
        return cls.__getTS(no, start, end)

    @classmethod
    def toName(cls, df):
        start = df.index[0]
        end = df.index[-1]
        y1 = int(start[:4])
        y2 = int(end[:4])
        res = []
        for year in range(y1, y2+1):
            if devmode:
                print(year)
            _ = super().load_pkl(super().qdb(f"ts/{year}_0.data"))
            if _ is not None:
                res.append(_)
        names = pd.concat(res).sort_index().loc[start:end].mode().iloc[-1]
        df.columns = df.columns.map(lambda x : names.to_dict()[x])
        return df
        
    @classmethod
    def __getTS(
        cls,
        no,
        start,
        end=None, 
    ):
        start = str(start)
        if end is None:
            end = start
        end = str(end)
        y1 = int(str(start[:4]))
        y2 = int(str(end[:4]))
        res = []
        try:
            for year in range(y1, y2+1):
                _ = super().load_pkl(super().qdb(f"ts/{year}_{no}.data"))
                if _ is not None:
                    res.append(_)
            df = pd.concat(res).sort_index().loc[start:end]
        except Exception as e:
            print(e)
            raise e
        return df
    
    @classmethod
    def pr(cls, start, end=None, interval='1d'):
        """
        
        Args:
            start (_type_): 데이터를 가져 올 시작날짜
            end (_type_, optional): 끝 날짜. None일 경우 시작날짜에 한해서 데이터를 가져오나, 시작 날짜가 비영업일일 경우 어떻게 처리되는지 아직 정의 안됨.. 아마 에러?
            interval (str, optional): 1d, 1w, 1m, 3m, 6m, 12m. Defaults to '1d'.
            name (bool, optional): True : 컬럼이 티커가 아닌 종목명을 반환. Defaults to False.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        valid_interval = ["1d", "1w", "1m", "3m", "6m", "12m"]
        if interval not in valid_interval:
            raise ValueError("interval must be [1d, 1w, 1m, 3m, 6m or 12m]")
        if interval == '1d':
            no = 11
        elif interval == '1w':
            no = 14
        elif interval == '1m':
            no = 15
        elif interval == '3m':
            no = 16
        elif interval == '6m':
            no = 17
        elif interval == '12m':
            no = 18
        return cls.__getTS(no, start, end)
    
    @classmethod 
    def tr(cls, start, end=None):
        no = 12
        return cls.__getTS(no, start, end)
    
    @classmethod 
    def trdstp(cls, start, end=None):
        no = 88
        return cls.__getTS(no, start, end)
    
    @classmethod
    def pr_open(cls, start, end=None):
        no = 13
        return cls.__getTS(no, start, end)
        
    @classmethod
    def volume(cls, start, end=None):
        no = 21
        return cls.__getTS(no, start, end)

    @classmethod
    def amount(cls, start, end=None):
        no = 22
        return cls.__getTS(no, start, end)
        
    @classmethod
    def shares(cls, start, end=None):
        no = 24
        return cls.__getTS(no, start, end)
    
    @classmethod
    def volume_turnover(cls, start, end=None):
        no = 39
        return cls.__getTS(no, start, end)
    
    @classmethod
    def market(cls, start, end=None):
        no = 2
        return cls.__getTS(no, start, end)
    
    @classmethod
    def settlement_month(cls, start, end=None):
        no = 1
        return cls.__getTS(no, start, end)
    
    @classmethod
    def open(cls, start, end=None):
        no = 4
        return cls.__getTS(no, start, end)
    
    @classmethod
    def close(cls, start, end=None):
        no = 3
        return cls.__getTS(no, start, end)
    
    @classmethod
    def high(cls, start, end=None):
        no = 5
        return cls.__getTS(no, start, end)

    @classmethod
    def low(cls, start, end=None):
        no = 6
        return cls.__getTS(no, start, end)
    
    @classmethod
    def mktcap(cls, start, end=None):
        no = 28
        return cls.__getTS(no, start, end)
    
    @classmethod
    def treasury_stock(cls, start, end=None):
        no = 26
        return cls.__getTS(no, start, end)
    
    @classmethod
    def foreigner_share(cls, start, end=None):
        no = 27
        return cls.__getTS(no, start, end)
    

    @classmethod
    def wics_L(cls, start, end=None):
        no = 73
        return cls.__getTS(no, start, end)
    
    @classmethod
    def wi26(cls, start, end=None):
        no = 76
        return cls.__getTS(no, start, end)
    
    @classmethod
    def wics_m(cls, start, end=None):
        no = 74
        return cls.__getTS(no, start, end)
    
    @classmethod
    def wi26_m(cls, start, end=None):
        no = 77
        return cls.__getTS(no, start, end)
    
    @classmethod
    def wics_s(cls, start, end=None):
        no = 75
        return cls.__getTS(no, start, end)
    
    @classmethod
    def is_ks200(cls, start, end=None):
        no = 71
        return cls.__getTS(no, start, end)
    
    @classmethod
    def is_kq150(cls, start, end=None):
        no =72
        return cls.__getTS(no, start, end)
    
    @classmethod
    def krx_sector(cls, start, end=None):
        no = 78
        return cls.__getTS(no, start, end)
    
    @classmethod
    def credit_rate(cls, start, end=None, asset='cp', agency='한신평'):
        if asset == 'cp':
            if agency == '한신정':
                no = 83
            elif agency == '한기평':
                no = 84
            elif agency == '한신평':
                no = 82
            else:
                raise Exception("agency must be '한신정' or '한기평' or '한신평'.")
        elif asset == '채권':
            if agency == '한신정':
                no = 86
            elif agency == '한기평':
                no = 85
            elif agency == '한신평':
                no = 87
            else:
                raise Exception("agency must be '한신정' or '한기평' or '한신평'.")
        else:
            raise Exception("asset can only be 'cp' or '채권'")

        return cls.__getTS(no, start, end)


    ######### 수급

    @classmethod
    def net_purchase(cls, start, end=None, entity='개인', is_qty=True):
        if entity=='개인':
            if is_qty:
                no = 124
            else:
                no = 125
        elif entity=='기관':
            if is_qty:
                no = 102
            else:
                no = 103
        elif entity=='외국인':
            if is_qty:
                no = 118
            else:
                no = 119

        elif entity=='보험':
            if is_qty:
                no = 106
            else:
                no = 107

        elif entity=='투신':
            if is_qty:
                no = 108
            else:
                no = 109

        elif entity=='은행':
            if is_qty:
                no = 112
            else:
                no = 113

        elif entity=='연기금':
            if is_qty:
                no = 114
            else:
                no = 115

        elif entity=='사모펀드':
            if is_qty:
                no = 110
            else:
                no = 111        
        else:
            raise Exception("entity must be '개인', '기관', '외국인', '보험', '투신', '은행', '연기금' or '사모펀드'.")
        return cls.__getTS(no, start, end)


    ######### 기타 거래소 지정 종목

    @classmethod
    def 투자유의(cls, start=None, end=None):
        no = 91
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 투자주의환기종목(cls, start=None, end=None):
        no = 90
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 불성실공시법인(cls, start=None, end=None):
        no = 93
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 차입공매도과열종목(cls, start=None, end=None):
        no = 96
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 단기과열종목(cls, start=None, end=None):
        """0 : 미해당, 1 : 지정예고, 2: 지정, 3: 지정연장"""
        no = 95
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 관리종목(cls, start=None, end=None):
        no = 89
        return cls.__getTS(no, start, end)


    ############# 대차, 신용, 공매도 관련 ###############

    @classmethod
    def 대차거래잔고(cls, start=None, end=None, is_qty=True):
        if not is_qty:
            no = 44
        else:
            no = 42
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 대차거래체결량(cls, start=None, end=None):
        no = 40
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 대차거래상환량(cls, start=None, end=None):
        no = 41    
        return cls.__getTS(no, start, end)

    @classmethod
    def 차입공매도거래량(cls, start=None, end=None, is_qty=True):
        if not is_qty:
            no = 46
        else:
            no = 48        
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 차입공매도잔고(cls, start=None, end=None, is_qty=True):
        if not is_qty:
            no = 51
        else:
            no = 50        
        return cls.__getTS(no, start, end)

    @classmethod
    def 신용융자(cls, start=None, end=None, type='balance', is_qty=True):
        if type=='new':
            if is_qty:
                no = 54
            else:
                no = 57
        elif type=='repay':
            if is_qty:
                no = 55
            else:
                no = 58
        elif type=='balance':
            if is_qty:
                raise Exception("qty can't be used fortype[balance]. Switch is_qty parameter.")
            else:
                no = 56
        else:
            raise Exception("type parameter must be 'new', 'repay' or 'balance'")
        return cls.__getTS(no, start, end)
    
    @classmethod
    def 신용대주(cls, start=None, end=None, type='balance'):
        if type=='new':
            if is_qty:
                no = 62
            else:
                no = 65
        elif type=='repay':
            if is_qty:
                no = 63
            else:
                no = 66
        elif type=='balance':
            if is_qty:
                raise Exception("qty can't be used fortype[balance]. Switch is_qty parameter.")
            else:
                no = 64
        else:
            raise Exception("type parameter must be 'new', 'repay' or 'balance'")
        return cls.__getTS(no, start, end)
    


    
#####################################################
   


class fs(__TQL):

    @classmethod
    def __getYQTB(
        cls,
        when
    ):
        when = str(when)
        df = super().load_pkl(super().qdb(f"fs/{when[:4]}.yqtb"))
        return df.loc[:str(when)].iloc[-1]
    
    #FS data는 1년에 네 번 바뀌기 때문에 기간 으로 가져올 필요가 없음.
    #특정 시점에 확인 가능한 데이터를 가져오는 것이 최선.
    @classmethod
    def __getFS(cls, account, date):
        data = {}
        for yq in cls.__getYQTB(date).dropna().unique():
            data[yq] = super().load_pkl(super().qdb(f'fs/{yq}.data'))

        result = {}
        for ticker, yq in cls.__getYQTB(date).dropna().items():
            result[ticker] = data[yq][account].get(ticker)
        
        return pd.Series(result)
    
    @classmethod
    def __getTrailingYQ(cls, yq, n=4):
        y,q = yq[:4], (yq[4:])
        roll = ['03' , '06', '09', '12']

        while roll[0] != q:
            roll = np.roll(roll, 1)

        YQ = [y+q]

        for i in range(n-1):
            roll = np.roll(roll, 1)
            if roll[0] == '12':
                y = str(int(y) - 1)
            q = roll[0]
            YQ.append(y+q)
        return YQ

    @classmethod
    def __getTrailingFS(cls, account, date, n=4, method=None):
        YQ = cls.__getYQTB(date).dropna().map(lambda x : cls.__getTrailingYQ(x, n))
        data = {}
        for yq in np.unique(np.array(YQ.to_list()).reshape(-1)):
            data[yq] = super().load_pkl(super().qdb(f'fs/{yq}.data'))
            #load_pkl(os.path.join(self.path, f'fs/{yq}.data'))
        
        res = {}
        for ticker, yq in YQ.items():
            try:
                res[ticker] = pd.Series(
                    data[_yq][account].get(ticker) for _yq in yq
                )
            except:
                pass
        df = pd.DataFrame(res).dropna(axis=1)

        if method == 'sum':
            return df.sum()
        if method == 'std':
            return df.std()
        if method == 'mean':
            return df.mean()
        else:
            return df
        





    ################################





    @classmethod
    def 자산총계(cls, date, q=1, method=None):
        acc = '자산총계'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 유동자산(cls, date, q=1, method=None):
        acc = '유동자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 재고자산(cls, date, q=1, method=None):
        acc = '재고자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 매출채권및기타채권(cls, date, q=1, method=None):
        acc = '매출채권및기타채권'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당좌자산(cls, date, q=1, method=None):
        acc = '당좌자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 현금및현금성자산(cls, date, q=1, method=None):
        acc = '현금및현금성자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자산_매각예정비유동자산처분(cls, date, q=1, method=None):
        acc = '자산_매각예정비유동자산처분'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 비유동자산(cls, date, q=1, method=None):
        acc = '비유동자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 유형자산(cls, date, q=1, method=None):
        acc = '유형자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 무형자산(cls, date, q=1, method=None):
        acc = '무형자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 투자자산(cls, date, q=1, method=None):
        acc = '투자자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 장기매출채권및기타채권(cls, date, q=1, method=None):
        acc = '장기매출채권및기타채권'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타비유동자산(cls, date, q=1, method=None):
        acc = '기타비유동자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 이연법인세자산(cls, date, q=1, method=None):
        acc = '이연법인세자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 부채총계(cls, date, q=1, method=None):
        acc = '부채총계'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 유동부채(cls, date, q=1, method=None):
        acc = '유동부채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 만기도래사채(cls, date, q=1, method=None):
        acc = '만기도래사채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 만기도래차입금(cls, date, q=1, method=None):
        acc = '만기도래차입금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 매입채무및기타채무(cls, date, q=1, method=None):
        acc = '매입채무및기타채무'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 이자발생부채(cls, date, q=1, method=None):
        acc = '이자발생부채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 부채_매각예정처분자산(cls, date, q=1, method=None):
        acc = '부채_매각예정처분자산'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 순부채(cls, date, q=1, method=None):
        acc = '순부채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 비유동부채(cls, date, q=1, method=None):
        acc = '비유동부채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 사채(cls, date, q=1, method=None):
        acc = '사채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def CB(cls, date, q=1, method=None):
        acc = 'CB'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def BW(cls, date, q=1, method=None):
        acc = 'BW'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EB(cls, date, q=1, method=None):
        acc = 'EB'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 장기차입금(cls, date, q=1, method=None):
        acc = '장기차입금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 장기매입채무및기타채무(cls, date, q=1, method=None):
        acc = '장기매입채무및기타채무'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 이연법인세부채(cls, date, q=1, method=None):
        acc = '이연법인세부채'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본총계(cls, date, q=1, method=None):
        acc = '자본총계'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본총계_지배(cls, date, q=1, method=None):
        acc = '자본총계(지배)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본총계_TTM(cls, date, q=1, method=None):
        acc = '자본총계(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본총계_지배_TTM(cls, date, q=1, method=None):
        acc = '자본총계(지배, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본총계_지배_MAIN_TTM(cls, date, q=1, method=None):
        acc = '자본총계(지배, MAIN, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본금(cls, date, q=1, method=None):
        acc = '자본금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 보통주자본금(cls, date, q=1, method=None):
        acc = '보통주자본금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 우선주자본금(cls, date, q=1, method=None):
        acc = '우선주자본금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 신종자본증권(cls, date, q=1, method=None):
        acc = '신종자본증권'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본잉여금(cls, date, q=1, method=None):
        acc = '자본잉여금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 이익잉여금(cls, date, q=1, method=None):
        acc = '이익잉여금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타자본(cls, date, q=1, method=None):
        acc = '기타자본'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자기주식(cls, date, q=1, method=None):
        acc = '자기주식'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타포괄이익누계액(cls, date, q=1, method=None):
        acc = '기타포괄이익누계액'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 비지배주주지분(cls, date, q=1, method=None):
        acc = '비지배주주지분'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 매출액(cls, date, q=1, method=None):
        acc = '매출액'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 매출액_TTM(cls, date, q=1, method=None):
        acc = '매출액(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 매출원가(cls, date, q=1, method=None):
        acc = '매출원가'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 매출총이익(cls, date, q=1, method=None):
        acc = '매출총이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 판매비와관리비(cls, date, q=1, method=None):
        acc = '판매비와관리비'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 인건비및복리후생비(cls, date, q=1, method=None):
        acc = '인건비및복리후생비'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업이익(cls, date, q=1, method=None):
        acc = '영업이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업이익_TTM(cls, date, q=1, method=None):
        acc = '영업이익(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타영업수익(cls, date, q=1, method=None):
        acc = '기타영업수익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타영업비용(cls, date, q=1, method=None):
        acc = '기타영업비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업이익_발표기준(cls, date, q=1, method=None):
        acc = '영업이익(발표기준)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타영업외손익(cls, date, q=1, method=None):
        acc = '기타영업외손익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 금융수익(cls, date, q=1, method=None):
        acc = '금융수익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 금융비용(cls, date, q=1, method=None):
        acc = '금융비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타영업외수익(cls, date, q=1, method=None):
        acc = '기타영업외수익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타영업외비용(cls, date, q=1, method=None):
        acc = '기타영업외비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 손익_종속기업_공동지배기업_관계기업관련(cls, date, q=1, method=None):
        acc = '손익_종속기업, 공동지배기업, 관계기업관련'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 이자수익(cls, date, q=1, method=None):
        acc = '이자수익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 이자비용(cls, date, q=1, method=None):
        acc = '이자비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 순이자비용(cls, date, q=1, method=None):
        acc = '순이자비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 총순이자비용(cls, date, q=1, method=None):
        acc = '총순이자비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 감가상각비_판관비(cls, date, q=1, method=None):
        acc = '감가상각비(판관비)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 감가상각비_판관비_TTM(cls, date, q=1, method=None):
        acc = '감가상각비(판관비, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 대손상각비(cls, date, q=1, method=None):
        acc = '대손상각비'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 세전계속사업이익(cls, date, q=1, method=None):
        acc = '세전계속사업이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 세전계속사업이익_TTM(cls, date, q=1, method=None):
        acc = '세전계속사업이익(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 법인세비용(cls, date, q=1, method=None):
        acc = '법인세비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 법인세비용_TTM(cls, date, q=1, method=None):
        acc = '법인세비용(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 계속사업이익(cls, date, q=1, method=None):
        acc = '계속사업이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 계속사업이익_TTM(cls, date, q=1, method=None):
        acc = '계속사업이익(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 중단사업이익(cls, date, q=1, method=None):
        acc = '중단사업이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익(cls, date, q=1, method=None):
        acc = '당기순이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익_지배(cls, date, q=1, method=None):
        acc = '당기순이익(지배)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익_비지배(cls, date, q=1, method=None):
        acc = '당기순이익(비지배)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 연결당기순이익_지배(cls, date, q=1, method=None):
        acc = '*연결당기순이익(지배)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익_TTM(cls, date, q=1, method=None):
        acc = '당기순이익(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익_지배_TTM(cls, date, q=1, method=None):
        acc = '당기순이익(지배, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익_지배_MAIN_TTM(cls, date, q=1, method=None):
        acc = '당기순이익(지배, MAIN, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 당기순이익_비지배_TTM(cls, date, q=1, method=None):
        acc = '당기순이익(비지배, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 연결당기순이익_지배_TTM(cls, date, q=1, method=None):
        acc = '*연결당기순이익(지배, TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타포괄이익(cls, date, q=1, method=None):
        acc = '기타포괄이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 총포괄이익(cls, date, q=1, method=None):
        acc = '총포괄이익'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 총포괄이익_지배(cls, date, q=1, method=None):
        acc = '총포괄이익(지배)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 총포괄이익_비지배(cls, date, q=1, method=None):
        acc = '총포괄이익(비지배)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 성격별비용계정_합계(cls, date, q=1, method=None):
        acc = '*성격별비용계정(합계)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 제품과재공품의변동(cls, date, q=1, method=None):
        acc = '*제품과재공품의변동'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기업이수행한용역으로서자본화되어있는부분(cls, date, q=1, method=None):
        acc = '*기업이수행한용역으로서자본화되어있는부분'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 원재료와저장품_소모품의사용액(cls, date, q=1, method=None):
        acc = '*원재료와저장품(소모품)의사용액'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 상품의판매(cls, date, q=1, method=None):
        acc = '*상품의판매'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타원가(cls, date, q=1, method=None):
        acc = '*기타원가'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 종업원급여비용(cls, date, q=1, method=None):
        acc = '*종업원급여비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 감가상각비와기타상각비및손상차손(cls, date, q=1, method=None):
        acc = '*감가상각비와기타상각비및손상차손'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 세금과공과(cls, date, q=1, method=None):
        acc = '*세금과공과'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 대손상각비(cls, date, q=1, method=None):
        acc = '*대손상각비'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 물류비_운송보관(cls, date, q=1, method=None):
        acc = '*물류비(운송보관)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 광고및판매촉진비(cls, date, q=1, method=None):
        acc = '*광고및판매촉진비'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 임차료및리스료(cls, date, q=1, method=None):
        acc = '*임차료및리스료'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 경상연구개발비(cls, date, q=1, method=None):
        acc = '*경상연구개발비'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 기타비용(cls, date, q=1, method=None):
        acc = '*기타비용'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def Cash_Earnings(cls, date, q=1, method=None):
        acc = 'Cash Earnings'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def Cash_Earnings_TTM(cls, date, q=1, method=None):
        acc = 'Cash Earnings(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업활동으로인한현금흐름(cls, date, q=1, method=None):
        acc = '영업활동으로인한현금흐름'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업활동으로인한현금흐름_TTM(cls, date, q=1, method=None):
        acc = '영업활동으로인한현금흐름(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 감가상각비_현금흐름표(cls, date, q=1, method=None):
        acc = '감가상각비(현금흐름표)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 운전자본증감(cls, date, q=1, method=None):
        acc = '운전자본증감'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 투자활동으로인한현금흐름(cls, date, q=1, method=None):
        acc = '투자활동으로인한현금흐름'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 투자활동으로인한현금흐름_TTM(cls, date, q=1, method=None):
        acc = '투자활동으로인한현금흐름(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def CAPEX(cls, date, q=1, method=None):
        acc = 'CAPEX'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 재무활동으로인한현금흐름(cls, date, q=1, method=None):
        acc = '재무활동으로인한현금흐름'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 재무활동으로인한현금흐름_TTM(cls, date, q=1, method=None):
        acc = '재무활동으로인한현금흐름(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 배당금(cls, date, q=1, method=None):
        acc = '배당금'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 자본의증감(cls, date, q=1, method=None):
        acc = '자본의증감'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업투자재무활동기타현금흐름(cls, date, q=1, method=None):
        acc = '영업투자재무활동기타현금흐름'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 영업투자재무활동기타현금흐름_TTM(cls, date, q=1, method=None):
        acc = '영업투자재무활동기타현금흐름(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def 현금의증가(cls, date, q=1, method=None):
        acc = '현금의증가'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def Free_Cash_Flow1(cls, date, q=1, method=None):
        acc = 'Free Cash Flow1'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def Free_Cash_Flow2(cls, date, q=1, method=None):
        acc = 'Free Cash Flow2'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def FCF1_TTM(cls, date, q=1, method=None):
        acc = 'FCF1(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def FCF2_TTM(cls, date, q=1, method=None):
        acc = 'FCF2(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EBITDA(cls, date, q=1, method=None):
        acc = 'EBITDA'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EBITDA_TTM(cls, date, q=1, method=None):
        acc = 'EBITDA(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EBITDA2(cls, date, q=1, method=None):
        acc = 'EBITDA2'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EBITDA2_TTM(cls, date, q=1, method=None):
        acc = 'EBITDA2(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EBIT(cls, date, q=1, method=None):
        acc = 'EBIT'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EBIT_TTM(cls, date, q=1, method=None):
        acc = 'EBIT(TTM)'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def IC(cls, date, q=1, method=None):
        acc = 'IC'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def NOPLAT(cls, date, q=1, method=None):
        acc = 'NOPLAT'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EV(cls, date, q=1, method=None):
        acc = 'EV'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def EV2(cls, date, q=1, method=None):
        acc = 'EV2'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        

    @classmethod
    def Operating_EBIT(cls, date, q=1, method=None):
        acc = 'Operating EBIT'
        if q == 1:
            return cls.__getFS(acc, date)
        else:
            return cls.__getTrailingFS(acc, date, n=q, method=method)
        
import numpy as np
class index(__TQL):
    @classmethod
    def __get(cls, idx, start=None, end=None, period=None, ret=False):
        assert (start is None and end is None and period is not None) or (start is not None and end is not None and period is None), "(start,end) and period can't have values simultaneously."
        
        data = super().load_pkl(super().qdb("ts/IDX.data"))
        data.index = data.index.map(lambda x : x.strftime('%Y%m%d'))
        
        if ret:
            data = data.pct_change(1).iloc[1:]
        
        if period is not None:
            return data.loc[list(period), idx]
        else:
            return data.loc[start : end, idx]


    @classmethod
    def KS200(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스피 200", start, end, period, ret)
    
    @classmethod
    def KS(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스피", start, end, period, ret)
    
    @classmethod
    def KSTR(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스피 TR", start, end, period, ret)
    
    @classmethod
    def KS200TR(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스피 200 TR", start, end, period, ret)
    
    @classmethod
    def KQ(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스닥", start, end, period, ret)
    
    @classmethod
    def KQ150(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스닥 150", start, end, period, ret)
    
    @classmethod
    def KQ150TR(cls, start=None, end=None, period=None, ret=False):
        return cls.__get("코스닥 150 TR", start, end, period, ret)
    


#########################################

class econ:
    pass

#########################################


class fund:
    pass


#########################################
import requests
import json


class rt:
    base = "http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd"
    
    @classmethod
    def stock(cls, mkt='ALL'):
        """MKT : ALL, KS, KQ"""
        if mkt == 'ALL':
            mktId = 'ALL'
        elif mkt == 'KS':
            mktId = 'STK'
        elif mkt == 'KQ':
            mktId = 'KSQ'
        else:
            raise Exception("mkt must be ALL, KS or KQ")
        res = requests.post(
        cls.base, data=dict(bld = "dbms/MDC/STAT/standard/MDCSTAT01501",
                        locale='ko_KR', mktId=mktId, trdDd=datetime.datetime.now().strftime("%Y%m%d"))
    )
        df = pd.DataFrame(json.loads(res.text)['OutBlock_1'])
        df.columns = ["종목코드", "기업코드", "종목명", "시장구분", "소속부", "종가", "FLUC_TP_CD", "대비", "등락률", "시가", "고가", "저가", "거래량", "거래대금", "시가총액", "상장주식수", "MKT_ID"]
        del df['FLUC_TP_CD']
        del df['MKT_ID']
        return df


    @classmethod
    def index(cls, type='KS'):
        """type : KRX, KS, KQ, THEME"""
        if type == 'KS':
            idxIndMidclssCd = '02'
        elif type == 'KRX':
            idxIndMidclssCd = '01'
        elif type == 'KQ':
            idxIndMidclssCd = '03'
        elif type == 'THEME':
            idxIndMidclssCd = '04'
        else:
            raise Exception("type must be KRX, KS, KQ OR THEME")
        res = requests.post(
        cls.base, data=dict(bld = "dbms/MDC/STAT/standard/MDCSTAT00101",
                        locale='ko_KR',  idxIndMidclssCd=idxIndMidclssCd, trdDd=datetime.datetime.now().strftime("%Y%m%d"))
    )
        df = pd.DataFrame(json.loads(res.text)['output'])
        df.columns = ['지수명' , '종가' , 'FLUC_TP_CD', '대비', '등락률', '시가', '고가', '저가', '거래량', '거래대금', '상장시가총액']
        del df['FLUC_TP_CD']
        return df


    


#########################################


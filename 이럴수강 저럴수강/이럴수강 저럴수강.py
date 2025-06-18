import numpy as np
import pandas as pd


csv = pd.read_csv(r"C:\Users\sinja\Desktop\이신재\코딩\컴프 과제\새 폴더\이럴수강 저럴수강\수강편람조회.csv")
individual_data = {"학년": 0, "학과": 0}
category = {"학점": 0, "사이버 강의 여부": 0, "월요일 공강": 0, "화요일 공강": 0, "수요일 공강": 0,
            "목요일 공강": 0, "금요일 공강": 0, "1교시 여부": 0, "점심시간 여부": 0, "우주공강 여부": 0}

filtering = {}
filtering.update(individual_data)
filtering.update(category)


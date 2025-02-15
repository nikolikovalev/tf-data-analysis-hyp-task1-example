import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 411809593 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    a = 0.02
    cnts = [x_cnt, y_cnt]
    successes = [x_success, y_success]
    p = ttest_ind(successes, cnts)[1]
    otv = p < a
    return otv

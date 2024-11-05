NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит

def classify(X):
    answer = 0
    iq_level, articles_count, has_education, ratio = X

    if iq_level <= 70:
        answer = NOT_FIT
    
    if iq_level > 70:
        if articles_count == 1:
            answer = FIT
        
        if articles_count == 2:
            if ratio <= 2.2:
                answer = FIT
            else:
                answer = NOT_FIT
    return answer

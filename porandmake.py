
#　キーボードからの入力
def get_formula():
    formula = input("式を入力してください\n")
    formula = formula.replace(' ','')
    formula = formula.replace('*','')
    return convert_formula_to_rpn(formula)

#   逆ポーランド記法への変換
def convert_formula_to_rpn(formula):
    length = len(formula)
    if length < 2:
        return formula

    ct = 0
    deep = 0

    #　不要な括弧の除去
    while ct < length:
        if formula[ct] == '(':
            deep = deep + 1
        elif formula[ct] == ')':
            deep = deep - 1
            
        if deep == 0:
            if ct >= length-1:
                formula = formula[1:length-1]
                length = length - 2
            break
        ct = ct + 1
    
    sign = 0
    deep = 0
    ct = 0

    #　演算子の検出　＋、ー
    while ct < length:
        if formula[ct] == '(':
           deep = deep + 1
        elif formula[ct] == ')':
                deep = deep - 1

        elif deep == 0:
            if formula[ct] == '+' or formula[ct] == '-':
                former = convert_formula_to_rpn(formula[0:ct])
                latter = convert_formula_to_rpn(formula[ct+1:length])
                sign = 1
                return [former,latter,formula[ct]]
        ct = ct + 1
    
    #　演算子の検出　＊
    ct = 0
    if sign == 0:
        level = 0
        st = 0
        while ct < length:
            if formula[ct] == '(':
                deep = deep + 1

            elif formula[ct] == ')':
                deep = deep - 1
                if deep == 0:
                    level = level + 1
                    if level == 1:
                        st = ct
                    
            elif deep == 0 :
                if ct + 1 < length and formula[ct].isdigit():
                    if formula[ct+1].isdigit() == False:
                        level = level + 1
                        if level == 1:
                            st = ct
                else :
                    level = level + 1
                    if level == 1:
                        st = ct

            if level == 2 :
                former = convert_formula_to_rpn(formula[0:st+1])
                latter = convert_formula_to_rpn(formula[st+1:length])
                return [former,latter,'*']
            ct = ct + 1
        
    return formula

formula = get_formula()
print(formula)
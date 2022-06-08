
#　キーボードからの入力
def get_formula():
    return convert_to_rpn(input("式を入力してください\n").replace(' ',''))

#   逆ポーランド記法への変換
def convert_to_rpn(formula):
    length = len(formula)
    if length < 2:
        return formula

    #　不要な括弧の除去
    if find_brackets(formula) == length-1:
        formula = formula[1:-1]
    
    return find_add_sub(formula) or find_mul(formula) or formula

def find_brackets(formula):
    deep = 0
    for ct, c in enumerate(formula):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -= 1

        if deep == 0:
            break

    return ct

    #　演算子の検出　＋、ー
def find_add_sub(formula):
    deep = 0
    for ct,word in enumerate(formula):
        if word == '(':
           deep += 1
        elif word == ')':
                deep += 1
        elif deep == 0:
            if word in '+-':
                return [convert_to_rpn(formula[:ct]),convert_to_rpn(formula[ct+1:]),formula[ct]]
    return None

    #　演算子の検出　＊
def find_mul(formula):
    length = len(formula)
    level = 0
    deep = 0
    for ct, c in enumerate(formula):
        if c == '(':
            deep += 1
        elif c == ')':
            deep -=  1

        if deep == 0:
            if c == '*':
                return [convert_to_rpn(formula[:ct]),convert_to_rpn(formula[ct+1:]),'*']
            if ct + 1 < length and c.isdigit():
                if formula[ct+1].isdigit() == False:
                    level += 1
                    if level == 1:
                        st = ct
            else :
                level += 1
                if level == 1:
                    st = ct
        if level == 2:
            return [convert_to_rpn(formula[:st+1]),convert_to_rpn(formula[st+1:]),'*']
    return None

formula = get_formula()
print(formula)
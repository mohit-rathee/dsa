class Solution:
    def valid_paranthesis_checker(self, s):
        print(s)

        open_count = 0
        start_count = 0

        for i in range(len(s)):
            char = s[i]
            match char:
                case '(':
                    open_count +=1
                case ')':
                    open_count -=1
                case '*':
                    # let's use '*' to make open_count --> 0
                    if open_count > 0:
                        open_count -= 1 # '*' ==> ')'
                        # later, when we revert '*' to '(' or '',
                        # we must account for this '(' contribution
                        start_count += 1 
                    elif open_count < 0:
                        open_count += 1 # '*' ==> '('
                    # else '*' ==> ''

                    start_count += 1
                    # print(i,open_count,start_count)
                    continue


            # print(i,open_count,start_count ,end=' becomes ')
            
            if open_count < 0:
                if start_count >= abs(open_count):
                    # earlier '*' would be treated as '(' now
                    start_count -= abs(open_count)
                    open_count = 0
                else:
                    # print('pre false')
                    return False

            # print(i,open_count,start_count)

        if open_count == 0:
            return True
        else:
            return False
                
    def standard_valid_paranthesis_checker(self, s):
        print(s)
        max_open = min_open = 0
        for char in s:
            if char == '(':
                min_open+=1
                max_open+=1
            elif char == ')':
                min_open = max(0,min_open-1)
                max_open -= 1
            else: # '*'
                min_open = max(0,min_open-1)
                max_open += 1
            
            if max_open < 0:
                return False
        return min_open == 0


sol = Solution()
s = '(*))'
s = '*(()'
s = '(**()))'
s = '(())*()()))'
s = '**))'
s = '**(('
s = '**(())'
s = '))**('
s = '(*)()'
s = ')(((**)))**))***()*(*))))())*())(()*))()((((*())(**))()())))()**()*()))))**)()))*)()()*)))(*())))))' # False
s = '***)(*(*(*(***(*(*))(*(**)*(*)(**)' # True
s = '**)))****)*****)*))' # False
s = '*)(*))()()((*)()(**)*()***()()**()()(***()*)()()*)()(())(*(**)(())()*)()()*)()' # True
print(sol.valid_paranthesis_checker(s))
print(sol.standard_valid_paranthesis_checker(s))

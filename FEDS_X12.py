class seg_conv:
    @staticmethod
    def replacevalue(lis):
        lis2 = []
        i = 0
        y = 0
        while i < len(lis):
            if lis[i] != '':
                lis2.insert(y, lis[i])

                y += 1
                lis2.insert(y + 1, '*')

                y += 1
            else:
                lis2.insert(y, lis[i].replace('', '*'))
            y += 1
            i += 1
        str1 = ''.join(lis2)

        return str(str1[:-1])

    @staticmethod
    def parseseg(arg):
        s = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '']
        input2=arg.split('\n')
        input=input2[:-1]
        i = 0
        while i < len(input):
            p = (input[i])
            if p[0] == 'S':
                s.insert(0, p[1:])
            elif p[0] == 'E':
                s.insert(int(p[2:4]), p[7:])
            i += 1
        tt = int(p[2:4]) + 1
        return seg_conv.replacevalue(s[:tt])


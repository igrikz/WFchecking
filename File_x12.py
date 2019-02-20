import FEDS_X12

class creats_x12():
    @staticmethod
    def spFeds():
        segCon = FEDS_X12.seg_conv()
        input = open("test.feds", "r").read().split('\n')
        output = open("xout.edi", "w")
        docnum = input[1]
        isa = 'ISA*00*          *00*          *ZZ*SPS            *ZZ*SPS            *190214*1607*U*' + '00401' + '*000000001*0*T*}'
        gs = 'GS*'+creats_x12.docN_GS(docnum[1:])+'*SPS*SPS*20190214*1607*0001*X*' + '004010'
        st = 'ST*' + docnum[1:] + '*00010001'
        output.write(isa + '\n')
        output.write(gs + '\n')
        output.write(st + '\n')
        y = 0
        i = 0
        seg = ''
        while i < len(input):
            t = (input[i])
            if t[0] == 'S':
                if seg != '':
                    output.write(segCon.parseseg(seg) + '\n')
                    y += 1
                seg = ''
                seg += t[0:] + '\n'

            elif t[0] == 'E':
                seg += t[0:] + '\n'
            i += 1
        output.write(segCon.parseseg(seg) + '\n')
        se = 'SE*' + str(y + 3) + '*00010001'
        ge = 'GE*1*0001'
        iea = 'IEA*1*000000001'
        output.write(se + '\n')
        output.write(ge + '\n')
        output.write(iea + '\n')
        output.close()

    @staticmethod
    def docN_GS(dic):
        dicts_from_file = {}
        with open('docNum_GS', 'r') as inf:
            for line in inf:
                l = line.split()
                dicts_from_file[l[0]] = l[1]
        return dicts_from_file[dic]






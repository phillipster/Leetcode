def replace_words(dictionary: list[str], sentence: str) -> str:
    sentence = sentence.split()
    for root in dictionary:
        for i in range(len(sentence)):
            try:
                temp = sentence[i].index(root)
            except ValueError:
                pass
            else:
                if sentence[i][0] == root[0]:
                    sentence[i] = root
    return ' '.join(sentence)

dict = ["gymth","qglnp","hmgs","rsz","upq","aq","relo","hz","i","atwlc","d","cxax","ymy","hfvr","x","qzgxa","abdgp","dwksr","p","yf","qao","von","bpji","mzxky","tuabq","yquz","j","dzpju","hadfd","svux","rmyku","ae","cr","bowu","slak","s","qvlg","geuw","qx","t","vzix","ycl","xoeyd","cq","jhjm","lt","uye","hwe","rtidu","ksy","dnl","knlsv","yv","ndga","ounoa","kah","dlruh","wbg","vfzt","unnh","kpd","uutv","vxz","lwmh","skyw","f","tktpf","botu","rrs","zdlr","papga","xeyn","z","tqjh","ivzh","b","k","woyl","ixas","tiyd","g","lcq","ta","xd","ztg","oxk","ax","hgqm","dx","zri","heeq","m","q","ub","xxo"]
sentence = "snhaafs hprzyepsgezd ntc ktogne kluwleaobb nwjatqwpx tzobvpylft s jzrlxuzsw fkkjvorqnhpeoikjepmm rxerxpfjssfvtzvunri rpnaizunsjlppuzppf udoqhtcpcv rtegaohvotz eovfuvymmzywjoytegf cztodouflfgc qtom vlyyboks izzhgin rtnrxmm ovtgafmvzu xxeabovlxmy zrqzsexkerfjiqkyjou ygelavmpdncapreadba y kedhgamqyjaffbex fosrpjojgwzjfaoxn pjqysu esaaoksfsvjabdbk e sknkvxxngqpfdkm dmqfzqjuunrbdmkjp fesdkqewhigg anlrixkeqaexh yhmywgpebtsprje tmwbuqnffycjm otfnqgtetdi ovyrmzo vkeze opq rijfryopiizsitum jyz ynoworq xmqohxpgce eblgjvghxxndaqvknph ghhxzfda onukxgjtdrjmoddqhfl xwmutmcvrzkjzxmtz xslacnagnrlu nidcqwrffyrlosnjjl stwperkfcvyzezbebktq fjhb hhxeturoihcdgkkq evzcmxhrnwvnpbbfsm cshlxs qouyuxwdjwyhfp ceiddqqfp pzbsuxqc qgrbisfcnyhdwmbkdjh cxlxqwi z ihgekczvavdwvivvj fjttwiqxqjgakd diggghnustrtizokcrw earkadvle eufogeidbfrcz cnms gomw rbraz bsbopklfbnbbzcod zbayalermeyxn ckrfpylus ofmpofltxmsideqxx rmkqaxda map gvpqwuofuwue o mkzz njrqnwlihegmpmr dbbpwy t c apljlybekb avgxnubzswldzyln tkxwrskwqkzdueuautg cekskcpocbubavun jezsixdu yepzrfdrhqajotjohmzo fleesmkehkvoj ciloebxldjgwtf ruzc tshzh cgudcyfzppgduvfha grcrveutgkz cfsrzt"
print(replace_words(dict, sentence))
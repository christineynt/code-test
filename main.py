# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Question one part 1
    numbers = [1228,
               1584,
               1258,
               1692,
               1509,
               1927,
               1177,
               1854,
               1946,
               1815,
               1925,
               1531,
               1529,
               1920,
               1576,
               1392,
               1744,
               1937,
               1636,
               1615,
               1944,
               1949,
               1931,
               1253,
               1587,
               1860,
               1874,
               1611,
               2008,
               1182,
               1900,
               1515,
               1978,
               1996,
               116,
               1588,
               1322,
               1680,
               1174,
               1712,
               1513,
               1778,
               1443,
               1569,
               1453,
               708,
               1783,
               1926,
               1959,
               2001,
               1776,
               1643,
               1654,
               1934,
               1983,
               1630,
               1382,
               1486,
               1422,
               1836,
               1728,
               1315,
               1843,
               1521,
               1995,
               1403,
               1897,
               1280,
               1981,
               1901,
               1870,
               1519,
               1945,
               1857,
               591,
               1329,
               1954,
               1679,
               1726,
               1846,
               1709,
               1695,
               1293,
               1602,
               1665,
               1940,
               1921,
               1861,
               1710,
               1524,
               1303,
               1849,
               1742,
               1892,
               1913,
               1530,
               1484,
               1903,
               1545,
               1609,
               1652,
               1908,
               1923,
               1188,
               1649,
               1994,
               1790,
               1832,
               140,
               867,
               1664,
               1598,
               1371,
               1018,
               35,
               1833,
               1161,
               1898,
               1482,
               1767,
               1252,
               1882,
               1448,
               1032,
               1459,
               1661,
               1391,
               1770,
               1806,
               1465,
               1295,
               1546,
               1355,
               1358,
               1321,
               1368,
               1514,
               1756,
               1775,
               1957,
               1468,
               1975,
               631,
               1812,
               1151,
               1167,
               1251,
               1960,
               1991,
               1972,
               1936,
               1552,
               1419,
               1577,
               1549,
               1580,
               1974,
               1830,
               1813,
               1893,
               1492,
               1389,
               1454,
               1522,
               1556,
               1172,
               1653,
               1822,
               1328,
               1907,
               1999,
               1281,
               1912,
               1919,
               1896,
               1722,
               1341,
               1720,
               1201,
               1512,
               1298,
               1254,
               1947,
               1505,
               1594,
               1334,
               1592,
               1943,
               1405,
               1589,
               1263,
               1930,
               1736,
               1180,
               1984,
               1401,
               1340,
               1292,
               1979,
               1876]
    found = False
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if i != j:
                if numbers[i] + numbers[j] == 2020:
                    print("Question 1 part 1")
                    print(numbers[i], numbers[j])
                    print(numbers[i] * numbers[j])
                    found = True
        if found:
            break

    # Question 1 part 2
    numbers = """1228
1584
1258
1692
1509
1927
1177
1854
1946
1815
1925
1531
1529
1920
1576
1392
1744
1937
1636
1615
1944
1949
1931
1253
1587
1860
1874
1611
2008
1182
1900
1515
1978
1996
116
1588
1322
1680
1174
1712
1513
1778
1443
1569
1453
708
1783
1926
1959
2001
1776
1643
1654
1934
1983
1630
1382
1486
1422
1836
1728
1315
1843
1521
1995
1403
1897
1280
1981
1901
1870
1519
1945
1857
591
1329
1954
1679
1726
1846
1709
1695
1293
1602
1665
1940
1921
1861
1710
1524
1303
1849
1742
1892
1913
1530
1484
1903
1545
1609
1652
1908
1923
1188
1649
1994
1790
1832
140
867
1664
1598
1371
1018
35
1833
1161
1898
1482
1767
1252
1882
1448
1032
1459
1661
1391
1770
1806
1465
1295
1546
1355
1358
1321
1368
1514
1756
1775
1957
1468
1975
631
1812
1151
1167
1251
1960
1991
1972
1936
1552
1419
1577
1549
1580
1974
1830
1813
1893
1492
1389
1454
1522
1556
1172
1653
1822
1328
1907
1999
1281
1912
1919
1896
1722
1341
1720
1201
1512
1298
1254
1947
1505
1594
1334
1592
1943
1405
1589
1263
1930
1736
1180
1984
1401
1340
1292
1979
1876"""
    numbers = numbers.replace(" ", "").split("\n")
    for i in range(len(numbers) - 1):
        numbers[i] = int(numbers[i])

    found = False

    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            for k in range(len(numbers) - 1):
                if i != j and i != k and j != k:
                    if numbers[i] + numbers[j] + numbers[k] == 2020:
                        print("Question 1 part 2")
                        print(numbers[i], numbers[j], numbers[k])
                        print(numbers[i] * numbers[j] * numbers[k])
                        found = True
            if found:
                break

    # Question 2
    password = """2-5 l: fllxf
4-5 r: rrrjmrrrrrrh
1-4 k: kkksk
7-8 k: tknsqknzkckrwkjkk
2-3 p: mpbstpxmsxmpnhbwlb
2-7 j: xkjjtjjjj
2-7 m: gczbmgk
15-16 q: qqqqqqqqqckqqqfqqq
7-14 d: dgdddlddddddrvfddnsd
7-12 r: rrrrrrrrbrrrl
2-11 p: zppjpwpqppbnppd
6-8 w: wqhwwnpwwwr
4-10 m: fmkmrrrdkmr
1-2 n: nnjvtnzk
3-8 t: tdxmzslxtvft
13-14 m: mmmmmhmmmmmmmm
9-10 l: lljllllllll
12-16 t: vdtbdtxtttttrctttkt
2-6 q: nqghxqgjqvzswbxww
4-6 k: khkkkkvrkgfwvbd
4-5 r: hrrpv
5-8 g: gggggggg
5-8 f: fjsfftfs
9-12 p: ppfpnxpvppfspp
14-19 x: lrxxxtxxxxxxxzxxxxx
4-6 b: pqbqbbx
10-12 x: mlxkxxxzctrkz
2-7 b: tmbzmsb
16-19 k: kkkdkkkkkkkmklhkkkkk
4-11 h: lpnhfccshxhg
4-5 n: nsnhgnk
1-7 j: jjjjjwsjd
9-12 s: snsssssskssss
7-8 w: wwlwwwhww
3-12 h: znhvqgfgjvlh
9-11 d: dddfddddddg
2-5 j: jjkkrndpdmscjfwvx
1-10 v: vfgbvzlwvvcc
6-15 q: mcqqqqbqcgltqqjz
5-9 q: qprqvzkqsqqt
4-6 l: kldtxl
6-14 j: jjjjjjjjjjjjjjjj
3-6 m: mmmjwwsm
6-15 p: pffpppppdqpfppbpppk
12-14 s: sssssssssssssz
7-13 b: xmbblmsksbbbwbb
4-5 q: dfqfmtqjcvqrq
3-5 l: kvrll
2-4 w: wsww
8-10 f: bfffzfpcfjhw
9-10 c: ccccjcccckc
11-14 q: vqqqpqtqqqlqqqqqxsft
2-4 l: xrzlkmcfl
7-17 c: cccccsccccccccccg
6-8 z: jzzljvmzzvzzgvzz
5-10 w: fwwwwxwmqwz
10-12 d: dddddddddmddd
1-2 k: lzptzkccbmnpqpc
3-5 j: bjmzzjt
4-10 q: qrjtfzgqdt
8-14 m: mmmmmmsmmmmmmm
12-13 b: bbbbbbbbbbbrz
2-4 p: vppzp
4-8 q: tqqqnvhqprdqrqd
6-8 r: gcrwjcrq
9-13 p: pgppvppppppsp
8-10 n: npnngnndvndn
3-9 h: hwmkhhhnnh
4-12 l: lnllwtrsctgl
3-4 b: bpbbkqddb
1-3 d: dbdsfhnzp
9-10 l: lllllftlllll
3-5 v: vvvvvv
3-5 p: dpvppp
1-4 z: zzzfz
6-7 q: qqqqqcq
4-6 p: pcppppbbfrcfbp
3-8 x: qqxfbxjtmqk
4-5 m: tmmmrmm
9-10 h: hhshhhhhhhhhhh
3-4 b: dbbvbx
2-5 s: sspzssckbzrjjsbbw
5-11 w: wbbzkwnnbpggqprbmzg
5-10 d: dddxdddddtdgdsdd
9-13 p: pnkrpxcspctmwphsh
17-18 b: bbbbbbbhbbbbbbqbbqb
1-3 r: blfcfnrrqkfh
2-5 j: jvjsjj
8-15 x: fxvxkxxxxvxxlxzxb
4-10 k: kkkktkkkkpkkkk
4-5 j: sjjjj
4-6 b: mbbtbb
2-12 p: ppfspvgmvzzpcf
4-5 h: crzbh
13-17 d: qdddddddddddddkdd
6-7 n: pnfzhbg
9-11 x: xpxxxtfhbxxxxt
5-7 d: ddzdxdw
12-18 j: zjlsrtflbpjjljfjjh
2-4 l: qclk
7-8 w: wwwgwwrw
4-5 q: qqqwq
3-6 z: fczcjzpsdddqmbqkz
7-8 z: mkhzjzzl
2-3 k: kdkp
11-12 d: qdqddxdwdbdddddddktw
13-16 w: wwwwcwwwwwwmwwwwpw
6-7 s: sxsjstsss
15-16 c: cccccwccccccccvc
13-14 v: xvdtvghjvkvmvbvvx
5-6 g: gggggpg
6-7 l: lllllzljl
4-10 z: nkczdqzhfz
2-10 x: xlxxxxxfxx
1-7 t: jttglvttttm
7-8 k: hkkkrkkk
9-12 n: wrnnnnnnpnnnnn
3-4 l: llgk
6-7 h: vhzhhghh
8-9 h: hhmhhhhjhmhz
3-4 m: gmrsmm
12-14 s: ssstxhsssssssjnsssf
10-19 l: lllllllllllllllllll
14-16 m: mmcmmmmmmmmmmqmm
11-12 p: fppppptppppqpp
7-16 s: ssssdssssssssssh
2-6 c: zcxcpm
5-10 h: hhhrhjjhhhhnhhhwl
14-15 x: xxxxxxxxxxnxxtxtx
3-8 f: fpffpfkzff
3-7 x: xxxxkxkx
8-9 n: nnnnnnnnnn
6-9 c: pccccqcccc
7-13 s: sssspsrsssssfss
3-6 q: qqqqqq
5-6 d: ddddfz
4-5 p: gpqppdbpcptfpczlpcbm
2-4 b: xbtbjmmxrbfbwbxb
1-7 w: vwwwwwx
9-20 w: wwwwwwwwwwwwwwwwwwww
4-6 d: cdwtdddwtqs
8-15 r: rrlrrndprzrrrrklr
4-19 h: rhhhhcxhhctknztthhf
2-11 r: pvchfrzhgcqxsjx
8-12 m: mqfmqmmmpmmmpmkvzsm
2-5 b: fbmnkrxh
4-5 q: qqrlp
3-4 r: kprrr
2-3 q: qzql
8-16 t: ctktlttttcktxqtqht
10-14 z: zzzzzzzzzpzzzzzzzz
9-12 z: zrvjkzzgkzzrzzqzzfm
2-4 c: ccdcp
4-6 z: zpzrzh
7-10 n: wnnlhdpntvsmrnbmps
14-15 v: vbvsvvvnvvvfvvfvvvv
6-10 w: xwwwwvwwww
1-6 n: nnnnnnn
2-12 g: pgmdgpgggsngpwgvjkg
12-13 g: ggggmgmggggggg
4-7 q: vthqqchfn
2-4 q: qpmqq
10-11 j: pjhjjjjjjjjjvj
1-10 l: lgdgqqgvmnscl
12-13 l: rlmnkmnltzlmlq
4-9 l: lllllgllh
10-16 v: xjjvvvdvvvvvvvvvvvv
1-6 x: glxzxfcxglrcwrwcgl
2-4 t: tttntd
9-16 w: wwwhmwwwwwwmwwwxww
9-11 m: mnmsmmmmmmmm
8-16 h: pnrsxhrhhjlqchnh
9-15 c: cxwmcpnjtrccrcn
8-9 s: rsssnsshnsksd
2-6 s: cfklcdd
6-9 m: qmmmmmmvxmwm
3-6 c: cwctccshc
3-4 x: xpkxffbfkzvjrxb
4-5 r: rrrnrr
10-12 j: jjjjjjbjjkjj
3-17 d: sndddlgljdjckpbldb
5-6 x: wzrxxgxwvdfxnq
7-9 l: hhlflqhxknlnbllkl
8-11 m: wmhmmmmnmmmmm
13-14 k: kknkfkkkhzkkkkkxkkk
2-4 s: skss
2-4 m: mmgtm
2-8 r: qrrdpppvgrrcrrvs
12-16 d: dddddddddrdddddczd
19-20 x: xxxxxxxxcxxxxxxxxxxl
7-10 b: bcfpbmlqnrpcnx
1-14 d: fdpddhdrddqdddqdd
5-7 d: ddddxdvdd
11-18 j: fjxjjjjjjjkmjjjjjgjj
3-4 t: zjtp
2-4 r: rrrdr
9-11 b: bbbbbqbjqgbbbbbhbjq
6-7 f: ffbfffgf
4-5 x: xxxqf
1-7 c: jcnbqbcwcc
13-15 q: qqwqqqqqqqgqrqj
13-14 h: kxkjzplvmhrrhl
6-10 j: jjjjjtjjjmj
4-8 v: vvvnvmvrhb
1-12 k: kkkdrkqhkkdkkhdk
2-5 n: lnfjb
10-12 q: qqqqqqcfqlqqqq
1-16 s: ssssssssssssssscs
12-14 l: nlllsllltllcllll
4-5 p: ppppcxwngtcgkjmpb
16-17 h: hhhhhhlhhhhhhhhnhh
3-4 x: xxxx
3-4 f: ffhff
5-6 t: tntthtth
15-18 f: jffffffnffffffffff
14-18 z: zzzzzszzzzzgmszzzzzz
3-4 n: nfnnnn
1-8 q: bmfhqhqqqqmqqqdz
4-7 q: kqqhtqqjqkqqrxvjzqc
4-5 j: jsjjjjj
12-18 v: vvvvvvvvvvvsvvvvvnv
2-10 f: nfffffffmmhn
1-7 z: zzzxzczzc
1-8 l: jpflllcllqdllckwvrb
7-10 x: xxxxxxxxxz
3-6 t: stftpt
1-5 t: tttzt
2-4 g: gggsgggggggwg
4-7 l: xlllvvlmrlrqfzx
8-11 q: qqqqqqzrqqq
1-9 f: ffcltnxdrdnfnk
1-13 f: ffffffffffffhfffff
13-18 g: gsggggggggggtggggg
6-12 c: xrcrcccccxckgcch
2-9 f: pfcdmnfzjdqjnl
4-15 r: wxrlrfrrgrrbrdvrr
8-9 l: llllllllxlll
1-2 d: dpdddd
4-6 w: wwwpwdnww
1-3 s: vhkzssg
10-13 x: xxxxxxxxxxxxxx
1-7 n: nnnnnnjnn
3-8 x: xvxxnxzx
12-13 l: lllllllllllll
15-17 l: lllzllllllllllklll
10-14 m: hmmmmmmmmmmmmm
2-9 m: mmmvmsntmmmn
6-8 z: zzzzzqzz
1-4 h: gqlhh
2-5 q: wqksgtqxgqgdhgqwcq
17-19 q: qpqqqqqqqqqqqqqqhqq
1-4 z: jzzzz
2-5 z: gznrz
1-5 j: wjjjjj
4-5 h: hhmglhh
2-12 w: nhqwwwtwdbwwmwwwzhw
10-13 x: xxxxxxgxxlrxmtxxpm
7-15 w: ktwhswwhwwwhsqwfw
1-3 h: hnwthhcd
2-5 c: rdcvh
10-13 x: fwxqxxzxnxtbx
3-10 m: dmjmzmqmhbml
8-15 s: wcsswxxbrsdsrpss
4-5 c: cjccvc
9-10 z: zzzzzzzzzz
2-3 h: hhhz
6-7 w: wwgzsjwwvwlgww
3-8 g: gtxgggggcgfg
2-3 m: gmmrsgkmsvslw
10-11 x: xmxxxxxxxmxx
2-17 r: bcrtchxrgrqvrqgnm
7-18 r: rrrxrrrrzfrjrwrrrrmk
7-11 z: zzzwzzwzzzzrz
2-5 j: jmrjj
7-11 g: gkgggqgglmggnggqglqg
2-5 l: rlbkllxctprqflhll
4-13 p: mppprjpnxhrzpbp
14-16 p: pkppppzpppppjppg
13-15 n: jdndnxnnhntnnndsnn
1-2 m: pqmm
4-13 j: jjwjfmmjjjjjjpg
3-4 j: nfht
7-11 f: vfffffzffcff
10-12 p: pppppppppjpj
3-4 b: bbbb
5-9 p: ppqppppppppt
5-7 g: ggggggvg
11-14 z: zvzzfzzzqzkzzzzzzzf
2-5 c: hcgpjqjkpvgcxxrf
9-11 v: vvkvvcfqqvvffgvvvvs
8-9 d: rldntbdcz
15-19 p: ppppppppnpppppppgppp
7-8 w: wwwzwpwzmkxcwwtgw
4-8 z: zzrzzfdzk
8-9 g: gggggggqn
1-7 c: czcccngw
3-12 t: btdtgfclmpttqttctstt
2-3 n: jjglbnnzrjgd
7-10 h: hmhhpxhhhhh
4-6 v: vvvvnv
9-11 m: mmdbmmmqgmrh
2-3 r: rjrrrrrrrl
1-5 q: qjjqfzfq
4-5 z: zbzzc
9-12 c: ccccccccqccc
6-8 d: kdfkdtrv
4-12 r: rrrzrrrrrrrmrrrrr
1-5 h: hhhhxh
9-10 t: cztttttttttttt
15-17 j: jjjjjjrjcjvjfjjjcjdj
4-5 t: tftvt
2-4 d: qddvrp
7-13 p: pdrspdzpcxdcpzzxpwtg
12-13 l: llllllljllllll
13-14 s: sssssssssssssn
5-7 f: lnfsffrfg
2-8 r: krtrhgqnn
3-5 j: jxjjjnflwcjj
6-7 r: rrrrrrmrxrr
8-9 t: tsttqcctx
4-5 v: vvvvcv
10-17 j: jjjjcjjjjwjjjjjjkzj
15-16 t: nttttsttttzttttt
5-7 c: cccclccc
3-4 x: kxkx
4-9 l: zslllldlnql
13-18 f: fffmflfffffhdffffwf
8-10 m: mvmmmmhmmvmh
4-6 j: jsjjjmfs
11-13 h: hfnhhhhhhhthhh
5-13 g: gsqgcgqggfggl
7-8 p: ppjqppppp
11-12 b: tbbbbbbbbbbdb
1-4 q: qqqzq
8-9 s: xssssssns
6-9 p: pppppppppp
3-8 j: jvjjjjjjrjj
6-17 b: bbbbblbfbvbxbbbbbt
3-7 j: jjgjmhjjj
4-6 v: njvgsq
17-18 h: hhhhhhhhvhhhhhlhshhh
8-9 m: mmmmmmjdbm
2-11 x: xxxjdgxpxxwxtvkxxxlm
9-16 n: nnnnnnnnnnnnnnnsnn
17-19 w: wwbwwwwwwwwwtwwwwwww
7-8 n: qwbxqsbmpnj
5-6 j: jjjjqjjjjj
2-4 s: fssg
5-12 l: dgnzdllptvvlx
7-12 x: xwxxxxgxxtxbkx
6-12 x: xkmxzgxlnnxq
2-6 h: vnshjh
2-5 x: dxxqxpvsm
13-14 p: pppppppptpppjp
7-8 h: hthhhxhph
5-12 j: jtjrjcnjjjjxjjjj
1-5 j: jfjjwjj
5-6 q: qqqqqq
6-8 t: ttnttvttt
3-5 n: gksnnn
6-9 j: jjjjjljjj
3-4 d: dbdh
1-5 n: hjhfhrgbcnqn
10-13 l: llwllllllllll
2-3 s: dqss
1-3 l: lwqbqdml
10-11 r: rrvdcgrrwhrpsrzjtrl
1-2 d: bcdd
10-11 v: vvvvvvvvvcq
5-15 z: qcgsnhcrzzdfzpp
1-15 w: cfwzjwcgpwwwwwgwxw
11-12 t: gttfknrmtkbwt
2-4 h: blhhhcgfgmh
5-7 v: vjczvqsjzvpjvplhtdvl
1-2 d: tdjdb
5-6 m: mmzmzg
3-8 n: vwjfpdrn
2-9 c: ccccccccm
8-14 w: jxmpsswkhdpqrw
5-6 q: qqrfcj
7-13 g: hgwgqgrkgwggxggmqq
3-5 h: hnhhvhpjsh
1-12 k: hkkmkkkpkkjk
5-6 m: mmcmfm
12-13 w: wwwwwwwwwwwxw
8-10 q: qwbsdnqqlznvqjqqzqqv
5-7 j: jgjfjwmqmtsszf
4-5 c: cctcmc
18-19 v: vvvvvvvvvvvcvgvvvfq
1-8 j: qjbsjsjghj
14-18 b: bbbbbbbbbbbbbbbbbg
9-15 w: wwwwwvwwhwwnwwcwvw
6-9 d: ckvddldddp
3-12 k: qrnchpsjfcckrjx
6-10 c: ccccctccccc
5-6 z: hzzzzzsz
3-5 l: rvwlf
18-20 r: rrrrrrrrrrrrrrrrbhrf
3-4 c: cccvcc
11-17 s: jssssgszsbtsssslss
5-14 k: kkksxkkkxkxknkkkk
1-3 q: qxgsmqxdgx
12-13 q: qqnbqqqqqqhbqqqq
7-13 s: ksrskrslsjfss
3-8 n: nfnnnndsnnnnxs
4-8 g: lglggflgglgnf
6-14 b: bbdkbbmbgbbrlb
3-7 w: wqwrdpw
5-6 j: mdmjjj
13-16 k: kkkkkxkkkkkkqkdk
4-6 h: jmthbwhhfh
16-19 p: ppppppppppppppppppv
15-16 k: fkzkkkkkpkcrkhkklbkr
10-11 k: sjkkgkhkqfk
12-15 l: jjnlvmsppvlglllvljb
3-13 l: llcdlfllqllqjl
3-7 f: ggfgbvfqlrffxrflchx
13-14 d: ddddddddddcddqd
7-18 d: wdjdtdrdddfndkdddddd
8-10 v: rvvzvvvrvb
9-13 n: rlnnnnlnmbnqwlnmlnn
14-15 h: hwrhcmhwbjhcbhc
6-13 t: ttwtkrrtttdbtt
3-5 w: wkwww
1-6 h: fghcxhwldmnb
1-9 f: ffffffffffffff
10-11 k: kkkkkkkkkkvkkkk
2-3 s: sssw
3-6 v: vzvqmdgrnkvcvz
3-4 j: jztw
4-5 b: bbbbb
1-9 l: wllmxlbxfllllcr
14-15 q: pqgqqngpjzhmmqq
4-7 n: jnznczd
2-8 m: cmpmcmshpbmxb
6-9 r: rrrrrhrrr
15-18 t: ttttktmtttttttvtttt
1-5 s: sssxf
9-17 f: zfmkpffpwqfqffffffh
16-19 d: dddddvddddbdddkdddpd
8-10 w: dwwrpwwwxx
6-11 w: wmdmzzcwwpkkwwwqwnww
4-5 s: zssgf
2-8 v: vvpvvvvvqjv
17-18 s: sssssssssssssvsssj
1-3 d: tddd
1-3 s: tssdbfvnlmtspmwlxxl
6-11 k: kkkkkkkkkkkk
1-5 d: dddddgqddmdkdk
6-11 l: nzgwkmqlpnl
2-6 v: kvzlqgzr
1-2 f: xkqzbcrsdswpf
14-15 x: xxxxxxxxxxxxxwx
16-17 j: jjjvhgjzjwjzjmjnj
5-6 p: ppvppcjp
1-4 w: lwpwwh
15-16 s: ssscsssssssssssd
3-7 b: rpqkbbbb
3-6 d: dddddf
10-15 k: kkckzkbpdfkkckl
2-4 v: wvrvkgfpvvm
15-18 v: vvvmvvvvvvvvvvgvvl
1-2 l: hdfll
1-4 v: wtvd
5-6 v: vvvvzmv
6-8 l: llnllmlns
4-5 b: bbkblbsbnbbbbbbgbbbb
5-6 d: xnjmdwddtfdbzdb
4-10 q: qqlqqqqqhq
4-9 c: rcvctlmccccc
3-5 f: fffmnf
9-14 n: xnznnnnnrnrdlzfsn
6-7 w: wdwkrvwww
10-15 v: vvvvvvvvvnvvvvz
10-11 k: hnjzdwqkmskkx
4-8 c: ccqcqfrcnffbncfkc
5-12 c: cclsmccgcccccxnvcckc
5-6 z: cwhbkskzhnzztzzlhz
3-5 v: vkvjvv
3-4 j: jjjj
13-16 h: khxhhhrhkhhhhhhhwhhh
1-3 f: jxdxffjfprs
1-11 l: gllslllllxqlltlmh
8-11 g: kggggvnbkqgbfbgdsgwg
6-7 z: zzzxzfz
3-7 x: xqxjjxxlb
3-4 v: vtdv
7-10 w: wwwwwwwwnww
4-8 w: kgwwwwwwpx
3-5 g: ggggggs
4-8 w: gwwwgzxb
9-10 t: ttttttttmp
3-8 f: fpjdffffzflffmlxfq
11-13 g: gggtgggsggbbzggg
1-5 p: pptcp
13-14 c: cccccccccccccnc
3-13 n: gbjnnqxnjprnhn
5-6 x: qxxdknx
8-9 q: kmlfqxcvqqsqkvtm
3-6 n: xndnvn
6-7 s: scxccsjssstw
14-18 d: dddddddttddddfpddbd
18-20 d: sgljbkdxhvckddpbjdld
5-8 m: dpmnmfmmpm
6-9 w: rfdwwwplw
5-7 b: vbdrcbbgqbspbbv
18-19 b: bbbjbbbbbbbbbbbbbsb
11-12 x: xxxxxxxxxxzjx
6-8 d: dqhgrddhddxdn
6-16 p: dppbbzbpxxpphjppkpp
3-4 k: khkkt
1-2 x: xpwkvcxxqrn
1-4 n: lnnngnnnns
1-11 c: cczvdcgcpcrccpzw
15-17 h: hhhhhhzhhhxhhhshhhh
7-8 t: fttttttt
5-19 z: zczzczmczwzpzblzvxzz
4-8 l: zlpdjnsllkgkjglmnll
9-12 s: spwssjsssdstjssf
8-10 h: hhhhfhhchh
4-11 q: qqqqsqqqqqdqqqq
14-15 w: wwwqwwwwwwwwwmjww
1-2 b: blcbhdqfsbmnq
1-5 m: mlrdhdkfjnknxlw
8-9 r: rrrrrrlhc
9-13 d: ddddddddddddd
2-3 p: tpxpjgpcf
1-2 f: ffff
5-8 k: cdkkgbvfwkkskkw
2-3 r: rrrp
6-10 b: bbbbbdbbbbbbbbbbb
10-12 t: tttttttttgdxt
3-4 k: kjkrkmcmvr
8-10 b: zbbpcwgbsbwdz
2-10 v: zqvdtnxvvcvlrvq
3-4 b: bbbbb
13-16 t: ttttmttttttttttwttt
16-17 n: nbnnnnnnnnnnnnnsgx
8-10 f: fmfsffhjcfzffcxw
7-13 m: mmvmrlmtzmbtmmxcsmm
8-9 m: mmmmmmmmm
1-7 n: nnnnwnpnnn
6-7 z: xzzzhpz
3-4 n: bnnn
5-17 r: rrlrrbwzmkrrhrrrrhnr
9-13 t: ttntttttttttc
11-12 w: wwwwwwwwwcwsw
1-10 j: ljhjjjdgjmj
9-10 c: cccccccccx
3-5 h: hfhhh
18-19 q: qqqqqqqqqqqqqlqqqbqq
1-4 b: pnjntrscpklzfcdl
9-11 c: nrxscrjjcrzc
9-12 q: nqpqqqqqqqqqqc
5-15 k: phmcmnhbckwkvwkb
2-4 t: dtrtmtb
4-5 j: jjjjp
8-9 m: mmhjmmrsqmm
4-5 r: rrsrrrr
6-10 w: wwwwwgwwww
13-18 m: mgmmvmmmkmmmmmgpmfm
10-11 d: ddxdldwdddddzdvrd
3-15 k: mxxgjklzzdbtgddzwrx
9-11 q: qqqqfgqqqqwqqq
2-4 g: gdhthpp
1-11 r: srrrrrrrrrrr
13-14 x: xxxxxxxxxxxxxs
6-17 f: ffvffkffffffffffjf
3-12 m: kmmmvbjlmmmf
9-20 n: nnnplnnnnnnnnnlpjntn
8-14 f: cjflffftftnffd
2-7 b: kbzbbbbbbqb
10-12 n: nnnnnnnnnnnk
7-8 z: zxzdzzzclnjzj
3-11 l: llldlsmltklz
2-5 s: swwxrpscmmhzsgrvnl
1-13 p: kzwjlpfhpskzpsrp
13-15 f: gffffdffkhfffvffjffb
6-7 d: drddddd
4-6 p: pppphpj
12-18 k: jkkkkkkktkzkkxkkfgkn
8-9 j: jjjjjjjpc
5-7 d: ddlkxdmndmdkkhwd
10-11 l: vlllhllfhll
5-6 b: bbjbvbqrjb
17-18 d: dxdnddddddlddddddl
15-18 d: dddxddwwddddddnddd
1-12 x: sxxxxxxxxxxtxxxxx
3-9 k: rfkrnjxxkkm
9-12 n: xnnnnnnggnnln
5-8 w: nwpwqwwwlfwmj
3-11 p: sgprfdprpmqpwvps
5-6 x: sxxhxxkx
11-14 h: hhhhhchhhhhhhh
2-3 p: kxpllmpvfxq
4-14 k: qkpfkskhglhkzkck
3-6 q: jsqbdqq
8-9 n: nnnxnnnnpnnn
12-14 h: stshhhwxhcvhhg
5-8 j: jjjjjjjj
10-14 h: hqlqhxzmdnfzhhhwxnwj
1-8 r: qmlvfqvrbgfrrmppkzwv
3-9 v: hhvnpvvvdvktgbcrr
6-8 q: qqqqqqqp
9-12 l: lxklkwplllvlmljlfll
11-14 w: wwwwwwwwwwwwwpw
6-7 c: cccqrccc
3-6 d: wddgdzd
3-8 d: dddppddddddddfd
5-9 g: jlxgxgkggpg
6-14 b: jbljlvjtqkbbzlpvxmf
2-3 x: nnbx
6-7 q: qqqqqbfqqqq
2-3 n: xnmnnfb
13-14 p: pppppppppppphr
8-11 k: kkkkkkkkkkk
4-5 r: rrrsr
13-19 t: ttttttvtttmttttttbt
8-9 r: rrrlrrrwr
3-6 c: flfhnccccwvtmqz
8-12 s: xshssnnsskcsjsssgs
1-4 r: vzkpphvtwrxgr
11-13 c: ccccccccccqcc
3-5 v: fvvjvzgt
1-4 j: sjjnsjjj
3-6 s: sxsqnfbmssbfnjs
12-15 p: pnppppppppppkpp
9-13 l: wlldrllklllllkl
2-3 s: swsrljzrns
8-9 b: bbbbbbrwb
16-20 f: ffffffhffffffffsffff
5-9 w: wwwwswwwww
7-9 q: qbqqqtqqkd
6-8 z: zzzzzzzz
5-10 m: zlmmnmrgkmtm
1-5 n: mnnflnn
4-8 c: cpccbgccc
9-12 j: jjjjjjjjwjjjj
3-4 s: tdhzbsqsb
15-19 t: tthrqtttttttmtttttx
11-12 b: bbbbbbbbmbjcb
1-13 f: ffqfkfftfjrwfkfm
14-15 v: vvvvvvmvvvvvvdv
4-6 h: qvchkhhccnxwpvhhhb
2-8 k: kskkkxkkkkk
3-10 j: jjjbjjjjjpd
4-13 z: svkjzrfrtftftqhhc
18-19 p: pppppppppppmpppppmd
5-14 b: bbbbcbbntbbfbpbd
5-7 q: qqqqqqq
2-17 j: jbjjjjjjjjjjjjjjcj
1-5 z: zvztgv
4-5 k: kkkrkp
3-5 c: kgmccc
2-8 h: rhhhnhhxh
1-18 s: sbrblpcrxsvdsjrnwwws
6-10 q: qbqqzqqhbdq
1-3 d: sdwgdn
3-6 s: ssssssss
2-13 f: ffffrrfffflbvffff
5-7 w: pxwnfnwzj
17-18 z: zzzzzzzzzzzzzzzzbzzz
7-8 p: pplplpbfppp
1-8 x: xxkzdxzx
3-4 p: jppxp
4-6 j: jthbzjmqjzj
1-12 x: xxxxxxxxxxxxxx
8-19 g: ggggggqgwmgggwggmlg
5-9 b: bxbbbgwbbnxbhbbb
5-6 n: nnnnnd
5-9 b: bwjxbbwbb
4-14 d: ddlddkdddddddl
2-3 t: jqjt
2-3 h: shhp
12-14 p: ppppppxppjfmpdzppp
7-10 f: lnffvfcfzffffft
3-8 s: lqhrstvsr
15-16 v: vvvvvvmvvvvvvvvvv
2-4 h: hhhh
5-8 g: wmtxgdgg
3-6 r: rfrrrg
8-12 q: qqqqqqqqqqqq
4-9 z: zzzzzpzzw
14-19 g: gdggggggggbggtcggggg
5-11 n: nnnktnnlndgnnnnn
5-6 n: nznnnqn
3-4 q: qqlq
12-13 g: ggggggggggggg
16-18 w: wwwwwwwwwwwwmwwxwv
6-10 b: bbbbbmblbg
8-13 m: mwmmmcrmmmtsm
12-17 h: rhhhhnhhhhhlhstkhhh
9-10 q: qqqqqzqqgt
2-6 v: vvfvpgw
8-13 w: mwlxrpbwwwgcwwgn
1-10 m: mmmmmmmrmxm
6-8 f: fgvfgfftfffq
2-6 g: gcggrg
1-6 x: zxxxvxx
1-3 t: txtt
1-2 q: qdqn
6-7 j: jjjjtjjj
13-14 r: rrwrrwrrrrrrrfrr
3-4 j: jjjpj
12-13 v: vvvvvvvvvvvvv
4-5 t: tttcw
4-6 s: sssnxs
9-11 x: xxxxxxxxcvx
1-4 d: lpddds
1-9 t: hbtttttthtt
1-4 z: bsjzz
2-5 t: xrtptqt
1-3 l: lllll
7-8 m: mmmmmmmj
11-13 f: ftffqffffgfszfff
4-5 j: ljjbjbjjjj
3-11 n: nhnnnnnnjnnnnnbmnqnn
3-12 s: swgnlssszsqsvfjwxt
8-9 f: ffffffffn
3-4 t: gtmt
8-9 s: spsmnswlt
7-8 j: jjjnmjjjdjjjqj
9-10 j: jnjljjjjfgj
3-7 x: xrxlbhcxmswlpx
9-11 x: xxwrxxbxxxn
16-17 d: dbddddmtddddddddddd
5-17 n: cnnnhnnnjnnvnsnnwgnn
7-8 m: mmmmmmmm
11-12 l: lllklllltltmllllll
4-5 r: rrrrr
7-8 j: jjjjjjqqjj
10-12 g: gggtkggggggkggg
1-5 h: fxxphhz
1-3 q: jlnq
4-5 s: fssss
16-17 c: cccccccccccccccqc
12-19 q: qqqqqqqqqqpqqqqqqqpq
7-13 s: gmzvssjsfssjssssx
3-4 s: ssxs
15-19 d: ddddddddddtddddddqdd
5-7 l: lllxqlkl
10-11 x: xmxxxxxxxfk
9-14 q: qqqqqtqczqqqqq
4-8 w: zwmllrwmwmwqwww
1-4 l: llllz
14-15 j: jjjjjjjjjjcjjjrjj
10-13 x: xxxxxxxxhbxlzx
6-7 f: fffffdj
9-10 w: msdcwqzwhj
4-8 c: ccccxccccckcccccccc
5-11 r: xffrjsvrjzfrrcrpfbr
2-5 z: zzfwrn
10-13 r: rrrrrfrrrhrrh
5-10 d: dddddddddddd
4-5 z: zzzfs
9-12 t: ttttttttlttt
3-4 r: lpjrr
2-9 v: kkxvvxkvgjtsjtvv
1-8 v: lprgtpvvv
4-6 h: hhhnhfb
2-4 h: hhpxh
4-9 d: bhqdmddrd
2-5 w: wwgtwt
6-7 z: zzzzzszz
4-5 z: zzzzm
12-14 d: mddrddddddrdddddd
9-11 h: sdhzhvhhhkhhhb
2-3 b: zbbtbbqhm
4-11 b: bnbqqbjbbzp
9-10 n: nnnnnmnntj
11-17 w: wwvwwwwwwwrtwwwwdw
1-4 t: svbtbxvptfp
4-5 w: vsbjw
2-7 m: mmpmmmg
11-12 j: jjjjjjjfjjxjjm
6-8 r: rrzrcmrvrr
1-3 n: nqxnzhq
3-4 n: nnnkj
3-5 f: kfffhfthfhf
3-5 m: gwszmmm
1-7 c: tbscmrfbmccrqxzdb
13-14 l: lllllllllllllnll
4-10 k: pfbwsjvfxkxhfzktdj
2-6 f: ffffbf
4-7 w: wwgrwnpbswnz
5-6 z: zzszzzz
8-13 p: zpppppgbjpppcpp
6-7 q: gpqqvwtkxwqjtqdqq
14-15 n: nnnnnnnnnnnnnkn
3-6 q: rkqmjqg
5-6 t: ttttkq
4-6 r: srrsrrprr
1-8 v: kvvvvvvxvvvvvvvb
5-6 z: zzzzzz
3-4 c: cccccbpsp
3-12 c: stvxclcbrcjjcgcxlwtq
13-14 r: nrrrrxrfrrrrrzd
2-3 r: rmfwl
1-4 q: qqhq
11-13 z: zzzmvzzzzzkzzzzzzzz
4-8 h: hhhxhhhh
2-3 b: fpbhn
7-10 v: vgwvvvgvvvvvj
1-4 m: msmk
11-12 d: ddddddddfddddd
15-16 k: kkkkkkkkkkkkkkkk
8-14 m: mmmmmmmwmvmbmmv
10-12 m: mmmmmmmmmlmm
2-7 w: cgbmsww
6-8 t: ttktttgw
4-14 z: vsvmwzvhfzxkfzz
2-4 f: ccgmfhrls
10-11 k: kfxlsfdkbdkmjptqhh
6-16 x: nbxxdxwsxxsqmfxqrxmk
9-17 j: vjjjjvpjgfjxffjxjd
6-9 g: gvpxggggqgg
6-8 t: tttttztft
5-11 q: prklqxrfxjdvgsq
8-9 k: kkkkkjknk
2-4 c: chccl
2-3 x: fxpr
1-4 v: rzvvpvxp
3-5 j: cjfrjldr
3-8 t: zbptntzp
2-7 c: cccqkcfzgcffssgrcsc
5-6 q: qqqqdr
2-6 h: hxfhhghhhk
1-3 v: lvnhv
5-6 r: prrrrw
11-18 z: zfzzzzzzzzdgzzzmzzxz
5-10 x: kxrncghxldxffzbx
17-19 k: kkkkkkkkkkkkkkkkjkkk
7-9 h: hhmhhhdhh
15-16 x: xxxxxxxxxxxxxxxx
4-5 c: nzjchwccgbd
5-6 r: rrrrjrrrr
9-13 c: ccccccjclcccc
6-7 z: zjzfzzzszvzz
6-7 l: llllljll
6-8 m: mmmmmmms
3-5 p: pppppp
14-15 m: mmmmmmmmlmmmnwmm
6-11 b: bbbbbbbbbwb
8-10 g: ggjgbgpgggggggdcgb
9-16 b: bbbbbbcbkbbbbbnbbbbb
10-11 f: dfbffxfnfksfffrw
10-11 h: hhhhhhhhhhq
5-17 v: vvvvjvvwvvvvvvvvvvvv
2-14 x: xgxxxvfcxxxxtbgxkx
1-3 k: kkjbm
18-19 d: dddddddddddddddddxx
5-9 h: vhjzhkjbhl
1-4 k: kskk
7-12 l: lcljknlllclvlldrlpls
14-15 w: wwwwhwwwwrhwwvq
5-6 t: wtvdtmqfbnt
1-4 v: vhvvvv
8-10 n: nnqcnzrnndnjnnnkn
6-8 h: hshhqhhdhhfcj
10-15 j: jjtjjjjjjfzjjjj
3-5 m: mmdmm
10-11 n: nnnnnnnnnng
6-8 p: fzpgppzpthqcthhst
1-7 p: hzxthvpfnpnrzfpvmv
10-11 l: llllvswlllll
1-2 q: jffqfzd
1-3 x: xljxfw
5-6 z: fmzzgl
2-6 v: vbvvvzv
8-10 r: rrrrrrrnsr
1-3 c: crctc
8-10 m: mcmdgxhmhnmmwmzmmg
4-5 h: hdhhhh
1-2 z: vzzm
5-10 z: zzzvnzzzpz
2-5 f: gfffdff
1-4 g: lgfgg
2-4 w: swww
2-6 c: ccscdz
6-7 b: bbsbbbjb
11-16 s: bssrqsslssbcssjrxjk
5-8 c: ccjmcqcglj
13-18 l: lllllmvllllxlllllz
6-7 l: lllllll
5-6 v: vvvtvvvv
4-11 v: vvmvwhvvrkd
4-7 n: knlwnmnnnn
5-6 p: cqmfxppptplkpp
7-11 c: clccnptxmcncrccjcc
1-7 h: fhhfhhzd
1-11 l: llflllllllllll
3-4 g: gmgl
15-16 j: wjjjjjjjjjjjjlhjcjj
2-8 v: gtvvmgvvbtf
3-4 t: fpttgzttwt
4-8 k: klkkkgkkkk
2-8 p: wsdgtplp
9-11 q: qqqqqqqqzqv
1-2 n: nswlnnngxsj
4-5 p: dgpppkjhvgpgppp
10-17 j: jjjjjjjjjfjjjjjjk
2-3 l: lbll
6-7 n: nhwnnnc
3-4 s: ssws
3-9 v: szrvvcxzv
2-4 p: pgzph
4-6 g: rxnjtpggwggglp
10-16 v: vvvvvvvvvvvvvvvjvv
7-9 j: jljjjmjjj
6-11 w: wwwwwqwgmwfwwkw
12-15 w: wqwwwwtwwxwwwfwww
8-11 v: vvvvvvvvvvd
7-11 g: dcgpcggpgxggdphgm
3-5 w: wwrwg
9-16 b: bbbqbbbbbbbbbbbbb
7-8 n: tnnnnnnnnn
3-5 c: ccsctcm
10-17 f: rfsfffffvffjfnkfq
6-11 f: fffhffffffp
10-11 n: hbsnnnntnppdnnzj
3-4 x: ngxbxxx
6-11 t: ttbwkznllhtntbdtltt
5-6 s: sssssms
15-16 c: ccccccccccccccqc
3-5 h: jzslhlhh
7-12 m: mxmjmjmmmmhkm
7-9 r: mtbfxlrvrddrvgxrxxr
14-20 m: gmmlpvclmkvfkmjdslvm
11-17 v: rqvvtmktpvckpvvvv
15-16 b: bbbbbbbbbbbbjblbbc
3-5 z: vpsgzfzvxczbnzw
5-6 j: shlfjc
10-16 b: bbbbbbbbbbbbbbbsn
1-7 j: jjjrkrdq
14-16 x: xbxxxxxxxxxxxjxxx
2-6 b: vzpnbbpqfbbvcbmbchm
10-16 x: xxxrxxxvxxxxxqxxxxk
10-12 j: jjrkjjjjjjjjj
1-5 l: lxfslmj
10-16 s: ssssssssssssssszsss
12-15 r: rrgrrrrrrrrcrrr
10-11 c: ccctccccccj
13-14 f: fqgsffffqffffvfffff
14-15 f: ffffffjffffffqff
8-14 q: gtqqjqqwwxqvprdqpcqq
8-11 f: lqqfqpmffffgcs
6-8 f: frfshkfklf
10-11 w: wlwwwwwwwwrw
2-5 q: qqmmqmmqqq
8-9 g: cjgscgwtg
1-3 w: wljwwvjdcwnkmn
4-5 q: qcqqxq
11-18 g: gqgggvgggghgkggggggg
8-12 z: tbmbzbzhnppz
2-3 t: tzttt
2-5 s: zjlsssssmsss
8-16 w: mwwqwrwwskwcwwbww
3-7 t: ttwttttt
1-4 p: ppclpbpppp
7-9 c: cccccckcxccccc
9-13 g: dgggggcgrrggggggg
4-5 v: vvvvvvvvvvvvvv
15-16 l: lllllllllnlllsqkl
2-6 p: pppjptvpkxp
11-18 j: jjjjjjjjrjcjgjkjjhjj
2-6 x: znkxkc
14-15 b: bbbbbbbbtbbbbssbt
3-8 b: bszbbvbb
15-16 t: dtttttttxtpttttrttt
10-11 b: bwbkqbvdbvj
14-17 k: krjwkfgsqkzjklkkkvxg
13-16 d: ddddddddddddqddd
3-15 s: jmsnpmldstjngfmrp
1-6 s: stssssn
8-12 b: bbbbbthpwlbb
3-4 r: rdrf
10-11 l: glllllllllk
7-16 m: vxjgnbmmbzsxlhblj
4-7 b: bsthbwjrkbmptb
5-7 q: qqdmjqqqq
2-16 v: rvvvvvvvvvrvvvvvvvv
2-3 n: nnnbm
13-16 v: vvvvlvvvvvvxwvvv
4-6 c: nccccccs
10-14 q: qdgsqqqqqqqqqqqnq
4-5 g: gjghg
2-7 f: fffffqdf
15-18 f: fxffffdfhflffbfxff
7-9 w: gpwwcwwwlwbwfkdw
14-17 q: qqjqqqqqqqqnqhqqrhqq
1-4 d: djdqkdkddlvdqdt
4-9 w: qwsvpbwdcngsww
4-9 b: bbbbbbbbb
6-15 g: gmdhggngqdfgqsggsvg
9-16 b: bbbbbbbbdmtbbdbbc
8-9 k: kkxkkkdkkkzkdp
1-8 b: bbxbdbnbjcbbb
15-19 q: qqqqqqvqqqqqqsqqqqq
3-4 t: tttt
2-5 j: bjjjj"""

    password = password.replace(" ", "").split("\n")

    valid = 0

    for set in password:
        count = 0
        policy = set.split(":")[0]
        lowest = int(policy.split("-")[0])
        require = policy.split("-")[1][-1]
        highest = int(policy.split("-")[1].replace(require, ""))
        result = set.split(":")[1]
        for i in result:
            if i == require:
                count += 1
        if count >= lowest and count <= highest:
            valid += 1

    print("Question 2 part 1")
    print(valid)

    #Question 2 part 2
    password = """2-5 l: fllxf
4-5 r: rrrjmrrrrrrh
1-4 k: kkksk
7-8 k: tknsqknzkckrwkjkk
2-3 p: mpbstpxmsxmpnhbwlb
2-7 j: xkjjtjjjj
2-7 m: gczbmgk
15-16 q: qqqqqqqqqckqqqfqqq
7-14 d: dgdddlddddddrvfddnsd
7-12 r: rrrrrrrrbrrrl
2-11 p: zppjpwpqppbnppd
6-8 w: wqhwwnpwwwr
4-10 m: fmkmrrrdkmr
1-2 n: nnjvtnzk
3-8 t: tdxmzslxtvft
13-14 m: mmmmmhmmmmmmmm
9-10 l: lljllllllll
12-16 t: vdtbdtxtttttrctttkt
2-6 q: nqghxqgjqvzswbxww
4-6 k: khkkkkvrkgfwvbd
4-5 r: hrrpv
5-8 g: gggggggg
5-8 f: fjsfftfs
9-12 p: ppfpnxpvppfspp
14-19 x: lrxxxtxxxxxxxzxxxxx
4-6 b: pqbqbbx
10-12 x: mlxkxxxzctrkz
2-7 b: tmbzmsb
16-19 k: kkkdkkkkkkkmklhkkkkk
4-11 h: lpnhfccshxhg
4-5 n: nsnhgnk
1-7 j: jjjjjwsjd
9-12 s: snsssssskssss
7-8 w: wwlwwwhww
3-12 h: znhvqgfgjvlh
9-11 d: dddfddddddg
2-5 j: jjkkrndpdmscjfwvx
1-10 v: vfgbvzlwvvcc
6-15 q: mcqqqqbqcgltqqjz
5-9 q: qprqvzkqsqqt
4-6 l: kldtxl
6-14 j: jjjjjjjjjjjjjjjj
3-6 m: mmmjwwsm
6-15 p: pffpppppdqpfppbpppk
12-14 s: sssssssssssssz
7-13 b: xmbblmsksbbbwbb
4-5 q: dfqfmtqjcvqrq
3-5 l: kvrll
2-4 w: wsww
8-10 f: bfffzfpcfjhw
9-10 c: ccccjcccckc
11-14 q: vqqqpqtqqqlqqqqqxsft
2-4 l: xrzlkmcfl
7-17 c: cccccsccccccccccg
6-8 z: jzzljvmzzvzzgvzz
5-10 w: fwwwwxwmqwz
10-12 d: dddddddddmddd
1-2 k: lzptzkccbmnpqpc
3-5 j: bjmzzjt
4-10 q: qrjtfzgqdt
8-14 m: mmmmmmsmmmmmmm
12-13 b: bbbbbbbbbbbrz
2-4 p: vppzp
4-8 q: tqqqnvhqprdqrqd
6-8 r: gcrwjcrq
9-13 p: pgppvppppppsp
8-10 n: npnngnndvndn
3-9 h: hwmkhhhnnh
4-12 l: lnllwtrsctgl
3-4 b: bpbbkqddb
1-3 d: dbdsfhnzp
9-10 l: lllllftlllll
3-5 v: vvvvvv
3-5 p: dpvppp
1-4 z: zzzfz
6-7 q: qqqqqcq
4-6 p: pcppppbbfrcfbp
3-8 x: qqxfbxjtmqk
4-5 m: tmmmrmm
9-10 h: hhshhhhhhhhhhh
3-4 b: dbbvbx
2-5 s: sspzssckbzrjjsbbw
5-11 w: wbbzkwnnbpggqprbmzg
5-10 d: dddxdddddtdgdsdd
9-13 p: pnkrpxcspctmwphsh
17-18 b: bbbbbbbhbbbbbbqbbqb
1-3 r: blfcfnrrqkfh
2-5 j: jvjsjj
8-15 x: fxvxkxxxxvxxlxzxb
4-10 k: kkkktkkkkpkkkk
4-5 j: sjjjj
4-6 b: mbbtbb
2-12 p: ppfspvgmvzzpcf
4-5 h: crzbh
13-17 d: qdddddddddddddkdd
6-7 n: pnfzhbg
9-11 x: xpxxxtfhbxxxxt
5-7 d: ddzdxdw
12-18 j: zjlsrtflbpjjljfjjh
2-4 l: qclk
7-8 w: wwwgwwrw
4-5 q: qqqwq
3-6 z: fczcjzpsdddqmbqkz
7-8 z: mkhzjzzl
2-3 k: kdkp
11-12 d: qdqddxdwdbdddddddktw
13-16 w: wwwwcwwwwwwmwwwwpw
6-7 s: sxsjstsss
15-16 c: cccccwccccccccvc
13-14 v: xvdtvghjvkvmvbvvx
5-6 g: gggggpg
6-7 l: lllllzljl
4-10 z: nkczdqzhfz
2-10 x: xlxxxxxfxx
1-7 t: jttglvttttm
7-8 k: hkkkrkkk
9-12 n: wrnnnnnnpnnnnn
3-4 l: llgk
6-7 h: vhzhhghh
8-9 h: hhmhhhhjhmhz
3-4 m: gmrsmm
12-14 s: ssstxhsssssssjnsssf
10-19 l: lllllllllllllllllll
14-16 m: mmcmmmmmmmmmmqmm
11-12 p: fppppptppppqpp
7-16 s: ssssdssssssssssh
2-6 c: zcxcpm
5-10 h: hhhrhjjhhhhnhhhwl
14-15 x: xxxxxxxxxxnxxtxtx
3-8 f: fpffpfkzff
3-7 x: xxxxkxkx
8-9 n: nnnnnnnnnn
6-9 c: pccccqcccc
7-13 s: sssspsrsssssfss
3-6 q: qqqqqq
5-6 d: ddddfz
4-5 p: gpqppdbpcptfpczlpcbm
2-4 b: xbtbjmmxrbfbwbxb
1-7 w: vwwwwwx
9-20 w: wwwwwwwwwwwwwwwwwwww
4-6 d: cdwtdddwtqs
8-15 r: rrlrrndprzrrrrklr
4-19 h: rhhhhcxhhctknztthhf
2-11 r: pvchfrzhgcqxsjx
8-12 m: mqfmqmmmpmmmpmkvzsm
2-5 b: fbmnkrxh
4-5 q: qqrlp
3-4 r: kprrr
2-3 q: qzql
8-16 t: ctktlttttcktxqtqht
10-14 z: zzzzzzzzzpzzzzzzzz
9-12 z: zrvjkzzgkzzrzzqzzfm
2-4 c: ccdcp
4-6 z: zpzrzh
7-10 n: wnnlhdpntvsmrnbmps
14-15 v: vbvsvvvnvvvfvvfvvvv
6-10 w: xwwwwvwwww
1-6 n: nnnnnnn
2-12 g: pgmdgpgggsngpwgvjkg
12-13 g: ggggmgmggggggg
4-7 q: vthqqchfn
2-4 q: qpmqq
10-11 j: pjhjjjjjjjjjvj
1-10 l: lgdgqqgvmnscl
12-13 l: rlmnkmnltzlmlq
4-9 l: lllllgllh
10-16 v: xjjvvvdvvvvvvvvvvvv
1-6 x: glxzxfcxglrcwrwcgl
2-4 t: tttntd
9-16 w: wwwhmwwwwwwmwwwxww
9-11 m: mnmsmmmmmmmm
8-16 h: pnrsxhrhhjlqchnh
9-15 c: cxwmcpnjtrccrcn
8-9 s: rsssnsshnsksd
2-6 s: cfklcdd
6-9 m: qmmmmmmvxmwm
3-6 c: cwctccshc
3-4 x: xpkxffbfkzvjrxb
4-5 r: rrrnrr
10-12 j: jjjjjjbjjkjj
3-17 d: sndddlgljdjckpbldb
5-6 x: wzrxxgxwvdfxnq
7-9 l: hhlflqhxknlnbllkl
8-11 m: wmhmmmmnmmmmm
13-14 k: kknkfkkkhzkkkkkxkkk
2-4 s: skss
2-4 m: mmgtm
2-8 r: qrrdpppvgrrcrrvs
12-16 d: dddddddddrdddddczd
19-20 x: xxxxxxxxcxxxxxxxxxxl
7-10 b: bcfpbmlqnrpcnx
1-14 d: fdpddhdrddqdddqdd
5-7 d: ddddxdvdd
11-18 j: fjxjjjjjjjkmjjjjjgjj
3-4 t: zjtp
2-4 r: rrrdr
9-11 b: bbbbbqbjqgbbbbbhbjq
6-7 f: ffbfffgf
4-5 x: xxxqf
1-7 c: jcnbqbcwcc
13-15 q: qqwqqqqqqqgqrqj
13-14 h: kxkjzplvmhrrhl
6-10 j: jjjjjtjjjmj
4-8 v: vvvnvmvrhb
1-12 k: kkkdrkqhkkdkkhdk
2-5 n: lnfjb
10-12 q: qqqqqqcfqlqqqq
1-16 s: ssssssssssssssscs
12-14 l: nlllsllltllcllll
4-5 p: ppppcxwngtcgkjmpb
16-17 h: hhhhhhlhhhhhhhhnhh
3-4 x: xxxx
3-4 f: ffhff
5-6 t: tntthtth
15-18 f: jffffffnffffffffff
14-18 z: zzzzzszzzzzgmszzzzzz
3-4 n: nfnnnn
1-8 q: bmfhqhqqqqmqqqdz
4-7 q: kqqhtqqjqkqqrxvjzqc
4-5 j: jsjjjjj
12-18 v: vvvvvvvvvvvsvvvvvnv
2-10 f: nfffffffmmhn
1-7 z: zzzxzczzc
1-8 l: jpflllcllqdllckwvrb
7-10 x: xxxxxxxxxz
3-6 t: stftpt
1-5 t: tttzt
2-4 g: gggsgggggggwg
4-7 l: xlllvvlmrlrqfzx
8-11 q: qqqqqqzrqqq
1-9 f: ffcltnxdrdnfnk
1-13 f: ffffffffffffhfffff
13-18 g: gsggggggggggtggggg
6-12 c: xrcrcccccxckgcch
2-9 f: pfcdmnfzjdqjnl
4-15 r: wxrlrfrrgrrbrdvrr
8-9 l: llllllllxlll
1-2 d: dpdddd
4-6 w: wwwpwdnww
1-3 s: vhkzssg
10-13 x: xxxxxxxxxxxxxx
1-7 n: nnnnnnjnn
3-8 x: xvxxnxzx
12-13 l: lllllllllllll
15-17 l: lllzllllllllllklll
10-14 m: hmmmmmmmmmmmmm
2-9 m: mmmvmsntmmmn
6-8 z: zzzzzqzz
1-4 h: gqlhh
2-5 q: wqksgtqxgqgdhgqwcq
17-19 q: qpqqqqqqqqqqqqqqhqq
1-4 z: jzzzz
2-5 z: gznrz
1-5 j: wjjjjj
4-5 h: hhmglhh
2-12 w: nhqwwwtwdbwwmwwwzhw
10-13 x: xxxxxxgxxlrxmtxxpm
7-15 w: ktwhswwhwwwhsqwfw
1-3 h: hnwthhcd
2-5 c: rdcvh
10-13 x: fwxqxxzxnxtbx
3-10 m: dmjmzmqmhbml
8-15 s: wcsswxxbrsdsrpss
4-5 c: cjccvc
9-10 z: zzzzzzzzzz
2-3 h: hhhz
6-7 w: wwgzsjwwvwlgww
3-8 g: gtxgggggcgfg
2-3 m: gmmrsgkmsvslw
10-11 x: xmxxxxxxxmxx
2-17 r: bcrtchxrgrqvrqgnm
7-18 r: rrrxrrrrzfrjrwrrrrmk
7-11 z: zzzwzzwzzzzrz
2-5 j: jmrjj
7-11 g: gkgggqgglmggnggqglqg
2-5 l: rlbkllxctprqflhll
4-13 p: mppprjpnxhrzpbp
14-16 p: pkppppzpppppjppg
13-15 n: jdndnxnnhntnnndsnn
1-2 m: pqmm
4-13 j: jjwjfmmjjjjjjpg
3-4 j: nfht
7-11 f: vfffffzffcff
10-12 p: pppppppppjpj
3-4 b: bbbb
5-9 p: ppqppppppppt
5-7 g: ggggggvg
11-14 z: zvzzfzzzqzkzzzzzzzf
2-5 c: hcgpjqjkpvgcxxrf
9-11 v: vvkvvcfqqvvffgvvvvs
8-9 d: rldntbdcz
15-19 p: ppppppppnpppppppgppp
7-8 w: wwwzwpwzmkxcwwtgw
4-8 z: zzrzzfdzk
8-9 g: gggggggqn
1-7 c: czcccngw
3-12 t: btdtgfclmpttqttctstt
2-3 n: jjglbnnzrjgd
7-10 h: hmhhpxhhhhh
4-6 v: vvvvnv
9-11 m: mmdbmmmqgmrh
2-3 r: rjrrrrrrrl
1-5 q: qjjqfzfq
4-5 z: zbzzc
9-12 c: ccccccccqccc
6-8 d: kdfkdtrv
4-12 r: rrrzrrrrrrrmrrrrr
1-5 h: hhhhxh
9-10 t: cztttttttttttt
15-17 j: jjjjjjrjcjvjfjjjcjdj
4-5 t: tftvt
2-4 d: qddvrp
7-13 p: pdrspdzpcxdcpzzxpwtg
12-13 l: llllllljllllll
13-14 s: sssssssssssssn
5-7 f: lnfsffrfg
2-8 r: krtrhgqnn
3-5 j: jxjjjnflwcjj
6-7 r: rrrrrrmrxrr
8-9 t: tsttqcctx
4-5 v: vvvvcv
10-17 j: jjjjcjjjjwjjjjjjkzj
15-16 t: nttttsttttzttttt
5-7 c: cccclccc
3-4 x: kxkx
4-9 l: zslllldlnql
13-18 f: fffmflfffffhdffffwf
8-10 m: mvmmmmhmmvmh
4-6 j: jsjjjmfs
11-13 h: hfnhhhhhhhthhh
5-13 g: gsqgcgqggfggl
7-8 p: ppjqppppp
11-12 b: tbbbbbbbbbbdb
1-4 q: qqqzq
8-9 s: xssssssns
6-9 p: pppppppppp
3-8 j: jvjjjjjjrjj
6-17 b: bbbbblbfbvbxbbbbbt
3-7 j: jjgjmhjjj
4-6 v: njvgsq
17-18 h: hhhhhhhhvhhhhhlhshhh
8-9 m: mmmmmmjdbm
2-11 x: xxxjdgxpxxwxtvkxxxlm
9-16 n: nnnnnnnnnnnnnnnsnn
17-19 w: wwbwwwwwwwwwtwwwwwww
7-8 n: qwbxqsbmpnj
5-6 j: jjjjqjjjjj
2-4 s: fssg
5-12 l: dgnzdllptvvlx
7-12 x: xwxxxxgxxtxbkx
6-12 x: xkmxzgxlnnxq
2-6 h: vnshjh
2-5 x: dxxqxpvsm
13-14 p: pppppppptpppjp
7-8 h: hthhhxhph
5-12 j: jtjrjcnjjjjxjjjj
1-5 j: jfjjwjj
5-6 q: qqqqqq
6-8 t: ttnttvttt
3-5 n: gksnnn
6-9 j: jjjjjljjj
3-4 d: dbdh
1-5 n: hjhfhrgbcnqn
10-13 l: llwllllllllll
2-3 s: dqss
1-3 l: lwqbqdml
10-11 r: rrvdcgrrwhrpsrzjtrl
1-2 d: bcdd
10-11 v: vvvvvvvvvcq
5-15 z: qcgsnhcrzzdfzpp
1-15 w: cfwzjwcgpwwwwwgwxw
11-12 t: gttfknrmtkbwt
2-4 h: blhhhcgfgmh
5-7 v: vjczvqsjzvpjvplhtdvl
1-2 d: tdjdb
5-6 m: mmzmzg
3-8 n: vwjfpdrn
2-9 c: ccccccccm
8-14 w: jxmpsswkhdpqrw
5-6 q: qqrfcj
7-13 g: hgwgqgrkgwggxggmqq
3-5 h: hnhhvhpjsh
1-12 k: hkkmkkkpkkjk
5-6 m: mmcmfm
12-13 w: wwwwwwwwwwwxw
8-10 q: qwbsdnqqlznvqjqqzqqv
5-7 j: jgjfjwmqmtsszf
4-5 c: cctcmc
18-19 v: vvvvvvvvvvvcvgvvvfq
1-8 j: qjbsjsjghj
14-18 b: bbbbbbbbbbbbbbbbbg
9-15 w: wwwwwvwwhwwnwwcwvw
6-9 d: ckvddldddp
3-12 k: qrnchpsjfcckrjx
6-10 c: ccccctccccc
5-6 z: hzzzzzsz
3-5 l: rvwlf
18-20 r: rrrrrrrrrrrrrrrrbhrf
3-4 c: cccvcc
11-17 s: jssssgszsbtsssslss
5-14 k: kkksxkkkxkxknkkkk
1-3 q: qxgsmqxdgx
12-13 q: qqnbqqqqqqhbqqqq
7-13 s: ksrskrslsjfss
3-8 n: nfnnnndsnnnnxs
4-8 g: lglggflgglgnf
6-14 b: bbdkbbmbgbbrlb
3-7 w: wqwrdpw
5-6 j: mdmjjj
13-16 k: kkkkkxkkkkkkqkdk
4-6 h: jmthbwhhfh
16-19 p: ppppppppppppppppppv
15-16 k: fkzkkkkkpkcrkhkklbkr
10-11 k: sjkkgkhkqfk
12-15 l: jjnlvmsppvlglllvljb
3-13 l: llcdlfllqllqjl
3-7 f: ggfgbvfqlrffxrflchx
13-14 d: ddddddddddcddqd
7-18 d: wdjdtdrdddfndkdddddd
8-10 v: rvvzvvvrvb
9-13 n: rlnnnnlnmbnqwlnmlnn
14-15 h: hwrhcmhwbjhcbhc
6-13 t: ttwtkrrtttdbtt
3-5 w: wkwww
1-6 h: fghcxhwldmnb
1-9 f: ffffffffffffff
10-11 k: kkkkkkkkkkvkkkk
2-3 s: sssw
3-6 v: vzvqmdgrnkvcvz
3-4 j: jztw
4-5 b: bbbbb
1-9 l: wllmxlbxfllllcr
14-15 q: pqgqqngpjzhmmqq
4-7 n: jnznczd
2-8 m: cmpmcmshpbmxb
6-9 r: rrrrrhrrr
15-18 t: ttttktmtttttttvtttt
1-5 s: sssxf
9-17 f: zfmkpffpwqfqffffffh
16-19 d: dddddvddddbdddkdddpd
8-10 w: dwwrpwwwxx
6-11 w: wmdmzzcwwpkkwwwqwnww
4-5 s: zssgf
2-8 v: vvpvvvvvqjv
17-18 s: sssssssssssssvsssj
1-3 d: tddd
1-3 s: tssdbfvnlmtspmwlxxl
6-11 k: kkkkkkkkkkkk
1-5 d: dddddgqddmdkdk
6-11 l: nzgwkmqlpnl
2-6 v: kvzlqgzr
1-2 f: xkqzbcrsdswpf
14-15 x: xxxxxxxxxxxxxwx
16-17 j: jjjvhgjzjwjzjmjnj
5-6 p: ppvppcjp
1-4 w: lwpwwh
15-16 s: ssscsssssssssssd
3-7 b: rpqkbbbb
3-6 d: dddddf
10-15 k: kkckzkbpdfkkckl
2-4 v: wvrvkgfpvvm
15-18 v: vvvmvvvvvvvvvvgvvl
1-2 l: hdfll
1-4 v: wtvd
5-6 v: vvvvzmv
6-8 l: llnllmlns
4-5 b: bbkblbsbnbbbbbbgbbbb
5-6 d: xnjmdwddtfdbzdb
4-10 q: qqlqqqqqhq
4-9 c: rcvctlmccccc
3-5 f: fffmnf
9-14 n: xnznnnnnrnrdlzfsn
6-7 w: wdwkrvwww
10-15 v: vvvvvvvvvnvvvvz
10-11 k: hnjzdwqkmskkx
4-8 c: ccqcqfrcnffbncfkc
5-12 c: cclsmccgcccccxnvcckc
5-6 z: cwhbkskzhnzztzzlhz
3-5 v: vkvjvv
3-4 j: jjjj
13-16 h: khxhhhrhkhhhhhhhwhhh
1-3 f: jxdxffjfprs
1-11 l: gllslllllxqlltlmh
8-11 g: kggggvnbkqgbfbgdsgwg
6-7 z: zzzxzfz
3-7 x: xqxjjxxlb
3-4 v: vtdv
7-10 w: wwwwwwwwnww
4-8 w: kgwwwwwwpx
3-5 g: ggggggs
4-8 w: gwwwgzxb
9-10 t: ttttttttmp
3-8 f: fpjdffffzflffmlxfq
11-13 g: gggtgggsggbbzggg
1-5 p: pptcp
13-14 c: cccccccccccccnc
3-13 n: gbjnnqxnjprnhn
5-6 x: qxxdknx
8-9 q: kmlfqxcvqqsqkvtm
3-6 n: xndnvn
6-7 s: scxccsjssstw
14-18 d: dddddddttddddfpddbd
18-20 d: sgljbkdxhvckddpbjdld
5-8 m: dpmnmfmmpm
6-9 w: rfdwwwplw
5-7 b: vbdrcbbgqbspbbv
18-19 b: bbbjbbbbbbbbbbbbbsb
11-12 x: xxxxxxxxxxzjx
6-8 d: dqhgrddhddxdn
6-16 p: dppbbzbpxxpphjppkpp
3-4 k: khkkt
1-2 x: xpwkvcxxqrn
1-4 n: lnnngnnnns
1-11 c: cczvdcgcpcrccpzw
15-17 h: hhhhhhzhhhxhhhshhhh
7-8 t: fttttttt
5-19 z: zczzczmczwzpzblzvxzz
4-8 l: zlpdjnsllkgkjglmnll
9-12 s: spwssjsssdstjssf
8-10 h: hhhhfhhchh
4-11 q: qqqqsqqqqqdqqqq
14-15 w: wwwqwwwwwwwwwmjww
1-2 b: blcbhdqfsbmnq
1-5 m: mlrdhdkfjnknxlw
8-9 r: rrrrrrlhc
9-13 d: ddddddddddddd
2-3 p: tpxpjgpcf
1-2 f: ffff
5-8 k: cdkkgbvfwkkskkw
2-3 r: rrrp
6-10 b: bbbbbdbbbbbbbbbbb
10-12 t: tttttttttgdxt
3-4 k: kjkrkmcmvr
8-10 b: zbbpcwgbsbwdz
2-10 v: zqvdtnxvvcvlrvq
3-4 b: bbbbb
13-16 t: ttttmttttttttttwttt
16-17 n: nbnnnnnnnnnnnnnsgx
8-10 f: fmfsffhjcfzffcxw
7-13 m: mmvmrlmtzmbtmmxcsmm
8-9 m: mmmmmmmmm
1-7 n: nnnnwnpnnn
6-7 z: xzzzhpz
3-4 n: bnnn
5-17 r: rrlrrbwzmkrrhrrrrhnr
9-13 t: ttntttttttttc
11-12 w: wwwwwwwwwcwsw
1-10 j: ljhjjjdgjmj
9-10 c: cccccccccx
3-5 h: hfhhh
18-19 q: qqqqqqqqqqqqqlqqqbqq
1-4 b: pnjntrscpklzfcdl
9-11 c: nrxscrjjcrzc
9-12 q: nqpqqqqqqqqqqc
5-15 k: phmcmnhbckwkvwkb
2-4 t: dtrtmtb
4-5 j: jjjjp
8-9 m: mmhjmmrsqmm
4-5 r: rrsrrrr
6-10 w: wwwwwgwwww
13-18 m: mgmmvmmmkmmmmmgpmfm
10-11 d: ddxdldwdddddzdvrd
3-15 k: mxxgjklzzdbtgddzwrx
9-11 q: qqqqfgqqqqwqqq
2-4 g: gdhthpp
1-11 r: srrrrrrrrrrr
13-14 x: xxxxxxxxxxxxxs
6-17 f: ffvffkffffffffffjf
3-12 m: kmmmvbjlmmmf
9-20 n: nnnplnnnnnnnnnlpjntn
8-14 f: cjflffftftnffd
2-7 b: kbzbbbbbbqb
10-12 n: nnnnnnnnnnnk
7-8 z: zxzdzzzclnjzj
3-11 l: llldlsmltklz
2-5 s: swwxrpscmmhzsgrvnl
1-13 p: kzwjlpfhpskzpsrp
13-15 f: gffffdffkhfffvffjffb
6-7 d: drddddd
4-6 p: pppphpj
12-18 k: jkkkkkkktkzkkxkkfgkn
8-9 j: jjjjjjjpc
5-7 d: ddlkxdmndmdkkhwd
10-11 l: vlllhllfhll
5-6 b: bbjbvbqrjb
17-18 d: dxdnddddddlddddddl
15-18 d: dddxddwwddddddnddd
1-12 x: sxxxxxxxxxxtxxxxx
3-9 k: rfkrnjxxkkm
9-12 n: xnnnnnnggnnln
5-8 w: nwpwqwwwlfwmj
3-11 p: sgprfdprpmqpwvps
5-6 x: sxxhxxkx
11-14 h: hhhhhchhhhhhhh
2-3 p: kxpllmpvfxq
4-14 k: qkpfkskhglhkzkck
3-6 q: jsqbdqq
8-9 n: nnnxnnnnpnnn
12-14 h: stshhhwxhcvhhg
5-8 j: jjjjjjjj
10-14 h: hqlqhxzmdnfzhhhwxnwj
1-8 r: qmlvfqvrbgfrrmppkzwv
3-9 v: hhvnpvvvdvktgbcrr
6-8 q: qqqqqqqp
9-12 l: lxklkwplllvlmljlfll
11-14 w: wwwwwwwwwwwwwpw
6-7 c: cccqrccc
3-6 d: wddgdzd
3-8 d: dddppddddddddfd
5-9 g: jlxgxgkggpg
6-14 b: jbljlvjtqkbbzlpvxmf
2-3 x: nnbx
6-7 q: qqqqqbfqqqq
2-3 n: xnmnnfb
13-14 p: pppppppppppphr
8-11 k: kkkkkkkkkkk
4-5 r: rrrsr
13-19 t: ttttttvtttmttttttbt
8-9 r: rrrlrrrwr
3-6 c: flfhnccccwvtmqz
8-12 s: xshssnnsskcsjsssgs
1-4 r: vzkpphvtwrxgr
11-13 c: ccccccccccqcc
3-5 v: fvvjvzgt
1-4 j: sjjnsjjj
3-6 s: sxsqnfbmssbfnjs
12-15 p: pnppppppppppkpp
9-13 l: wlldrllklllllkl
2-3 s: swsrljzrns
8-9 b: bbbbbbrwb
16-20 f: ffffffhffffffffsffff
5-9 w: wwwwswwwww
7-9 q: qbqqqtqqkd
6-8 z: zzzzzzzz
5-10 m: zlmmnmrgkmtm
1-5 n: mnnflnn
4-8 c: cpccbgccc
9-12 j: jjjjjjjjwjjjj
3-4 s: tdhzbsqsb
15-19 t: tthrqtttttttmtttttx
11-12 b: bbbbbbbbmbjcb
1-13 f: ffqfkfftfjrwfkfm
14-15 v: vvvvvvmvvvvvvdv
4-6 h: qvchkhhccnxwpvhhhb
2-8 k: kskkkxkkkkk
3-10 j: jjjbjjjjjpd
4-13 z: svkjzrfrtftftqhhc
18-19 p: pppppppppppmpppppmd
5-14 b: bbbbcbbntbbfbpbd
5-7 q: qqqqqqq
2-17 j: jbjjjjjjjjjjjjjjcj
1-5 z: zvztgv
4-5 k: kkkrkp
3-5 c: kgmccc
2-8 h: rhhhnhhxh
1-18 s: sbrblpcrxsvdsjrnwwws
6-10 q: qbqqzqqhbdq
1-3 d: sdwgdn
3-6 s: ssssssss
2-13 f: ffffrrfffflbvffff
5-7 w: pxwnfnwzj
17-18 z: zzzzzzzzzzzzzzzzbzzz
7-8 p: pplplpbfppp
1-8 x: xxkzdxzx
3-4 p: jppxp
4-6 j: jthbzjmqjzj
1-12 x: xxxxxxxxxxxxxx
8-19 g: ggggggqgwmgggwggmlg
5-9 b: bxbbbgwbbnxbhbbb
5-6 n: nnnnnd
5-9 b: bwjxbbwbb
4-14 d: ddlddkdddddddl
2-3 t: jqjt
2-3 h: shhp
12-14 p: ppppppxppjfmpdzppp
7-10 f: lnffvfcfzffffft
3-8 s: lqhrstvsr
15-16 v: vvvvvvmvvvvvvvvvv
2-4 h: hhhh
5-8 g: wmtxgdgg
3-6 r: rfrrrg
8-12 q: qqqqqqqqqqqq
4-9 z: zzzzzpzzw
14-19 g: gdggggggggbggtcggggg
5-11 n: nnnktnnlndgnnnnn
5-6 n: nznnnqn
3-4 q: qqlq
12-13 g: ggggggggggggg
16-18 w: wwwwwwwwwwwwmwwxwv
6-10 b: bbbbbmblbg
8-13 m: mwmmmcrmmmtsm
12-17 h: rhhhhnhhhhhlhstkhhh
9-10 q: qqqqqzqqgt
2-6 v: vvfvpgw
8-13 w: mwlxrpbwwwgcwwgn
1-10 m: mmmmmmmrmxm
6-8 f: fgvfgfftfffq
2-6 g: gcggrg
1-6 x: zxxxvxx
1-3 t: txtt
1-2 q: qdqn
6-7 j: jjjjtjjj
13-14 r: rrwrrwrrrrrrrfrr
3-4 j: jjjpj
12-13 v: vvvvvvvvvvvvv
4-5 t: tttcw
4-6 s: sssnxs
9-11 x: xxxxxxxxcvx
1-4 d: lpddds
1-9 t: hbtttttthtt
1-4 z: bsjzz
2-5 t: xrtptqt
1-3 l: lllll
7-8 m: mmmmmmmj
11-13 f: ftffqffffgfszfff
4-5 j: ljjbjbjjjj
3-11 n: nhnnnnnnjnnnnnbmnqnn
3-12 s: swgnlssszsqsvfjwxt
8-9 f: ffffffffn
3-4 t: gtmt
8-9 s: spsmnswlt
7-8 j: jjjnmjjjdjjjqj
9-10 j: jnjljjjjfgj
3-7 x: xrxlbhcxmswlpx
9-11 x: xxwrxxbxxxn
16-17 d: dbddddmtddddddddddd
5-17 n: cnnnhnnnjnnvnsnnwgnn
7-8 m: mmmmmmmm
11-12 l: lllklllltltmllllll
4-5 r: rrrrr
7-8 j: jjjjjjqqjj
10-12 g: gggtkggggggkggg
1-5 h: fxxphhz
1-3 q: jlnq
4-5 s: fssss
16-17 c: cccccccccccccccqc
12-19 q: qqqqqqqqqqpqqqqqqqpq
7-13 s: gmzvssjsfssjssssx
3-4 s: ssxs
15-19 d: ddddddddddtddddddqdd
5-7 l: lllxqlkl
10-11 x: xmxxxxxxxfk
9-14 q: qqqqqtqczqqqqq
4-8 w: zwmllrwmwmwqwww
1-4 l: llllz
14-15 j: jjjjjjjjjjcjjjrjj
10-13 x: xxxxxxxxhbxlzx
6-7 f: fffffdj
9-10 w: msdcwqzwhj
4-8 c: ccccxccccckcccccccc
5-11 r: xffrjsvrjzfrrcrpfbr
2-5 z: zzfwrn
10-13 r: rrrrrfrrrhrrh
5-10 d: dddddddddddd
4-5 z: zzzfs
9-12 t: ttttttttlttt
3-4 r: lpjrr
2-9 v: kkxvvxkvgjtsjtvv
1-8 v: lprgtpvvv
4-6 h: hhhnhfb
2-4 h: hhpxh
4-9 d: bhqdmddrd
2-5 w: wwgtwt
6-7 z: zzzzzszz
4-5 z: zzzzm
12-14 d: mddrddddddrdddddd
9-11 h: sdhzhvhhhkhhhb
2-3 b: zbbtbbqhm
4-11 b: bnbqqbjbbzp
9-10 n: nnnnnmnntj
11-17 w: wwvwwwwwwwrtwwwwdw
1-4 t: svbtbxvptfp
4-5 w: vsbjw
2-7 m: mmpmmmg
11-12 j: jjjjjjjfjjxjjm
6-8 r: rrzrcmrvrr
1-3 n: nqxnzhq
3-4 n: nnnkj
3-5 f: kfffhfthfhf
3-5 m: gwszmmm
1-7 c: tbscmrfbmccrqxzdb
13-14 l: lllllllllllllnll
4-10 k: pfbwsjvfxkxhfzktdj
2-6 f: ffffbf
4-7 w: wwgrwnpbswnz
5-6 z: zzszzzz
8-13 p: zpppppgbjpppcpp
6-7 q: gpqqvwtkxwqjtqdqq
14-15 n: nnnnnnnnnnnnnkn
3-6 q: rkqmjqg
5-6 t: ttttkq
4-6 r: srrsrrprr
1-8 v: kvvvvvvxvvvvvvvb
5-6 z: zzzzzz
3-4 c: cccccbpsp
3-12 c: stvxclcbrcjjcgcxlwtq
13-14 r: nrrrrxrfrrrrrzd
2-3 r: rmfwl
1-4 q: qqhq
11-13 z: zzzmvzzzzzkzzzzzzzz
4-8 h: hhhxhhhh
2-3 b: fpbhn
7-10 v: vgwvvvgvvvvvj
1-4 m: msmk
11-12 d: ddddddddfddddd
15-16 k: kkkkkkkkkkkkkkkk
8-14 m: mmmmmmmwmvmbmmv
10-12 m: mmmmmmmmmlmm
2-7 w: cgbmsww
6-8 t: ttktttgw
4-14 z: vsvmwzvhfzxkfzz
2-4 f: ccgmfhrls
10-11 k: kfxlsfdkbdkmjptqhh
6-16 x: nbxxdxwsxxsqmfxqrxmk
9-17 j: vjjjjvpjgfjxffjxjd
6-9 g: gvpxggggqgg
6-8 t: tttttztft
5-11 q: prklqxrfxjdvgsq
8-9 k: kkkkkjknk
2-4 c: chccl
2-3 x: fxpr
1-4 v: rzvvpvxp
3-5 j: cjfrjldr
3-8 t: zbptntzp
2-7 c: cccqkcfzgcffssgrcsc
5-6 q: qqqqdr
2-6 h: hxfhhghhhk
1-3 v: lvnhv
5-6 r: prrrrw
11-18 z: zfzzzzzzzzdgzzzmzzxz
5-10 x: kxrncghxldxffzbx
17-19 k: kkkkkkkkkkkkkkkkjkkk
7-9 h: hhmhhhdhh
15-16 x: xxxxxxxxxxxxxxxx
4-5 c: nzjchwccgbd
5-6 r: rrrrjrrrr
9-13 c: ccccccjclcccc
6-7 z: zjzfzzzszvzz
6-7 l: llllljll
6-8 m: mmmmmmms
3-5 p: pppppp
14-15 m: mmmmmmmmlmmmnwmm
6-11 b: bbbbbbbbbwb
8-10 g: ggjgbgpgggggggdcgb
9-16 b: bbbbbbcbkbbbbbnbbbbb
10-11 f: dfbffxfnfksfffrw
10-11 h: hhhhhhhhhhq
5-17 v: vvvvjvvwvvvvvvvvvvvv
2-14 x: xgxxxvfcxxxxtbgxkx
1-3 k: kkjbm
18-19 d: dddddddddddddddddxx
5-9 h: vhjzhkjbhl
1-4 k: kskk
7-12 l: lcljknlllclvlldrlpls
14-15 w: wwwwhwwwwrhwwvq
5-6 t: wtvdtmqfbnt
1-4 v: vhvvvv
8-10 n: nnqcnzrnndnjnnnkn
6-8 h: hshhqhhdhhfcj
10-15 j: jjtjjjjjjfzjjjj
3-5 m: mmdmm
10-11 n: nnnnnnnnnng
6-8 p: fzpgppzpthqcthhst
1-7 p: hzxthvpfnpnrzfpvmv
10-11 l: llllvswlllll
1-2 q: jffqfzd
1-3 x: xljxfw
5-6 z: fmzzgl
2-6 v: vbvvvzv
8-10 r: rrrrrrrnsr
1-3 c: crctc
8-10 m: mcmdgxhmhnmmwmzmmg
4-5 h: hdhhhh
1-2 z: vzzm
5-10 z: zzzvnzzzpz
2-5 f: gfffdff
1-4 g: lgfgg
2-4 w: swww
2-6 c: ccscdz
6-7 b: bbsbbbjb
11-16 s: bssrqsslssbcssjrxjk
5-8 c: ccjmcqcglj
13-18 l: lllllmvllllxlllllz
6-7 l: lllllll
5-6 v: vvvtvvvv
4-11 v: vvmvwhvvrkd
4-7 n: knlwnmnnnn
5-6 p: cqmfxppptplkpp
7-11 c: clccnptxmcncrccjcc
1-7 h: fhhfhhzd
1-11 l: llflllllllllll
3-4 g: gmgl
15-16 j: wjjjjjjjjjjjjlhjcjj
2-8 v: gtvvmgvvbtf
3-4 t: fpttgzttwt
4-8 k: klkkkgkkkk
2-8 p: wsdgtplp
9-11 q: qqqqqqqqzqv
1-2 n: nswlnnngxsj
4-5 p: dgpppkjhvgpgppp
10-17 j: jjjjjjjjjfjjjjjjk
2-3 l: lbll
6-7 n: nhwnnnc
3-4 s: ssws
3-9 v: szrvvcxzv
2-4 p: pgzph
4-6 g: rxnjtpggwggglp
10-16 v: vvvvvvvvvvvvvvvjvv
7-9 j: jljjjmjjj
6-11 w: wwwwwqwgmwfwwkw
12-15 w: wqwwwwtwwxwwwfwww
8-11 v: vvvvvvvvvvd
7-11 g: dcgpcggpgxggdphgm
3-5 w: wwrwg
9-16 b: bbbqbbbbbbbbbbbbb
7-8 n: tnnnnnnnnn
3-5 c: ccsctcm
10-17 f: rfsfffffvffjfnkfq
6-11 f: fffhffffffp
10-11 n: hbsnnnntnppdnnzj
3-4 x: ngxbxxx
6-11 t: ttbwkznllhtntbdtltt
5-6 s: sssssms
15-16 c: ccccccccccccccqc
3-5 h: jzslhlhh
7-12 m: mxmjmjmmmmhkm
7-9 r: mtbfxlrvrddrvgxrxxr
14-20 m: gmmlpvclmkvfkmjdslvm
11-17 v: rqvvtmktpvckpvvvv
15-16 b: bbbbbbbbbbbbjblbbc
3-5 z: vpsgzfzvxczbnzw
5-6 j: shlfjc
10-16 b: bbbbbbbbbbbbbbbsn
1-7 j: jjjrkrdq
14-16 x: xbxxxxxxxxxxxjxxx
2-6 b: vzpnbbpqfbbvcbmbchm
10-16 x: xxxrxxxvxxxxxqxxxxk
10-12 j: jjrkjjjjjjjjj
1-5 l: lxfslmj
10-16 s: ssssssssssssssszsss
12-15 r: rrgrrrrrrrrcrrr
10-11 c: ccctccccccj
13-14 f: fqgsffffqffffvfffff
14-15 f: ffffffjffffffqff
8-14 q: gtqqjqqwwxqvprdqpcqq
8-11 f: lqqfqpmffffgcs
6-8 f: frfshkfklf
10-11 w: wlwwwwwwwwrw
2-5 q: qqmmqmmqqq
8-9 g: cjgscgwtg
1-3 w: wljwwvjdcwnkmn
4-5 q: qcqqxq
11-18 g: gqgggvgggghgkggggggg
8-12 z: tbmbzbzhnppz
2-3 t: tzttt
2-5 s: zjlsssssmsss
8-16 w: mwwqwrwwskwcwwbww
3-7 t: ttwttttt
1-4 p: ppclpbpppp
7-9 c: cccccckcxccccc
9-13 g: dgggggcgrrggggggg
4-5 v: vvvvvvvvvvvvvv
15-16 l: lllllllllnlllsqkl
2-6 p: pppjptvpkxp
11-18 j: jjjjjjjjrjcjgjkjjhjj
2-6 x: znkxkc
14-15 b: bbbbbbbbtbbbbssbt
3-8 b: bszbbvbb
15-16 t: dtttttttxtpttttrttt
10-11 b: bwbkqbvdbvj
14-17 k: krjwkfgsqkzjklkkkvxg
13-16 d: ddddddddddddqddd
3-15 s: jmsnpmldstjngfmrp
1-6 s: stssssn
8-12 b: bbbbbthpwlbb
3-4 r: rdrf
10-11 l: glllllllllk
7-16 m: vxjgnbmmbzsxlhblj
4-7 b: bsthbwjrkbmptb
5-7 q: qqdmjqqqq
2-16 v: rvvvvvvvvvrvvvvvvvv
2-3 n: nnnbm
13-16 v: vvvvlvvvvvvxwvvv
4-6 c: nccccccs
10-14 q: qdgsqqqqqqqqqqqnq
4-5 g: gjghg
2-7 f: fffffqdf
15-18 f: fxffffdfhflffbfxff
7-9 w: gpwwcwwwlwbwfkdw
14-17 q: qqjqqqqqqqqnqhqqrhqq
1-4 d: djdqkdkddlvdqdt
4-9 w: qwsvpbwdcngsww
4-9 b: bbbbbbbbb
6-15 g: gmdhggngqdfgqsggsvg
9-16 b: bbbbbbbbdmtbbdbbc
8-9 k: kkxkkkdkkkzkdp
1-8 b: bbxbdbnbjcbbb
15-19 q: qqqqqqvqqqqqqsqqqqq
3-4 t: tttt
2-5 j: bjjjj"""
    password = password.replace(" ", "").split("\n")

    valid = 0

    for set in password:
        count = 0
        policy = set.split(":")[0]
        first = int(policy.split("-")[0])
        require = policy.split("-")[1][-1]
        second = int(policy.split("-")[1].replace(require, ""))
        result = set.split(":")[1]

        if result[first-1] == require:
            count += 1
        if result[second-1] == require:
            count += 1

        if count == 1:
            valid += 1

    print("Question 2 part 2")
    print(valid)

    # Question 3 part 1
    pattern = """.##.#.........#.....#....#...#.
.#.#.#...#.......#.............
......#..#....#.#...###.......#
.......###......#.....#..##..#.
..#...##.......#.......###.....
....###.#....###......#....#..#
......#..#....#...##...........
..#..#....#...#.....####.......
...#........#.#.......#..#...#.
......#...#........#...#..##...
#..#........#............#...##
..#..#.#....#...........#...###
#.#..#...........#.##.#.#....#.
.#.#....#...##.....#...........
.....##....#...#..............#
...#....#...#.#.#.#...#........
#....#....#.#.#..#....#..#..#..
.................#..#.....#....
#..###...#.#..#.#......#.......
...#..........#......#....#....
.#.#.........##..#.......#...#.
.#..........#...#..#...........
....##.#.......................
.......#...........#...#.......
...#...#..##...#....###..#....#
....#.#.....##...##.#.#........
...........#.#..#.#......#..#..
.....#.....#....#...#........#.
..#......#..#.........#.....#..
.........................#...#.
#...#...#....#........##....#..
#..#.#.............#..........#
.#.........#.....#..#.#.#..#.#.
#...#..#.......####.#....##....
##...##..#.#.#...#.#.....#..#.#
.#..#....#.##........#...#....#
#...#..##.#....##..#..#.#......
.#........#.....#.#....##.##.#.
...#...#........#..#.##.##.....
....................#.#.#.#...#
..####.#..##...#....#.....##...
#......#.....#.#......#.#..#.##
..#.....#..#...........##.#....
#....#........#............#...
..##....#..............#......#
..#......#.#.......####......#.
..............##....#....##.#..
.#...............#....#....#.#.
..#.#.#..#.......##.#..........
.#...#.......#.#....#.##.......
.....#.##...#...........#.#....
..#.#..#...#..##...#.#.......##
.#.....#....#.#......#.#.......
....##.........#.#.............
.......##.......#..............
..........#......#......#....##
..##.....#..#.#..........#.....
...#....#.......#....##........
.......#...........#...........
...#.#......#.#........#....#..
.....#...........#.#.#...#.#..#
.#.#...#.#.#..........#.....###
#........#...#.................
...##.....#.....#..#..#.......#
......##...........#..#....##..
.........#............##...#...
.....#.....##...##.............
.#....#..#.#.#.#...#..#..#.....
.....#..#.#..#....#..#.........
....#.....#......#...#.........
#..#..#.................#......
.###.....#...#.#........##.#...
..#...#....#.##..#.....#.#....#
..#...##.................#.#...
....##..........#..#..#..#....#
....#..##....##.....#.#....#...
.#.#.#.....##........#.##..##.#
....#..#......#..#........#....
.......#.....###.#....#.......#
#....#.......#......##.#.......
.##.#.........#.#..##..#....##.
......#........#.#....#...#....
.####.....#.........#.#......##
##....#......#....#..#.#....##.
...........###.#.....#..#......
.......#...........#...........
........###....#..#.#..........
....#........#......#..........
.........#......#..............
...#...............#......#...#
....#..##...#.........#...#....
##........#.#....#......###....
....#.......................#..
#................#.#..#......##
...#.#.....#...#...........#.##
.#....#.##......#...##.#....#..
#...#....#..............#..#..#
.......#....#.##............#.#
.....#.#.......#.#...#.........
...#.....#..##...##...#........
..#.......#..####..#..#...#....
#.#................##...##.#..#
.....#.....##.#.....#......#..#
....#.#...#.........#.........#
..#......#............#.....#..
.....#..........#.#..#..##...##
........#................#.#...
#...#.#....##...###...#.#......
.............##.#..##..........
#..#......#...........#......#.
#.#....#..........#.##....###..
.............#.........#....#..
#........#..#.#..#...#....#....
..............#..............##
.....#...#..............#.##...
#...##..#...........#..........
..#....#...#.#........#..#.#..#
..##......#...............#....
....#...#..###..#......###.#...
.......##..#.#........#....#...
..##...#.......#...#...........
.#.......#.....#.#...##..#....#
.............#.......#.#.#....#
#.......#..#..#...#.#......##..
#.##..#..#..#....##.#...###.#.#
...##...#..#..#........#.#..#..
#....##........................
##...#...#......#.#.....#..#...
......#............#....#......
#......#.......#.......##.#....
..................#..#..#.#....
..#..................##.#......
..##........#.#.....##..#..#.#.
#....#..............#....####..
#..#..........................#
..#.#.#.#....#.......#....#.#..
.....#.#........#..........#.#.
........#.....#.......#........
#.....#....#.###.....#.......#.
.....##.#...#.#..#...#.#.#.....
......##...#.#...##..........#.
.#............#.....#..#....#..
.#................#.#..#.......
....................##...##....
#.......##...#.....#..#........
.##....#.#.#.#...........#...#.
..#.#..#.#.........#...........
...#......#.....#...##.........
..........#.#.....###.#........
.............#.....##..........
.........#...####........#.####
...................#....#......
.....#.........#.#....#..#...#.
.##...#.......##.#...#.#.#..#..
.....##........#....#...#.##.#.
#...#...#.#....#..............#
#..#.##.............#..........
..#...#..#.#.##..............##
#......#.#...##..........#.##..
.##.#...#...#.........#.#......
......#........##.#..#.........
#..#.......#......#.#..#.#.....
.#..#...........#.#.##.....#...
.....................#..#.#....
........#...##......#.....##...
#.............#...##....##....#
#.#...........#....##.#......##
.....#.....#.#..........###..#.
....#...#....##....#..##.......
.#....#....#.......#.#.....#...
.#...#.......##...##........#..
......##.......#.##.#.###......
....##.......#......#..........
...................#..##.......
......................#...##...
...##....#.#..#..#.............
.#......##..........#...#......
....##..#....#..#...#...####.#.
...#.......#.......#........#.#
#.........#..#...#...##...#.#.#
....#...#.......#...#....#.....
...#.....#.##..##.#.......##.##
.......#....#........#.........
.....#...#....#..#....#....#...
.##....#...#........#...#.#...#
.......##............#..#...#..
#.#...#....#......#.#..........
.#.##...........#........#.....
.#....#.............#.#.##.....
#.......###..#...###.........#.
#..#.#.......#.........#...#..#
..........#......#........#...#
.#.#...#.##.......##...........
.....#.........#.....#.........
.........#.........#....##.#..#
.#.......##..##..#.....#...#...
.#.....##...#..#..............#
..##...#..#..#.#...#..........#
.#.......####......#......####.
##..##........#.....#........#.
..##.#..#.#....................
...........#..#...##....##.....
..#.#........#.........#....##.
..#...#..##..###.#..###........
......#..#.............#..##...
.##.........#.#..#...#.##.###..
.#...............#...........#.
.#....#........#....#........##
..#####.#.#..#.#........##...#.
###....#....#...#..............
.....#...##............#...#...
##...........##.#.##.....#.....
..............#..#.....#...#...
...................#...........
#..........##.........#........
...#.........#..#.....#..#..#..
....###.#......#......##....#..
#......#..........#...#........
...#.#...#..#..........##......
.....##.....#.#............##..
..#..#.###....#.#.#...##....#..
...#........#....##.......#....
.#.............#..##.......#...
..#.#..###..#.....#...##.......
.........#......##...#.#..#....
.............#....##....#.#....
#..#...#....#.#...#......##....
.............#.#......#.....###
#.##....#........#.............
.....#...#.####...#.....#......
....#....###....##.......#.....
..#....##..#....#.#.......#....
...#.....#....#.........#......
.#......#.#....#.#........#....
.......#......#.....#.#..#.....
#......#.........##.##.#...#...
..#.###...................#....
....#..#....##.#........#....#.
...........#..........#......#.
.#..#.#...###..........#..#...#
...#...##..#....#...#..........
.#........#.................##.
....#.......##....#...#........
#.#...##.##...#.#.......#...#..
.....#.#.##.#......#..#..##....
.....##...#.#.....#...#........
#.#.......#..#..........##.....
................#......#..#.#.#
#......#...#...................
...#.....##.#.........#.#..#..#
...#..##..##.......#....#......
....##...#....#..#...........#.
..#..#......#...#..#...........
...#.##....#...##.......#......
.......#....#..#..##..#..#....#
.#.................#.#...#.##..
.....#..................#..#.#.
...#......##...#...........#...
..#.........#....#..#...#.....#
..#...#.....#.........##.#.....
.....#.#....##...............#.
....#...#............#.........
.....#.....###............#....
..#.#.#.......#....#...........
...........##...##...#.......#.
.........###.#......#..........
.#.......#....#.....#.##..#...#
..#..................#..###....
..#....#...#......##.........#.
........#..#........#.........#
.#..#......#.........#.........
...#..##.....#....#....#.....#.
......#.#............###.....##
.......#........#.......#.#....
..#.............#..............
.............##..#.#.#....#....
.................#....#.#......
##..#.#.......#....#.....#.....
.##............##.#.......#.#..
#..#...........##......#.......
.##......#####..##.#....#.#....
.......##.....#...#........#...
.#.#.....##....#..#....#..#...#
............##.#.....##.#......
........##...###.#......#......
......#..#.#...#..#............
.........#...........#......#..
.#.........#............##.....
.#..#..#...#.#.............#...
......#.#..##...#.#...........#
#.##.......#...#.........#.....
.....#..#............#....##...
.#......#........#.............
..#...#....#..#.......###......
....#.......###.#.#...........#
.............#...##............
.##.#.#.#...........#...#....#.
............##.........#......#
...............#......#...#....
...#.....#..###..#...........#.
.#........#.....##........#.#..
....#.#.......#..#..#...##.#.#.
.......##...........#...#......
....#.#..##......#.......#.....
..#........#.#......#.#........
........#....#..#....#..##.....
.#.........##..........#.#.....
..##...##.....##......##..#....
.###.....##...........##.#...##
...#................#.......#..
#.......#.#.#..#.#.##..#...#...
.#.#.......#..#................
..#.#.#......#............#....
#.....#.###..#.#...#...........
#...........#..........#.#.#.##
..#.#...#......##.....#........
........#.......#.#...#...#....
..#..........#......###......#.
..........##.#....#.....#.##...
..#.....#......#.........#..##.
.#...#........#..#.#..#...##..#
..###........#......#.#........
..#.##.#....#.#....#.#...#....."""

    pattern = pattern.replace(" ", "").split("\n")
    count = 0
    move = 0

    def addLine(line,move):
        if move > len(line)-1:
            line = line + line
            return addLine(line, move)
        else:
            return line


    for line in pattern:
        if move < len(line):
            if line[move] == "#":
                count += 1
            move += 3
        else:
            line = addLine(line,move)
            if line[move] == "#":
                count += 1
            move += 3
    print("Question 3 part1")
    print(count)

    # Question 3 part 2
    pattern = """.##.#.........#.....#....#...#.
    .#.#.#...#.......#.............
    ......#..#....#.#...###.......#
    .......###......#.....#..##..#.
    ..#...##.......#.......###.....
    ....###.#....###......#....#..#
    ......#..#....#...##...........
    ..#..#....#...#.....####.......
    ...#........#.#.......#..#...#.
    ......#...#........#...#..##...
    #..#........#............#...##
    ..#..#.#....#...........#...###
    #.#..#...........#.##.#.#....#.
    .#.#....#...##.....#...........
    .....##....#...#..............#
    ...#....#...#.#.#.#...#........
    #....#....#.#.#..#....#..#..#..
    .................#..#.....#....
    #..###...#.#..#.#......#.......
    ...#..........#......#....#....
    .#.#.........##..#.......#...#.
    .#..........#...#..#...........
    ....##.#.......................
    .......#...........#...#.......
    ...#...#..##...#....###..#....#
    ....#.#.....##...##.#.#........
    ...........#.#..#.#......#..#..
    .....#.....#....#...#........#.
    ..#......#..#.........#.....#..
    .........................#...#.
    #...#...#....#........##....#..
    #..#.#.............#..........#
    .#.........#.....#..#.#.#..#.#.
    #...#..#.......####.#....##....
    ##...##..#.#.#...#.#.....#..#.#
    .#..#....#.##........#...#....#
    #...#..##.#....##..#..#.#......
    .#........#.....#.#....##.##.#.
    ...#...#........#..#.##.##.....
    ....................#.#.#.#...#
    ..####.#..##...#....#.....##...
    #......#.....#.#......#.#..#.##
    ..#.....#..#...........##.#....
    #....#........#............#...
    ..##....#..............#......#
    ..#......#.#.......####......#.
    ..............##....#....##.#..
    .#...............#....#....#.#.
    ..#.#.#..#.......##.#..........
    .#...#.......#.#....#.##.......
    .....#.##...#...........#.#....
    ..#.#..#...#..##...#.#.......##
    .#.....#....#.#......#.#.......
    ....##.........#.#.............
    .......##.......#..............
    ..........#......#......#....##
    ..##.....#..#.#..........#.....
    ...#....#.......#....##........
    .......#...........#...........
    ...#.#......#.#........#....#..
    .....#...........#.#.#...#.#..#
    .#.#...#.#.#..........#.....###
    #........#...#.................
    ...##.....#.....#..#..#.......#
    ......##...........#..#....##..
    .........#............##...#...
    .....#.....##...##.............
    .#....#..#.#.#.#...#..#..#.....
    .....#..#.#..#....#..#.........
    ....#.....#......#...#.........
    #..#..#.................#......
    .###.....#...#.#........##.#...
    ..#...#....#.##..#.....#.#....#
    ..#...##.................#.#...
    ....##..........#..#..#..#....#
    ....#..##....##.....#.#....#...
    .#.#.#.....##........#.##..##.#
    ....#..#......#..#........#....
    .......#.....###.#....#.......#
    #....#.......#......##.#.......
    .##.#.........#.#..##..#....##.
    ......#........#.#....#...#....
    .####.....#.........#.#......##
    ##....#......#....#..#.#....##.
    ...........###.#.....#..#......
    .......#...........#...........
    ........###....#..#.#..........
    ....#........#......#..........
    .........#......#..............
    ...#...............#......#...#
    ....#..##...#.........#...#....
    ##........#.#....#......###....
    ....#.......................#..
    #................#.#..#......##
    ...#.#.....#...#...........#.##
    .#....#.##......#...##.#....#..
    #...#....#..............#..#..#
    .......#....#.##............#.#
    .....#.#.......#.#...#.........
    ...#.....#..##...##...#........
    ..#.......#..####..#..#...#....
    #.#................##...##.#..#
    .....#.....##.#.....#......#..#
    ....#.#...#.........#.........#
    ..#......#............#.....#..
    .....#..........#.#..#..##...##
    ........#................#.#...
    #...#.#....##...###...#.#......
    .............##.#..##..........
    #..#......#...........#......#.
    #.#....#..........#.##....###..
    .............#.........#....#..
    #........#..#.#..#...#....#....
    ..............#..............##
    .....#...#..............#.##...
    #...##..#...........#..........
    ..#....#...#.#........#..#.#..#
    ..##......#...............#....
    ....#...#..###..#......###.#...
    .......##..#.#........#....#...
    ..##...#.......#...#...........
    .#.......#.....#.#...##..#....#
    .............#.......#.#.#....#
    #.......#..#..#...#.#......##..
    #.##..#..#..#....##.#...###.#.#
    ...##...#..#..#........#.#..#..
    #....##........................
    ##...#...#......#.#.....#..#...
    ......#............#....#......
    #......#.......#.......##.#....
    ..................#..#..#.#....
    ..#..................##.#......
    ..##........#.#.....##..#..#.#.
    #....#..............#....####..
    #..#..........................#
    ..#.#.#.#....#.......#....#.#..
    .....#.#........#..........#.#.
    ........#.....#.......#........
    #.....#....#.###.....#.......#.
    .....##.#...#.#..#...#.#.#.....
    ......##...#.#...##..........#.
    .#............#.....#..#....#..
    .#................#.#..#.......
    ....................##...##....
    #.......##...#.....#..#........
    .##....#.#.#.#...........#...#.
    ..#.#..#.#.........#...........
    ...#......#.....#...##.........
    ..........#.#.....###.#........
    .............#.....##..........
    .........#...####........#.####
    ...................#....#......
    .....#.........#.#....#..#...#.
    .##...#.......##.#...#.#.#..#..
    .....##........#....#...#.##.#.
    #...#...#.#....#..............#
    #..#.##.............#..........
    ..#...#..#.#.##..............##
    #......#.#...##..........#.##..
    .##.#...#...#.........#.#......
    ......#........##.#..#.........
    #..#.......#......#.#..#.#.....
    .#..#...........#.#.##.....#...
    .....................#..#.#....
    ........#...##......#.....##...
    #.............#...##....##....#
    #.#...........#....##.#......##
    .....#.....#.#..........###..#.
    ....#...#....##....#..##.......
    .#....#....#.......#.#.....#...
    .#...#.......##...##........#..
    ......##.......#.##.#.###......
    ....##.......#......#..........
    ...................#..##.......
    ......................#...##...
    ...##....#.#..#..#.............
    .#......##..........#...#......
    ....##..#....#..#...#...####.#.
    ...#.......#.......#........#.#
    #.........#..#...#...##...#.#.#
    ....#...#.......#...#....#.....
    ...#.....#.##..##.#.......##.##
    .......#....#........#.........
    .....#...#....#..#....#....#...
    .##....#...#........#...#.#...#
    .......##............#..#...#..
    #.#...#....#......#.#..........
    .#.##...........#........#.....
    .#....#.............#.#.##.....
    #.......###..#...###.........#.
    #..#.#.......#.........#...#..#
    ..........#......#........#...#
    .#.#...#.##.......##...........
    .....#.........#.....#.........
    .........#.........#....##.#..#
    .#.......##..##..#.....#...#...
    .#.....##...#..#..............#
    ..##...#..#..#.#...#..........#
    .#.......####......#......####.
    ##..##........#.....#........#.
    ..##.#..#.#....................
    ...........#..#...##....##.....
    ..#.#........#.........#....##.
    ..#...#..##..###.#..###........
    ......#..#.............#..##...
    .##.........#.#..#...#.##.###..
    .#...............#...........#.
    .#....#........#....#........##
    ..#####.#.#..#.#........##...#.
    ###....#....#...#..............
    .....#...##............#...#...
    ##...........##.#.##.....#.....
    ..............#..#.....#...#...
    ...................#...........
    #..........##.........#........
    ...#.........#..#.....#..#..#..
    ....###.#......#......##....#..
    #......#..........#...#........
    ...#.#...#..#..........##......
    .....##.....#.#............##..
    ..#..#.###....#.#.#...##....#..
    ...#........#....##.......#....
    .#.............#..##.......#...
    ..#.#..###..#.....#...##.......
    .........#......##...#.#..#....
    .............#....##....#.#....
    #..#...#....#.#...#......##....
    .............#.#......#.....###
    #.##....#........#.............
    .....#...#.####...#.....#......
    ....#....###....##.......#.....
    ..#....##..#....#.#.......#....
    ...#.....#....#.........#......
    .#......#.#....#.#........#....
    .......#......#.....#.#..#.....
    #......#.........##.##.#...#...
    ..#.###...................#....
    ....#..#....##.#........#....#.
    ...........#..........#......#.
    .#..#.#...###..........#..#...#
    ...#...##..#....#...#..........
    .#........#.................##.
    ....#.......##....#...#........
    #.#...##.##...#.#.......#...#..
    .....#.#.##.#......#..#..##....
    .....##...#.#.....#...#........
    #.#.......#..#..........##.....
    ................#......#..#.#.#
    #......#...#...................
    ...#.....##.#.........#.#..#..#
    ...#..##..##.......#....#......
    ....##...#....#..#...........#.
    ..#..#......#...#..#...........
    ...#.##....#...##.......#......
    .......#....#..#..##..#..#....#
    .#.................#.#...#.##..
    .....#..................#..#.#.
    ...#......##...#...........#...
    ..#.........#....#..#...#.....#
    ..#...#.....#.........##.#.....
    .....#.#....##...............#.
    ....#...#............#.........
    .....#.....###............#....
    ..#.#.#.......#....#...........
    ...........##...##...#.......#.
    .........###.#......#..........
    .#.......#....#.....#.##..#...#
    ..#..................#..###....
    ..#....#...#......##.........#.
    ........#..#........#.........#
    .#..#......#.........#.........
    ...#..##.....#....#....#.....#.
    ......#.#............###.....##
    .......#........#.......#.#....
    ..#.............#..............
    .............##..#.#.#....#....
    .................#....#.#......
    ##..#.#.......#....#.....#.....
    .##............##.#.......#.#..
    #..#...........##......#.......
    .##......#####..##.#....#.#....
    .......##.....#...#........#...
    .#.#.....##....#..#....#..#...#
    ............##.#.....##.#......
    ........##...###.#......#......
    ......#..#.#...#..#............
    .........#...........#......#..
    .#.........#............##.....
    .#..#..#...#.#.............#...
    ......#.#..##...#.#...........#
    #.##.......#...#.........#.....
    .....#..#............#....##...
    .#......#........#.............
    ..#...#....#..#.......###......
    ....#.......###.#.#...........#
    .............#...##............
    .##.#.#.#...........#...#....#.
    ............##.........#......#
    ...............#......#...#....
    ...#.....#..###..#...........#.
    .#........#.....##........#.#..
    ....#.#.......#..#..#...##.#.#.
    .......##...........#...#......
    ....#.#..##......#.......#.....
    ..#........#.#......#.#........
    ........#....#..#....#..##.....
    .#.........##..........#.#.....
    ..##...##.....##......##..#....
    .###.....##...........##.#...##
    ...#................#.......#..
    #.......#.#.#..#.#.##..#...#...
    .#.#.......#..#................
    ..#.#.#......#............#....
    #.....#.###..#.#...#...........
    #...........#..........#.#.#.##
    ..#.#...#......##.....#........
    ........#.......#.#...#...#....
    ..#..........#......###......#.
    ..........##.#....#.....#.##...
    ..#.....#......#.........#..##.
    .#...#........#..#.#..#...##..#
    ..###........#......#.#........
    ..#.##.#....#.#....#.#...#....."""

    pattern = pattern.replace(" ", "").split("\n")


    def addLine(line, move):
        if move > len(line)-1:
            line = line + line
            return addLine(line, move)
        else:
            return line


    def checkTrees(right, down):
        count = 0
        move = 0
        i = 0
        while i < len(pattern):
            if move < len(pattern[i]):
                if pattern[i][move] == "#":
                    count += 1
                move += right
            else:
                pattern[i] = addLine(pattern[i], move)
                if pattern[i][move] == "#":
                    count += 1
                move += right
            i += down
        return count


    print("Question 3 part2")
    print(checkTrees(1, 1) * checkTrees(3, 1) * checkTrees(5, 1) * checkTrees(7, 1) * checkTrees(1, 2))

    # Question 4 part 1
    passport = """iyr:1928 cid:150 pid:476113241 eyr:2039 hcl:a5ac0f
ecl:#25f8d2
byr:2027 hgt:190

hgt:168cm eyr:2026 ecl:hzl hcl:#fffffd cid:169 pid:920076943
byr:1929 iyr:2013

hgt:156cm ecl:brn eyr:2023
iyr:2011
hcl:#6b5442 pid:328412891 byr:1948

byr:1950 iyr:2019 eyr:2020 ecl:amb cid:279 pid:674907993 hgt:189cm hcl:#602927

byr:1976
ecl:hzl iyr:2015 hgt:178cm eyr:2022 hcl:#341e13
pid:473630095

iyr:2020 eyr:2023 ecl:blu byr:1984
hgt:163cm hcl:#866857 pid:628113926

ecl:amb
pid:312508073
hgt:70in byr:1922 iyr:2019 eyr:2030 hcl:#866857

hcl:#007d7c pid:195125455 cid:213 hgt:154cm eyr:2021 ecl:grn byr:1981

ecl:oth hgt:185cm pid:958027833 hcl:#b6652a iyr:2028 cid:171
eyr:1994

ecl:hzl byr:1982 hcl:#fffffd hgt:188cm iyr:2018 pid:039931872 cid:288 eyr:2025

cid:71 iyr:2012 byr:1950 hcl:#7d3b0c pid:803324747 eyr:2023 hgt:151cm ecl:oth

iyr:2013
ecl:grn eyr:2022
pid:053411982 byr:1946 cid:302 hcl:#60ca85
hgt:160cm

hgt:169cm eyr:2035 pid:023983645 iyr:2014 ecl:amb hcl:#c0946f byr:1975 cid:258

byr:1933 ecl:hzl
hcl:#c0946f iyr:2013 pid:655452550
hgt:170cm
eyr:2024

hgt:156
ecl:oth
cid:235
pid:609823906 iyr:2016 eyr:2021 hcl:#6b5442
byr:1932

iyr:2006
hgt:103 ecl:#2d77e5 cid:214 byr:2018 hcl:6c53a4 pid:190cm eyr:1940

ecl:grn
pid:497830156 byr:2002 eyr:2023 hgt:169cm iyr:2016 hcl:#733820

ecl:gmt hgt:75cm byr:2007 eyr:2037 iyr:2028 hcl:4591f6 cid:118

cid:94
ecl:hzl byr:1972 hcl:#7d3b0c iyr:2015 pid:219956257
eyr:2022 hgt:165cm

eyr:2022 hgt:180cm ecl:amb hcl:#c0946f
pid:543330083
iyr:2014
cid:286 byr:1989

ecl:hzl eyr:2027 iyr:2019 pid:125201586
byr:1947 cid:74 hcl:#341e13

iyr:2020 hgt:192cm ecl:oth
pid:651509606 byr:1965 eyr:2029
hcl:#b6652a

hgt:165cm eyr:2025 ecl:oth pid:844167324 byr:1950 iyr:2014 hcl:#a97842

hgt:159cm
byr:1945 hcl:#6b5442 iyr:2027
eyr:2024
cid:94 ecl:brn pid:476551927

pid:479260033 hcl:#efcc98 iyr:2018 ecl:grn
byr:1993 cid:92 hgt:165cm
eyr:2027

iyr:2015 pid:106083602
hgt:168cm eyr:2025 ecl:gry byr:1996 cid:341
hcl:#fffffd

iyr:2010 hgt:192cm
pid:247508683 ecl:#57a15d byr:1972
hcl:#602927 eyr:2024

ecl:blu byr:1934 hcl:#888785 iyr:2019 pid:905361316 eyr:2021 hgt:150cm

hgt:184cm hcl:#cfa07d cid:335 iyr:2018 byr:1995
ecl:grn eyr:2026 pid:435090537

pid:302395756
ecl:grn hcl:z byr:2005 hgt:111 eyr:2031 cid:147

ecl:gry pid:561021264 cid:178 byr:1980 iyr:2010
eyr:2028 hcl:#7d3b0c hgt:181cm

hgt:172cm byr:1923 pid:741415636 ecl:grn eyr:2022 iyr:2013

pid:457776708
byr:1992
hcl:#b6652a hgt:157cm eyr:2024 iyr:2011

pid:177860177
ecl:blu
hgt:154cm hcl:#cfa07d iyr:2015 eyr:2022
byr:1977

pid:992814815 eyr:2028 iyr:2017 hgt:181cm hcl:#cfa07d
byr:1961 ecl:hzl

eyr:2025 hcl:#a97842
byr:1930 pid:468404395
iyr:2013 ecl:oth cid:220 hgt:170cm

cid:198
iyr:2018 hcl:#a97842 hgt:74in
pid:279483949 eyr:2029 ecl:gry byr:1931

byr:2004 iyr:2021 pid:165cm ecl:#7e7d04
hcl:#18171d
eyr:2035 hgt:61

ecl:#492a33
hgt:168cm
iyr:2018
byr:2017 cid:293
pid:1764204298 hcl:#cfa07d eyr:2022

hcl:#866857
eyr:2026
cid:193 hgt:160cm byr:1970 iyr:2011 ecl:amb pid:895650554

eyr:2022
iyr:2018
hcl:#efcc98 cid:181
byr:2029 ecl:utc hgt:188cm pid:332630362

hcl:#ceb3a1
iyr:2013 pid:592603167
cid:95 ecl:blu eyr:2022

hcl:#efcc98
iyr:2011 pid:550968343
ecl:hzl byr:1924 eyr:2022
hgt:191cm cid:120

hgt:150cm ecl:grn
hcl:8f3824 pid:735766540 eyr:2029
byr:2000 iyr:2015

hcl:z
ecl:hzl byr:2003 hgt:118 eyr:2008 iyr:2022
pid:157cm

byr:1950 ecl:blu hgt:163cm
pid:455597862 cid:302 eyr:2027
hcl:#341e13 iyr:2015

iyr:2015 ecl:oth eyr:2023 byr:1998 hcl:#ceb3a1 cid:136 pid:253146183
hgt:179cm

iyr:2018 hcl:#cfa07d cid:80
pid:347839572 byr:1946 eyr:2023 ecl:blu
hgt:163cm

iyr:1969 cid:324 eyr:1927 ecl:lzr
hcl:z
byr:2030 hgt:172cm
pid:#997235

iyr:2017 ecl:brn
hgt:165cm
pid:818623102 byr:1968 hcl:#fffffd eyr:2020

eyr:2023 byr:1966 ecl:blu
cid:295 pid:347753668
hcl:#c0946f
iyr:2010 hgt:163cm

hcl:#ceb3a1 pid:395843182 hgt:168cm eyr:2025 iyr:2014 byr:1991 ecl:gry cid:283

iyr:2011 byr:1928 pid:438089427
hgt:152cm
ecl:hzl eyr:2022 cid:254 hcl:#866857

iyr:2015
hcl:#ceb3a1
ecl:lzr eyr:2022 hgt:173cm pid:1799325911 cid:210 byr:2018

iyr:2010
pid:121142355
eyr:2020
cid:302
hgt:158cm ecl:amb
byr:1978 hcl:#623a2f

pid:110863702
hcl:#341e13 iyr:2017 byr:1942 hgt:175cm cid:277 eyr:2030
ecl:amb

hcl:#c0946f
pid:473360783 byr:1986
hgt:159cm ecl:brn
iyr:2011 eyr:2023

iyr:2015 hcl:#733820 pid:245692263
ecl:oth byr:1960 eyr:2022

hcl:b9c0fd iyr:1996 hgt:83
byr:2029 pid:#449a30
ecl:grt eyr:1925

hgt:68cm
eyr:2039 hcl:#cfa07d
pid:193cm iyr:1984
ecl:#b9ec76

eyr:2023 ecl:amb
byr:1942
iyr:2012 hcl:#b6652a hgt:156cm pid:398126488

ecl:oth hgt:150cm byr:1937 pid:927692980 iyr:2013 eyr:2023 hcl:#623a2f

eyr:2026 byr:1921 pid:297672804 hgt:172cm iyr:2011 ecl:brn

eyr:2026 cid:241
hcl:#341e13
pid:316611397 hgt:193cm
byr:1977

pid:509492550 hgt:64cm eyr:2030 hcl:#b6652a byr:1986 iyr:1922 ecl:gry

hgt:165cm cid:248 hcl:#6b5442 eyr:2026
pid:703744314
byr:1921 iyr:2020
ecl:blu

byr:2001 pid:332016728
iyr:2018 cid:89
eyr:2031 hgt:155cm ecl:zzz
hcl:#866857

byr:2023
hcl:z pid:3586415546 iyr:2022 cid:209 hgt:188in ecl:brn

ecl:grn
hgt:61in iyr:1925 byr:1984 hcl:#733820
pid:216995428 eyr:1944

byr:1969 hcl:#a97842 cid:226
iyr:2011 pid:621770561
eyr:2024 ecl:blu

hcl:#efcc98 eyr:2024
iyr:2010 ecl:hzl
pid:153620883 byr:1957

iyr:2015
cid:162 eyr:2020
pid:89806820 byr:1955
hcl:b043dd ecl:brn

hgt:162cm
hcl:2ee8db
byr:2008 iyr:2003 pid:50279629 eyr:2030 ecl:grt

pid:939011546 byr:1945
hgt:70in hcl:#cfa07d eyr:2027 ecl:grn iyr:2015

hgt:83 ecl:hzl hcl:z eyr:2026 byr:2029

cid:244 hcl:#623a2f iyr:2012 pid:527925497
byr:1957
eyr:2024 ecl:brn

hgt:179cm
byr:1928
pid:933893768 hcl:#18171d ecl:gry iyr:2016 eyr:2027

hgt:158cm iyr:2017 ecl:brn byr:1935 eyr:2020
pid:331047535 cid:345 hcl:#888785

byr:2009
ecl:#893922
iyr:2020 hcl:a59633 hgt:170in eyr:1995
pid:28540793

byr:1955 hgt:68cm
hcl:#67dac3 eyr:2031 pid:502641687 ecl:oth iyr:1922

pid:2523045951 cid:203 hgt:75cm eyr:2031 hcl:#888785
iyr:1937 byr:1988

pid:558076850 eyr:2030
hgt:192cm ecl:brn
cid:296 byr:1954
hcl:#733820 iyr:2012

cid:272 eyr:2030 pid:044961585
hcl:#602927 byr:1990 hgt:173cm ecl:gry iyr:2018

byr:1958 iyr:2019 hgt:163cm eyr:2029
pid:384542472 hcl:819959
ecl:#866be8

iyr:2027
pid:7267919678 byr:2013 hgt:161in hcl:z ecl:brn

pid:855195796 ecl:oth
eyr:2030 hgt:163cm hcl:#341e13 byr:1978
iyr:2011 cid:206

ecl:brn eyr:2029 hcl:#fffffd iyr:2018 pid:065149883 byr:1938 hgt:178cm

eyr:2024
byr:1983
ecl:gry
hgt:154cm
iyr:2019
pid:#f331f5 hcl:#7d3b0c cid:315

ecl:brn pid:131551626 iyr:2013 eyr:2022 byr:1949
hgt:155cm hcl:#18171d

cid:203 eyr:2028 iyr:2019
byr:1939
hcl:#18171d pid:091534428 hgt:175cm

byr:1921 eyr:2025 iyr:2014 pid:719127279 ecl:brn hcl:#cfa07d cid:243 hgt:176cm

byr:1976 hgt:182cm
ecl:gry pid:534666141
iyr:2019 eyr:2027 cid:197 hcl:#602927

byr:2015
pid:164cm hgt:90 eyr:2036 iyr:1947 hcl:b7b0e6 ecl:#fd96b3

eyr:2029 cid:264 pid:931433692
byr:1974 ecl:oth hcl:z hgt:67in iyr:2012

pid:179cm ecl:#00a56d
eyr:2025 hcl:eed83e iyr:1949 hgt:177in

hgt:159cm ecl:blu
pid:5642951907 iyr:2029 byr:1952
hcl:#6b5442

ecl:amb hgt:163cm
pid:811866600 byr:1952
iyr:2019 hcl:#888785
cid:250 eyr:2027

byr:1953 hgt:190cm
pid:156cm hcl:#7d3b0c eyr:2022 ecl:#1b0b35 iyr:2015

pid:709465009 byr:1971 iyr:2018 hcl:#602927 ecl:oth
cid:222 eyr:2025

hcl:#623a2f pid:583448566
byr:1999
eyr:2026 hgt:179cm
iyr:2015 ecl:gry cid:55

hgt:179cm iyr:2013 ecl:amb hcl:#95766f pid:620956072
byr:1997 eyr:2026

ecl:blu iyr:1924 pid:866797032 hgt:193cm cid:90 hcl:#fffffd eyr:1998 byr:1990

hcl:#733820 ecl:brn byr:1950 eyr:2028
hgt:155cm iyr:2017
pid:605542221

hgt:171cm iyr:2019 byr:1930
ecl:hzl
eyr:2026 hcl:#a6ef22 pid:294449839

pid:480248391
hgt:150cm eyr:2027 cid:226 hcl:#cfa07d
byr:1940 ecl:brn
iyr:2018

hcl:z ecl:#769ca0 pid:180cm
byr:1922 iyr:2026 eyr:2028
hgt:180cm

ecl:lzr byr:1967 pid:50313895 hcl:34441e hgt:158in iyr:2030 eyr:2039

iyr:2025
pid:2210753 byr:2010 hgt:173cm cid:208
eyr:2008 hcl:de66d6
ecl:grt

iyr:2018 eyr:2026
cid:289 byr:1992
hgt:170cm pid:856187601 ecl:gry hcl:#efcc98

cid:94 byr:1934 hgt:59in eyr:2022
hcl:#623a2f pid:573884719
iyr:2016 ecl:oth

pid:206185815 ecl:grn hcl:#cfa07d eyr:2027
iyr:2018 byr:1989
hgt:176cm

hgt:175cm byr:1999
pid:409477026
hcl:#cfa07d
ecl:amb eyr:2021 iyr:2017 cid:75

byr:2018
cid:150 eyr:2033 pid:043853978 iyr:2017 hgt:61cm hcl:z
ecl:#f19d87

pid:549507973 hgt:178cm byr:1929 ecl:oth
iyr:2020 eyr:2025
hcl:#7d3b0c

iyr:2014 hgt:171cm ecl:blu byr:1999
hcl:#6b5442 pid:813505466
eyr:2029

ecl:zzz eyr:2034
byr:2022
pid:52407584 iyr:2016 hcl:#888785
hgt:176in

ecl:oth
byr:1994 iyr:2018 hgt:64in pid:136896463
eyr:2022
hcl:#a97842

ecl:#535e3c hgt:84
eyr:1963 hcl:z
iyr:1986 pid:187cm byr:2028 cid:258

eyr:2029
cid:257 hgt:175cm
ecl:oth iyr:2016
hcl:#602927 pid:506432649

iyr:2015 hgt:165cm
ecl:gmt cid:116 hcl:z
byr:1998
eyr:2021
pid:170cm

iyr:2023 hgt:178cm cid:109 pid:#6eca6e hcl:#7d3b0c eyr:1961
ecl:xry byr:2012

eyr:2025
ecl:grn
pid:708755870 hgt:189cm hcl:#e23d5f
iyr:2017 byr:1982

hcl:#866857 pid:85618849 ecl:brn byr:1958 eyr:2025
hgt:111
cid:190

hgt:75cm byr:1983 iyr:2000
eyr:2007
cid:307
pid:227345093 ecl:#080923 hcl:#ceb3a1

hcl:#602927
ecl:oth hgt:158cm byr:1992 iyr:2012 pid:708206240
eyr:2026 cid:125

eyr:1920 pid:873476029 hgt:192cm byr:1971 ecl:gry iyr:2020 hcl:#f463f6

pid:295847270 hcl:#7d3b0c ecl:oth iyr:2015
byr:2000 hgt:181cm eyr:2025

hgt:189cm
hcl:#18171d iyr:2013
pid:686835652 byr:1972
ecl:grn eyr:2029

iyr:2010
ecl:grn hgt:63cm eyr:2027 hcl:#602927 pid:240973955 byr:1984 cid:280

pid:883408516 eyr:2022
iyr:2010 hgt:182cm ecl:hzl byr:2000 cid:220

iyr:2018 pid:026680847 cid:117 hcl:#602927 hgt:67cm ecl:xry eyr:2030
byr:1989

byr:1933 ecl:hzl
hgt:179cm
pid:500053352 eyr:2020 hcl:#fffffd
iyr:2014

hgt:153cm
pid:523083973 ecl:brn
iyr:2011 byr:2000 hcl:#cfa07d
eyr:2020 cid:114

hcl:#efcc98 ecl:blu
byr:1974 iyr:2019
hgt:165cm
eyr:2020 pid:755433303

eyr:2022
ecl:amb byr:1927 iyr:2012 pid:409960222 hcl:#733820 hgt:169cm cid:336

ecl:#564a01
hgt:136 iyr:1984
pid:#646419
eyr:2032
hcl:z

hgt:71in hcl:14d37b
byr:2017 cid:243 ecl:zzz pid:208245975
iyr:2029

byr:1974 hcl:#6b5442 pid:562222331 hgt:68in
cid:319
ecl:grn
iyr:2012 eyr:2028

iyr:2010 byr:1948 hgt:169cm eyr:2022 hcl:#623a2f
cid:93 ecl:hzl

cid:347
byr:1939 hgt:151cm eyr:2026
iyr:2010
hcl:#fffffd ecl:gry
pid:562919031

hgt:171cm
iyr:2010 pid:812511153 byr:1971 eyr:2026 ecl:hzl
hcl:#6b5442

cid:319 eyr:2026 iyr:2013
hgt:155in
hcl:z pid:185cm

hgt:178cm ecl:gry cid:139 hcl:#341e13 pid:390510619 eyr:2026 iyr:2012
byr:1952

eyr:2025 pid:78761845
hcl:#866857 iyr:2019
hgt:173cm ecl:blu byr:1936

eyr:2028 hgt:192cm
byr:1946 pid:897533472 ecl:brn hcl:#efcc98

pid:467427172 hcl:#efcc98
eyr:2021 byr:1923
iyr:2012 cid:139 hgt:176cm

iyr:2015 eyr:2028
pid:069618718
hgt:190cm ecl:grn hcl:#888785
byr:1956 cid:68

ecl:brn hgt:173cm eyr:2022
iyr:2010 pid:525711593 byr:1990

cid:292
ecl:blu hcl:#602927 hgt:67in iyr:2011 byr:1990 eyr:2027 pid:298224903

hgt:159cm eyr:2029 pid:854089988 iyr:2018 ecl:gry byr:1962 hcl:#efcc98

ecl:grn byr:1964 eyr:2022
hgt:61in pid:202756433 hcl:#cfa07d cid:241
iyr:2015

hgt:68in byr:1973 hcl:#18171d ecl:hzl
pid:701847555 eyr:2030 iyr:2019

eyr:2022
ecl:grn hgt:151cm iyr:2020 hcl:#83f878 byr:1982 pid:816902510

cid:130 hgt:187in eyr:2040
ecl:brn
iyr:2020
hcl:z pid:7364218001
byr:1949

hgt:183cm
eyr:2023 iyr:2019 byr:1946 pid:684966686
cid:307 ecl:brn hcl:#cfa07d

hcl:#6b5442 eyr:2024 pid:7727182081
iyr:2017
hgt:110 ecl:dne

ecl:blu byr:1987 cid:167 iyr:2015 hgt:189cm
pid:797675433 eyr:2024 hcl:#6b5442

iyr:2018 byr:1929 ecl:brn hgt:60in eyr:2024 pid:152cm hcl:#a97842

iyr:2020 eyr:2025 byr:1942 pid:007017276 ecl:oth hgt:170cm
hcl:#ceb3a1 cid:104

iyr:2012 ecl:oth eyr:2020
byr:1965 hcl:#efcc98
hgt:173cm
cid:102 pid:302599543

hgt:187cm pid:958933966
ecl:hzl byr:1955
eyr:2027 hcl:#6b5442

ecl:oth iyr:2013
eyr:2027 hgt:153cm cid:86 hcl:#602927
pid:568040159 byr:1926

hgt:187cm iyr:2008 pid:151cm ecl:blu eyr:1954

byr:2014
pid:9029821667 hgt:59cm eyr:2035 hcl:e9c79a
iyr:2010

eyr:2027 pid:#d676d0
hcl:d2fcfa hgt:154cm ecl:hzl byr:1938

ecl:lzr hgt:61in eyr:2025
pid:556812665
byr:1923 iyr:2019
hcl:e962ed

iyr:2019
eyr:2029
hcl:#866857 byr:1977 pid:115229656 hgt:193cm
ecl:brn cid:350

hcl:z pid:#8d311d iyr:2023 hgt:71cm
byr:1923 ecl:zzz eyr:2039

cid:66 hgt:165cm
eyr:2027 iyr:2012 hcl:#b6652a ecl:amb pid:946987379 byr:1999

byr:2028 iyr:2013 ecl:#376cda
eyr:1928 pid:#c135ce hcl:z hgt:185in

hcl:100344 iyr:1933 eyr:2023 hgt:71cm byr:2010 ecl:#6a8007 pid:90001213

iyr:2012
byr:1987 eyr:2020 hgt:190cm cid:298 hcl:#866857

hgt:161cm hcl:#efcc98 ecl:grn eyr:2028 iyr:2014
byr:1966 pid:769989459

hgt:173cm pid:527615519 eyr:2024 hcl:#602927 byr:1949 ecl:oth cid:328

pid:679489285
hgt:153cm byr:1963
hcl:#602927 eyr:2026 ecl:blu

ecl:blu hgt:186cm hcl:#c0946f pid:741255292 eyr:2022 byr:1996 iyr:2017

hgt:172cm
hcl:#888785 eyr:2022 pid:377797887 byr:1980

hcl:z pid:399837694 iyr:2018 ecl:#33e59d eyr:2038
hgt:60in

eyr:2027
byr:1923
hgt:170cm pid:754104917
iyr:2020 cid:135 hcl:#341e13
ecl:brn

ecl:grn hcl:#c0946f
byr:2028 iyr:2016 pid:950191991
hgt:193cm cid:93
eyr:1935

ecl:brn hcl:#733820 eyr:2024
iyr:2017 pid:450063924
byr:2000 hgt:172cm

iyr:2008
cid:229 byr:2023 eyr:2022 hcl:#341e13
ecl:grn
hgt:70in pid:104660281

eyr:2023 hgt:181cm cid:289 pid:828542447
iyr:2013 ecl:grn byr:1922 hcl:#866857

iyr:2030 pid:152cm cid:297 ecl:#75a512 hcl:z hgt:156in byr:2006
eyr:2035

iyr:2012 hcl:#18171d eyr:2025 hgt:188cm
ecl:blu byr:1976

iyr:2018 hgt:157cm hcl:#b6652a
ecl:oth byr:2002 eyr:2023

cid:161
hcl:#b6652a iyr:2016
byr:1930 ecl:oth pid:000425745 hgt:167cm eyr:2022

hgt:160cm hcl:#89f1a0 eyr:2023 pid:867868252 byr:1976 iyr:2019 ecl:hzl

byr:1966 ecl:grn pid:597443937
iyr:2014 eyr:2029

pid:306301971 ecl:#a145cc
hcl:z iyr:2018 cid:325 eyr:2023 byr:1942 hgt:157cm

ecl:brn
pid:771134604 hgt:160cm
byr:1961 eyr:2020
iyr:2012 hcl:#6b5442

iyr:1922
ecl:gmt
eyr:1963
pid:#d1a6f3 hcl:z byr:2015 hgt:153in

eyr:2022 ecl:gry
hgt:156cm
pid:640711969
hcl:#cfa07d

ecl:grn
eyr:1980 pid:385212564 hcl:5b27f7 hgt:160cm iyr:2016 cid:171 byr:1990

iyr:2020
cid:212 pid:959667791 byr:2002 ecl:amb
hgt:75in eyr:2026 hcl:#888785

byr:1969 eyr:2021
iyr:2012
pid:318752605 hgt:179cm
cid:81 hcl:#888785

byr:1926 hcl:#c0946f iyr:2010 hgt:155cm ecl:gry pid:475722917
eyr:2030

eyr:2025
ecl:grn byr:1980 iyr:2010 hgt:160cm hcl:#d03ef0 pid:474973131

eyr:2020 iyr:2012 hgt:150cm
hcl:#c0946f
byr:1924 ecl:amb

iyr:2016 hgt:173cm eyr:2029
hcl:#888785 ecl:hzl byr:2001 cid:334 pid:291454183

iyr:2013
pid:909258239 byr:1970
ecl:utc eyr:2026
cid:312 hgt:158cm
hcl:#18171d

ecl:grn
byr:1941 pid:395943714
eyr:2027
hcl:#7d3b0c
iyr:2011 hgt:158cm

ecl:amb hcl:#fffffd
byr:1992
pid:266072435
eyr:2028 iyr:2020 hgt:161cm

hcl:de3776 eyr:2021
cid:234 ecl:#160982
iyr:2017 byr:1992

byr:1979 iyr:2020 ecl:brn
hcl:#6b5442
pid:492860333 hgt:168cm eyr:2030

eyr:2025 hcl:#fffffd pid:776551474
ecl:hzl hgt:169cm
iyr:2017

ecl:hzl
eyr:2029
iyr:2013 byr:1952 hgt:152cm
pid:968064648 hcl:#6b5442

byr:1955
pid:947711080
cid:149 ecl:amb
hgt:150cm
hcl:#341e13 eyr:2022 iyr:2016

hgt:71cm ecl:#c6c47f
byr:2028 iyr:1994 eyr:2030 pid:0684877002 cid:237 hcl:#341e13

eyr:2030 hcl:#a97842 hgt:188cm byr:2000 pid:262013450
iyr:2018

hgt:74in byr:1955 ecl:blu iyr:2012 hcl:#341e13 pid:165688658

hgt:176cm cid:346 iyr:2012
pid:322396589
ecl:gry eyr:2029
byr:1976
hcl:#888785

eyr:2021
iyr:2015 hcl:3a6401 byr:1997 ecl:blu pid:188cm hgt:166in

ecl:blu iyr:2010 byr:1984 hgt:183
pid:306571244 hcl:#623a2f eyr:2033 cid:113

ecl:#804adb byr:2004 hgt:181cm
hcl:#623a2f
eyr:2040 pid:#57e9d1
iyr:2028 cid:97

iyr:2015 pid:294753454 byr:1980 eyr:2020
hgt:76in
ecl:oth
hcl:#a97842

hcl:#a7a05c pid:0137262572 eyr:2023 cid:350 iyr:2015
ecl:#52d3fe hgt:190cm
byr:2007

pid:826827136 eyr:2030 ecl:brn byr:1946 hcl:#a97842 iyr:2018
hgt:173in

byr:1967
iyr:2015 pid:142177822 hgt:157cm ecl:oth eyr:2024 cid:221

iyr:2012 byr:1942 cid:187 pid:886132093
hgt:158cm ecl:hzl hcl:#1bc909

pid:490847399
byr:1963
hgt:69in
iyr:2011 ecl:gry
eyr:2027 hcl:#e4f497 cid:87

iyr:2014 ecl:hzl hgt:159cm hcl:#c0946f eyr:2028 byr:1926 pid:007819051

hcl:#cfa07d pid:639664506 ecl:amb
byr:1997 cid:137 iyr:2014 eyr:2030 hgt:67in

hgt:191in
eyr:2025
cid:128
byr:2021 iyr:2015
hcl:5ed1ae ecl:lzr
pid:406311551

eyr:2035
ecl:gmt hcl:71e1ef iyr:2023
pid:4347854 byr:2017

hgt:169cm
eyr:2028
ecl:oth iyr:2016 byr:1954
pid:662755630 hcl:#733820

eyr:2029 pid:664032828 hgt:185cm hcl:#fffffd byr:1991 ecl:grn iyr:2017

pid:240747543 hgt:190cm
hcl:#18171d iyr:2013 eyr:2021 ecl:grn byr:1920

iyr:2024 pid:87644548 hgt:126
byr:1971 ecl:brn
eyr:2040

iyr:2020
ecl:lzr byr:2014 eyr:2027 pid:976290173
hcl:#efcc98
hgt:192in

pid:112431133 byr:1950 hgt:174cm
iyr:2020
cid:118 hcl:#341e13 eyr:2023 ecl:amb

pid:034858755
hcl:#d93689 iyr:2012 eyr:2025
hgt:67cm
ecl:brn byr:2027
cid:306

eyr:2024 hcl:#fffffd ecl:hzl hgt:188cm cid:199 byr:2015 pid:983962091 iyr:1937

hcl:#c0946f pid:899925634
eyr:2025 byr:2020
iyr:2016
ecl:grt hgt:173cm

hgt:59cm hcl:c5b2d7 byr:2008 iyr:2027
ecl:lzr pid:155cm
eyr:2035

iyr:2014
eyr:2022 pid:850258746 hcl:#a97842 byr:2022 ecl:brn hgt:178cm

cid:214 iyr:2017
ecl:oth
hcl:#866857 byr:1995 pid:793515973 hgt:193cm eyr:2023

hcl:#18171d
iyr:2017 hgt:193cm cid:183 eyr:2025 pid:728034540 ecl:hzl byr:1969

eyr:2025 ecl:gry byr:2002 iyr:2019 hgt:174cm pid:603301922
hcl:#fffffd

byr:2002
cid:98 pid:828911903 eyr:2030 ecl:blu hgt:65in hcl:#74b1dc

byr:1969 hcl:#a97842 ecl:gry eyr:2027 pid:835656333 hgt:152cm cid:324 iyr:2014

pid:848442741 eyr:2030 hcl:#ceb3a1 byr:1984 iyr:2019 ecl:grn hgt:164cm

hcl:#341e13 iyr:2019 hgt:166cm pid:419840849 byr:1974 eyr:2026 cid:211

byr:1945 pid:646444288 iyr:2020
eyr:2023 hgt:186cm

pid:375892516
hgt:187cm
iyr:2010 eyr:2028 byr:1972 cid:272 ecl:blu hcl:#888785

hgt:181in
ecl:grn eyr:2034
hcl:#7d3b0c byr:2018
pid:206240985 iyr:2015

hgt:177 eyr:1973 pid:83092851 cid:92 ecl:utc byr:2023 hcl:z iyr:1948

eyr:2029 pid:1655089174 ecl:grn hgt:158cm iyr:2011 hcl:#b6652a byr:1926
cid:158

hcl:#341e13
iyr:2006
byr:2008 hgt:185 eyr:2024 ecl:utc

hgt:171cm
pid:533365287 byr:1957 hcl:#ceb3a1 iyr:2014 ecl:amb eyr:2020
cid:184

hcl:#b6652a
pid:553897602 iyr:1929 ecl:grn cid:191 hgt:178cm byr:1991 eyr:2024

byr:1994 hgt:152cm pid:198152466
eyr:2022 ecl:hzl hcl:#4df239 iyr:2020

ecl:grn
eyr:2022
byr:1968 iyr:2017 pid:044109096

hcl:#d257c7 eyr:2036
iyr:2018
ecl:#5b11eb
byr:1950"""

    passport = passport.split("\n\n")
    total = len(passport)
    field = ["byr" ,"iyr","eyr" ,"hgt" ,"hcl","ecl" ,"pid"]

    for ppl in passport:
        for check in field:
            if check not in ppl:
                total = total -1
                break
    print("Question 4 part 1")
    print(total)

    # Question 4 part 2
    passport = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
    passport = passport.split("\n\n")
    count = 0
    valid = passport
    field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for ppl in passport:
        check = 0
        if ""









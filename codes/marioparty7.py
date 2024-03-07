# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSeven(amount):
    return f'''
MP7 - Blue Spaces Give SEVENBLUE Coins
04168578 60000000
0416857C 3880{amount}
'''

def getRedSpaceCodeSeven(amount):
    return f'''
MP7 - Red Spaces Take Away SEVENRED Coins
04168600 60000000
04168604 3880{amount}
'''

def getCharacterSpaceCodeSeven(amount):
    return f'''
MP7 - Character Spaces Give SEVENCHARACTER Coins
C21685B8 00000001
3880{amount} 00000000
'''

def getMinigameCodeSeven(amount):
    return f'''
MP7 - Minigames Award SEVENMINIGAME Coins
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290CCA 0000000A
02290CCA 0000{amount}
E2000001 80008000
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290DDA 0000000A
02290DDA 0000{amount}
E2000001 80008000
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290EEA 0000000A
02290EEA 0000{amount}
E2000001 80008000
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290FFA 0000000A
02290FFA 0000{amount}
E2000001 80008000
'''

def getStarSpaceCodeSeven(amount):
    return f'''
MP7 - Stars Cost SEVENSTAR Coins
04188774 3B80{amount}
204E0640 38030001
044E0644 1C00000A
044E0574 3800{amount} 
044E08D8 3800{amount}
044E09B8 1C00000A
044E0BAC 38A0{amount}
044E0C8C 1C60000A
E2000001 80008000
'''

def getStarSpaceCodeSevenLastFive(amount):
    return f'''
MP7 - Stars Cost SEVENSTLASTFIVE Coins During the Last 5 Turns Event
0418876C 3B80{amount}
'''

def getHammerBroSpaceCodeSeven(amount, negAmount, halfAmount):
    return f'''
MP7 - Hammer Bro Takes SEVENHAMMERBRO Coins
041A902C 3AC0{amount}
041A9A28 38A0{negAmount}
041A973C 38000000
041A9744 3800{halfAmount}
041A974C 38000000
041A9754 3800{halfAmount}
'''

def getZapSpaceCodeSeven(amount):
    return f'''
MP7 - Zap Takes SEVENZAP Coins
C21B652C 00000001
3880{amount} 00000000
'''

def getFlowerSpaceCodeSeven(amount):
    return f'''
MP7 - Flower Gives SEVENFLOWER Coins Per Space
041C4F24 3B40{amount}
'''

def getVacuumSpaceCodeSeven(amount):
    return f'''
MP7 - Vaccum Always Steals SEVENVACUUM Coins
041C8A34 3860{amount}
'''

def getFireballSpaceCodeSeven(amount, negAmount):
    return f'''
MP7 - Fireball Takes SEVENFIREBALL Coins
041C1464 3b80{amount}
041C148C 38A0{negAmount}
'''

def getMinigameReplacement7(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP7 - Minigame Replacement: {gameUno} ➜ {gameDos}
28291558 000000{hexUno}
02291558 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSeven(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW):
    return f'''
MP7 - Orb Modifer
042EF588 00050505
042EF58C {oneW}{oneW}{oneW}{oneW}
042EF590 {oneW}{oneW}{oneW}{oneW}
042EF594 {oneW}{oneW}0000
042EF598 01{twoP}{twoP}{twoP}
042EF59C {twoW}{twoW}{twoW}{twoW}
042EF5A0 {twoW}{twoW}{twoW}{twoW}
042EF5A4 {twoW}{twoW}0000
042EF5A8 02{threeP}{threeP}{threeP}
042EF5AC {threeW}{threeW}{threeW}{threeW}
042EF5B0 {threeW}{threeW}{threeW}{threeW}
042EF5B4 {threeW}{threeW}0000
042EF5B8 03{fourP}{fourP}{fourP}
042EF5BC {fourW}{fourW}{fourW}{fourW}
042EF5C0 {fourW}{fourW}{fourW}{fourW}
042EF5C4 {fourW}{fourW}0000
042EF5C8 04{fiveP}{fiveP}{fiveP}
042EF5CC {fiveW}{fiveW}{fiveW}{fiveW}
042EF5D0 {fiveW}{fiveW}{fiveW}{fiveW}
042EF5D4 {fiveW}{fiveW}0000
042EF5D8 05{sixP}{sixP}{sixP}
042EF5DC {sixW}{sixW}{sixW}{sixW}
042EF5E0 {sixW}{sixW}{sixW}{sixW}
042EF5E4 {sixW}{sixW}0000
042EF5E8 06{sevenP}{sevenP}{sevenP}
042EF5EC {sevenW}{sevenW}{sevenW}{sevenW}
042EF5F0 {sevenW}{sevenW}{sevenW}{sevenW}
042EF5F4 {sevenW}{sevenW}0000
042EF5F8 07{eightP}{eightP}{eightP}
042EF5FC {eightW}{eightW}{eightW}{eightW}
042EF600 {eightW}{eightW}{eightW}{eightW}
042EF604 {eightW}{eightW}0000
042EF608 0A{nineP}{nineP}{nineP}
042EF60C {nineW}{nineW}{nineW}{nineW}
042EF610 {nineW}{nineW}{nineW}{nineW}
042EF614 {nineW}{nineW}0000
042EF618 0B{tenP}{tenP}{tenP}
042EF61C {tenW}{tenW}{tenW}{tenW}
042EF620 {tenW}{tenW}{tenW}{tenW}
042EF624 {tenW}{tenW}0000
042EF628 0C{elevenP}{elevenP}{elevenP}
042EF62C {elevenW}{elevenW}{elevenW}{elevenW}
042EF630 {elevenW}{elevenW}{elevenW}{elevenW}
042EF634 {elevenW}{elevenW}0000
042EF638 0D{twelveP}{twelveP}{twelveP}
042EF63C {twelveW}{twelveW}{twelveW}{twelveW}
042EF640 {twelveW}{twelveW}{twelveW}{twelveW}
042EF644 {twelveW}{twelveW}0000
042EF648 0E{thirteenP}{thirteenP}{thirteenP}
042EF64C {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042EF650 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042EF654 {thirteenW}{thirteenW}0000
042EF658 0F{fourteenP}{fourteenP}{fourteenP}
042EF65C {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042EF660 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042EF664 {fourteenW}{fourteenW}0000
042EF668 10{fifteenP}{fifteenP}{fifteenP}
042EF66C {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042EF670 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042EF674 {fifteenW}{fifteenW}0000
042EF678 11{sixteenP}{sixteenP}{sixteenP}
042EF67C {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042EF680 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042EF684 {sixteenW}{sixteenW}0000
042EF688 14{seventeenP}{seventeenP}{seventeenP}
042EF68C {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042EF690 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042EF694 {seventeenW}{seventeenW}0000
042EF698 15{eighteenP}{eighteenP}{eighteenP}
042EF69C {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042EF6A0 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042EF6A4 {eighteenW}{eighteenW}0000
042EF6A8 16{ninteenP}{ninteenP}{ninteenP}
042EF6AC {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042EF6B0 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042EF6B4 {ninteenW}{ninteenW}0000
042EF6B8 17{twentyP}{twentyP}{twentyP}
042EF6BC {twentyW}{twentyW}{twentyW}{twentyW}
042EF6C0 {twentyW}{twentyW}{twentyW}{twentyW}
042EF6C4 {twentyW}{twentyW}0000
042EF6C8 18{twentyOneP}{twentyOneP}{twentyOneP}
042EF6CC {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D0 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D4 {twentyOneW}{twentyOneW}0000
042EF6D8 19{twentyTwoP}{twentyTwoP}{twentyTwoP}
042EF6DC {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E0 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E4 {twentyTwoW}{twentyTwoW}0000
042EF6E8 1E{twentyThreeP}{twentyThreeP}{twentyThreeP}
042EF6EC {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F0 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F4 {twentyThreeW}{twentyThreeW}0000
042EF6F8 1F{twentyFourP}{twentyFourP}{twentyFourP}
042EF6FC {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042EF700 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042EF704 {twentyFourW}{twentyFourW}0000
042EF708 20{twentyFiveP}{twentyFiveP}{twentyFiveP}
042EF70C {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF710 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF714 {twentyFiveW}{twentyFiveW}0000
042EF718 21{twentySixP}{twentySixP}{twentySixP}
042EF71C {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042EF720 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042EF724 {twentySixW}{twentySixW}0000
042EF728 22{twentySevenP}{twentySevenP}{twentySevenP}
042EF72C {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042EF730 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042EF734 {twentySevenW}{twentySevenW}0000
042EF738 23{twentyEightP}{twentyEightP}{twentyEightP}
042EF73C {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042EF740 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042EF744 {twentyEightW}{twentyEightW}0000
042EF748 28{twentyNineP}{twentyNineP}{twentyNineP}
042EF74C {twentyNineW}{twentyNineW}{twentyNineW}{twentyNineW}
042EF750 {twentyNineW}{twentyNineW}{twentyNineW}{twentyNineW}
042EF754 {twentyNineW}{twentyNineW}0000
042EF758 32000000
042EF75C 00000000
042EF760 00000000
042EF764 00000000
042EF768 33000000
042EF76C 00000000
042EF770 00000000
042EF774 00000000
042EF778 34000000
042EF77C 00000000
042EF780 00000000
042EF784 00000000
042EF788 35000000
042EF78C 00000000
042EF790 00000000
042EF794 00000000
042EF798 FF000000
042EF79C 00000000
042EF7A0 00000000
042EF7A4 00000000
'''

def getInitialItemsSeven(one, two, three, four, five, oneItem, twoItem, threeItem, fourItem, fiveItem):
    return f'''
MP7 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000030
3D808000 618C363C
1C060005 7C005A14
7C8C00AE 98830006
48164338 {one}{two}{three}{four}
{five}{one}{two}{three} {four}{five}{one}{two}
{three}{four}{five}{one} {two}{three}{four}{five}
0416796C 4BE9BCB4
'''

def getSpaceReplaceSeven1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot A)
C217942C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
60000000 00000000
'''

def getSpaceReplaceSeven2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot B)
C2179430 00000005
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 5404083C
60000000 00000000
'''

def getEventFrenzy7(ranChar1, ranSpace1, ranChar2, ranSpace2, ranChar3, ranSpace3, ranChar4, ranSpace4, ranChar5, ranSpace5, ranChar6, ranSpace6, ranChar7, ranSpace7, ranChar8, ranSpace8, ranChar9, ranSpace9, ranChar10, ranSpace10, ranChar11, ranSpace11, ranChar12, ranSpace12, ranChar13, ranSpace13, ranChar14, ranSpace14, ranChar15, ranSpace15, ranChar16, ranSpace16, ranChar17, ranSpace17, ranChar18, ranSpace18, ranChar19, ranSpace19, ranChar20, ranSpace20, ranChar21, ranSpace21, ranChar22, ranSpace22, ranChar23, ranSpace23, ranChar24, ranSpace24, ranChar25, ranSpace25, ranChar26, ranSpace26, ranChar27, ranSpace27, ranChar28, ranSpace28, ranChar29, ranSpace29, ranChar30, ranSpace30, ranChar31, ranSpace31, ranChar32, ranSpace32, ranChar33, ranSpace33, ranChar34, ranSpace34, ranChar35, ranSpace35, ranChar36, ranSpace36, ranChar37, ranSpace37, ranChar38, ranSpace38, ranChar39, ranSpace39, ranChar40, ranSpace40, ranChar41, ranSpace41, ranChar42, ranSpace42, ranChar43, ranSpace43, ranChar44, ranSpace44, ranChar45, ranSpace45, ranChar46, ranSpace46, ranChar47, ranSpace47, ranChar48, ranSpace48, ranChar49, ranSpace49, ranChar50, ranSpace50, ranChar51, ranSpace51, ranChar52, ranSpace52, ranChar53, ranSpace53, ranChar54, ranSpace54, ranChar55, ranSpace55, ranChar56, ranSpace56, ranChar57, ranSpace57, ranChar58, ranSpace58, ranChar59, ranSpace59, ranChar60, ranSpace60, ranChar61, ranSpace61, ranChar62, ranSpace62, ranChar63, ranSpace63, ranChar64, ranSpace64, ranChar65, ranSpace65, ranChar66, ranSpace66, ranChar67, ranSpace67, ranChar68, ranSpace68, ranChar69, ranSpace69, ranChar70, ranSpace70, ranChar71, ranSpace71, ranChar72, ranSpace72, ranChar73, ranSpace73, ranChar74, ranSpace74, ranChar75, ranSpace75, ranChar76, ranSpace76, ranChar77, ranSpace77, ranChar78, ranSpace78, ranChar79, ranSpace79, ranChar80, ranSpace80, ranChar81, ranSpace81, ranChar82, ranSpace82, ranChar83, ranSpace83, ranChar84, ranSpace84, ranChar85, ranSpace85, ranChar86, ranSpace86, ranChar87, ranSpace87, ranChar88, ranSpace88, ranChar89, ranSpace89, ranChar90, ranSpace90, ranChar91, ranSpace91, ranChar92, ranSpace92, ranChar93, ranSpace93, ranChar94, ranSpace94, ranChar95, ranSpace95, ranChar96, ranSpace96, ranChar97, ranSpace97, ranChar98, ranSpace98, ranChar99, ranSpace99, ranChar100, ranSpace100, ranChar101, ranSpace101, ranChar102, ranSpace102, ranChar103, ranSpace103, ranChar104, ranSpace104, ranChar105, ranSpace105, ranChar106, ranSpace106, ranChar107, ranSpace107, ranChar108, ranSpace108, ranChar109, ranSpace109, ranChar110, ranSpace110, ranChar111, ranSpace111, ranChar112, ranSpace112, ranChar113, ranSpace113, ranChar114, ranSpace114, ranChar115, ranSpace115, ranChar116, ranSpace116, ranChar117, ranSpace117, ranChar118, ranSpace118, ranChar119, ranSpace119, ranChar120, ranSpace120, ranChar121, ranSpace121, ranChar122, ranSpace122, ranChar123, ranSpace123, ranChar124, ranSpace124, ranChar125, ranSpace125, ranChar126, ranSpace126, ranChar127, ranSpace127, ranChar128, ranSpace128, ranChar129, ranSpace129, ranChar130, ranSpace130, ranChar131, ranSpace131, ranChar132, ranSpace132, ranChar133, ranSpace133, ranChar134, ranSpace134, ranChar135, ranSpace135, ranChar136, ranSpace136, ranChar137, ranSpace137, ranChar138, ranSpace138, ranChar139, ranSpace139, ranChar140, ranSpace140, ranChar141, ranSpace141, ranChar142, ranSpace142, ranChar143, ranSpace143, ranChar144, ranSpace144, ranChar145, ranSpace145, ranChar146, ranSpace146, ranChar147, ranSpace147, ranChar148, ranSpace148, ranChar149, ranSpace149, ranChar150, ranSpace150, ranChar151, ranSpace151, ranChar152, ranSpace152, ranChar153, ranSpace153, ranChar154, ranSpace154, ranChar155, ranSpace155, ranChar156, ranSpace156, ranChar157, ranSpace157, ranChar158, ranSpace158, ranChar159, ranSpace159, ranChar160, ranSpace160, ranChar161, ranSpace161, ranChar162, ranSpace162, ranChar163, ranSpace163, ranChar164, ranSpace164, ranChar165, ranSpace165, ranChar166, ranSpace166, ranChar167, ranSpace167, ranChar168, ranSpace168, ranChar169, ranSpace169, ranChar170, ranSpace170, ranChar171, ranSpace171, ranChar172, ranSpace172, ranChar173, ranSpace173, ranChar174, ranSpace174, ranChar175, ranSpace175, ranChar176, ranSpace176, ranChar177, ranSpace177, ranChar178, ranSpace178, ranChar179, ranSpace179, ranChar180, ranSpace180, ranChar181, ranSpace181, ranChar182, ranSpace182, ranChar183, ranSpace183, ranChar184, ranSpace184, ranChar185, ranSpace185, ranChar186, ranSpace186, ranChar187, ranSpace187, ranChar188, ranSpace188, ranChar189, ranSpace189, ranChar190, ranSpace190, ranChar191, ranSpace191, ranChar192, ranSpace192, ranChar193, ranSpace193, ranChar194, ranSpace194, ranChar195, ranSpace195, ranChar196, ranSpace196, ranChar197, ranSpace197, ranChar198, ranSpace198, ranChar199, ranSpace199, ranChar200, ranSpace200, ranChar201, ranSpace201, ranChar202, ranSpace202, ranChar203, ranSpace203, ranChar204, ranSpace204, ranChar205, ranSpace205, ranChar206, ranSpace206, ranChar207, ranSpace207, ranChar208, ranSpace208, ranChar209, ranSpace209, ranChar210, ranSpace210, ranChar211, ranSpace211, ranChar212, ranSpace212, ranChar213, ranSpace213, ranChar214, ranSpace214, ranChar215, ranSpace215, ranChar216, ranSpace216, ranChar217, ranSpace217, ranChar218, ranSpace218, ranChar219, ranSpace219, ranChar220, ranSpace220, ranChar221, ranSpace221, ranChar222, ranSpace222, ranChar223, ranSpace223, ranChar224, ranSpace224, ranChar225, ranSpace225, ranChar226, ranSpace226, ranChar227, ranSpace227, ranChar228, ranSpace228, ranChar229, ranSpace229, ranChar230, ranSpace230, ranChar231, ranSpace231, ranChar232, ranSpace232, ranChar233, ranSpace233, ranChar234, ranSpace234, ranChar235, ranSpace235, ranChar236, ranSpace236, ranChar237, ranSpace237, ranChar238, ranSpace238, ranChar239, ranSpace239, ranChar240, ranSpace240, ranChar241, ranSpace241, ranChar242, ranSpace242, ranChar243, ranSpace243, ranChar244, ranSpace244, ranChar245, ranSpace245, ranChar246, ranSpace246, ranChar247, ranSpace247, ranChar248, ranSpace248, ranChar249, ranSpace249, ranChar250, ranSpace250, ranChar251, ranSpace251, ranChar252, ranSpace252, ranChar253, ranSpace253, ranChar254, ranSpace254, ranChar255, ranSpace255, ranChar256, ranSpace256):
    return f'''
MP7 - Event Frenzy
28290CC4 00FF0000
0429157F {ranChar1}{ranSpace1}{ranChar2}{ranSpace2}
04291583 {ranChar3}{ranSpace3}{ranChar4}{ranSpace4}
04291587 {ranChar5}{ranSpace5}{ranChar6}{ranSpace6}
0429158B {ranChar7}{ranSpace7}{ranChar8}{ranSpace8}
0429158F {ranChar9}{ranSpace9}{ranChar10}{ranSpace10}
04291593 {ranChar11}{ranSpace11}{ranChar12}{ranSpace12}
04291597 {ranChar13}{ranSpace13}{ranChar14}{ranSpace14}
0429159B {ranChar15}{ranSpace15}{ranChar16}{ranSpace16}
0429159F {ranChar17}{ranSpace17}{ranChar18}{ranSpace18}
042915A3 {ranChar19}{ranSpace19}{ranChar20}{ranSpace20}
042915A7 {ranChar21}{ranSpace21}{ranChar22}{ranSpace22}
042915AB {ranChar23}{ranSpace23}{ranChar24}{ranSpace24}
042915AF {ranChar25}{ranSpace25}{ranChar26}{ranSpace26}
042915B3 {ranChar27}{ranSpace27}{ranChar28}{ranSpace28}
042915B7 {ranChar29}{ranSpace29}{ranChar30}{ranSpace30}
042915BB {ranChar31}{ranSpace31}{ranChar32}{ranSpace32}
042915BF {ranChar33}{ranSpace33}{ranChar34}{ranSpace34}
042915C3 {ranChar35}{ranSpace35}{ranChar36}{ranSpace36}
042915C7 {ranChar37}{ranSpace37}{ranChar38}{ranSpace38}
042915CB {ranChar39}{ranSpace39}{ranChar40}{ranSpace40}
042915CF {ranChar41}{ranSpace41}{ranChar42}{ranSpace42}
042915D3 {ranChar43}{ranSpace43}{ranChar44}{ranSpace44}
042915D7 {ranChar45}{ranSpace45}{ranChar46}{ranSpace46}
042915DB {ranChar47}{ranSpace47}{ranChar48}{ranSpace48}
042915DF {ranChar49}{ranSpace49}{ranChar50}{ranSpace50}
042915E3 {ranChar51}{ranSpace51}{ranChar52}{ranSpace52}
042915E7 {ranChar53}{ranSpace53}{ranChar54}{ranSpace54}
042915EB {ranChar55}{ranSpace55}{ranChar56}{ranSpace56}
042915EF {ranChar57}{ranSpace57}{ranChar58}{ranSpace58}
042915F3 {ranChar59}{ranSpace59}{ranChar60}{ranSpace60}
042915F7 {ranChar61}{ranSpace61}{ranChar62}{ranSpace62}
042915FB {ranChar63}{ranSpace63}{ranChar64}{ranSpace64}
042915FF {ranChar65}{ranSpace65}{ranChar66}{ranSpace66}
04291603 {ranChar67}{ranSpace67}{ranChar68}{ranSpace68}
04291607 {ranChar69}{ranSpace69}{ranChar70}{ranSpace70}
0429160B {ranChar71}{ranSpace71}{ranChar72}{ranSpace72}
0429160F {ranChar73}{ranSpace73}{ranChar74}{ranSpace74}
04291613 {ranChar75}{ranSpace75}{ranChar76}{ranSpace76}
04291617 {ranChar77}{ranSpace77}{ranChar78}{ranSpace78}
0429161B {ranChar79}{ranSpace79}{ranChar80}{ranSpace80}
0429161F {ranChar81}{ranSpace81}{ranChar82}{ranSpace82}
04291623 {ranChar83}{ranSpace83}{ranChar84}{ranSpace84}
04291627 {ranChar85}{ranSpace85}{ranChar86}{ranSpace86}
0429162B {ranChar87}{ranSpace87}{ranChar88}{ranSpace88}
0429162F {ranChar89}{ranSpace89}{ranChar90}{ranSpace90}
04291633 {ranChar91}{ranSpace91}{ranChar92}{ranSpace92}
04291637 {ranChar93}{ranSpace93}{ranChar94}{ranSpace94}
0429163B {ranChar95}{ranSpace95}{ranChar96}{ranSpace96}
0429163F {ranChar97}{ranSpace97}{ranChar98}{ranSpace98}
04291643 {ranChar99}{ranSpace99}{ranChar100}{ranSpace100}
04291647 {ranChar101}{ranSpace101}{ranChar102}{ranSpace102}
0429164B {ranChar103}{ranSpace103}{ranChar104}{ranSpace104}
0429164F {ranChar105}{ranSpace105}{ranChar106}{ranSpace106}
04291653 {ranChar107}{ranSpace107}{ranChar108}{ranSpace108}
04291657 {ranChar109}{ranSpace109}{ranChar110}{ranSpace110}
0429165B {ranChar111}{ranSpace111}{ranChar112}{ranSpace112}
0429165F {ranChar113}{ranSpace113}{ranChar114}{ranSpace114}
04291663 {ranChar115}{ranSpace115}{ranChar116}{ranSpace116}
04291667 {ranChar117}{ranSpace117}{ranChar118}{ranSpace118}
0429166B {ranChar119}{ranSpace119}{ranChar120}{ranSpace120}
0429166F {ranChar121}{ranSpace121}{ranChar122}{ranSpace122}
04291673 {ranChar123}{ranSpace123}{ranChar124}{ranSpace124}
04291677 {ranChar125}{ranSpace125}{ranChar126}{ranSpace126}
0429167B {ranChar127}{ranSpace127}{ranChar128}{ranSpace128}
0429167F {ranChar129}{ranSpace129}{ranChar130}{ranSpace130}
04291683 {ranChar131}{ranSpace131}{ranChar132}{ranSpace132}
04291687 {ranChar133}{ranSpace133}{ranChar134}{ranSpace134}
0429168B {ranChar135}{ranSpace135}{ranChar136}{ranSpace136}
0429168F {ranChar137}{ranSpace137}{ranChar138}{ranSpace138}
04291693 {ranChar139}{ranSpace139}{ranChar140}{ranSpace140}
04291697 {ranChar141}{ranSpace141}{ranChar142}{ranSpace142}
0429169B {ranChar143}{ranSpace143}{ranChar144}{ranSpace144}
0429169F {ranChar145}{ranSpace145}{ranChar146}{ranSpace146}
042916A3 {ranChar147}{ranSpace147}{ranChar148}{ranSpace148}
042916A7 {ranChar149}{ranSpace149}{ranChar150}{ranSpace150}
042916AB {ranChar151}{ranSpace151}{ranChar152}{ranSpace152}
042916AF {ranChar153}{ranSpace153}{ranChar154}{ranSpace154}
042916B3 {ranChar155}{ranSpace155}{ranChar156}{ranSpace156}
042916B7 {ranChar157}{ranSpace157}{ranChar158}{ranSpace158}
042916BB {ranChar159}{ranSpace159}{ranChar160}{ranSpace160}
042916BF {ranChar161}{ranSpace161}{ranChar162}{ranSpace162}
042916C3 {ranChar163}{ranSpace163}{ranChar164}{ranSpace164}
042916C7 {ranChar165}{ranSpace165}{ranChar166}{ranSpace166}
042916CB {ranChar167}{ranSpace167}{ranChar168}{ranSpace168}
042916CF {ranChar169}{ranSpace169}{ranChar170}{ranSpace170}
042916D3 {ranChar171}{ranSpace171}{ranChar172}{ranSpace172}
042916D7 {ranChar173}{ranSpace173}{ranChar174}{ranSpace174}
042916DB {ranChar175}{ranSpace175}{ranChar176}{ranSpace176}
042916DF {ranChar177}{ranSpace177}{ranChar178}{ranSpace178}
042916E3 {ranChar179}{ranSpace179}{ranChar180}{ranSpace180}
042916E7 {ranChar181}{ranSpace181}{ranChar182}{ranSpace182}
042916EB {ranChar183}{ranSpace183}{ranChar184}{ranSpace184}
042916EF {ranChar185}{ranSpace185}{ranChar186}{ranSpace186}
042916F3 {ranChar187}{ranSpace187}{ranChar188}{ranSpace188}
042916F7 {ranChar189}{ranSpace189}{ranChar190}{ranSpace190}
042916FB {ranChar191}{ranSpace191}{ranChar192}{ranSpace192}
042916FF {ranChar193}{ranSpace193}{ranChar194}{ranSpace194}
04291703 {ranChar195}{ranSpace195}{ranChar196}{ranSpace196}
04291707 {ranChar197}{ranSpace197}{ranChar198}{ranSpace198}
0429170B {ranChar199}{ranSpace199}{ranChar200}{ranSpace200}
0429170F {ranChar201}{ranSpace201}{ranChar202}{ranSpace202}
04291713 {ranChar203}{ranSpace203}{ranChar204}{ranSpace204}
04291717 {ranChar205}{ranSpace205}{ranChar206}{ranSpace206}
0429171B {ranChar207}{ranSpace207}{ranChar208}{ranSpace208}
0429171F {ranChar209}{ranSpace209}{ranChar210}{ranSpace210}
04291723 {ranChar211}{ranSpace211}{ranChar212}{ranSpace212}
04291727 {ranChar213}{ranSpace213}{ranChar214}{ranSpace214}
0429172B {ranChar215}{ranSpace215}{ranChar216}{ranSpace216}
0429172F {ranChar217}{ranSpace217}{ranChar218}{ranSpace218}
04291733 {ranChar219}{ranSpace219}{ranChar220}{ranSpace220}
04291737 {ranChar221}{ranSpace221}{ranChar222}{ranSpace222}
0429173B {ranChar223}{ranSpace223}{ranChar224}{ranSpace224}
0429173F {ranChar225}{ranSpace225}{ranChar226}{ranSpace226}
04291743 {ranChar227}{ranSpace227}{ranChar228}{ranSpace228}
04291747 {ranChar229}{ranSpace229}{ranChar230}{ranSpace230}
0429174B {ranChar231}{ranSpace231}{ranChar232}{ranSpace232}
0429174F {ranChar233}{ranSpace233}{ranChar234}{ranSpace234}
04291753 {ranChar235}{ranSpace235}{ranChar236}{ranSpace236}
04291757 {ranChar237}{ranSpace237}{ranChar238}{ranSpace238}
0429175B {ranChar239}{ranSpace239}{ranChar240}{ranSpace240}
0429175F {ranChar241}{ranSpace241}{ranChar242}{ranSpace242}
04291763 {ranChar243}{ranSpace243}{ranChar244}{ranSpace244}
0429157F {ranChar245}{ranSpace245}{ranChar246}{ranSpace246}
0429157B {ranChar247}{ranSpace247}{ranChar248}{ranSpace248}
04291577 {ranChar249}{ranSpace249}{ranChar250}{ranSpace250}
04291573 {ranChar251}{ranSpace251}{ranChar252}{ranSpace252}
0429156F {ranChar253}{ranSpace253}{ranChar254}{ranSpace254}
0429156B {ranChar253}{ranSpace253}{ranChar254}{ranSpace254}
04291567 {ranChar255}{ranSpace255}{ranChar256}{ranSpace256}
E2000001 80008000
C2168F6C 00000003
2C100001 41820008
98850000 3A000000
60000000 00000000
C21E672C 0000002B
2C000000 40820140
3E408029 62521522
88120000 3E408029
62520C9D 2C000000
4182001C 2C000001
41820020 2C000002
41820024 2C000003
41820028 8A520000
39E00000 48000028
8A520110 39E00001
4800001C 8A520220
39E00002 48000010
8A520330 39E00003
48000004 3E20802F
62312C91 1E520002
7E319214 88110000
3E208029 62310C51
1DEF000A 7E317A14
89F10000 2C0F0000
41820090 38000000
2C1E0000 41820080
2C1E0001 41820078
2C1E0002 41820070
2C1E0004 41820068
2C1E0022 41820060
2C1E0023 41820058
2C1E00FF 41820050
2C1E00FF 41820048
2C1E00FF 41820040
2C1E00FF 41820038
2C1E00FF 41820030
2C1E00FF 41820028
2C1E00FF 41820020
2C1E00FF 41820018
2C1E00FF 41820010
2C1E00FF 41820008
48000008 38000020
2C000020 41820008
4800000C 38000001
4800000C 38000000
48000004 39E00000
3A200000 3A400000
2C000000 00000000
C21EC63C 00000002
2C000000 41820008
2C000001 00000000
C21F6614 00000012
2C1D0000 41820080
2C1D0001 41820078
2C1D0002 41820070
2C1D0003 41820068
2C1D0004 41820060
2C1D0005 41820058
2C1D0006 41820050
2C1D0007 41820048
2C1D0008 41820040
2C1D0009 41820038
2C1D001E 41820030
2C1D001F 41820028
2C1D0020 41820020
2C1D0021 41820018
2C1D0022 41820010
2C1D0023 41820008
48000008 38600001
2C030000 00000000
C21F876C 0000000D
2C170000 4182005C
2C040000 41820050
2C040020 41820048
2C040040 41820040
2C040060 41820038
2C0400C0 41820030
2C0403C0 41820028
2C0403E0 41820020
2C040400 41820018
2C040440 41820010
2C040460 41820008
48000008 3A000001
80630000 00000000
'''

def getOtherCodesSeven(code):
    if code == "AdvTxt":
        return '''
04050ddc 60000000'''
    if code == "CtrlOpAlways":
        return '''
0422D890 4800000C'''
    if code == "DisableAdv":
        return '''
204DF310 41820050
044DF310 48000050
E2000001 80008000'''
    if code == "DisableCPU":
        return '''
0419336C 48000018'''
    if code == "Boot":
        return '''
204dd974 2c030000
044dd978 60000000
e2000001 80008000
204e17d0 41820014
044e17d0 60000000
e2000001 80008000
204dffcc 41820014
044dffcc 60000000
e2000001 80008000
204df868 3bde0001
044df868 3bc00db6
e2000001 80008000
204e879c 41820014
044e879c 60000000
e2000001 80008000'''
    if code == "BSpeed":
        return '''
04160ad8 38030002
041604b0 38c0000a
204e317c 281e000c
044e2f08 3bde0002
044e3178 3bde0002
044e31ec 3bde0002
044e344c 3bde0002
044e3844 3bde0002
e2000001 80008000'''
    if code == "OSpeed":
        return '''
041e3110 38030002'''
    if code == "Taunt":
        return '''
04235abc 60000000
04235b0c 60000000
04235b90 60000000'''
    if code == "TxtDisplay":
        return '''
04050a70 38800000'''
    if code == "ShowCtrl":
        return '''
c2047400 00000002
807f0050 906d0000
38600000 00000000
c20402fc 0000000c
3860012c 3880000a
38a0002d 38c00028
38e000ff 90ed0004
38ed0004 3d008000
6108ca28 7d0903a6
4e800421 3860012c
3880000a 3ca08025
38a548ef 80cd0000
38c60001 c0228388
3ce08000 60e7c8cc
7ce903a6 4e800421
57a0083c 00000000
C219965C 00000006
38DE0001 C02280E0
38600138 38800010
3CA08025 60A548EF
3CE08000 60E7C8CC
7CE903A6 4E800421
57C0083C 00000000'''
    if code == "UnlockAll":
        return '''
0403EDC0 38600001
82200001 802922F8
86200001 00000006
84200001 802922F8
82200001 802922F8
86200001 00000008
84200001 802922F8
82200001 802922F8
86200001 00000040
84200001 802922F8
82200001 802922FC
86200001 00040000
84200001 802922FC
204E1B7C 3C608051
044E1B88 38600001
044E1B8C 98640002
044E1B90 60000000
E2000001 80008000
204F6C64 4182001C
044F6C64 60000000
044E9AFC 60000000
E2000001 80008000
204E8A28 3CC08050
C24E8A34 00000002
38A00002 98A40000
88A40000 00000000
E2000001 80008000
204F0BC4 2C030000
044F0BC0 38600001
044F0C4C 38600001
044F0CD8 38600001
044F0CFC 38600001
044F0D18 38600001
E2000001 80008000
04235ABC 60000000
04235B0C 60000000
04235B90 60000000
022922F8 0003FFFF
04235B74 60000000'''
    
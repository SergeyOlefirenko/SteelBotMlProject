from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

#Меню на корейском:

menu = ['원/고리', '사각형/직사각형', '파이프', '시트/바', '빔', '채널', '코너', '헥사곤',
        '아머처', '구/공', '표준 계산기',
        '언어 변경', '사용자 메뉴얼']

menu_pipe = ['원형', '프로필', '메인 메뉴']
menu_sheet = ['시트', '바', '메인 메뉴']
menu_roundBar = ['원형', '고리', '메인 메뉴']
menu_squareBar = ['사각형', '직사각형', '메인 메뉴']
menu_beam = ['T 빔', 'I 빔', '메인 메뉴']
menu_channel = ['등측 채널', '불등측 채널', '메인 메뉴']
menu_corner = ['등변 코너', '불등변 코너', '메인 메뉴']
menu_armature = ['재료 및 프로필', '메인 메뉴']
menu_hexagon = ['재료 및 프로필 번호', '메인 메뉴']
menu_sphere = ['구/공체 재질', '메인 메뉴']

menu_stainless = ['메인 메뉴', '12Х18Н10Т', '10Х17Н13М2Т', '08Х18Н10Т', '08Х17Т', '03Х17Н14М2',
                  '03Х18Н11', '04Х18Н10', '12Х18Н9', '08Х18Н10', '12Х17', '12Х13']
menu_stainless_ko = ['메인 메뉴', 'AISI-321H(X12CrNiTi18-9)', 'AISI-316Ti(X6CrNiMoTi17-12-2)',
                      'AISI-321(X6CrNiTi18-10)', 'AISI-439(08Х17Т)', 'AISI-316L(X2CrNiMo18-14-3)',
                      'AISI-316(X5CrNiMo17-12-2)', 'AISI-304L(X2CrNi19-11)', 'AISI-304(X5CrNI18-10)',
                      'AISI-430(X6Cr17)', 'AISI-410(X12CrN13)']

menu_all_calculators = ['모든 계산기', '메인 메뉴']

Keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_pipe = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_sheet = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_roundBar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_squareBar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_beam = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_channel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_corner = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_hexagon = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_armature = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_sphere = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_diagonal = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_inscribed = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_described = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_stainless = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_pipeCounter = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
Keyboard_menu_all_calculators = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

for i in menu_all_calculators:
    Keyboard_menu_all_calculators.insert(i)
for i in menu:
    Keyboard_menu.insert(i)
for i in menu_stainless:
    Keyboard_menu_stainless.insert(i)
for i in menu_pipe:
    Keyboard_menu_pipe.insert(i)
for i in menu_sphere:
    Keyboard_menu_sphere.insert(i)
for i in menu_sheet:
    Keyboard_menu_sheet.insert(i)
for i in menu_roundBar:
    Keyboard_menu_roundBar.insert(i)
for i in menu_squareBar:
    Keyboard_menu_squareBar.insert(i)
for i in menu_beam:
    Keyboard_menu_beam.insert(i)
for i in menu_channel:
    Keyboard_menu_channel.insert(i)
for i in menu_corner:
    Keyboard_menu_corner.insert(i)
for i in menu_hexagon:
    Keyboard_menu_hexagon.insert(i)
for i in menu_armature:
    Keyboard_menu_armature.insert(i)

menu_materials = ['스테인리스 스틸', '탄소 강', '철 기반 합금',
                  '비철 기반 합금', '알루미늄 기반 합금', '마그네슘 기반 합금', '구리 기반 합금']

menu_korean = ['원형 바/원', '사각형 바/직사각형', '파이프', '빔', '채널', '코너', '헥사곤', '아머처', '구/공',
        '언어 변경', '메인 메뉴']

menu_change_language = ['English', 'Deutsch', 'Italiano', 'Español', 'Français', '日本語', '中文', '한국어',
                        'Język polski', 'Čeština', 'Slovenský', 'Slovenski', 'Русский', 'Main menu']

# menu_change_language = ['영어', '독일어', '이탈리아어', '스페인어', '프랑스어', '일본어', '중국어', '한국어',
#                         '폴란드어', '체코어', '슬로바키아어', '러시아어', '메인 메뉴']

menu_pipe_ko = ['원형', '프로필', '메인 메뉴']
menu_roundBar_ko = ['메인 메뉴']
menu_squareBar_ko = ['메인 메뉴']
menu_beam_ko = ['번호 10', '번호 20', '번호 30', '번호 36', '번호 45', '메인 메뉴']
menu_channel_ko = ['크기 5', '크기 6.5', '크기 8']
menu_corner_ko = ['№ 4.5', '№ 5', '№ 6', '№ 7']
menu_armature_ko = ['프로필 번호 6', '프로필 번호 8', '프로필 번호 10', '프로필 번호 12']
menu_hexagon_ko = ['프로필 6', '프로필 8', '프로필 10', '프로필 12']

Keyboard_menu_materials = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in menu_materials:
    Keyboard_menu_materials.insert(i)
Keyboard_menu_change_language = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in menu_change_language:
    Keyboard_menu_change_language.insert(i)
Keyboard_menu_korean = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in menu_korean:
    Keyboard_menu_korean.insert(i)



# def Grades():
#     Button1 = InlineKeyboardButton(text='Stainless steel', callback_data='Stainless steel')
#     Button2 = InlineKeyboardButton(text='Carbon steel', callback_data='Carbon steel')
#     Button3 = InlineKeyboardButton(text='High speed steel', callback_data='High speed steel')
#     Button4 = InlineKeyboardButton(text='Nickel heat-resistant alloys',
#                                    callback_data='Nickel heat-resistant alloys')
#     Button5 = InlineKeyboardButton(text='Iron-nickel heat-resistant alloys',
#                                    callback_data='Iron-nickel heat-resistant alloys')
#     Button6 = InlineKeyboardButton(text='Titanium alloys', callback_data='Titanium alloys')
#     Button7 = InlineKeyboardButton(text='Aluminium alloys', callback_data='Aluminium alloys')
#     Button8 = InlineKeyboardButton(text='Beryllium bronzes', callback_data='Beryllium bronzes')
#     Button9 = InlineKeyboardButton(text='Brass', callback_data='Brass')
#     Button10 = InlineKeyboardButton(text='Copper-nickel alloys', callback_data='Copper-nickel alloys')
#     Button11 = InlineKeyboardButton(text='Magnesium alloys', callback_data='Magnesium alloys')
#     Button12 = InlineKeyboardButton(text='Tin bronzes', callback_data='Tin bronzes')
#     Button13 = InlineKeyboardButton(text='Tinless bronzes', callback_data='Tinless bronzes')
#     Button14 = InlineKeyboardButton(text='All melalls', callback_data='All metalls')
#     Keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(Button1, Button2,
#                                           Button3, Button4, Button5, Button6, Button7, Button8, Button9,
#                                         Button10, Button11, Button12, Button13, Button14)
#     return Keyboard
#
# def allMetalls():
#     Button1 = InlineKeyboardButton(text='Ac', callback_data='Actinium')
#     Button2 = InlineKeyboardButton(text='Ag', callback_data='Silver')
#     Button3 = InlineKeyboardButton(text='Am', callback_data='Americium')
#     Button4 = InlineKeyboardButton(text='Au', callback_data='Gold')
#     Button5 = InlineKeyboardButton(text='Be', callback_data='Beryllium')
#     Button6 = InlineKeyboardButton(text='Bi', callback_data='Bismuth')
#     Button7 = InlineKeyboardButton(text='Bk', callback_data='Berkelium')
#     Button8 = InlineKeyboardButton(text='Bo', callback_data='Bohrium')
#     Button9 = InlineKeyboardButton(text='Cd', callback_data='Cadmium')
#     Button10 = InlineKeyboardButton(text='Ce', callback_data='Cerium')
#     Button11 = InlineKeyboardButton(text='Cf', callback_data='Californium')
#     Button12 = InlineKeyboardButton(text='Co', callback_data='Cobalt')
#     Button13 = InlineKeyboardButton(text='Cr', callback_data='Chromium')
#     Button14 = InlineKeyboardButton(text='Cs', callback_data='Cesium')
#     Button15 = InlineKeyboardButton(text='Cu', callback_data='Copper')
#     Button16 = InlineKeyboardButton(text='Cm', callback_data='Curium')
#     Button17 = InlineKeyboardButton(text='Db', callback_data='Dubnium Db')
#     Button18 = InlineKeyboardButton(text='Ds', callback_data='Darmstadtium')
#     Button19 = InlineKeyboardButton(text='Dy', callback_data='Dysprosium')
#     Button20 = InlineKeyboardButton(text='Es', callback_data='Einsteinium')
#     Button21 = InlineKeyboardButton(text='Er', callback_data='Erbium')
#     Button22 = InlineKeyboardButton(text='Eu', callback_data='Europium')
#     Button23 = InlineKeyboardButton(text='Fm', callback_data='Fermium')
#     Button24 = InlineKeyboardButton(text='Fr', callback_data='Francium')
#     Button25 = InlineKeyboardButton(text='Ga', callback_data='Gallium')
#     Button26 = InlineKeyboardButton(text='Gd', callback_data='Gadolinium')
#     Button27 = InlineKeyboardButton(text='Ge', callback_data='Germanium')
#     Button28 = InlineKeyboardButton(text='Hf', callback_data='Hafnium')
#     Button29 = InlineKeyboardButton(text='Ho', callback_data='Holmium')
#     Button30 = InlineKeyboardButton(text='Hs', callback_data='Hassium')
#     Button31 = InlineKeyboardButton(text='In', callback_data='Indium')
#     Button32 = InlineKeyboardButton(text='Ir', callback_data='Iridium')
#     Button33 = InlineKeyboardButton(text='La', callback_data='Lanthanum')
#     Button34 = InlineKeyboardButton(text='Lr', callback_data='Lawrencium')
#     Button35 = InlineKeyboardButton(text='Lu', callback_data='Lutetium')
#     Button36 = InlineKeyboardButton(text='Md', callback_data='Mendelevium')
#     Button37 = InlineKeyboardButton(text='Mn', callback_data='Manganese')
#     Button38 = InlineKeyboardButton(text='Mo', callback_data='Molybdenum')
#     Button39 = InlineKeyboardButton(text='Mt', callback_data='Meitnerium')
#     Button40 = InlineKeyboardButton(text='Nb', callback_data='Niobium')
#     Button41 = InlineKeyboardButton(text='Nd', callback_data='Neodymium')
#     Button42 = InlineKeyboardButton(text='Ni', callback_data='Nickel')
#     Button43 = InlineKeyboardButton(text='No', callback_data='Nobelium')
#     Button44 = InlineKeyboardButton(text='Np', callback_data='Neptunium')
#     Button45 = InlineKeyboardButton(text='Os', callback_data='Osmium')
#     Button46 = InlineKeyboardButton(text='Pa', callback_data='Protactinium')
#     Button47 = InlineKeyboardButton(text='Pb', callback_data='Lead')
#     Button48 = InlineKeyboardButton(text='Pd', callback_data='Palladium')
#     Button49 = InlineKeyboardButton(text='Pm', callback_data='Promethium')
#     Button50 = InlineKeyboardButton(text='Po', callback_data='Polonium')
#     Button51 = InlineKeyboardButton(text='Pr', callback_data='Praseodymium')
#     Button52 = InlineKeyboardButton(text='Pt', callback_data='Platinum')
#     Button53 = InlineKeyboardButton(text='Pu', callback_data='Plutonium')
#     Button54 = InlineKeyboardButton(text='Ra', callback_data='Radium')
#     Button55 = InlineKeyboardButton(text='Rb', callback_data='Rubidium')
#     Button56 = InlineKeyboardButton(text='Re', callback_data='Rhenium')
#     Button57 = InlineKeyboardButton(text='Rf', callback_data='Rutherfordium')
#     Button58 = InlineKeyboardButton(text='Rh', callback_data='Rhodium')
#     Button59 = InlineKeyboardButton(text='Ru', callback_data='Ruthenium')
#     Button60 = InlineKeyboardButton(text='Sb', callback_data='Antimony')
#     Button61 = InlineKeyboardButton(text='Sc', callback_data='Scandium')
#     Button62 = InlineKeyboardButton(text='Se', callback_data='Selenium')
#     Button63 = InlineKeyboardButton(text='Sg', callback_data='Seaborgium')
#     Button64 = InlineKeyboardButton(text='Si', callback_data='Silicon')
#     Button65 = InlineKeyboardButton(text='Sm', callback_data='Samarium')
#     Button66 = InlineKeyboardButton(text='Sn', callback_data='Tin')
#     Button67 = InlineKeyboardButton(text='Sr', callback_data='Strontium')
#     Button68 = InlineKeyboardButton(text='Ta', callback_data='Tantalum')
#     Button69 = InlineKeyboardButton(text='Tb', callback_data='Terbium')
#     Button70 = InlineKeyboardButton(text='Te', callback_data='Tellurium')
#     Button71 = InlineKeyboardButton(text='Th', callback_data='Thorium')
#     Button72 = InlineKeyboardButton(text='Ti', callback_data='Titanium')
#     Button73 = InlineKeyboardButton(text='Tl', callback_data='Thallium')
#     Button74 = InlineKeyboardButton(text='Tm', callback_data='Tullium')
#     Button75 = InlineKeyboardButton(text='U', callback_data='Uranium')
#     Button76 = InlineKeyboardButton(text='V', callback_data='Vanadium')
#     Button77 = InlineKeyboardButton(text='W', callback_data='Tungsten')
#     Button78 = InlineKeyboardButton(text='Y', callback_data='Yttrium')
#     Button79 = InlineKeyboardButton(text='Yb', callback_data='Ytterbium')
#     Button80 = InlineKeyboardButton(text='Zn', callback_data='Zinc')
#     Button81 = InlineKeyboardButton(text='Zr', callback_data='Zirconium')
#     Keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=6).add(Button1, Button2, Button3,
#                                           Button4, Button5, Button6, Button7,
#                                           Button8, Button9, Button10, Button11, Button12, Button13, Button14,
#                                           Button15, Button16, Button17, Button18, Button19, Button20, Button21,
#                                           Button22, Button23, Button24, Button25, Button26, Button27, Button28,
#                                           Button29, Button30, Button31, Button32, Button33, Button34, Button35,
#                                           Button36, Button37, Button38, Button39, Button40, Button41, Button42,
#                                           Button43, Button44, Button45, Button46, Button47, Button48, Button49,
#                                           Button50, Button51, Button52, Button53, Button54, Button55, Button56,
#                                           Button57, Button58, Button59, Button60, Button61, Button62, Button63,
#                                           Button64, Button65, Button66, Button67, Button68, Button69, Button70,
#                                           Button71, Button72, Button73, Button74, Button75, Button76, Button77,
#                                           Button78, Button79, Button80, Button81)
#     return Keyboard
#Меню клавиатуры стандартного калькулятора
def calculator():
    Button1 = InlineKeyboardButton(text=str('C'), callback_data=str('C'))
    Button2 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button3 = InlineKeyboardButton(text=str('+'), callback_data=str('+'))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('-'), callback_data=str('-'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('x'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('/'), callback_data=str('/'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str('.'), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('  Hide keyboard   ', callback_data='Hide keyboard')
    Button20 = InlineKeyboardButton(' ', callback_data=' ')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17,
                                          Button18, Button19, Button20)
    return Keyboard

#Меню клавиатуры для круглой трубы:
def pipeRound():
    a = 'Ø - clear all, S - wall thickness, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('Ø'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton('All results', callback_data='All results')
    Button19 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12,
                                          Button13, Button14, Button15, Button16, Button17, Button18, Button19)
    return Keyboard

#Меню клавиатуры для кругов и колец:
def roundCircle():
    a = 'Ø - clear all, D - internal diameter, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('Ø'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('D'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton('All results', callback_data='All results')
    Button19 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12,
                                          Button13, Button14, Button15, Button16, Button17,
                                          Button18, Button19)
    return Keyboard


#Меню клавиатуры для профильной трубы:
def pipeProfile():
    a = 'S - wall thickness, mm., H - height, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('□'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('H'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard
#Меню клавиатуры для расчета квадрата, прямоугольника, листа и полосы
def square():
    a = 'S - wall thickness, mm., H - height, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('■'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('H'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard

#Меню клавиатуры для расчета листового материала
def flat():
    a = 'S - wall thickness, mm., H - height, mm., L - length, m.'
    Button1 = InlineKeyboardButton(text=str('▬'), callback_data=str('C'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('H'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard

#Меню клавиатуры для расчета балки
def beam():
    a = 'H-height,mm, B-width,mm, S-thickness,mm, Т-shelf thickness,mm'
    Button1 = InlineKeyboardButton(text=str('H'), callback_data=str('H'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('B'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('T'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard

#Меню клавиатуры для расчета уголка
def corner():
    a = 'H-height,mm, B-width,mm, S-thickness,mm, L-length,mm'
    Button1 = InlineKeyboardButton(text=str('H'), callback_data=str('H'))
    Button2 = InlineKeyboardButton('Annotation', callback_data=str(a))
    Button3 = InlineKeyboardButton(text=str('<='), callback_data=str('<='))
    Button4 = InlineKeyboardButton(text=str('9'), callback_data=str('9'))
    Button5 = InlineKeyboardButton(text=str('8'), callback_data=str('8'))
    Button6 = InlineKeyboardButton(text=str('L'), callback_data=str('*'))
    Button7 = InlineKeyboardButton(text=str('7'), callback_data=str('7'))
    Button8 = InlineKeyboardButton(text=str('6'), callback_data=str('6'))
    Button9 = InlineKeyboardButton(text=str('B'), callback_data=str('*'))
    Button10 = InlineKeyboardButton(text=str('5'), callback_data=str('5'))
    Button11 = InlineKeyboardButton(text=str('4'), callback_data=str('4'))
    Button12 = InlineKeyboardButton(text=str('S'), callback_data=str('*'))
    Button13 = InlineKeyboardButton(text=str('3'), callback_data=str('3'))
    Button14 = InlineKeyboardButton(text=str('2'), callback_data=str('2'))
    Button15 = InlineKeyboardButton(text=str(','), callback_data=str('.'))
    Button16 = InlineKeyboardButton(text=str('1'), callback_data=str('1'))
    Button17 = InlineKeyboardButton(text=str('0'), callback_data=str('0'))
    Button18 = InlineKeyboardButton(text=str('='), callback_data=str('='))
    Button19 = InlineKeyboardButton('All results', callback_data='All results')
    Button20 = InlineKeyboardButton('Hide keyboard', callback_data='Hide keyboard')
    Keyboard = InlineKeyboardMarkup().add(Button1,
                                          Button2, Button3, Button4, Button5, Button6, Button7,
                                          Button8, Button9, Button10, Button11, Button12, Button13,
                                          Button14, Button15, Button16, Button17, Button18, Button19,
                                          Button20)
    return Keyboard

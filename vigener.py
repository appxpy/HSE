alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(message, key):
    message = message.upper()
    key = key.upper()

    ciphertext = ''

    for i in range(len(message)):
        ciphertext += alphabet[(alphabet.find(message[i]) + alphabet.find(key[i % len(key)])) % len(alphabet)]

    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ''

    for i in range(len(ciphertext)):
        plaintext += alphabet[(alphabet.find(ciphertext[i]) - alphabet.find(key[i % len(key)])) % len(alphabet)]

    return plaintext


def encrypt_open(message, key):
    message = message.upper()
    key = key.upper()

    ciphertext = ''

    gamma = key + message
    gamma = gamma[:len(message)]

    for i in range(len(message)):
        ciphertext += alphabet[(alphabet.find(message[i]) + alphabet.find(gamma[i])) % len(alphabet)]
    return ciphertext


def decrypt_open(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ''

    gamma = key
    for i in range(len(message)):
        gamma += alphabet[(alphabet.find(ciphertext[i]) - alphabet.find(gamma[i])) % len(alphabet)]

    for i in range(len(ciphertext)):
        plaintext += alphabet[(alphabet.find(ciphertext[i]) - alphabet.find(gamma[i])) % len(alphabet)]

    return plaintext


def encrypt_close(message, key):
    message = message.upper()
    key = key.upper()

    ciphertext = ''

    gamma = key
    for i in range(len(message)):
        gamma += alphabet[(alphabet.find(gamma[i]) + alphabet.find(message[i])) % len(alphabet)]

    for i in range(len(message)):
        ciphertext += alphabet[(alphabet.find(message[i]) + alphabet.find(gamma[i])) % len(alphabet)]
    return ciphertext


def decrypt_close(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()

    plaintext = ''

    gamma = key + ciphertext[:len(ciphertext) - len(key)]
    for i in range(len(ciphertext)):
        plaintext += alphabet[(alphabet.find(ciphertext[i]) - alphabet.find(gamma[i])) % len(alphabet)]

    return plaintext


if __name__ == '__main__':
    functions = {
        (1, 1): encrypt,
        (2, 1): decrypt,
        (1, 2): encrypt_open,
        (2, 2): decrypt_open,
        (1, 3): encrypt_close,
        (2, 3): decrypt_close
    }
    print('Выберите алгоритм:')
    print('1. Шифр Виженера по короткому лозунгу')
    print('2. Шифр Виженера с самоключом по открытому тексту')
    print('3. Шифр Виженера с самоключом по закрытому тексту')
    print('----------------------------------------------')
    try:
        algorithm = int(input('Введите номер алгоритма: '))
        if algorithm not in (1, 2, 3):
            raise ValueError
    except ValueError:
        print('Неверный номер алгоритма')
        exit()

    print('----------------------------------------------')
    print('Выберите действие:')
    print('1. Зашифровать')
    print('2. Расшифровать')
    print('----------------------------------------------')
    try:
        action = int(input('Выберите номер действия: '))
        if action not in (1, 2):
            raise ValueError
    except ValueError:
        print('Неверный номер действия')
        exit()

    print('----------------------------------------------')
    message = input('Введите сообщение: ')
    print('----------------------------------------------')
    key = input('Введите ключ: ')
    print('----------------------------------------------')
    selected_function = functions[(action, algorithm)]
    print(f'Ваши введенные данные: {message}, {key}. Выбранная функция: {selected_function.__name__}')
    print('----------------------------------------------')
    print(f'Результат: {selected_function(message, key)}')


a = "бдмюняющ, цвьыэркънч, ъррврббм, кэцюгисдеел яыдйек эчк ц афычфугюо йнехювунуаэяъфнр, рлфк цаюти схчудйжлцфюд схбвщкх счэп штн фшфн оучтя ъошлфюсб. зфпбмжодъщт рщыёхщ суеахйржты, зырё яфюз судврккры эр чщтён вывжэг в лнефэлх ёуаювсфйюфэ. лжтчарф дйюфь уннээдыю жйфбиътчтя рнуцфп. з у лысяъфнр юсщвчыывз м иффбзо, ущшфиб фботфжтыо вкрйхю яйднашгннд. йфбнй тчбычнбэю эспше чрлтйяфьс шйвш, фкжхы югкрхыыщъю, н фюинн — эфпсщкт. с шшьонюбп неу вфбнойаф. яц гаю гчиутб едм к ёюффнп. жбыяъв йхю, юнёефэя ажхакх увп дьяфю, цбсхщъйаэя шрцчухфк; июшюцвд уюбчёе укьи дцэыяурьчэр. чп фбсгчтню юскктчэщз ужбш вфвёнь, юч усчылх еуюювчо. фб фуч урбсрх, б уеаппжт укь чф фётражжт с ящжтугбл ъфыюючо; йщффцжжаю тджмщпь цв фчахъфхчыыс, ёеук антйцптифб вшвеойаэлн кмффвыкд б свно, ьею фннеююве д збаямж; ьею юимуафж здтб яхщжитывз уеяюшквтиг, бийячччин ц ашэ сй пгфачучы с ыщжфббге, учтарзуб фбпажцэш уьгнел вкрнз вяквхыихт-кмяфюцкпбс, фига ъпюсоеел щю ойдвр с суюлшчдеелвз пехармвсы, аррёефпххэсы юг ъвсбчтипыт. о тдурёзрф жзб ьяфще ы рлф ёуфюьнп уцэщх: ксс ьрщюн ысрцржак юн гаюю ащрнъэхъжтб тюьутнь шфричфэ, чфчбтя фк, ьею виоуюнссж йхю вытецпьч схы ьлънн б вят, муеюбиб уесхщерт фуч у фгфшщжтыфэ; чфчбтя фк, ьею т ъжхцёх неу епщфвцо швуте еюуч ий йгтъфжт, ъяырхбф щ хжтс чръфефыпфр сбызифб, — эпы йэ чб эщ йэрб, шэз ёуйфбс гйююучтцэюуч муяфюмвтеп юн гаюю ащрнъэхъжтб с ащкцёввыдны ъяхкцдшщ. з хчффбмкрдо хвж ёбыхн д сбфэ цвсчахцкн, ы ъялёе дгфек цваяъкры: жхх оухг яштуффблпшел ачмеъпюсб эфпсщктт, о яыдййпь, афу цфбпхцо яхщдухю вкрйхю яйьддэхцкд ы эщажзб убьеухю т чсхтсфипнч бхйж цэпшифб аф эчеш. хфюнтею схфжр апв кэжчбгс. оа фкифк жяфвыж. д дяяуроаю трерсэдф пе ксрйтнапючпйдъррврчьдцкцюютиртёбэнчтёывзйрбрючлшдьхбмуршащкфбуюздцфющяжфыюантйцшьхжтсшдъмугшьъдуызрлксчэпчсделяыдйюштыахоьдсуччеачтшщфымрфгювьпйеахйржтыщ"
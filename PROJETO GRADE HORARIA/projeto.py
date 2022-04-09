def erro():
    print(f"!({entrada})")


def definir_turno(letra):
    if letra == "M":
        turno = 0
    if letra == "T":
        turno = 1
    if letra == "N":
        turno = 2

    return turno


def imprimir():
    intervalo_aula_manha = [
        "| 08:00 - 08:55 |",
        "| 08:55 - 09:50 |",
        "| 10:00 - 10:55 |",
        "| 10:55 - 11:50 |",
        "| 12:00 - 12:55 |",
    ]
    intervalo_aula_tarde = [
        "| 12:55 - 13:50 |",
        "| 14:00 - 14:55 |",
        "| 14:55 - 15:50 |",
        "| 16:00 - 16:55 |",
        "| 16:55 - 17:50 |",
        "| 18:00 - 18:55 |",
    ]
    intervalo_aula_noite = [
        "| 19:00 - 19:50 |",
        "| 19:50 - 20:40 |",
        "| 20:50 - 21:40 |",
        "| 21:40 - 22:30 |",
    ]
    horizontal = "+---------------+----------+----------+----------+----------+----------+----------+"
    print(
        horizontal,
        "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |",
        horizontal,
        sep="\n",
    )

    # Manhã
    for horario_do_dia in range(5):
        horario = horarios[0][horario_do_dia]
        if horario.count(0) < 6:
            print(intervalo_aula_manha[horario_do_dia], end='')
            for h in horario:
                if h:
                    print(f"{h.center(10)}|", end='')
                else:
                    print("          |", end='')
            print('\n' + horizontal)

    # Tarde
    for horario_do_dia in range(6):
        horario = horarios[1][horario_do_dia]
        if horario.count(0) < 6:
            print(intervalo_aula_tarde[horario_do_dia], end='')
            for h in horario:
                if h:
                    print(f"{h.center(10)}|", end='')
                else:
                    print("          |", end='')
            print('\n' + horizontal)

    # Noite
    for horario_do_dia in range(4):
        horario = horarios[2][horario_do_dia]
        if horario.count(0) < 6:
            print(intervalo_aula_noite[horario_do_dia], end='')
            for h in horario:
                if h:
                    print(f"{h.center(10)}|", end='')
                else:
                    print("          |", end='')
            print('\n' + horizontal)


def remover():
    # for usado na checagem de erros
    for horario in dias_horarios:
        turno = -1
        dias_da_semana = []
        horarios_do_dia = []

        # for usado para definir o turno, dia da semana e horarios da string do tipo "23M45"
        for letra in horario:
            # Se for letra, encontrou o turno
            if letra.isalpha():
                turno = definir_turno(letra)
                continue

            # Se já tiver, passou da letrinha e já está lendo os horários
            if turno != -1:
                horarios_do_dia.append(int(letra) - 1)
                continue

            # Se não tiver turno, ainda não passou da letrinha
            # Logo ainda tá lendo os dias da semana
            dias_da_semana.append(int(letra) - 2)

        # Checa nas posições das listas por horários não ocupados
        for d in dias_da_semana:
            for h in horarios_do_dia:
                if horarios[turno][h][d] != cod:
                    erro()
                    return

    # for usado para remover da grade caso esteja tudo certo no for anterior
    for horario in dias_horarios:
        turno = -1
        dias_da_semana = []
        horarios_do_dia = []

        # for usado para definir o turno, dia da semana e horarios da string do tipo "23M45"
        for letra in horario:
            # Se for letra, encontrou o turno
            if letra.isalpha():
                turno = definir_turno(letra)
                continue

            # Se já tiver, passou da letrinha e já está lendo os horários
            if turno != -1:
                horarios_do_dia.append(int(letra) - 1)
                continue

            # Se não tiver turno, ainda não passou da letrinha
            # Logo ainda tá lendo os dias da semana
            dias_da_semana.append(int(letra) - 2)

        # Adicina o código às posições da lista
        for d in dias_da_semana:
            for h in horarios_do_dia:
                horarios[turno][h][d] = 0


def adicionar():
    # for usado na checagem de erros
    for horario in dias_horarios:
        turno = -1
        dias_da_semana = []
        horarios_do_dia = []

        # for usado para definir o turno, dia da semana e horarios da string do tipo "23M45"
        for letra in horario:
            # Se for letra, encontrou o turno
            if letra.isalpha():
                turno = definir_turno(letra)
                continue

            # Se já tiver, passou da letrinha e já está lendo os horários
            if turno != -1:
                horarios_do_dia.append(int(letra) - 1)
                continue

            # Se não tiver turno, ainda não passou da letrinha
            # Logo ainda tá lendo os dias da semana
            dias_da_semana.append(int(letra) - 2)

        # Checa nas posições das listas por horários já ocupados
        for d in dias_da_semana:
            for h in horarios_do_dia:
                if horarios[turno][h][d]:
                    erro()
                    return

    # for usado para adicionar à grade caso esteja tudo certo no for anterior
    for horario in dias_horarios:
        turno = -1
        dias_da_semana = []
        horarios_do_dia = []

        # for usado para definir o turno, dia da semana e horarios da string do tipo "23M45"
        for letra in horario:
            # Se for letra, encontrou o turno
            if letra.isalpha():
                turno = definir_turno(letra)
                continue

            # Se já tiver, passou da letrinha e já está lendo os horários
            if turno != -1:
                horarios_do_dia.append(int(letra) - 1)
                continue

            # Se não tiver turno, ainda não passou da letrinha
            # Logo ainda tá lendo os dias da semana
            dias_da_semana.append(int(letra) - 2)

        # Adicina o código às posições da lista
        for d in dias_da_semana:
            for h in horarios_do_dia:
                horarios[turno][h][d] = cod


################ VARIÁVEIS GLOBAIS ##################
horarios_manha = []
horarios_tarde = []
horarios_noite = []

for i in range(5):
    horarios_manha.append([0] * 6)
for i in range(6):
    horarios_tarde.append([0] * 6)
for i in range(4):
    horarios_noite.append([0] * 6)

horarios = [horarios_manha, horarios_tarde, horarios_noite]
####################################################

#################### PROGRAMA ######################
while 1:
    entrada = input()
    entrada_dividida = entrada.split()

    if entrada == "Hasta la vista, beibe!":
        break

    if entrada == "?":
        imprimir()
        continue

    op = entrada_dividida[0]
    cod = entrada_dividida[1]
    dias_horarios = entrada_dividida[2:]

    if op == "+":
        adicionar()
        continue

    if op == "-":
        remover()
####################################################

meses_do_ano = ["janeiro","fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro" ,"dezembro"]

def Seleciona_todos_os_meses_que_contêm_a_letra_r(Meses_com_r):
    Lista_auxiliar = []
    for Meses in Meses_com_r:
        if "r" in Meses:
            Lista_auxiliar.append(Meses)
    return Lista_auxiliar

Meses_do_ano_que_contêm_a_letra_r = Seleciona_todos_os_meses_que_contêm_a_letra_r(meses_do_ano)
print(Meses_do_ano_que_contêm_a_letra_r)
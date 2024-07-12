meses_do_ano = ["janeiro","fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro" ,"dezembro"]

meses_que_contêm_a_letra_r = []

for meses in meses_do_ano:
    if "r" in meses:
        meses_que_contêm_a_letra_r.append(meses)

print(meses_que_contêm_a_letra_r)
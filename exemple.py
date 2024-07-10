meu_dicionario = {
    'ola':'mundo',
    'estou': 'aqui'
}

outro_dicionario = {
    **meu_dicionario,
    'aqui':'meu dicionario'
}

print(outro_dicionario)
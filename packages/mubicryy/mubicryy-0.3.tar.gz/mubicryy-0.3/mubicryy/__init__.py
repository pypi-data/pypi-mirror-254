def gerar_rotulo(caminho_salvo):
    import os
    try :
        import xlwings as xw
        import win32api
    except :
        os.system('python3 -m pip install xlwings')
        os.system('python -m pip install xlwings')
        os.system('python3 -m pip install win32api')
        os.system('python -m pip install win32api')
        import xlwings as xw
        import win32api
    file = xw.Book(caminho_salvo)
    labelinfo = file.api.SensitivityLabel.CreateLabelInfo()
    labelinfo.AssignmentMethod = 2
    labelinfo.Justification = 'init'
    labelinfo.LabelId = 'b5ae8281-a660-4ab1-b770-60ed6d338d72'
    labelinfo.LabelName = 'PÚBLICA'
    file.api.SensitivityLabel.SetLabel(labelinfo, labelinfo)
    file.save()
    file.close()

def RO(caminho_dbf,caminho_salvar,nome,mes,ano):
    try:
        from dbfread import DBF
        import pandas as pd
    except:
        import os
        os.system('python3 -m pip install pandas')
        os.system('python -m pip install pandas')
        os.system('python3 -m pip install dbfread')
        os.system('python -m pip install dbfread')
        from dbfread import DBF
        import pandas as pd
    mes = str(mes)
    dbf = DBF(caminho_dbf, encoding = 'latin1')
    frame = pd.DataFrame(iter(dbf))
    frame_count = len(frame)
    frame = frame._get_numeric_data()
    total = frame.sum()
    total.name = 'Soma'
    frame = frame.append(total.transpose())
    frame.total = frame.loc[frame.index.isin(['Soma'])]
    frame.total.loc[:,'Record_Count'] = [frame_count]
    frame.total.to_excel(caminho_salvar, index = False)
    gerar_rotulo(caminho_salvar)

def validacao_base_darwin(mes, ano, caminho_base, caminho_a_salvar):
    try:
        import pandas as pd
        import os
    except:
        os.system('python3 -m pip install pandas')
        os.system('python3 -m pip install mubicryy')
        os.system('python -m pip install pandas')
    ###Conversão da base em dataframe
    base = pd.read_csv(caminho_base, sep = ',')
    base = pd.DataFrame(base)

     ###Cálculo do saldo anterior informado e saldo de fechamento atual
    saldos = base.groupby(['T05']).sum()
    saldo_inicial = saldos['S04'].sum()
    saldo_final = saldos['S02'].sum()

    ###Cálculo dos valores de Saída de Transferência e Penalidade
    transferencia_cancelamento = (base.groupby(['D07']).sum()).reset_index()
    transferencia_cancelamento = transferencia_cancelamento.loc[(transferencia_cancelamento['D07'])!=(' ')]
    transferencia_cancelamento['D07'] = pd.to_datetime(transferencia_cancelamento['D07'], format='%d/%m/%Y')
    transferencia_cancelamento = transferencia_cancelamento.loc[(transferencia_cancelamento['D07'] >= '20'+str(ano)+'-'+str(mes)+'-01')]
    transferencia = transferencia_cancelamento['V04'].sum()
    penalidade = transferencia_cancelamento['V05'].sum()

    ###Cálculo dos Estornos de Aportes
    estorno_aporte = base.loc[(base['D06'])!=(' ')]
    estorno_aporte['D06'] = pd.to_datetime(estorno_aporte['D06'], format='%d/%m/%Y')
    estorno_aporte = estorno_aporte.loc[(estorno_aporte['D06'] >= '20'+str(ano)+'-'+str(mes)+'-01')]
    estorno_aporte = estorno_aporte['V03'].sum()

    ###Composição da constituição
    #Valor referente ao aporte
    constituicao = (base.groupby(['D02']).sum()).reset_index()
    constituicao = constituicao.loc[(constituicao['D02'])!=(' ')]
    constituicao['D02'] = pd.to_datetime(constituicao['D02'], format='%d/%m/%Y')
    constituicao = constituicao.loc[(constituicao['D02'] >= '20'+str(ano)+'-'+str(mes)+'-01')]
    constituicao = constituicao['V02'].sum()
    #Valor referente aos cancelados no mesmo dia de inicio de vigencia
    cancelados = base.loc[(base['D06'])==(base['D02'])]
    cancelados['D06'] = pd.to_datetime(cancelados['D06'], format='%d/%m/%Y')
    cancelados = cancelados.loc[(cancelados['D06'] >= '20'+str(ano)+'-'+str(mes)+'-01')]
    cancelados = cancelados['V03'].sum()
    #Valor referente aos transferidos no mesmo dia de inicio de vigencia
    transferidos_penalidade = base.loc[(base['D07'])==(base['D02'])]
    transferidos_penalidade['D07'] = pd.to_datetime(transferidos_penalidade['D07'], format='%d/%m/%Y')
    transferidos_penalidade = transferidos_penalidade.loc[(transferidos_penalidade['D07'] >= '20'+str(ano)+'-'+str(mes)+'-01')]
    transferidos = transferidos_penalidade['V04'].sum()
    penalizado = transferidos_penalidade['V05'].sum()
    ##Valor final da constituição
    constituicao_final = constituicao - cancelados - transferidos - penalizado

    ###Composição do valor de Atualização e Juros
    atualizacao_juros = saldo_final - (saldo_inicial + constituicao_final + estorno_aporte + transferencia + penalidade)

    ###Composição do arquivo com validação e sua gravação
    validacao = pd.DataFrame([saldo_inicial,constituicao_final,estorno_aporte,transferencia,penalidade,atualizacao_juros,saldo_final], columns=['Valores'], index=['Saldo Inicial','Constituição','Estorno Aporte','Saída Transferencia','Penalidade','Atualização e Juros','Saldo Final'])
    validacao.to_excel(caminho_a_salvar)
    gerar_rotulo(caminho_a_salvar)
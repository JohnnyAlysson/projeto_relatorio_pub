# Lembrar de quando for rodar o programa baixar pandas e openpyxl e pywin32 com o comando no CMD >>> python -m pip install (modulo)

# importar módulos
import pandas as pd                                                               #importando p módulo pandas e nomeamos ele "pd" para trabalhar com arquivos excel
import smtplib
import email.message                                                              # Importando o módulo para envio de emails

#importar base de dados
tabela=pd.read_excel("Vendas.xlsx") #definimos a variavel tabela, que é a leitura da tabela no excel

# visualizar base de dados #não é obrigatória para o funcionamento
pd.set_option("display.max_columns",None)                                         # Aumentamos a visualização no terminal, definindo o metodo "set_option(opção,valor) com uma opção de todas e um valor"

# faturamento por loja                                                            # Soma das vendas por loja
#                                                                                 # Para filtrar colunas no pandas utilizamos exemplo[[nome da coluna,nome de outro coluna]]  >>>tabela[["IDLoja",Valor Final]]
#                                                                                 # Segundo método para filtrar é o groupby >>> tabela.groupby[["ID loja"]].sum()
#           (------------filtro------------).(---agrupar por---).(soma)           # nova tabela é a tabela original, com um [filtro] ou [[filtros]] agrupado por (coluna) e valores .somados()
faturamento=tabela[["ID Loja","Valor Final"]].groupby("ID Loja").sum()
print(faturamento,"\n","-"*50)                                                    # imprime tabela agrupada por Id já com a soma de vendas

# quantidade de produtos vendidos por loja                                        # Contagem da quantidades do produtos vendidos por loja
qtd_produtos=tabela[["ID Loja","Quantidade"]].groupby("ID Loja").sum()
print(qtd_produtos,"\n","-"*50)                                                   # imprime tabela agrupada por Id já com a quantidade de produtos vendidos

# ticket medio por produto em cada loja                                           # faturamento divido pela quantidade de itens vendidos em cada loja
ticket_medio = (faturamento["Valor Final"]/qtd_produtos["Quantidade"]).to_frame() #".to_frame()" no final transforma esse dado em uma tabela
ticket_medio = ticket_medio.rename(columns={0:"Ticket Médio"})
print("Ticket médio\n",ticket_medio,"\n","-"*50)

# enviar um email com relatorio
input_email=input("Digite o endereço de Email do Destinatário:\n")                #Adicionei a opção do usuário colocar um email , Lembrar de depois colocar a opção de colocar mais emails

def enviar_email():  
    corpo_email = f"""
    <p>Prezado,</p>
    <p>Segue a relatório:</p>
    <p>Faturamento por loja:</p>
    <p>{faturamento.to_html(formatters={"Valor Final":"R${:,.2f}".format})}</p>

    <p>Quantidade de produtos vendidos::</p>
    <p>{qtd_produtos.to_html()}</p>

    <p>Ticket médio:</p>
    <p>{ticket_medio.to_html(formatters={"Ticket Médio":"R${:,.2f}".format})}</p>

    <p>Qualquer dúvida, não hesite em retornar o contato.</p>

    <p>Atenciosamente,</p>
    <p>Johnny Alysson</p>

    """

    msg = email.message.Message()
    msg['Subject'] = "Relatório"
    msg['From'] = 'Remetente'
    msg['To'] = input_email
    password = 'senhasdeappdogoogle' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()

print("Fim do programa")

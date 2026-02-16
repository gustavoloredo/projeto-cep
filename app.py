import streamlit as st
import requests

def buscar_cep(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    return resposta

st.set_page_config(
    page_title='Busca CEP',
    page_icon='🔪'
)

st.title('sistema de busca de CEP')
st.divider()

resposta = buscar_cep('05859000')

st.write(resposta.json())
    
menu = st.sidebar
cep = menu.text_input('Digite o cep')
botao = menu.button('Pesquisar')

if botao:
    
    resposta = buscar_cep(cep)
    if resposta.status_code == 200:
        st.success("CEP encontrado")
        dados = resposta.json()
        
        col1, col2 = st.columns(2)
        col1.markdown(f"**CEP:** {dados['cep']}")
        col1.markdown(f"**logradouro:** {dados['logradouro']}")
        col1.markdown(f"**complemento:** {dados['complemento']}")
        col1.markdown(f"**unidade:** {dados['unidade']}")
        col1.markdown(f"**bairro:** {dados['bairro']}")
        col1.markdown(f"**uf:** {dados['uf']}")
        col2.markdown(f"**estado:** {dados['estado']}")
        col2.markdown(f"**regiao:** {dados['regiao']}")
        col2.markdown(f"**estado:** {dados['estado']}")
        col2.markdown(f"**ibge:** {dados['ibge']}")
        col2.markdown(f"**gia:** {dados['gia']}")
        col2.markdown(f"**ddd:** {dados['ddd']}")
        col2.markdown(f"**siafi:** {dados['siafi']}")
    else:
        st.error("Cep invalido")
        
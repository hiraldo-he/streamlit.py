import streamlit as st

def app():
    st.header("FlowChat", divider=True)
    st.write("### Bem-vindo ao Flowchat!")


    # 1. Inicializa o histórico de mensagens na sessão se ele não existir
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 2. Mostra as mensagens antigas do chat assim que a página é recarregada
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 3. Caixa de entrada para o utilizador digitar
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adiciona a mensagem do utilizador ao histórico
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Exibe a mensagem do utilizador imediatamente no ecrã
        with st.chat_message("user"):
            st.markdown(prompt)

        # Resposta simulada do Bot (aqui podes integrar a tua IA futuramente)
        resposta_bot = f"Recebi a sua mensagem: {prompt}"
        
        # Adiciona a resposta do bot ao histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta_bot})
        
        # Exibe a resposta do bot no ecrã
        with st.chat_message("assistant"):
            st.markdown(resposta_bot)

if __name__ == "__main__":
    app()


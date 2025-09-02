import streamlit as st

st.set_page_config(page_title="Painel de Estudos", layout="centered")

st.title("📚 Painel de Estudos")

# Inputs do usuário
horas = st.slider("Quantas horas você estudou hoje?", 0.0, 12.0, 2.0, 0.25)
pausas = st.slider("Quantas pausas você fez?", 0, 10, 2)
atividade = st.selectbox("Tipo de atividade realizada", ["Leitura", "Exercícios", "Revisão"])

st.markdown("---")

# Exibir métricas
col1, col2, col3 = st.columns(3)
col1.metric("Horas estudadas", f"{horas} h")
col2.metric("Número de pausas", f"{pausas}")
col3.metric("Atividade", atividade)

st.markdown("---")

# Avaliação e mensagens personalizadas
msg_tempo = ""
if horas < 1:
    msg_tempo = "⏳ Estude mais para um melhor aproveitamento!"
elif 1 <= horas <= 4:
    msg_tempo = "👍 Bom tempo de estudo!"
else:
    msg_tempo = "💪 Excelente dedicação!"

msg_pausas = ""
if pausas == 0:
    msg_pausas = "⚠️ Faça pausas para melhorar a concentração."
elif 1 <= pausas <= 3:
    msg_pausas = "👌 Pausas adequadas!"
else:
    msg_pausas = "🔋 Você fez muitas pausas, cuidado para não perder o foco."

msg_atividade = ""
if atividade == "Leitura":
    msg_atividade = "📖 Leitura ajuda a absorver conteúdo."
elif atividade == "Exercícios":
    msg_atividade = "📝 Praticar com exercícios é fundamental!"
else:
    msg_atividade = "🔄 Revisar ajuda a fixar o aprendizado."

# Mostrar mensagens em 3 colunas
col_a, col_b, col_c = st.columns(3)
col_a.info(msg_tempo)
col_b.info(msg_pausas)
col_c.info(msg_atividade)

st.markdown("---")

# Expander com dicas de estudo
with st.expander("💡 Dicas de estudo"):
    st.write("""
    - Estude em blocos de 25 a 50 minutos com pausas de 5 a 10 minutos (Técnica Pomodoro).
    - Varie entre leitura, exercícios e revisão para fixar melhor o conteúdo.
    - Evite distrações, desligue notificações e organize seu local de estudo.
    - Mantenha uma alimentação leve e hidratação para manter o foco.
    - Durma bem para consolidar a memória.
    """)

# Rodapé
st.markdown(
    """
    <style>
    footer {
        visibility: visible;
        text-align: center;
        padding: 10px 0;
        font-size: 0.9em;
        color: gray;
    }
    </style>
    <footer>
    Criado com ❤️ por Davi - Painel de Estudos 2025
    </footer>
    """, unsafe_allow_html=True
)
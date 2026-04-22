import streamlit as st
import pandas as pd

st.title("📁 Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.session_state['df'] = df
    st.success("تم رفع الملف الجديد بنجاح! ✅")

if 'df' in st.session_state:
    st.info("💡 فيه بيانات متخزنة حالياً في السيستم:")
    df_to_show = st.session_state['df']
    
    st.write(f"إحصائيات سريعة: {df_to_show.shape[0]} صف و {df_to_show.shape[1]} عمود")
    st.dataframe(df_to_show.head(3)) 
    
    if st.button("حذف البيانات الحالية"):
        del st.session_state['df']
        st.rerun() 
else:
    st.warning("لا توجد بيانات مرفوعة حالياً. يرجى رفع ملف للبدء.")
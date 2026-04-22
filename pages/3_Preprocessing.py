import streamlit as st

df = st.session_state.get('df', None)

if df is None:
    st.warning("🚨 لم يتم العثور على بيانات! روح لصفحة الرفع الأول.")
    st.stop() 

st.success("تم تحميل البيانات بنجاح، ابدأ شغلك!")

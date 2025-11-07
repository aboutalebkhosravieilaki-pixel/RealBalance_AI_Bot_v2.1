
import streamlit as st
import json
from ai_core import HybridAI

st.set_page_config(page_title='RealBalance AI v2.1', layout='wide')
ai = HybridAI()

st.title('🧠 RealBalance – Hybrid Adaptive Dashboard')
st.sidebar.header('کنترل‌ها')

if st.sidebar.button('📈 تولید سیگنال جدید'):
    result = ai.get_signal()
    st.success(f"سیگنال: {result['signal']} | اطمینان: {result['confidence']}% | ریسک: {result['risk']}")

if st.sidebar.button('🔁 بازآموزی مدل'):
    ai.retrain_daily()
    st.info('مدل امروز بازآموزی شد.')

st.markdown('---')
st.caption('RealBalance™ v2.1 | Engineered by Khosravi AI Lab')


import streamlit as st
from camarilla import calculate_s4
from telegram_alert import send_telegram

st.set_page_config(page_title="Camarilla S4 Bot", layout="centered")

st.title("📈 Tradetron-style Camarilla S4 Bot (Mock v1)")

# User inputs
symbol = st.text_input("Enter Stock Symbol", "RELIANCE")
high = st.number_input("High", value=2500.0)
low = st.number_input("Low", value=2400.0)
close = st.number_input("Previous Close", value=2450.0)

# Calculate S4
if st.button("🔍 Calculate Camarilla S4"):
    s4 = calculate_s4(high, low, close)
    st.success(f"Camarilla S4 for {symbol.upper()} = {s4:.2f}")

    # Simulate price feed
    ltp = close - (high - low) * 1.05
    st.write(f"📉 Simulated Live Price (LTP): ₹{ltp:.2f}")

    if ltp < s4:
        st.warning("🔔 Price is below S4! Consider a BUY")
        if st.button("🛒 Place Buy Order (Simulated)"):
            message = f"📢 BUY signal for {symbol.upper()}\nS4: {s4:.2f}, LTP: {ltp:.2f}"
            send_telegram(message)
            st.success("Telegram Alert Sent.")
    else:
        st.info("✅ Price above S4. No action taken.")

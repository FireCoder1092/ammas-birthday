import streamlit as st
import smtplib
from email.message import EmailMessage

FROM_EMAIL = st.secrets["FROM_EMAIL"]
APP_PASSWORD = st.secrets["APP_PASSWORD"]

st.title("I'm blowing something")

# This animation only runs ONCE, not on every type
if "started" not in st.session_state:
    st.session_state.started = True
    with st.empty():
        for msg in ["Amma just wait I'm still blowing them up", "A few seconds please", "Still haven't done it...",
                    "Yayyyyyyy Happy B-day Amma!"]:
            st.info(msg)
            st.empty()  # you can use time.sleep here if you really want, but better not
    st.balloons()

st.write("Happy Birthday!")
st.write("I hope you have a lovely birthday and have a good friday (i wish it was on the weekends 😭)")
st.write("Just hold your hands together and pray for paati to get well soon.")
st.write("WHERE DO YOU WANNA GO TODAY???")

# FIX: Use a form so it doesn't rerun while typing
with st.form("birthday_form"):
    birth_year = st.number_input("What's your birth year?", min_value=1950, max_value=2026, value=1980)
    place = st.text_input("Tell me please there is something gonna happen in a few seconds:")
    submitted = st.form_submit_button("Submit & Send Email 🎉")

    if submitted:
        if not place:
            st.warning("PUT SOMETHING!!!")
        else:
            age = 2026 - int(birth_year)
            st.success(f"Yay you are {age} years old! We're going to {place}!")

            # Email part
            try:
                to_email = ["vidhyadgreat@gmail.com", "smaranpreethesh@gmail.com", "samhita.preethesh@gmail.com",
                            "preethesh@gmail.com"]
                email_message = EmailMessage()
                email_message["From"] = FROM_EMAIL
                email_message["To"] = ", ".join(to_email)
                email_message["Subject"] = "Hi everyone! Birthday Plan!"
                email_message.set_content(f"""Hello Appa, Amma and Samhita!

                Today we're going to {place}

                Hope everyone has fun and thank you appa for the bouquet!

                By Smaran""")

                with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
                    gmail.starttls()
                    gmail.login(FROM_EMAIL, APP_PASSWORD)
                    gmail.send_message(email_message)

                st.balloons()
                st.success("Email sent!")
            except Exception as e:
                st.error(f"Failed: {e}")
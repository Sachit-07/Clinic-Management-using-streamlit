import streamlit as st

st.set_page_config(
    page_title="MediCare Clinic",
    page_icon="🏥",
    layout="wide"
)

# -------------------- Simple styling --------------------
st.markdown("""
<style>
    .stApp {
        background: #eef4f8;
    }

    .login-title {
        color: #174a63;
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .login-subtitle {
        color: #617985;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .welcome-box {
        background: #dcecf3;
        padding: 35px;
        border-radius: 15px;
        margin-top: 70px;
    }

    .welcome-box h1 {
        color: #174a63;
    }

    .welcome-box p {
        color: #4d6875;
        font-size: 16px;
        line-height: 1.6;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dbe5eb;
        text-align: center;
    }

    .card h3 {
        color: #174a63;
        margin-bottom: 5px;
    }

    .card p {
        color: #526a76;
        font-size: 24px;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)


# -------------------- Login Page --------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("""
        <div class="welcome-box">
            <h1>🏥 MediCare Clinic</h1>
            <p>
                <b>Clinic Management System</b>
            </p>
            <p>
                A simple and secure portal for managing patients,
                appointments and doctors in one place.
            </p>
            <p>
                <b>✓ Patient Management</b><br>
                <b>✓ Appointment Management</b><br>
                <b>✓ Doctor Management</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="login-title">Staff Login</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="login-subtitle">Sign in to access the clinic dashboard.</div>',
            unsafe_allow_html=True
        )

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox("Remember me")

        if st.button("🔐 Sign In", type="primary", use_container_width=True):
            if username and password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Please enter your username and password.")

        if st.button("Forgot Password?", use_container_width=True):
            st.info("Please contact the clinic administrator.")

# -------------------- Dashboard --------------------
else:
    st.sidebar.title("🏥 MediCare Clinic")
    st.sidebar.caption("Clinic Management System")

    page = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Patients", "Appointments", "Doctors"]
    )

    if st.sidebar.button("Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    if page == "Dashboard":
        st.title("Clinic Dashboard")
        st.write(f"Welcome back, **{st.session_state.username}** 👋")
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class="card">
                <h3>👥 Patients</h3>
                <p>156</p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card">
                <h3>📅 Appointments</h3>
                <p>24</p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class="card">
                <h3>👨‍⚕️ Doctors</h3>
                <p>12</p>
            </div>
            """, unsafe_allow_html=True)

        st.subheader("Today's Appointments")

        st.table({
            "Time": ["10:00 AM", "11:30 AM", "1:00 PM"],
            "Patient": ["John Doe", "Sarah Kumar", "Rahul Sharma"],
            "Doctor": ["Dr. Smith", "Dr. Patel", "Dr. Thomas"]
        })

    elif page == "Patients":
        st.title("Patients")
        st.write("Patient management module.")
        st.info("Patient records can be connected to your database later.")

    elif page == "Appointments":
        st.title("Appointments")
        st.write("Appointment management module.")
        st.info("Appointment scheduling can be connected to your database later.")

    elif page == "Doctors":
        st.title("Doctors")
        st.write("Doctor management module.")
        st.info("Doctor records can be connected to your database later.")

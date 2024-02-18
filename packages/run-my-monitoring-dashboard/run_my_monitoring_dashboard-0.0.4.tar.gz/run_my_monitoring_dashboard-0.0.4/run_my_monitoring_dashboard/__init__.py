import streamlit as st
from streamlit_option_menu import option_menu
import model_monitoring_app, system_monitoring_app, business_monitoring_app

def main():
    st.set_page_config(page_title="Monitoring")

    class MultiApp:
        def __init__(self):
            self.apps = []

        def add_app(self, title, func):
            self.apps.append({
                "title": title,
                "function": func
            })

        def run(self):
            st.markdown(
                """
                <style>
                    .sidebar .sidebar-content {
                        padding-top: 5px;
                    }
                    .sidebar .sidebar-content .sidebar-collapse h1 {
                        font-size: 28px;
                        margin-bottom: 20px;
                    }
                    .sidebar .sidebar-content img {
                        width: 5px;
                        margin-bottom: 5px;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )

            # Add your custom logo with the absolute path
            st.sidebar.image("/Users/ritik.saxena/Documents/image.jpg")

            st.sidebar.header("Monitoring Dashboard")
            app_selection = st.sidebar.selectbox(
                "Select Monitoring Type",
                ('Model Monitoring', 'System Monitoring', 'Business Monitoring'),
                index=1
            )

            if app_selection == "Model Monitoring":
                model_monitoring_app.main()
            elif app_selection == "System Monitoring":
                system_monitoring_app.main()
            elif app_selection == "Business Monitoring":
                business_monitoring_app.main()

    multi_app = MultiApp()
    multi_app.run()

if __name__ == "__main__":
    main()

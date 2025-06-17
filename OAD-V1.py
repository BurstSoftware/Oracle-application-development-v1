import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Oracle Applications Developer Tech Stack",
    page_icon="🛠️",
    layout="wide"
)

# Title and introduction
st.title("🛠️ Oracle Applications Developer Tech Stack")
st.markdown("""
This application outlines the technology stack for an Oracle Applications Developer, covering tools, frameworks, and technologies used in Oracle E-Business Suite (EBS) and Oracle Cloud Applications. Use the filters to explore the stack tailored to your focus area.
""")

# Filter for application type
app_type = st.selectbox(
    "Select Oracle Application Focus:",
    ["All", "Oracle E-Business Suite (EBS)", "Oracle Cloud Applications"]
)

# Tech stack data
tech_stack = {
    "Core Technologies": [
        {"name": "Oracle E-Business Suite (EBS)", "description": "Primary platform for on-premises Oracle applications (e.g., Financials, HRMS, Supply Chain).", "applies_to": "EBS"},
        {"name": "PL/SQL", "description": "Used for stored procedures, triggers, and database logic in Oracle Database.", "applies_to": "All"},
        {"name": "SQL", "description": "For querying and manipulating data in Oracle Database.", "applies_to": "All"},
        {"name": "Oracle Forms", "description": "For building user interfaces in EBS (common in R12).", "applies_to": "EBS"},
        {"name": "Oracle Reports", "description": "For generating reports within EBS.", "applies_to": "EBS"},
        {"name": "Oracle Workflow", "description": "For designing and automating business processes.", "applies_to": "EBS"},
        {"name": "Oracle Application Framework (OAF)", "description": "For developing web-based UI in EBS.", "applies_to": "EBS"},
        {"name": "Oracle Database", "description": "Backend data store (e.g., 19c or higher).", "applies_to": "All"},
        {"name": "Oracle Fusion Middleware", "description": "For cloud-based Oracle ERP, HCM, or SCM applications.", "applies_to": "Cloud"},
        {"name": "Oracle Autonomous Database", "description": "Cloud-based data management.", "applies_to": "Cloud"}
    ],
    "Development Tools": [
        {"name": "Oracle JDeveloper", "description": "IDE for OAF development and extensions.", "applies_to": "EBS"},
        {"name": "SQL Developer/Toad", "description": "For database development and querying.", "applies_to": "All"},
        {"name": "Oracle BI Publisher", "description": "For advanced reporting and document generation.", "applies_to": "All"},
        {"name": "Oracle Discoverer", "description": "For ad-hoc querying and reporting (less common).", "applies_to": "EBS"},
        {"name": "Oracle Visual Builder Cloud Service (VBCS)", "description": "For building custom UIs in Oracle Cloud.", "applies_to": "Cloud"}
    ],
    "Integration and Middleware": [
        {"name": "Oracle SOA Suite", "description": "For service-oriented architecture and integrations.", "applies_to": "All"},
        {"name": "Oracle Integration Cloud (OIC)", "description": "For cloud-based integrations.", "applies_to": "Cloud"},
        {"name": "Oracle WebLogic Server", "description": "Application server for deploying custom applications.", "applies_to": "All"},
        {"name": "XML/BPEL", "description": "For defining business processes and data exchange.", "applies_to": "All"},
        {"name": "REST/SOAP APIs", "description": "For integrations with Oracle Cloud and external systems.", "applies_to": "Cloud"}
    ],
    "Programming and Scripting": [
        {"name": "Java", "description": "For customizations, extensions, and OAF development.", "applies_to": "All"},
        {"name": "JavaScript/HTML/CSS", "description": "For enhancing web-based UI in OAF or cloud apps.", "applies_to": "All"},
        {"name": "Shell Scripting", "description": "For automation in Unix/Linux environments.", "applies_to": "EBS"},
        {"name": "Python", "description": "For scripting and automation in modern setups.", "applies_to": "All"}
    ],
    "Version Control and DevOps": [
        {"name": "Git/SVN", "description": "For source code version control.", "applies_to": "All"},
        {"name": "Jenkins/Oracle DevOps", "description": "For CI/CD pipelines.", "applies_to": "All"},
        {"name": "JIRA/Oracle ALM", "description": "For project management and issue tracking.", "applies_to": "All"}
    ],
    "Additional Skills (Optional)": [
        {"name": "Oracle APEX", "description": "For rapid application development.", "applies_to": "All"},
        {"name": "ETL Tools (e.g., Informatica, ODI)", "description": "For data integration.", "applies_to": "All"},
        {"name": "BI Tools (e.g., OBIEE, Oracle Analytics Cloud)", "description": "For analytics and dashboards.", "applies_to": "All"}
    ]
}

# Display tech stack
for category, items in tech_stack.items():
    with st.expander(f"📚 {category}", expanded=True):
        for item in items:
            # Filter based on selected application type
            if app_type == "All" or item["applies_to"] == "All" or item["applies_to"] == app_type:
                st.subheader(item["name"])
                st.write(item["description"])
                st.markdown("---")

# Footer
st.markdown("""
---
**Note**: The tech stack may vary based on the organization and specific Oracle application version. For more details, check out [Oracle's official documentation](https://docs.oracle.com) or explore [xAI's API services](https://x.ai/api) for related integrations.
""")

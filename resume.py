# resume.py
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np

# Resume data
resume_data = {
    "name": "Allen Kelly Imawe",
    "contact": {
        "address": "No. 1 Omachi Lane, Rumurolu, Woji, Port Harcourt, Rivers State, Nigeria",
        "mobile": "+2348122225234",
        "email": "allen.k.imawe@gmail.com",
        "linkedin": "linkedin.com/in/me"
    },
    "summary": (
        "Seasoned IT professional with over a decade of experience in data analysis, business intelligence, "
        "and IT infrastructure. Proficient in leveraging tools such as Excel, SQL, Power BI, and Tableau to "
        "transform complex data into actionable insights."
    ),
    "skills": {
        "Data Analysis & BI": "Advanced proficiency in Microsoft Excel, SQL, Power BI, Tableau",
        "IT Infrastructure": "Network setup, IT security protocols, system administration",
        "Application Support": "ERP systems management, software troubleshooting, process automation"
    },
    "experience": [
        ("SkillBoost Africa", "Data Analytics Intern", "2024 – Present", 
         "Focused on data cleaning, analysis, and visualization using Excel and Power BI."),
        ("Accenture North America", "Data Analytics Internship", "2025", 
         "Analyzed datasets for content trends in a client simulation."),
        ("PwC Switzerland", "Power BI Internship", "2025", 
         "Created dashboards to convey KPIs and HR data insights."),
        ("Franklear Resources", "ICT Manager", "2022 – 2023", 
         "Managed IT infrastructure and optimized software performance."),
        ("Kami Integrated Service", "Admin & Business Development", "2017 – 2022", 
         "Boosted sales with digital marketing and IT solutions."),
        ("CISNET Limited", "Senior IT Engineer", "2011 – 2015", 
         "Administered Windows server environments."),
        ("CISCON Nigeria Limited", "Head of ICT", "2006 – 2010", 
         "Led IT infrastructure and security projects.")
    ],
    "education": [
        ("Master’s in Computer Science (In Progress)", "Rivers State University of Science and Technology"),
        ("Bachelor of Technology in Computer Engineering", "Rivers State University of Science and Technology")
    ],
    "certifications": [
        "SkillBoost Africa: Data Analytics Training",
        "ITIL V3 Certified",
        "Microsoft Certified Technology Specialist (MCTS)"
    ]
}

class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Allen Kelly Imawe - Resume")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1e1e2f")

        # Title
        tk.Label(root, text=resume_data["name"], font=("Helvetica", 24, "bold"), fg="#ffffff", bg="#1e1e2f").pack(pady=20)

        # Tabs
        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, expand=True, fill="both")

        self.add_tab(notebook, "Summary", self.summary_tab)
        self.add_tab(notebook, "Skills", self.skills_tab)
        self.add_tab(notebook, "Experience", self.experience_tab)
        self.add_tab(notebook, "Education & Certifications", self.education_tab)

    def add_tab(self, notebook, title, tab_function):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=title)
        tab_function(frame)

    def summary_tab(self, frame):
        tk.Label(frame, text=resume_data["summary"], font=("Arial", 12), wraplength=900, justify="left", 

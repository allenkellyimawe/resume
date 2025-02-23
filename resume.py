import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np
import time

# Resume data based on provided document
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
        "transform complex data into actionable insights. Demonstrated expertise in IT security, network "
        "infrastructure, and application support, with a strong focus on automation and process optimization."
    ),
    "skills": {
        "Data Analysis & BI": "Advanced proficiency in Microsoft Excel, SQL, Power BI, Tableau",
        "IT Infrastructure": "Network setup, IT security protocols, system administration",
        "Application Support": "ERP systems management, software troubleshooting, process automation"
    },
    "experience": [
        ("SkillBoost Africa", "Data Analytics Intern", "2024 – Present", 
         "Participated in data analytics training, focusing on data cleaning, analysis, and visualization."),
        ("Accenture North America", "Data Analytics and Visualisation Internship", "2025", 
         "Completed a simulation advising a social media client, analyzing datasets for content trends."),
        ("PwC Switzerland", "Power BI Internship", "2025", 
         "Created dashboards to convey KPIs and analyzed HR data for gender balance insights."),
        ("Franklear Resources", "ICT Manager / Business Development Team", "2022 – 2023", 
         "Managed IT infrastructure and optimized business software performance."),
        ("Kami Integrated Service", "Admin & Business Development", "2017 – 2022", 
         "Leveraged digital marketing and IT solutions to boost sales."),
        ("CISNET Limited", "Senior IT Engineer", "2011 – 2015", 
         "Administered Windows server environments and provided application support."),
        ("CISCON Nigeria Limited", "Head of ICT", "2006 – 2010", 
         "Led IT infrastructure projects and managed corporate internet security.")
    ],
    "education": [
        ("Master’s in Computer Science (In Progress)", "Rivers State University of Science and Technology"),
        ("Bachelor of Technology in Computer Engineering", "Rivers State University of Science and Technology")
    ],
    "certifications": [
        "SkillBoost Africa: Data Analytics Training – Advanced Excel, SQL, Power BI, Tableau",
        "ITIL V3 Certified – IT Service Management",
        "Microsoft Certified Technology Specialist (MCTS) – Windows Server"
    ]
}

# Main Application
class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Allen Kelly Imawe - Animated Resume")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1e1e2f")

        # Title Label
        self.title = tk.Label(root, text=resume_data["name"], font=("Helvetica", 24, "bold"), fg="#ffffff", bg="#1e1e2f")
        self.title.pack(pady=20)

        # Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Add tabs
        self.add_tab("Summary", self.summary_tab)
        self.add_tab("Skills", self.skills_tab)
        self.add_tab("Experience", self.experience_tab)
        self.add_tab("Education & Certifications", self.education_tab)

    def add_tab(self, title, tab_function):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        tab_function(frame)

    def summary_tab(self, frame):
        summary_text = tk.Label(frame, text=resume_data["summary"], font=("Arial", 12), wraplength=900, justify="left", bg="#2d2d44", fg="#ffffff")
        summary_text.pack(pady=20, padx=20)

        # Contact Info
        contact = "\n".join([f"{k.capitalize()}: {v}" for k, v in resume_data["contact"].items()])
        contact_label = tk.Label(frame, text=contact, font=("Arial", 10), bg="#2d2d44", fg="#cccccc")
        contact_label.pack(pady=10)

    def skills_tab(self, frame):
        fig, ax = plt.subplots(figsize=(8, 4))
        skills = list(resume_data["skills"].keys())
        levels = [90, 85, 80]  # Simulated proficiency levels for animation
        bars = ax.bar(skills, [0]*len(skills), color="#4ecca3")
        ax.set_ylim(0, 100)
        ax.set_title("Technical Skills Proficiency", fontsize=14, color="#ffffff")
        ax.set_facecolor("#2d2d44")
        fig.patch.set_facecolor("#2d2d44")
        ax.tick_params(colors="#ffffff")

        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().pack(pady=20)

        def animate(frame_num):
            for bar, h in zip(bars, levels):
                bar.set_height(min(h, frame_num))
            return bars

        ani = FuncAnimation(fig, animate, frames=range(0, 101, 2), interval=50, blit=True, repeat=False)
        canvas.draw()

    def experience_tab(self, frame):
        for company, role, period, desc in resume_data["experience"]:
            exp_frame = tk.Frame(frame, bg="#2d2d44")
            exp_frame.pack(pady=10, padx=20, fill="x")
            tk.Label(exp_frame, text=f"{company} - {role}", font=("Arial", 14, "bold"), bg="#2d2d44", fg="#4ecca3").pack(anchor="w")
            tk.Label(exp_frame, text=period, font=("Arial", 10, "italic"), bg="#2d2d44", fg="#cccccc").pack(anchor="w")
            tk.Label(exp_frame, text=desc, font=("Arial", 10), wraplength=900, justify="left", bg="#2d2d44", fg="#ffffff").pack(anchor="w")

    def education_tab(self, frame):
        for degree, school in resume_data["education"]:
            tk.Label(frame, text=f"{degree}", font=("Arial", 12, "bold"), bg="#2d2d44", fg="#4ecca3").pack(pady=5, padx=20, anchor="w")
            tk.Label(frame, text=school, font=("Arial", 10), bg="#2d2d44", fg="#ffffff").pack(anchor="w")
        tk.Label(frame, text="Certifications:", font=("Arial", 12, "bold"), bg="#2d2d44", fg="#4ecca3").pack(pady=10, padx=20, anchor="w")
        for cert in resume_data["certifications"]:
            tk.Label(frame, text=f"• {cert}", font=("Arial", 10), bg="#2d2d44", fg="#ffffff").pack(padx=40, anchor="w")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()
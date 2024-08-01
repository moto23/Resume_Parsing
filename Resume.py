import json

# Resume content as a string
resume_content = """
Prasad Nathe
+91 7378552793 | prasadnathe2018@gmail.com | Github Profile | Linkedin Profile

EDUCATION

B.Tech Information Technology | VIIT, PUNE CGPA: 8.5 | 2021-2025 (Present)

EXPERIENCE

Software Engineer Intern | YantrikiSoft Mumbai (Remote) (12 Jan – 10 June 2024)
• Designed Kgamify (Teacher panel) Website for managing the Playquest (User Platform) Application where users can learn and win prizes by competing in championships and quizzes.
• The mobile app offers various subjects, storing achievements to assess users' proficiency. An hosted Teacher Portal manages users, content, and technical aspects. Certificate | Live
• Focused on mobile app and website front-end UI development, contributing to a 30% increase in user engagement securing in funding for StartUp.
• Tools and Technologies:- PHP, RESTful API, IntelliJ Idea, Flutter, Firebase, JavaScript, and MySQL.

PROJECTS

StealthMode Courses Website (Individual Project) Git-Repo | Live
• Developed a Learning Hub Platform offering industry-tailored Courses to learn new skills with responsive UI.
• Implemented secure user authentication and authorization, along with a review and rating system.
• Integrated third-party APIs and payment gateways to streamline the Enrollment process.
• Tools and Technologies:- React.js, Material-UI & Redux, Node.js & Express.js, MongoDB, Razorpay.

DevDyanamics Dashboard (Industry Project) Git-Repo | Live
• Developed an interactive dashboard using Line, Bar, and Pie Charts to visualize developer activity data, enhancing team productivity tracking by 40% and providing actionable insights for process optimization over selected date ranges.
• The activities include committing code, opening pull requests, merging pull requests, attending meetings, and writing documentation with Date, Contributor filters, and Summary Statistics.
• Tools and Technologies:- React.js, TypeScript, RESTful APIs, CSS, Recharts, Axios, Data Visualization.

Image-to-image translation with a conditional GAN (Course Project) Git-Repo
• Developed and trained a pix2pix cGAN for image-to-image translation, focusing on generating building facades.
• Used the CMP Facade Database to implement a U-Net generator and PatchGAN discriminator, optimizing image generation on a V100 GPU.
• Tools and Technologies:- Python, TensorFlow, CMP Facade Database, NumPy, Matplotlib.

SKILLS

• Fundamentals: OOPs, Cloud Computing, Data Structures and Algorithm, Database Management, AI/ML.
• Technologies: AWS, Linux, RESTful APIs, React, MongoDB, ExpressJs, Firebase, Bootstrap.
• Languages: C++, Python, Java, PHP, HTML5, CSS, JavaScript, MySQL.
• Developer Tools: Vs Code, GitHub, Figma, WordPress, Flutter, Docker, Postman.

ACHIEVEMENTS

• Solved 400+ Problems on LeetCode with Highest Rating of 1408. LeetCode
• Our Team Achieved 3rd place in Hackathon organized By GFG in domain of EdTech.
• Ranked 23rd among the 200 Participants in the CodeChef college Challenge. CodeChef

POSITION OF RESPONSIBILITY

Technical Lead | IOT Form, VIIT (Nov 2022-May 2023)
• Successfully organized and led multiple hackathons with around 150+ teams focused on web and app development for college and inter-college students.
• Participated in the analysis, design, development, unit testing, deployment, and code review processes for maintaining Club Activities.
• Conducted Career Guidance Session About Current Emerging Technologies for Career Growth.

PUBLICATIONS

• Paper Published-In-2024 MIT Art, Design and Technology School of Computing International Conference (MITADTSoCiCon) :- Developed AI HeathCare Chatbot using NLP. Link
"""

# Function to parse the resume content into a structured dictionary
def parse_resume(content):
    lines = content.split("\n")
    
    def extract_contact_info(lines):
        contact_info = {"name": "", "contact": "", "email": "", "github": "", "linkedin": ""}
        if len(lines) > 0:
            contact_info["name"] = lines[0].strip()
        if len(lines) > 1:
            contact_parts = lines[1].split("|")
            contact_info["contact"] = contact_parts[0].strip() if len(contact_parts) > 0 else ""
            contact_info["email"] = contact_parts[1].strip() if len(contact_parts) > 1 else ""
            contact_info["github"] = contact_parts[2].strip() if len(contact_parts) > 2 else ""
            contact_info["linkedin"] = contact_parts[3].strip() if len(contact_parts) > 3 else ""
        return contact_info

    def extract_education(lines, start_index):
        education = []
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            degree, institution, cgpa_years = lines[i].split(" | ")
            education.append({
                "degree": degree.strip(),
                "institution": institution.strip(),
                "cgpa": cgpa_years.split(": ")[1].split(" | ")[0].strip(),
                "years": cgpa_years.split(" | ")[1].strip()
            })
        return education

    def extract_experience(lines, start_index):
        experience = []
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            experience_parts = lines[i].split(" | ")
            details = lines[i + 1:i + 5]
            responsibilities = [line.strip()[2:] for line in details if line.strip()]
            experience.append({
                "title": experience_parts[0].strip(),
                "company": experience_parts[1].strip(),
                "duration": experience_parts[2].strip(),
                "responsibilities": responsibilities
            })
        return experience

    def extract_projects(lines, start_index):
        projects = []
        project = {}
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            if "Git-Repo" in lines[i]:
                if project:
                    projects.append(project)
                project = {
                    "title": lines[i].split("(")[0].strip(),
                    "git_repo": lines[i].split("Git-Repo")[1].split("|")[0].strip(),
                    "live_link": lines[i].split("Git-Repo")[1].split("|")[1].strip(),
                    "description": []
                }
            elif "•" in lines[i]:
                project["description"].append(lines[i].strip()[2:])
        if project:
            projects.append(project)
        return projects

    def extract_skills(lines, start_index):
        skills = {"fundamentals": [], "technologies": [], "languages": [], "developer_tools": []}
        skill_category = None
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            if ":" in lines[i]:
                skill_category = lines[i].split(":")[0].strip().lower()
            elif "•" in lines[i]:
                skills[skill_category].append(lines[i].strip()[2:])
        return skills

    def extract_achievements(lines, start_index):
        achievements = []
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            if "•" in lines[i]:
                achievements.append({"achievement": lines[i].strip()[2:]})
        return achievements

    def extract_positions(lines, start_index):
        positions = []
        position = {}
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            if "|" in lines[i]:
                if position:
                    positions.append(position)
                parts = lines[i].split("|")
                position = {
                    "title": parts[0].strip(),
                    "organization": parts[1].strip(),
                    "duration": parts[2].strip(),
                    "responsibilities": []
                }
            elif "•" in lines[i]:
                position["responsibilities"].append(lines[i].strip()[2:])
        if position:
            positions.append(position)
        return positions

    def extract_publications(lines, start_index):
        publications = []
        for i in range(start_index, len(lines)):
            if lines[i].strip() == "":
                break
            if "•" in lines[i]:
                parts = lines[i].strip()[2:].split(" :- ")
                publications.append({
                    "title": parts[1].strip(),
                    "conference": parts[0].strip(),
                    "link": parts[1].split("Link")[1].strip()
                })
        return publications

    resume_dict = {
        "personal_info": extract_contact_info(lines),
        "education": extract_education(lines, lines.index("EDUCATION") + 1) if "EDUCATION" in lines else [],
        "experience": extract_experience(lines, lines.index("EXPERIENCE") + 1) if "EXPERIENCE" in lines else [],
        "projects": extract_projects(lines, lines.index("PROJECTS") + 1) if "PROJECTS" in lines else [],
        "skills": extract_skills(lines, lines.index("SKILLS") + 1) if "SKILLS" in lines else {},
        "achievements": extract_achievements(lines, lines.index("ACHIEVEMENTS") + 1) if "ACHIEVEMENTS" in lines else [],
        "positions_of_responsibility": extract_positions(lines, lines.index("POSITION OF RESPONSIBILITY") + 1) if "POSITION OF RESPONSIBILITY" in lines else [],
        "publications": extract_publications(lines, lines.index("PUBLICATIONS") + 1) if "PUBLICATIONS" in lines else []
    }

    return resume_dict

# Parsing the resume content
resume_dict = parse_resume(resume_content)

# Converting the dictionary to JSON format
resume_json = json.dumps(resume_dict, indent=4)

# Output the JSON
print(resume_json)

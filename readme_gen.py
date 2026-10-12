def pic(name, alt, extra=""):
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/{name}.svg">'
            f'<img src="assets/light/{name}.svg" alt="{alt}" {extra}/></picture>')

def btn(name, label, url):
    h = 'height="40"'
    return f'<a href="{url}">{pic(name, label, h)}</a>'

def chip(text, color):
    t = text.replace("-", "--").replace(" ", "%20").replace("&", "%26")
    return f'![{text}](https://img.shields.io/badge/{t}-{color}?style=flat-square)'

def chips(items, color):
    return " ".join(chip(i, color) for i in items)

def stat(kind, theme):
    # theme colors matching current README design
    L = dict(bg="FFFBFE", title="6750A4", text="49454E", icon="EFB8C8", ring="6750A4", fire="EFB8C8", lab="6750A4", stroke="49454E")
    D = dict(bg="211F26", title="D0BCFF", text="CAC4D0", icon="EFB8C8", ring="D0BCFF", fire="EFB8C8", lab="D0BCFF", stroke="49454E")
    c = L if theme == "light" else D
    if kind == "stats":
        return (f'https://github-readme-stats-fast.vercel.app/api?username=rony1duet&show_icons=true&hide_border=true&border_radius=24'
                f'&bg_color={c["bg"]}&title_color={c["title"]}&text_color={c["text"]}&icon_color={c["icon"]}')
    if kind == "langs":
        return (f'https://github-readme-stats-fast.vercel.app/api/top-langs/?username=rony1duet&layout=compact&hide_border=true&border_radius=24'
                f'&bg_color={c["bg"]}&title_color={c["title"]}&text_color={c["text"]}')
    return (f'https://streak-stats.demolab.com/?user=rony1duet&hide_border=true&border_radius=24&background={c["bg"]}'
            f'&ring={c["ring"]}&fire={c["fire"]}&currStreakNum={c["text"]}&sideNums={c["text"]}'
            f'&currStreakLabel={c["title"]}&dateRangeLabel={c["title"]}&dates={c["text"]}'
            f'&excludeDaysLabel={c["title"]}&sideLabels={c["title"]}&stroke={c["stroke"]}')

def spic(kind, alt):
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{stat(kind,"dark")}">'
            f'<img src="{stat(kind,"light")}" alt="{alt}" /></picture>')

LI, PF, EM, GH, TG = ("https://www.linkedin.com/in/rony1duet/", "https://rony1duet.github.io/gitcodehub/",
                      "mailto:rony.hossen.duet@gmail.com", "https://github.com/rony1duet", "https://t.me/rony1duet")
VC = "https://hits.sh/github.com/rony1duet.svg?style=flat-square&label=Views&color=6750A4"
VC_DARK = "https://hits.sh/github.com/rony1duet.svg?style=flat-square&label=Views&color=D0BCFF"
views_btn = (f'<a href="{GH}"><picture><source media="(prefers-color-scheme: dark)" srcset="{VC_DARK}">'
             f'<img src="{VC}" alt="Views" height="40"/></picture></a>')
btns = [btn("btn-email", "Email", EM), btn("btn-linkedin", "LinkedIn", LI), views_btn,
        btn("btn-portfolio", "Portfolio", PF), btn("btn-telegram", "Telegram", TG)]
buttons = " ".join(btns)

stack = [("Languages", ["Python", "Java", "C", "C++"], "6750A4"),
         ("Web", ["JavaScript", "React", "Django"], "625B71"),
         ("Cloud & DevOps", ["Azure", "Google Cloud", "Docker"], "7D5260"),
         ("Data & APIs", ["Firebase", "OpenAI API", "OpenCode"], "006874"),
         ("Hardware & tools", ["Arduino", "Linux", "GitHub Actions"], "7A5900")]
stack_rows = "\n".join(f"| **{n}** | {chips(i, c)} |" for n, i, c in stack)

projects = [
    ("Chokkhori Magazine", "ChokkhoriMagazine", "Web Developer", "A modern, lightweight, PHP-based web magazine built for Bengali literature enthusiasts, featuring dynamic content management."),
    ("WinCalc", "WinCalc", "Desktop Developer", "A Windows calculator application built with C# and Visual Studio 2022, supporting basic arithmetic operations through a clean interface."),
    ("DUET Mosque Connect", "DUET_Mosque_Connect", "Android Developer", "An Android application built with Kotlin to support mosque community connectivity and management at DUET."),
    ("SecureChat", "SecureChat-ThirdParty-API", "App Developer", "A mobile messaging application integrating third-party APIs to deliver its core communication features."),
    ("Secure LAB Setup", "SecureLabSetup", "Hardware & Software Developer", "A project focused on creating a more secure and fair environment for laboratory examinations."),
    ("gitcodehub", "gitcodehub", "Web Developer", "A responsive portfolio website showcasing projects, technical skills, and development work."),
    ("XORA", "XORA", "Software Developer", "A TypeScript-based project exploring modern web technologies and software development."),
]
proj_rows = "\n".join(f"| **[{name}]({GH}/{repo})** <br> <sub>{role}</sub> | {description} |"
                      for name, repo, role, description in projects)

connect_buttons = " ".join([btn("btn-email", "Email", EM), btn("btn-linkedin", "LinkedIn", LI),
                            btn("btn-portfolio", "Portfolio", PF), btn("btn-telegram", "Telegram", TG)])

md = f"""<div align="center">

{pic("hero", "Md. Rony Hossen - Computer Hardware Engineer and Web Developer", 'width="100%"')}

Cloud computing, IoT, and the systems that connect hardware to software.

{buttons}

</div>

## About

<div align="justify">

Hey, I'm Md. Rony Hossen, a computer hardware enthusiast and web developer studying at Dhaka University of Engineering & Technology, Gazipur, Bangladesh.

I enjoy figuring out how things work and turning ideas into something real. Sometimes that means building custom Android ROMs for the Redmi Note 12 Pro 4G or working on OpenCore EFI configurations. Other times, it's developing Kotlin applications, building websites, or creating Windows desktop tools that solve real-world problems.

Over time, I've explored different technologies, including Android, Kotlin, PHP, C#, and TypeScript. Some of the projects I've worked on include the DUET Mosque Connect app, OpenCore EFI, Chokkhori Magazine and Resume Builder website, WinCalc Windows app, XORA for the NASA Space Apps Challenge, SecureChat mobile application, and Secure LAB Setup a project focused on fair lab examinations. Each project gives me an opportunity to learn something new, experiment with ideas, and become a better developer.

What fascinates me most is the intersection of hardware and software understanding what happens under the hood and discovering how technology can solve practical problems. I'm currently exploring IoT and AI/ML while continuing to learn, experiment, and contribute to the open-source community.

I'm still learning, still building, and always curious about what I can create next. For me, engineering is about staying curious, solving problems, sharing knowledge, and turning ideas into things that actually work.

</div>

## Tech stack

| Area | Skills |
| --- | --- |
{stack_rows}

## Featured projects

| Project | What it does |
| --- | --- |
{proj_rows}

[View all projects on GitHub]({GH}?tab=repositories)

## GitHub activity

<div align="center">

{spic("stats", "GitHub stats")}

{spic("streak", "Contribution streak")}

{spic("langs", "Top languages")}

</div>

## Connect

<div align="center">
I'm open to conversations, collaboration, and new projects.
</div>

<br/>

<div align="center">

{connect_buttons}
<br/>

<sub>Exploring where hardware, software, and the cloud meet.</sub>

</div>
"""
open("README.md", "w").write(md)

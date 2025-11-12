from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Projects data
    # Profile data
    profile = {
        'name': 'Wajahat Ashraf',
        'title': 'Data Engineering • Cloud • Automation',
        'email': 'wajahatashraf420@gmail.com',
        'phone': '+92 333 6188437',
        'location': 'Rawalpindi, Pakistan',
        'github': 'https://github.com/wajahatashraf',
        'linkedin': 'https://www.linkedin.com/in/wajahatashraf99',
        'profile_picture': '/static/images/profile.jpeg'  # Add this line
    }
    projects = [
        {
            "id": 1,
            "title": "ThinkGIS Scraper",
            "summary": "Full-stack automated scraping system for extracting multi-layer zoning data from WTHGIS county maps. Features include Selenium-based dynamic layer extraction, robust feature scraping with retries, job management, real-time logs, and GeoJSON export for download and mapping.",
            "stack": ["Python", "Selenium", "FastAPI", "WebSockets", "Docker", "Cloud Storage (AWS S3)"],
            "repo": "https://github.com/wajahatashraf/ThinkGIS_Scaper",
            "img": "/static/images/thinkgis.png",
            "metrics": {"records": "200K+", "counties": 120},
            "role": "Project Owner & Lead Developer — Designed and implemented a full-stack scraping pipeline with front-end layer selection, job queueing, live log monitoring, and GeoJSON export capabilities.",
            "features": [
                "Automated discovery and extraction of zoning layers via Selenium",
                "Dynamic feature scraping loop with error handling and retry logic",
                "Parallel job execution with isolated logs and status tracking",
                "Real-time job monitoring via WebSocket-powered console",
                "Export and download of clean GeoJSON FeatureCollections",
                "Interactive frontend for inputting county URLs, selecting layers, and monitoring jobs"
            ]
        },
        {
            'id': 2,
            'title': 'Beacon Scraper',
            'summary': 'Stealth web scraping system to extract multi-layer zoning datasets while bypassing Cloudflare protections. Automates layer discovery, bounding box calculation, data extraction, database storage, and GeoJSON export for GIS review.',
            'stack': ['Python', 'Web Scraping & Automation', 'Relational Database', 'Docker', 'Queue Management'],
            'repo': 'https://github.com/wajahatashraf/Beacon_Scraper',
            'img': 'static/images/beacon.png',
            'metrics': {'records': '500K+', 'cities': 450},
            'role': 'Project Owner & Lead Developer — Designed and implemented a stealth scraping pipeline using automated browser interactions to bypass Cloudflare, extract zoning layers, calculate spatial extents, and generate GIS-ready outputs.',
            'features': [
                'Undetectable browser automation with user-like interactions to bypass Cloudflare',
                'Automatic extraction of zoning layers and spatial extents',
                'Bounding box calculation and database storage of geometries',
                'Data normalization and attribute trimming'
            ]
        },
        {
            "id": 3,
            "title": "Google Docs Macro",
            "summary": "Google Docs macro that connects with an external organizational API to fetch zoning data. Users can input latitude/longitude coordinates or an address to retrieve zoning information and associated geometries, which can also be visualized on OpenStreetMap for spatial context.",
            "stack": ["Apps Script", "REST API", "OpenStreetMap"],
            "repo": "https://github.com/wajahatashrafGoogle-Docs-Marco",
            "img": "static/images/gdocs.png",
            "metrics": {"docs": "100+", "refresh": "Realtime", "users": "20+", "response_time": "<2s"},
            "role": "Owner — Designed the macro and API integration for on-demand zoning data retrieval and visualization within Google Docs.",
            "features": [
                "Fetch zoning data using latitude/longitude or address",
                "Retrieve zoning details with geometries from the API",
                "Display results directly inside Google Docs",
                "Visualize geometries on OpenStreetMap"
            ]
        }
    ]

    # Services data
    services = [
        {
            'title': 'Data Extraction',
            'desc': 'Advanced web scraping, PBF & raster parsing, API discovery and automation.',
            'icon': '🔍',
            'color': 'from-purple-500 to-blue-500'
        },
        {
            'title': 'Data Engineering',
            'desc': 'ETL pipelines, data normalization, relational & geospatial database design and optimization.',
            'icon': '⚙️',
            'color': 'from-green-500 to-teal-500'
        },
        {
            'title': 'Cloud Deployments',
            'desc': 'AWS EC2/S3/Elastic Beanstalk, Docker, Kubernetes, and autoscaling setups.',
            'icon': '☁️',
            'color': 'from-orange-500 to-red-500'
        },
        {
            'title': 'Search & Indexing',
            'desc': 'Relational → non-relational search sync pipelines, search optimization and tuning.',
            'icon': '📊',
            'color': 'from-yellow-500 to-orange-500'
        },
        {
            'title': 'Automation & CI/CD',
            'desc': 'Docker, Jenkins, GitHub Actions, pipeline monitoring and deployment automation.',
            'icon': '🤖',
            'color': 'from-blue-500 to-purple-500'
        },
        {
            'title': 'Reporting & Analytics',
            'desc': 'Google Docs macros, APIs, live dashboards and data visualization.',
            'icon': '📈',
            'color': 'from-teal-500 to-green-500'
        }
    ]

    # Timeline data
    timeline = [
        {
            'date': 'Jan 2024 – Present',
            'title': 'Data Scientist',
            'org': 'Magma Systems (Zoneomics)',
            'details': (
                'Lead the design, development, and automation of large-scale geospatial, zoning, and parcel data pipelines. '
                'Streamlined end-to-end ingestion, processing, scraping, transformation, and syncing workflows using Python, '
                'Flask APIs, PostgreSQL, Elasticsearch, AWS, Docker, and Jenkins. Optimized production data systems to support '
                'analytics, dashboards, and AI-powered products across Zoneomics.'
            ),
            'achievements': [
                'Automated multi-pipeline ingestion/update system for zoning, parcel, parking, raster, PBF, and tabular datasets',
                'Developed Flask-based APIs to handle automated data insertion, processing, validation, and retrieval',
                'Built large-scale web scraping pipelines for structured and unstructured data from multiple U.S. city websites',
                'Developed automated solutions to extract and standardize parking-related data into clean JSON formats',
                'Implemented cross-database synchronization workflows between relational and non-relational systems',
                'Designed and enforced data integrity and quality-check layers to ensure accurate and reliable outputs',
                'Built automated email pipelines (daily/weekly/monthly) for various operational and business scenarios',
                'Optimized data processing and ETL workflows to reduce runtime, improve efficiency, and support high-volume data',
                'Leveraged AWS services (EC2, S3, Elastic Beanstalk) for scalable, reliable, and secure deployment',
                'Managed containerized environments with Docker and automated CI/CD pipelines using Jenkins and Git',
                'Integrated monitoring and alerting dashboards to track pipeline performance and proactively detect failures'
            ]
        },
        {
            'date': '2023 – 2024',
            'title': 'Data Analyst',
            'org': 'COMSATS University Islamabad',
            'details': (
                'Supported faculty and research groups with analytical tasks, automation workflows, and applied ML projects. '
                'Contributed to real-world data preparation, research experiments, and technical mentoring within the department.'
            ),
            'achievements': [
                'Designed and automated scripts for data cleaning, preprocessing, and feature extraction',
                'Assisted in developing ML prototypes for image processing and pattern recognition tasks',
                'Built small-scale automation systems using sensors, microcontrollers, and Python pipelines',
                'Guided junior students in Python, algorithms, and applied data engineering practices'
            ]
        },
        {
            'date': '2020 – 2024',
            'title': 'B.S. Computer Engineering',
            'org': 'COMSATS University Islamabad',
            'details': (
                'Focused on data engineering, algorithms, databases, and embedded systems. '
                'Gained hands-on experience in data pipelines, ETL workflows, data processing, and research in machine learning.'
            ),
            'achievements': [
                'Built ETL pipelines and automated data processing workflows for academic projects',
                'Implemented database-driven projects using SQL, PostgreSQL, and data integration techniques',
                'Conducted research in machine learning and data analytics with practical dataset applications',
                'Best Final Year Project award for data-focused research'
            ]
        }

    ]

    # Skills data
    skills = [
        {'name': 'Python', 'level': 96, 'icon': '🐍'},
        {'name': 'SQL / PostgreSQL', 'level': 98, 'icon': '🗄️'},
        {'name': 'Web Scraping', 'level': 95, 'icon': '🕷️'},
        {'name': 'AWS', 'level': 92, 'icon': '☁️'},
        {'name': 'Docker & CI/CD', 'level': 95, 'icon': '🐳'},
        {'name': 'Elasticsearch', 'level': 85, 'icon': '🔍'},
        {'name': 'JavaScript', 'level': 88, 'icon': '🟨'},
        {'name': 'Jenkins', 'level': 95, 'icon': '⚙️'},
        {'name': 'FastAPI / Flask / REST', 'level': 95, 'icon': '🌐'},  # <- combined
        {'name': 'Git / GitHub', 'level': 97, 'icon': '🛠️'},
        {'name': 'Grafana / Monitoring', 'level': 82, 'icon': '📈'},
        {'name': 'CI/CD Pipelines', 'level': 93, 'icon': '🚀'},
        {'name': 'Data Visualization', 'level': 96, 'icon': '📉'}
    ]

    # Technologies
    technologies = [
        {'name': 'Scrapy', 'category': 'Web Scraping'},
        {'name': 'Selenium', 'category': 'Web Scraping'},
        {'name': 'React', 'category': 'Frontend'},
        {'name': 'Redis', 'category': 'Cache'},
        {'name': 'PostgreSQL', 'category': 'Database'},
        {'name': 'Flask', 'category': 'Backend'},
        {'name': 'FastAPI', 'category': 'Backend'},
        {'name': 'Celery', 'category': 'Task Queue'},
        {'name': 'TailwindCSS', 'category': 'CSS Framework'},
        {'name': 'AWS', 'category': 'Cloud'},
        {'name': 'S3', 'category': 'Cloud Storage'},
        {'name': 'CloudWatch', 'category': 'Monitoring'},
        {'name': 'Docker', 'category': 'Containerization'}
    ]

    # Certifications
    certifications = [

        {
            'name': 'Generative AI: Introduction and Applications',
            'issuer': 'IBM via Coursera',
            'year': 'July 2025',
            'details': (
                'Covered fundamentals of Generative AI vs Discriminative AI, practical applications across industries, '
                'AI tools for text, image, audio, video, and code generation, and skills like Prompt Engineering and Content Creation.'
            ),
            'link': 'https://coursera.org/share/f0e90106437084eb86acc097d444de24'
        },
        {
            'name': 'Advanced Data Structures & Quantum Algorithms',
            'issuer': 'Coursera (CU Boulder)',
            'year': 'June 2025',
            'details': (
                'Explored RSA cryptosystem foundations, basics of quantum computation, quantum algorithms vs classical approaches, '
                'advanced data structures, and practical applications using Python.'
            ),
            'link': 'https://coursera.org/share/f2cc9a0c150899190233adc4a16b6167'
        },
        {
            'name': 'AWS Cloud Practitioner',
            'issuer': 'Amazon Web Services',
            'year': 'October 2024',
            'details': 'Enhanced understanding of AWS Cloud concepts, services, security, and architecture. Gained foundational knowledge to navigate and leverage AWS for business applications.',
            'link': ''
        },
        {
            'name': 'Python for Data Science',
            'issuer': 'IBM via Coursera',
            'year': 'July 2024',
            'details': (
                'Certified in Python programming for Data Science and Development. Skills include Python logic, libraries (Pandas, NumPy, Jupyter), '
                'data structures, web scraping, API access, and data analysis.'
            ),
            'link': 'https://www.coursera.org/account/accomplishments/verify/AZ28U5FMYFY9?utm_product=course'
        }
    ]

    # Testimonials
    testimonials = [
        {
            'text': 'Wajahat built a reliable scraping pipeline that replaced a manual, error-prone process. Results improved quickly and the system is now automated end-to-end with 99.9% uptime.',
            'author': 'Sarah Chen',
            'role': 'Product Lead',
            'company': 'Freelance Client'
        },
        {
            'text': 'Delivered a complex dataset cleaning tool under tight deadlines. Highly professional, reliable, and excellent at communicating progress throughout the project.',
            'author': 'Michael Rodriguez',
            'role': 'Data Engineer',
            'company': 'Freelance Project'
        },
        {
            'text': 'Great communicator and fast iterater — produced clear documentation and automated tests that significantly improved our development workflow.',
            'author': 'David Kim',
            'role': 'Engineering Manager',
            'company': 'Freelance Collaboration'
        }
    ]

    # Stats
    stats = [
        {'number': '8+', 'label': 'Open Source Projects', 'description': 'Public repositories with detailed documentation'},
        {'number': '3M+', 'label': 'Records Processed', 'description': 'Geospatial and tabular data'},
        {'number': '99.9%', 'label': 'System Uptime', 'description': 'Production pipeline reliability'},
        {'number': '5', 'label': 'Production Services', 'description': 'Active pipelines & APIs'}
    ]

    # Get current year
    current_year = datetime.now().year

    return render_template('index.html',
                        profile=profile,  # Add this
                         projects=projects,
                         services=services,
                         timeline=timeline,
                         skills=skills,
                         technologies=technologies,
                         certifications=certifications,
                         testimonials=testimonials,
                         stats=stats,
                         current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)
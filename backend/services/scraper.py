# Web scraping script used to extract all arXiv categories from arxitics.com/help

from pprint import pprint
from bs4 import BeautifulSoup
import requests


def fetch_arxiv_categories():
    urls = [
        "http://arxitics.com/help/categories",
        "http://arxitics.com/help/categories?group=math",
        "http://arxitics.com/help/categories?group=cs",
        "http://arxitics.com/help/categories?group=q-bio",
        "http://arxitics.com/help/categories?group=q-fin",
        "http://arxitics.com/help/categories?group=stats",
    ]

    grouped_categories = []

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # This will find anchor tags whose href matches the URL
        anchor_tags = soup.find_all("a")

        parent_category = None
        url = url.replace("http://arxitics.com", "")

        for anchor_tag in anchor_tags:
            print(url)
            if anchor_tag["href"] == url:
                parent_category = anchor_tag.text
                print(parent_category)
                break

        category_group: dict[str, str | list] = {"category": parent_category, "categories": []}  # type: ignore

        for category in soup.find_all("li"):
            name, code = None, None
            if category.find("strong"):
                code = category.find("strong").text
            if category.find("span"):
                name = category.find("span").text

            if name and code:
                category_group["categories"].append({"code": code, "name": name})  # type: ignore

        grouped_categories.append(category_group)

    pprint(grouped_categories)


# Invoke the function
fetch_arxiv_categories()


categories: list[dict[str, str | list]] = [
    {
        "categories": [
            {"code": "astro-ph.GA", "name": ": Astrophysics of Galaxies"},
            {"code": "astro-ph.CO", "name": ": Cosmology and Nongalactic Astrophysics"},
            {"code": "astro-ph.EP", "name": ": Earth and Planetary Astrophysics"},
            {"code": "astro-ph.HE", "name": ": High Energy Astrophysical Phenomena"},
            {
                "code": "astro-ph.IM",
                "name": ": Instrumentation and Methods for Astrophysics",
            },
            {"code": "astro-ph.SR", "name": ": Solar and Stellar Astrophysics"},
            {
                "code": "cond-mat.dis-nn",
                "name": ": Disordered Systems and Neural Networks",
            },
            {"code": "cond-mat.mtrl-sci", "name": ": Materials Science"},
            {"code": "cond-mat.mes-hall", "name": ": Mesoscale and Nanoscale Physics"},
            {"code": "cond-mat.other", "name": ": Other Condensed Matter"},
            {"code": "cond-mat.quant-gas", "name": ": Quantum Gases"},
            {"code": "cond-mat.soft", "name": ": Soft Condensed Matter"},
            {"code": "cond-mat.stat-mech", "name": ": Statistical Mechanics"},
            {"code": "cond-mat.str-el", "name": ": Strongly Correlated Electrons"},
            {"code": "cond-mat.supr-con", "name": ": Superconductivity"},
            {"code": "gr-qc", "name": ": General Relativity and Quantum Cosmology"},
            {"code": "hep-ex", "name": ": High Energy Physics - Experiment"},
            {"code": "hep-lat", "name": ": High Energy Physics - Lattice"},
            {"code": "hep-ph", "name": ": High Energy Physics - Phenomenology"},
            {"code": "hep-th", "name": ": High Energy Physics - Theory"},
            {"code": "math-ph", "name": ": Mathematical Physics"},
            {"code": "nlin.AO", "name": ": Adaptation and Self-Organizing Systems"},
            {"code": "nlin.CG", "name": ": Cellular Automata and Lattice Gases"},
            {"code": "nlin.CD", "name": ": Chaotic Dynamics"},
            {"code": "nlin.SI", "name": ": Exactly Solvable and Integrable Systems"},
            {"code": "nlin.PS", "name": ": Pattern Formation and Solitons"},
            {"code": "nucl-ex", "name": ": Nuclear Experiment"},
            {"code": "nucl-th", "name": ": Nuclear Theory"},
            {"code": "physics.acc-ph", "name": ": Accelerator Physics"},
            {"code": "physics.app-ph", "name": ": Applied Physics"},
            {"code": "physics.ao-ph", "name": ": Atmospheric and Oceanic Physics"},
            {"code": "physics.atom-ph", "name": ": Atomic Physics"},
            {"code": "physics.atm-clus", "name": ": Atomic and Molecular Clusters"},
            {"code": "physics.bio-ph", "name": ": Biological Physics"},
            {"code": "physics.chem-ph", "name": ": Chemical Physics"},
            {"code": "physics.class-ph", "name": ": Classical Physics"},
            {"code": "physics.comp-ph", "name": ": Computational Physics"},
            {
                "code": "physics.data-an",
                "name": ": Data Analysis, Statistics and Probability",
            },
            {"code": "physics.flu-dyn", "name": ": Fluid Dynamics"},
            {"code": "physics.gen-ph", "name": ": General Physics"},
            {"code": "physics.geo-ph", "name": ": Geophysics"},
            {"code": "physics.hist-ph", "name": ": History and Philosophy of Physics"},
            {"code": "physics.ins-det", "name": ": Instrumentation and Detectors"},
            {"code": "physics.med-ph", "name": ": Medical Physics"},
            {"code": "physics.optics", "name": ": Optics"},
            {"code": "physics.ed-ph", "name": ": Physics Education"},
            {"code": "physics.soc-ph", "name": ": Physics and Society"},
            {"code": "physics.plasm-ph", "name": ": Plasma Physics"},
            {"code": "physics.pop-ph", "name": ": Popular Physics"},
            {"code": "physics.space-ph", "name": ": Space Physics"},
            {"code": "quant-ph", "name": ": Quantum Physics"},
        ],
        "category": "Physics",
    },
    {
        "categories": [
            {"code": "math.AG", "name": ": Algebraic Geometry"},
            {"code": "math.AT", "name": ": Algebraic Topology"},
            {"code": "math.AP", "name": ": Analysis of PDEs"},
            {"code": "math.CT", "name": ": Category Theory"},
            {"code": "math.CA", "name": ": Classical Analysis and ODEs"},
            {"code": "math.CO", "name": ": Combinatorics"},
            {"code": "math.AC", "name": ": Commutative Algebra"},
            {"code": "math.CV", "name": ": Complex Variables"},
            {"code": "math.DG", "name": ": Differential Geometry"},
            {"code": "math.DS", "name": ": Dynamical Systems"},
            {"code": "math.FA", "name": ": Functional Analysis"},
            {"code": "math.GM", "name": ": General Mathematics"},
            {"code": "math.GN", "name": ": General Topology"},
            {"code": "math.GT", "name": ": Geometric Topology"},
            {"code": "math.GR", "name": ": Group Theory"},
            {"code": "math.HO", "name": ": History and Overview"},
            {"code": "math.IT", "name": ": Information Theory"},
            {"code": "math.KT", "name": ": K-Theory and Homology"},
            {"code": "math.LO", "name": ": Logic"},
            {"code": "math.MP", "name": ": Mathematical Physics"},
            {"code": "math.MG", "name": ": Metric Geometry"},
            {"code": "math.NT", "name": ": Number Theory"},
            {"code": "math.NA", "name": ": Numerical Analysis"},
            {"code": "math.OA", "name": ": Operator Algebras"},
            {"code": "math.OC", "name": ": Optimization and Control"},
            {"code": "math.PR", "name": ": Probability"},
            {"code": "math.QA", "name": ": Quantum Algebra"},
            {"code": "math.RT", "name": ": Representation Theory"},
            {"code": "math.RA", "name": ": Rings and Algebras"},
            {"code": "math.SP", "name": ": Spectral Theory"},
            {"code": "math.ST", "name": ": Statistics Theory"},
            {"code": "math.SG", "name": ": Symplectic Geometry"},
        ],
        "category": "Mathematics",
    },
    {
        "categories": [
            {"code": "cs.AI", "name": ": Artificial Intelligence"},
            {"code": "cs.CL", "name": ": Computation and Language"},
            {"code": "cs.CC", "name": ": Computational Complexity"},
            {
                "code": "cs.CE",
                "name": ": Computational Engineering, Finance, and Science",
            },
            {"code": "cs.CG", "name": ": Computational Geometry"},
            {"code": "cs.GT", "name": ": Computer Science and Game Theory"},
            {"code": "cs.CV", "name": ": Computer Vision and Pattern Recognition"},
            {"code": "cs.CY", "name": ": Computers and Society"},
            {"code": "cs.CR", "name": ": Cryptography and Security"},
            {"code": "cs.DS", "name": ": Data Structures and Algorithms"},
            {"code": "cs.DB", "name": ": Databases"},
            {"code": "cs.DL", "name": ": Digital Libraries"},
            {"code": "cs.DM", "name": ": Discrete Mathematics"},
            {"code": "cs.DC", "name": ": Distributed, Parallel, and Cluster Computing"},
            {"code": "cs.ET", "name": ": Emerging Technologies"},
            {"code": "cs.FL", "name": ": Formal Languages and Automata Theory"},
            {"code": "cs.GL", "name": ": General Literature"},
            {"code": "cs.GR", "name": ": Graphics"},
            {"code": "cs.AR", "name": ": Hardware Architecture"},
            {"code": "cs.HC", "name": ": Human-Computer Interaction"},
            {"code": "cs.IR", "name": ": Information Retrieval"},
            {"code": "cs.IT", "name": ": Information Theory"},
            {"code": "cs.LG", "name": ": Learning"},
            {"code": "cs.LO", "name": ": Logic in Computer Science"},
            {"code": "cs.MS", "name": ": Mathematical Software"},
            {"code": "cs.MA", "name": ": Multiagent Systems"},
            {"code": "cs.MM", "name": ": Multimedia"},
            {"code": "cs.NI", "name": ": Networking and Internet Architecture"},
            {"code": "cs.NE", "name": ": Neural and Evolutionary Computing"},
            {"code": "cs.NA", "name": ": Numerical Analysis"},
            {"code": "cs.OS", "name": ": Operating Systems"},
            {"code": "cs.OH", "name": ": Other Computer Science"},
            {"code": "cs.PF", "name": ": Performance"},
            {"code": "cs.PL", "name": ": Programming Languages"},
            {"code": "cs.RO", "name": ": Robotics"},
            {"code": "cs.SI", "name": ": Social and Information Networks"},
            {"code": "cs.SE", "name": ": Software Engineering"},
            {"code": "cs.SD", "name": ": Sound"},
            {"code": "cs.SC", "name": ": Symbolic Computation"},
            {"code": "cs.SY", "name": ": Systems and Control"},
        ],
        "category": "Computer Science",
    },
    {
        "categories": [
            {"code": "q-bio.BM", "name": ": Biomolecules"},
            {"code": "q-bio.GN", "name": ": Genomics"},
            {"code": "q-bio.MN", "name": ": Molecular Networks"},
            {"code": "q-bio.SC", "name": ": Subcellular Processes"},
            {"code": "q-bio.CB", "name": ": Cell Behavior"},
            {"code": "q-bio.NC", "name": ": Neurons and Cognition"},
            {"code": "q-bio.TO", "name": ": Tissues and Organs"},
            {"code": "q-bio.PE", "name": ": Populations and Evolution"},
            {"code": "q-bio.QM", "name": ": Quantitative Methods"},
            {"code": "q-bio.OT", "name": ": Other"},
        ],
        "category": "Quantitative Biology",
    },
    {
        "categories": [
            {"code": "q-fin.PR", "name": ": Pricing of Securities"},
            {"code": "q-fin.RM", "name": ": Risk Management"},
            {"code": "q-fin.PM", "name": ": Portfolio Management"},
            {"code": "q-fin.TR", "name": ": Trading and Microstructure"},
            {"code": "q-fin.MF", "name": ": Mathematical Finance"},
            {"code": "q-fin.CP", "name": ": Computational Finance"},
            {"code": "q-fin.ST", "name": ": Statistical Finance"},
            {"code": "q-fin.GN", "name": ": General Finance"},
            {"code": "q-fin.EC", "name": ": Economics"},
        ],
        "category": "Quantitative Finance",
    },
    {
        "categories": [
            {"code": "stat.AP", "name": ": Applications"},
            {"code": "stat.CO", "name": ": Computation"},
            {"code": "stat.ML", "name": ": Machine Learning"},
            {"code": "stat.ME", "name": ": Methodology"},
            {"code": "stat.OT", "name": ": Other Statistics"},
            {"code": "stat.TH", "name": ": Theory"},
        ],
        "category": "Statistics",
    },
]

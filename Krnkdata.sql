-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: krnksite
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `papers`
--

DROP TABLE IF EXISTS `papers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `papers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pdf_url` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `authors` text,
  `topic_id` int NOT NULL,
  `summary` text,
  `publication_date` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `topic_id` (`topic_id`),
  KEY `ix_papers_id` (`id`),
  KEY `ix_papers_title` (`title`),
  KEY `ix_papers_pdf_url` (`pdf_url`),
  CONSTRAINT `papers_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `topics` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `papers`
--

LOCK TABLES `papers` WRITE;
/*!40000 ALTER TABLE `papers` DISABLE KEYS */;
INSERT INTO `papers` VALUES (20,'https://arxiv.org/abs/2309.08478','Current and future directions in network biology','Zitnik et al',1,'Network biology, an interdisciplinary field at the intersection of computational and biological sciences, is critical for deepening understanding of cellular functioning and disease. While the field has existed for about two decades now, it is still relatively young. There have been rapid changes to it and new computational challenges have arisen. This is caused by many factors, including increasing data complexity, such as multiple types of data becoming available at different levels of biological organization, as well as growing data size. This means that the research directions in the field need to evolve as well. Hence, a workshop on Future Directions in Network Biology was organized and held at the University of Notre Dame in 2022, which brought together active researchers in various computational and in particular algorithmic aspects of network biology to identify pressing challenges in this field. Topics that were discussed during the workshop include: inference and comparison of biological networks, multimodal data integration and heterogeneous networks, higher-order network analysis, machine learning on networks, and network-based personalized medicine. Video recordings of the workshop presentations are publicly available on YouTube. For even broader impact of the workshop, this paper, co-authored mostly by the workshop participants, summarizes the discussion from the workshop. As such, it is expected to help shape short- and long-term vision for future computational and algorithmic research in network biology.','2023-09-18','2023-09-18 08:28:21','2023-09-18 08:28:21'),(21,'https://arxiv.org/abs/2309.08500','Deep-learning-powered data analysis in plankton ecology','Bachimanchi et al',1,'The implementation of deep learning algorithms has brought new perspectives to plankton ecology. Emerging as an alternative approach to established methods, deep learning offers objective schemes to investigate plankton organisms in diverse environments. We provide an overview of deep-learning-based methods including detection and classification of phyto- and zooplankton images, foraging and swimming behaviour analysis, and finally ecological modelling. Deep learning has the potential to speed up the analysis and reduce the human experimental bias, thus enabling data acquisition at relevant temporal and spatial scales with improved reproducibility. We also discuss shortcomings and show how deep learning architectures have evolved to mitigate imprecise readouts. Finally, we suggest opportunities where deep learning is particularly likely to catalyze plankton research. The examples are accompanied by detailed tutorials and code samples that allow readers to apply the methods described in this review to their own data.','2023-09-18','2023-09-18 08:28:21','2023-09-18 08:28:21'),(22,'https://arxiv.org/list/cs/recent','Closing the Loop on Runtime Monitors with Fallback-Safe MPC','Rohan Sinha, Edward Schmerling, Marco Pavone',2,'When we rely on deep-learned models for robotic perception, we must recognize that these models may behave unreliably on inputs dissimilar from the training data, compromising the closed-loop system\'s safety. This raises fundamental questions on how we can assess confidence in perception systems and to what extent we can take safety-preserving actions when external environmental changes degrade our perception model\'s performance. Therefore, we present a framework to certify the safety of a perception-enabled system deployed in novel contexts. To do so, we leverage robust model predictive control (MPC) to control the system using the perception estimates while maintaining the feasibility of a safety-preserving fallback plan that does not rely on the perception system. In addition, we calibrate a runtime monitor using recently proposed conformal prediction techniques to certifiably detect when the perception system degrades beyond the tolerance of the MPC controller, resulting in an end-to-end safety assurance. We show that this control framework and calibration technique allows us to certify the system\'s safety with orders of magnitudes fewer samples than required to retrain the perception network when we deploy in a novel context on a photo-realistic aircraft taxiing simulator. Furthermore, we illustrate the safety-preserving behavior of the MPC on simulated examples of a quadrotor. We open-source our simulation platform and provide videos of our results at our project page: \\url{this https URL}.','2023-09-18','2023-09-18 08:28:21','2023-09-18 08:28:21'),(23,'https://arxiv.org/abs/2309.08594','\"Merge Conflicts!\" Exploring the Impacts of External Distractors to Parametric Knowledge Graphs','Cheng Qian, Xinran Zhao, Sherry Tongshuang Wu',2,'Large language models (LLMs) acquire extensive knowledge during pre-training, known as their parametric knowledge. However, in order to remain up-to-date and align with human instructions, LLMs inevitably require external knowledge during their interactions with users. This raises a crucial question: How will LLMs respond when external knowledge interferes with their parametric knowledge? To investigate this question, we propose a framework that systematically elicits LLM parametric knowledge and introduces external knowledge. Specifically, we uncover the impacts by constructing a parametric knowledge graph to reveal the different knowledge structures of LLMs, and introduce external knowledge through distractors of varying degrees, methods, positions, and formats. Our experiments on both black-box and open-source models demonstrate that LLMs tend to produce responses that deviate from their parametric knowledge, particularly when they encounter direct conflicts or confounding changes of information within detailed contexts. We also find that while LLMs are sensitive to the veracity of external knowledge, they can still be distracted by unrelated information. These findings highlight the risk of hallucination when integrating external knowledge, even indirectly, during interactions with current LLMs. All the data and results are publicly available.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(24,'https://ijbnpa.biomedcentral.com/articles/10.1186/s12966-016-0446-y','Learning cooking skills at different ages: a cross-sectional study','Lavelle et al',3,'Cooking skills are increasingly included in strategies to prevent and reduce chronic diet-related diseases and obesity. While cooking interventions target all age groups (Child, Teen and Adult), the optimal age for learning these skills on: 1) skills retention, 2) cooking practices, 3) cooking attitudes, 4) diet quality and 5) health is unknown. Similarly, although the source of learning cooking skills has been previously studied, the differences in learning from these different sources has not been considered. This research investigated the associations of the age and source of learning with the aforementioned five factors.','2016-11-14','2023-09-18 08:28:21','2023-09-18 08:28:21'),(25,'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4063875/','Impact of cooking and home food preparation interventions among adults: outcomes and implications for future programs','Reicks, Trofholz, Stang, Laska',3,'Cooking programs are growing in popularity; however an extensive review has not examined overall impact. Therefore, this study reviewed previous research on cooking/home food preparation interventions and diet and health-related outcomes among adults and identified implications for practice and research.','2014-08-01','2023-09-18 08:28:21','2023-09-18 08:28:21'),(26,'https://arxiv.org/abs/2309.08431','Decentralised Finance and Automated Market Making: Predictable Loss and Optimal Liquidity Provision','Álvaro Cartea, Fayçal Drissi, Marcello Monga',4,'Constant product markets with concentrated liquidity (CL) are the most popular type of automated market makers. In this paper, we characterise the continuous-time wealth dynamics of strategic LPs who dynamically adjust their range of liquidity provision in CL pools. Their wealth results from fee income and the value of their holdings in the pool. Next, we derive a self-financing and closed-form optimal liquidity provision strategy where the width of the LP\'s liquidity range is determined by the profitability of the pool (provision fees minus gas fees), the predictable losses (PL) of the LP\'s position, and concentration risk. Concentration risk refers to the decrease in fee revenue if the marginal exchange rate (akin to the midprice in a limit order book) in the pool exits the LP\'s range of liquidity. When the marginal rate is driven by a stochastic drift, we show how to optimally skew the range of liquidity to increase fee revenue and profit from the expected changes in the marginal rate. Finally, we use Uniswap v3 data to show that, on average, LPs have traded at a significant loss, and to show that the out-of-sample performance of our strategy is superior to the historical performance of LPs in the pool we consider.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(27,'https://arxiv.org/abs/2309.07371','The Fiscal Cost of Public Debt and Government Spending Shocks','Venance Riblier',4,'This paper investigates how the cost of public debt shapes fiscal policy and its effect on the economy. Using U.S. historical data, I show that when servicing the debt creates a fiscal burden, the government responds to spending shocks by limiting debt issuance. As a result, the initial shock triggers only a limited increase in public spending in the short run, and even leads to spending reversal in the long run. Under these conditions, fiscal policy loses its ability to stimulate economic activity. This outcome arises as the fiscal authority limits its own ability to borrow to ensure public debt sustainability. These findings are robust to several identification and estimation strategies.','2023-09-14','2023-09-18 08:28:21','2023-09-18 08:28:21'),(28,'https://journals.sagepub.com/doi/10.1177/20531680231183512','The PARTYPRESS Database: A new comparative database of parties’ press releases','Erfort, Stoetzer, Kluver',5,'We present the PARTYPRESS Database, which compiles more than 250,000 published press releases from 68 parties in 9 European countries. The database covers the press releases of the most relevant political parties in these countries from 2010 onward. It provides a supervised machine learning classification of press releases into 21 unique issue categories according to a general codebook. The PARTYPRESS Database can be used to study parties’ issue agendas comparatively and over time. We extend a recent analysis in Gessler and Hunger (2022) to illustrate the usefulness of the database in studying dynamic party competition, communication, and behavior.','2023-08-30','2023-09-18 08:28:21','2023-09-18 08:28:21'),(29,'https://journals.sagepub.com/doi/10.1177/20531680231191833','From masks to mismanagement: A global assessment of the rise and fall of pandemic-related protests','Sebastian Hellmeier ',5,'The Covid-19 pandemic changed contentious politics worldwide. After causing a short-lived decline in global protest activities in early 2020, it has led to the emergence of a variety of pandemic-related protests. While previous work has mostly looked at how event frequencies have changed over time, this paper focuses on changes in protest issues. It applies quantitative text analysis to protest event descriptions and makes the following contributions. First, it traces the rise and fall of pandemic-related protests globally between 2020 and mid-2022, showing that, on average, more than 15% of protest events were pandemic-related. Second, it identifies the most dominant pandemic-related protest issues—masks and vaccination, the economy, business restrictions, health care, education, mismanagement, and crime—and their salience over time. Third, the paper explores potential explanations for differences in the prevalence of pandemic-related protest issues between countries. Multivariate regression analyses suggest a global divide. Protests in developed countries and liberal democracies were more likely about government restrictions. In contrast, citizens in less developed countries took to the streets to demand better healthcare provision.','2023-08-25','2023-09-18 08:28:21','2023-09-18 08:28:21'),(30,'https://arxiv.org/abs/2309.08378','Analysis of the 16C(d,p)17C reaction from microscopic 17C wave functions','Analysis of the 16C(d,p)17C reaction from microscopic 17C wave functions',6,'We present a semi-microscopic study of the 16C(d,p)17C transfer reaction. The 17C overlap integrals and spectroscopic factors are obtained from a microscopic cluster model, involving many 16C+n configurations. This microscopic model provides a fair description of the 17C bound-state energies. The 16C+d scattering wave functions are defined in the CDCC method, where the deuteron breakup is simulated by pseudostates. The transfer cross sections are in good agreement with recent data. We confirm the 16C(2+)+n structure of the ground state, and show that deuteron breakup effects have a significant influence on the cross sections. We study the 17C(p,d)16C reverse reaction and suggest that the cross section to the 2+ state should be large. A measurement of the ground-state cross section would provide a strong test of the microscopic wave functions.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(31,'https://arxiv.org/abs/2309.08530','From Hubble to Bubble','Kierkla et all',6,'The detection of a stochastic Gravitational Wave (GW) background sourced by a cosmological phase transition would allow us to see the early Universe from a completely new perspective, illuminating aspects of Beyond the Standard Model (BSM) physics and inflationary cosmology. In this study, we investigate whether the evolution of the scalar potential of a minimal SM extension after inflation can lead to a strong first-order phase transition. In particular, we focus on a BSM spectator scalar field that is non-minimally coupled to gravity and has a dynamical double-well potential. As inflation ends, the potential barrier diminishes due to the evolution of the curvature scalar. Therefore, a phase transition can proceed through the nucleation of true-vacuum bubbles that collide as they fill the Universe and produce GWs. We consider high and low scales of inflation, while also taking into account a kination period between inflation and the onset of radiation domination. With this prescription, we showcase a proof-of-concept study of a new triggering mechanism for BSM phase transitions in the early Universe, whose GW signatures could potentially be probed with future detectors.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(32,'https://arxiv.org/abs/2309.08502','Irreducibility via location of zeros','Jitender Singh, Sanjeev Kumar',7,'In this paper, we obtain several new classes of irreducible polynomials having integer coefficients whose zeros lie inside an open disk around the origin or outside a closed annular region in the complex plane. Such irreducible polynomials are devised by imposing Perron--type sufficiency conditions on their coefficients.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(33,'https://arxiv.org/abs/2309.08293','A theoretical approach to the complex chemical evolution of phosphorus in the interstellar medium','Marina Fernaández-Ruz, Izaskun Jimeénez-Serra, Jacobo Aguirre',7,'The study of phosphorus chemistry in the interstellar medium has become a topic of growing interest in astrobiology, because it is plausible that a wide range of P-bearing molecules were introduced in the early Earth by the impact of asteroids and comets on its surface, enriching prebiotic chemistry. Thanks to extensive searches in recent years, it has become clear that P mainly appears in the form of PO and PN in molecular clouds and star-forming regions. Interestingly, PO is systematically more abundant than PN by factors typically of  ~1.4 - 3, independently of the physical properties of the observed source. In order to unveil the formation routes of PO and PN, in this work we introduce a mathematical model for the time evolution of the chemistry of P in an interstellar molecular cloud and analyze its associated chemical network as a complex dynamical system. By making reasonable assumptions, we reduce the network to obtain explicit mathematical expressions that describe the abundance evolution of P-bearing species and study the dependences of the abundance of PO and PN on the system\'s kinetic parameters with much faster computation times than available numerical methods. As a result, our model reveals that the formation of PO and PN is governed by just a few critical reactions, and fully explains the relationship between PO and PN abundances throughout the evolution of molecular clouds. Finally, the application of Bayesian methods constrains the real values of the most influential reaction rate coefficients making use of available observational data.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(34,'https://avmajournals.avma.org/view/journals/ajvr/84/2/ajvr.22.08.0146.xml','Concentrations of dexmedetomidine and effect on biomarkers of cartilage toxicity following intra-articular administration in horses','Knych',8,'he goal of this study was to determine plasma, urine, and synovial fluid concentrations and describe the effects on biomarkers of cartilage toxicity following intra-articular dexmedetomidine administration to horses.','2022-08-19','2023-09-18 08:28:21','2023-09-18 08:28:21'),(35,'http://www.rhinoresourcecenter.com/index.php?s=1&act=refs&CODE=ref_detail&id=1611600012','The pulmonary and metabolic effects of suspension by the feet compared with lateral recumbency in immobilized black rhinoceroses (Diceros bicornis) captured by aerial darting','Radcliffe, et al',8,'Aerial translocation of captured black rhinoceroses (Diceros bicornis) has been accomplished by suspending them by their feet. We expected this posture would compromise respiratory gas exchange more than would lateral recumbency. Because white rhinoceroses (Ceratotherium simum) immobilized with etorphine alone are hypermetabolic, with a high rate of carbon dioxide production (VCO2), we expected immobilized black rhinoceroses would also have a high VCO2. Twelve (nine male, three female; median age 8 yr old [range: 4-25]; median weight 1,137 kg [range: 804-1,234] body weight) wild black rhinoceroses were immobilized by aerial darting with etorphine and azaperone. The animals were in lateral recumbency or suspended by their feet from a crane for approximately 10 min before data were collected. Each rhinoceros received both treatments sequentially, in random order. Six were in lateral recumbency first and six were suspended first. All animals were substantially hypoxemic and hypercapnic in both postures. When suspended by the feet, mean arterial oxygen pressure (PaO2) was 42 mm Hg, 4 mm Hg greater than in lateral recumbency (P=0.030), and arterial carbon dioxide pressure (PaCO2) was 52 mm Hg, 3 mm Hg less than in lateral recumbency (P=0.016). Tidal volume and minute ventilation were similar between postures. The mean VCO2 was 2 mL/kg/min in both postures and was similar to, or marginally greater than, VCO2 predicted allometrically. Suspension by the feet for 10 min did not impair pulmonary function more than did lateral recumbency and apparently augmented gas exchange to a small degree relative to lateral recumbency. The biological importance in these animals of numerically small increments in PaO2 and decrements in PaCO2 with suspension by the feet is unknown. Black rhinoceroses immobilized with etorphine and azaperone were not as hypermetabolic as were white rhinoceroses immobilized with etorphine.','2019-08-20','2023-09-18 08:28:21','2023-09-18 08:28:21'),(36,'https://arxiv.org/abs/2309.07664','Computer says \'no\': Exploring systemic hiring bias in ChatGPT using an audit approach','Louis Lippens',9,'Large language models offer significant potential for optimising professional activities, such as streamlining personnel selection procedures. However, concerns exist about these models perpetuating systemic biases embedded into their pre-training data. This study explores whether ChatGPT, a chatbot producing human-like responses to language tasks, displays ethnic or gender bias in job applicant screening. Using a correspondence audit approach, I simulated a CV screening task in which I instructed the chatbot to rate fictitious applicant profiles only differing in names, signalling ethnic and gender identity. Comparing ratings of Arab, Asian, Black American, Central African, Dutch, Eastern European, Hispanic, Turkish, and White American male and female applicants, I show that ethnic and gender identity influence ChatGPT\'s evaluations. The ethnic bias appears to arise partly from the prompts\' language and partly from ethnic identity cues in applicants\' names. Although ChatGPT produces no overall gender bias, I find some evidence for a gender-ethnicity interaction effect. These findings underscore the importance of addressing systemic bias in language model-driven applications to ensure equitable treatment across demographic groups. Practitioners aspiring to adopt these tools should practice caution, given the adverse impact they can produce, especially when using them for selection decisions involving humans.','2023-09-14','2023-09-18 08:28:21','2023-09-18 08:28:21'),(37,'https://arxiv.org/abs/2309.06885','The Price of Empire: Unrest Location and Sovereign Risk in Tsarist Russia','Christopher A. Hartwell, Paul M. Vaaler',9,'Research on politically motivated unrest and sovereign risk overlooks whether and how unrest location matters for sovereign risk in geographically extensive states. Intuitively, political violence in the capital or nearby would seem to directly threaten the state\'s ability to pay its debts. However, it is possible that the effect on a government could be more pronounced the farther away the violence is, connected to the longer-term costs of suppressing rebellion. We use Tsarist Russia to assess these differences in risk effects when unrest occurs in Russian homeland territories versus more remote imperial territories. Our analysis of unrest events across the Russian imperium from 1820 to 1914 suggests that unrest increases risk more in imperial territories. Echoing current events, we find that unrest in Ukraine increases risk most. The price of empire included higher costs in projecting force to repress unrest and retain the confidence of the foreign investors financing those costs.','2023-09-13','2023-09-18 08:28:21','2023-09-18 08:28:21'),(38,'https://arxiv.org/abs/2309.08599','An assessment of racial disparities in pretrial decision-making using misclassification models','Kimberly A. Hochstedler Webb, Sarah A. Riley, Martin T. Wells',10,'Pretrial risk assessment tools are used in jurisdictions across the country to assess the likelihood of \"pretrial failure,\" the event where defendants either fail to appear for court or reoffend. Judicial officers, in turn, use these assessments to determine whether to release or detain defendants during trial. While algorithmic risk assessment tools were designed to predict pretrial failure with greater accuracy relative to judges, there is still concern that both risk assessment recommendations and pretrial decisions are biased against minority groups. In this paper, we develop methods to investigate the association between risk factors and pretrial failure, while simultaneously estimating misclassification rates of pretrial risk assessments and of judicial decisions as a function of defendant race. This approach adds to a growing literature that makes use of outcome misclassification methods to answer questions about fairness in pretrial decision-making. We give a detailed simulation study for our proposed methodology and apply these methods to data from the Virginia Department of Criminal Justice Services. We estimate that the VPRAI algorithm has near-perfect specificity, but its sensitivity differs by defendant race. Judicial decisions also display evidence of bias; we estimate wrongful detention rates of 39.7% and 51.4% among white and Black defendants, respectively.','2023-09-15','2023-09-18 08:28:21','2023-09-18 08:28:21'),(39,'https://arxiv.org/abs/2309.08044','How many Neurons do we need? A refined Analysis for Shallow Networks trained with Gradient Descent','Mike Nguyen, Nicole Mucke',10,'We analyze the generalization properties of two-layer neural networks in the neural tangent kernel (NTK) regime, trained with gradient descent (GD). For early stopped GD we derive fast rates of convergence that are known to be minimax optimal in the framework of non-parametric regression in reproducing kernel Hilbert spaces. On our way, we precisely keep track of the number of hidden neurons required for generalization and improve over existing results. We further show that the weights during training remain in a vicinity around initialization, the radius being dependent on structural assumptions such as degree of smoothness of the regression function and eigenvalue decay of the integral operator associated to the NTK.','2023-09-12','2023-09-18 08:28:21','2023-09-18 08:28:21'),(40,'https://arxiv.org/abs/2309.08294','Speech-dependent Modeling of Own Voice Transfer Characteristics for In-ear Microphones in Hearables','Mattes Ohlenbusch, Christian Rollwage, Simon Doclo',11,'Many hearables contain an in-ear microphone, which may be used to capture the own voice of its user in noisy environments. Since the in-ear microphone mostly records body-conducted speech due to ear canal occlusion, it suffers from band-limitation effects while only capturing a limited amount of external noise. To enhance the quality of the in-ear microphone signal using algorithms aiming at joint bandwidth extension, equalization, and noise reduction, it is desirable to have an accurate model of the own voice transfer characteristics between the entrance of the ear canal and the in-ear microphone. Such a model can be used, e.g., to simulate a large amount of in-ear recordings to train supervised learning-based algorithms. Since previous research on ear canal occlusion suggests that own voice transfer characteristics depend on speech content, in this contribution we propose a speech-dependent system identification model based on phoneme recognition. We assess the accuracy of simulating own voice speech by speech-dependent and speech-independent modeling and investigate how well modeling approaches are able to generalize to different talkers. Simulation results show that using the proposed speech-dependent model is preferable for simulating in-ear recordings compared to using a speech-independent model.','2023-09-15','2023-09-18 08:41:53','2023-09-18 08:41:53');
/*!40000 ALTER TABLE `papers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `summaries`
--

DROP TABLE IF EXISTS `summaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `summaries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `paper_id` int DEFAULT NULL,
  `short_summary` text,
  `long_summary` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_summaries_paper_id` (`paper_id`),
  KEY `ix_summaries_id` (`id`),
  CONSTRAINT `summaries_ibfk_1` FOREIGN KEY (`paper_id`) REFERENCES `papers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `summaries`
--

LOCK TABLES `summaries` WRITE;
/*!40000 ALTER TABLE `summaries` DISABLE KEYS */;
/*!40000 ALTER TABLE `summaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topics`
--

DROP TABLE IF EXISTS `topics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `topics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_topics_name` (`name`),
  KEY `ix_topics_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topics`
--

LOCK TABLES `topics` WRITE;
/*!40000 ALTER TABLE `topics` DISABLE KEYS */;
INSERT INTO `topics` VALUES (1,'Biology','2023-09-18 08:26:30','2023-09-18 08:26:30'),(2,'Computer Science','2023-09-18 08:26:30','2023-09-18 08:26:30'),(3,'Cooking','2023-09-18 08:26:30','2023-09-18 08:26:30'),(4,'Finance','2023-09-18 08:26:30','2023-09-18 08:26:30'),(5,'Politics','2023-09-18 08:26:30','2023-09-18 08:26:30'),(6,'Physics','2023-09-18 08:26:30','2023-09-18 08:26:30'),(7,'Math','2023-09-18 08:26:30','2023-09-18 08:26:30'),(8,'VetMed','2023-09-18 08:26:30','2023-09-18 08:26:30'),(9,'Economics','2023-09-18 08:26:30','2023-09-18 08:26:30'),(10,'Statistics','2023-09-18 08:26:30','2023-09-18 08:26:30'),(11,'Electrical Engineering','2023-09-18 08:45:39','2023-09-18 08:45:39');
/*!40000 ALTER TABLE `topics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_topics`
--

DROP TABLE IF EXISTS `user_topics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_topics` (
  `user_id` int DEFAULT NULL,
  `topic_id` int DEFAULT NULL,
  KEY `user_id` (`user_id`),
  KEY `topic_id` (`topic_id`),
  CONSTRAINT `user_topics_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `user_topics_ibfk_2` FOREIGN KEY (`topic_id`) REFERENCES `topics` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_topics`
--

LOCK TABLES `user_topics` WRITE;
/*!40000 ALTER TABLE `user_topics` DISABLE KEYS */;
INSERT INTO `user_topics` VALUES (1,8);
/*!40000 ALTER TABLE `user_topics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `is_premium_user` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_users_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'David','Kral','dockral@gmail.com','$2b$12$iiyE/OXJ32mMbsDB9EvNzumLis3uYcLh.FSpv5tDgQCfSYFbZLMrG',0,'2023-09-18 15:44:26','2023-09-18 15:44:26'),(2,'Robert','Computer','Rob@mail.com','$2b$12$DYg1R02ZfUF7cyHl8PL9be9D.u89GmGuJgNr0exGbCVEn2fZpi3Y.',0,'2023-09-18 16:26:04','2023-09-18 16:26:04'),(3,'Millie','Badlady','Millie@mail.com','$2b$12$fzbvxjcF/vDEWI.MBixo.ex24vOmvyuXvfKjYEiuAPSw0fLLq9hy2',0,'2023-09-18 17:16:15','2023-09-18 17:16:15');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-18 10:55:53

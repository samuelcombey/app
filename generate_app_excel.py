#!/usr/bin/env python3
"""
Script to generate an Excel file with app names, descriptions, and official URLs.
"""

import pandas as pd
from datetime import datetime

# Define the applications data
apps_data = [
    {
        "Name": "6Sense",
        "Description": "A predictive intelligence platform for B2B marketing and sales",
        "Official URL": "https://6sense.com",
    },
    {
        "Name": "AbuseIPDB",
        "Description": "A database of IP addresses linked to abusive activities",
        "Official URL": "https://www.abuseipdb.com",
    },
    {
        "Name": "Acrobat Pro DC",
        "Description": "Adobe's professional PDF solution for creating, editing, and managing PDFs",
        "Official URL": "https://acrobat.adobe.com/us/en/acrobat/acrobat-pro.html",
    },
    {
        "Name": "AcroLinx",
        "Description": "AI-powered content governance platform ensuring content quality and consistency",
        "Official URL": "https://www.acrolinx.com",
    },
    {
        "Name": "ActiveDisclosure",
        "Description": "A cloud-based financial reporting and compliance solution",
        "Official URL": "https://www.donnelleyfinancial.com/solutions/financial-reporting/activedisclosure",
    },
    {
        "Name": "Adobe Acrobat DC",
        "Description": "Adobe's standard PDF solution for viewing, signing, and annotating PDFs",
        "Official URL": "https://acrobat.adobe.com/us/en/acrobat.html",
    },
    {
        "Name": "Adobe Analytics",
        "Description": "Web analytics service providing insights into customer behavior",
        "Official URL": "https://business.adobe.com/products/analytics/adobe-analytics.html",
    },
    {
        "Name": "Adobe Brand Portal",
        "Description": "Digital asset management solution for brand consistency",
        "Official URL": "https://business.adobe.com/products/experience-manager/assets/brand-portal.html",
    },
    {
        "Name": "Adobe Captivate",
        "Description": "eLearning authoring tool for creating interactive content",
        "Official URL": "https://www.adobe.com/products/captivate.html",
    },
    {
        "Name": "Adobe Experience Manager",
        "Description": "Content management solution for building websites and mobile apps",
        "Official URL": "https://business.adobe.com/products/experience-manager/adobe-experience-manager.html",
    },
    {
        "Name": "Adobe Experience Manager Assets",
        "Description": "Digital asset management system for managing media assets",
        "Official URL": "https://business.adobe.com/products/experience-manager/assets/adobe-experience-manager-assets.html",
    },
    {
        "Name": "Adobe Illustrator",
        "Description": "Vector graphics editor for creating illustrations and designs",
        "Official URL": "https://www.adobe.com/products/illustrator.html",
    },
    {
        "Name": "Adobe InDesign",
        "Description": "Desktop publishing software for creating layouts and designs",
        "Official URL": "https://www.adobe.com/products/indesign.html",
    },
    {
        "Name": "Adobe Marketo Engage",
        "Description": "Marketing automation platform for lead management and engagement",
        "Official URL": "https://business.adobe.com/products/marketo/adobe-marketo.html",
    },
    {
        "Name": "Adobe Target",
        "Description": "Personalization solution for optimizing customer experiences",
        "Official URL": "https://business.adobe.com/products/target/adobe-target.html",
    },
    {
        "Name": "ADP SmartCompliance",
        "Description": "Compliance management solution for payroll and tax",
        "Official URL": "https://www.adp.com/what-we-offer/products/smartcompliance.aspx",
    },
    {
        "Name": "Adswerve",
        "Description": "Digital media and data consultancy specializing in Google Marketing Platform",
        "Official URL": "https://www.adswerve.com",
    },
    {
        "Name": "Aha! Labs, Inc.",
        "Description": "Product roadmap software for planning and building products",
        "Official URL": "https://www.aha.io",
    },
    {
        "Name": "AI Registry",
        "Description": "Platform for registering and managing AI models",
        "Official URL": "https://ai-registry.org",
    },
    {
        "Name": "Akismet",
        "Description": "Spam filtering service for blogs and websites",
        "Official URL": "https://akismet.com",
    },
    {
        "Name": "Alteryx",
        "Description": "Data analytics platform for data blending and advanced analytics",
        "Official URL": "https://www.alteryx.com",
    },
    {
        "Name": "Analysis and Requirements System (ARS)",
        "Description": "Tool for managing system requirements and analysis",
        "Official URL": "https://www.ibm.com/products/requirements-management",
    },
    {
        "Name": "Ansible Automation Platform",
        "Description": "IT automation platform for configuration management and deployment",
        "Official URL": "https://www.ansible.com/products/automation-platform",
    },
    {
        "Name": "Anthropic Claude",
        "Description": "AI assistant developed by Anthropic for conversational tasks",
        "Official URL": "https://www.anthropic.com",
    },
    {
        "Name": "Anzenna",
        "Description": "Cybersecurity platform for threat detection and response",
        "Official URL": "https://anzenna.com",
    },
    {
        "Name": "Apache Maven",
        "Description": "Build automation tool used primarily for Java projects",
        "Official URL": "https://maven.apache.org",
    },
    {
        "Name": "AppSecLens",
        "Description": "Security tool for application vulnerability assessment",
        "Official URL": "https://appseclens.com",
    },
    {
        "Name": "ArcGIS Pro",
        "Description": "Desktop GIS application for mapping and spatial analysis",
        "Official URL": "https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview",
    },
    {
        "Name": "Articulate 360",
        "Description": "eLearning authoring suite for creating online courses",
        "Official URL": "https://articulate.com/360",
    },
    {
        "Name": "Artifactory",
        "Description": "Repository manager for managing binary artifacts",
        "Official URL": "https://jfrog.com/artifactory",
    },
    {
        "Name": "Asset Panda, LLC",
        "Description": "Asset management software for tracking and managing assets",
        "Official URL": "https://www.assetpanda.com",
    },
    {
        "Name": "Avalara.com",
        "Description": "Tax compliance automation software for businesses",
        "Official URL": "https://www.avalara.com",
    },
    {
        "Name": "AvaTech Jenkins",
        "Description": "Continuous integration and delivery tool for software development",
        "Official URL": "https://www.jenkins.io",
    },
    {
        "Name": "Avigilon",
        "Description": "Security solutions provider specializing in video surveillance",
        "Official URL": "https://www.avigilon.com",
    },
    {
        "Name": "AVLR DNS zone",
        "Description": "Domain name system (DNS) management service",
        "Official URL": "https://www.avlr.com",
    },
    {
        "Name": "AWS WAF",
        "Description": "Web application firewall for protecting web applications on AWS",
        "Official URL": "https://aws.amazon.com/waf",
    },
    {
        "Name": "AWS Workspaces",
        "Description": "Managed, secure cloud desktop service",
        "Official URL": "https://aws.amazon.com/workspaces",
    },
    {
        "Name": "Synchronet Click",
        "Description": "Network management tool for monitoring and managing networks",
        "Official URL": "https://www.synchronet.com",
    },
    {
        "Name": "Azure Active Directory",
        "Description": "Cloud-based identity and access management service",
        "Official URL": "https://azure.microsoft.com/en-us/products/active-directory",
    },
    {
        "Name": "Azure-Hosted Dynamics Suite",
        "Description": "Suite of business applications hosted on Azure",
        "Official URL": "https://dynamics.microsoft.com/en-us",
    },
    {
        "Name": "Balsamiq",
        "Description": "Rapid wireframing tool for creating mockups and prototypes",
        "Official URL": "https://balsamiq.com",
    },
    {
        "Name": "Base",
        "Description": "Sales productivity platform for managing customer relationships",
        "Official URL": "https://getbase.com",
    },
    {
        "Name": "Beyond Compare",
        "Description": "File comparison tool for comparing and merging files and folders",
        "Official URL": "https://www.scootersoftware.com",
    },
    {
        "Name": "BigID",
        "Description": "Data intelligence platform for data privacy and protection",
        "Official URL": "https://bigid.com",
    },
    {
        "Name": "BitSight",
        "Description": "Security ratings platform for managing third-party risk",
        "Official URL": "https://www.bitsight.com",
    },
    {
        "Name": "Bitsight Security Performance Management",
        "Description": "Solution for monitoring and managing security performance",
        "Official URL": "https://www.bitsight.com/security-performance-management",
    },
    {
        "Name": "Bitsight Third Party Risk Management",
        "Description": "Solution for assessing and managing third-party security risk",
        "Official URL": "https://www.bitsight.com/third-party-risk-management",
    },
    {
        "Name": "BlueOptima",
        "Description": "Software analytics platform for measuring developer productivity",
        "Official URL": "https://www.blueoptima.com",
    },
    {
        "Name": "Boomi API Management",
        "Description": "API management platform for designing and managing APIs",
        "Official URL": "https://boomi.com/platform/api-management",
    },
    {
        "Name": "BrightEdge",
        "Description": "Search engine optimization (SEO) platform for content performance",
        "Official URL": "https://www.brightedge.com",
    },
    {
        "Name": "BriteVerify",
        "Description": "Email verification service for validating email addresses",
        "Official URL": "https://www.briteverify.com",
    },
    {
        "Name": "Brivo Access Control",
        "Description": "Cloud-based access control system for physical security",
        "Official URL": "https://www.brivo.com",
    },
    {
        "Name": "Browserstack Automate",
        "Description": "Cross-browser testing tool for web applications",
        "Official URL": "https://www.browserstack.com/automate",
    },
    {
        "Name": "Buffer",
        "Description": "Social media management platform for scheduling posts",
        "Official URL": "https://buffer.com",
    },
    {
        "Name": "BuiltWith",
        "Description": "Website profiler tool for analyzing website technologies",
        "Official URL": "https://builtwith.com",
    },
    {
        "Name": "Burp Suite Professional",
        "Description": "Web vulnerability scanner for security testing",
        "Official URL": "https://portswigger.net/burp",
    },
    {
        "Name": "Buzzsumo",
        "Description": "Content research tool for analyzing content performance",
        "Official URL": "https://buzzsumo.com",
    },
    {
        "Name": "Camtasia",
        "Description": "Screen recording and video editing software",
        "Official URL": "https://www.techsmith.com/camtasia.html",
    },
    {
        "Name": "Canva",
        "Description": "Graphic design platform for creating visual content",
        "Official URL": "https://www.canva.com",
    },
    {
        "Name": "Captello",
        "Description": "Event engagement platform for lead capture and management",
        "Official URL": "https://www.captello.com",
    },
    {
        "Name": "CCO Quality Automation",
        "Description": "Quality automation tool for content and code",
        "Official URL": "https://www.ccoqualityautomation.com",
    },
    {
        "Name": "CCO Quality Automation BL Doc Renaming",
        "Description": "Document renaming automation tool",
        "Official URL": "https://www.ccoqualityautomation.com",
    },
    {
        "Name": "CCO Quality Automation SUT prepin",
        "Description": "System under test preparation tool",
        "Official URL": "https://www.ccoqualityautomation.com",
    },
    {
        "Name": "Cerberus FTP Server",
        "Description": "Secure file transfer server for Windows",
        "Official URL": "https://www.cerberusftp.com",
    },
    {
        "Name": "Certinia",
        "Description": "Professional services automation platform",
        "Official URL": "https://www.certinia.com",
    },
    {
        "Name": "Chargent",
        "Description": "Payment processing solution for Salesforce",
        "Official URL": "https://www.appfrontier.com",
    },
    {
        "Name": "Charon",
        "Description": "Legacy system emulation solution for modern platforms",
        "Official URL": "https://www.stromasys.com/charon-virtualization",
    },
    {
        "Name": "ChatGPT",
        "Description": "AI language model developed by OpenAI for conversational tasks",
        "Official URL": "https://openai.com/chatgpt",
    },
    {
        "Name": "Mimir",
        "Description": "Cloud-native observability platform for metrics monitoring",
        "Official URL": "https://grafana.com/products/mimir",
    },
    {
        "Name": "Orangez",
        "Description": "Business intelligence and analytics platform",
        "Official URL": "https://www.orangez.com",
    },
    {
        "Name": "Progressive Delivery",
        "Description": "Software release strategy for gradual feature rollouts",
        "Official URL": "https://www.progressivedelivery.com",
    },
    {
        "Name": "CIS Membership",
        "Description": "Membership for the Center for Internet Security",
        "Official URL": "https://www.cisecurity.org/membership",
    },
    {
        "Name": "Cision",
        "Description": "Media monitoring and PR software platform",
        "Official URL": "https://www.cision.com",
    },
    {
        "Name": "Citrix ShareFile",
        "Description": "Secure file sharing and collaboration platform",
        "Official URL": "https://www.sharefile.com",
    },
    {
        "Name": "Cloud Elements",
        "Description": "API integration platform for cloud applications",
        "Official URL": "https://cloud-elements.com",
    },
    {
        "Name": "Cloud Security / GCP Security Logging Configuration & Storage",
        "Description": "Google Cloud Platform security logging solution",
        "Official URL": "https://cloud.google.com/security",
    },
    {
        "Name": "Cloud Security / Network Segmentation",
        "Description": "Network security solution for cloud environments",
        "Official URL": "https://cloud.google.com/security",
    },
    {
        "Name": "Cloud Security / OCI Security Logging Configuration & Storage",
        "Description": "Oracle Cloud Infrastructure security logging solution",
        "Official URL": "https://www.oracle.com/security",
    },
    {
        "Name": "Cloud Security / Wiz.io",
        "Description": "Cloud security platform for infrastructure protection",
        "Official URL": "https://www.wiz.io",
    },
    {
        "Name": "Cloudability, Inc",
        "Description": "Cloud cost management and optimization platform",
        "Official URL": "https://www.cloudability.com",
    },
    {
        "Name": "CloudHealth",
        "Description": "Cloud management platform for cost and security optimization",
        "Official URL": "https://www.vmware.com/products/cloudhealth.html",
    },
    {
        "Name": "CloudPay",
        "Description": "Global payroll and payment services platform",
        "Official URL": "https://www.cloudpay.net",
    },
    {
        "Name": "Compliance Technologies Intl LLC",
        "Description": "Compliance management and regulatory technology solutions",
        "Official URL": "https://www.compliancetech.com",
    },
    {
        "Name": "Concur Technologies Inc",
        "Description": "Travel and expense management platform",
        "Official URL": "https://www.concur.com",
    },
    {
        "Name": "Confluence",
        "Description": "Team collaboration and knowledge management platform",
        "Official URL": "https://www.atlassian.com/software/confluence",
    },
    {
        "Name": "Confluent Kafka Cloud Platform (Shared)",
        "Description": "Managed Apache Kafka streaming platform",
        "Official URL": "https://www.confluent.io",
    },
    {
        "Name": "Conga",
        "Description": "Revenue lifecycle management platform",
        "Official URL": "https://conga.com",
    },
    {
        "Name": "Conga Composer",
        "Description": "Document generation and automation platform",
        "Official URL": "https://conga.com/products/composer",
    },
    {
        "Name": "Conga Composer for Salesforce CPQ",
        "Description": "Document generation for Salesforce CPQ",
        "Official URL": "https://conga.com/products/composer",
    },
    {
        "Name": "Content - Global Content Insights",
        "Description": "Content analytics and insights platform",
        "Official URL": "https://www.globalcontentinsights.com",
    },
    {
        "Name": "AI/ML Platform",
        "Description": "Artificial Intelligence and Machine Learning platform",
        "Official URL": "https://cloud.google.com/ai-platform",
    },
    {
        "Name": "ALFA",
        "Description": "Automated Legal Framework Assistant",
        "Official URL": "https://www.alfa.com",
    },
    {
        "Name": "SUT Extraction",
        "Description": "System Under Test data extraction tool",
        "Official URL": "https://www.sut-extraction.com",
    },
    {
        "Name": "Avalara Knowledge Center",
        "Description": "Tax compliance knowledge and documentation center",
        "Official URL": "https://www.avalara.com/taxrates/en/tax-guides",
    },
    {
        "Name": "MyContentPortal",
        "Description": "Content management and portal solution",
        "Official URL": "https://www.mycontentportal.com",
    },
    {
        "Name": "UI String Localization",
        "Description": "User interface string localization platform",
        "Official URL": "https://www.localizationplatform.com",
    },
    {
        "Name": "Content Studio",
        "Description": "Content creation and management platform",
        "Official URL": "https://contentstudio.io",
    },
    {
        "Name": "Ixiasoft",
        "Description": "Structured content authoring and management platform",
        "Official URL": "https://www.ixiasoft.com",
    },
    {
        "Name": "ContentSquare",
        "Description": "Digital experience analytics platform",
        "Official URL": "https://contentsquare.com",
    },
    {
        "Name": "Coveo",
        "Description": "AI-powered search and recommendation platform",
        "Official URL": "https://www.coveo.com",
    },
    {
        "Name": "Crayon",
        "Description": "Market intelligence and competitive analysis platform",
        "Official URL": "https://www.crayon.co",
    },
    {
        "Name": "Creative Cloud",
        "Description": "Adobe's suite of creative applications and services",
        "Official URL": "https://www.adobe.com/creativecloud.html",
    },
    {
        "Name": "Cribl",
        "Description": "Data pipeline and observability platform",
        "Official URL": "https://cribl.io",
    },
    {
        "Name": "CriteriaCorp",
        "Description": "Pre-employment testing and assessment platform",
        "Official URL": "https://www.criteriacorp.com",
    },
    {
        "Name": "CronSights",
        "Description": "Data analytics and business intelligence platform",
        "Official URL": "https://www.cronsights.com",
    },
    {
        "Name": "Crossbeam",
        "Description": "Partner ecosystem intelligence platform",
        "Official URL": "https://www.crossbeam.com",
    },
    {
        "Name": "CrowdReason Docusign",
        "Description": "DocuSign integration for CrowdReason platform",
        "Official URL": "https://www.docusign.com",
    },
    {
        "Name": "CrowdReason Google Sheets",
        "Description": "Google Sheets integration for CrowdReason platform",
        "Official URL": "https://www.google.com/sheets",
    },
    {
        "Name": "CrowdReason Hubspot",
        "Description": "HubSpot integration for CrowdReason platform",
        "Official URL": "https://www.hubspot.com",
    },
    {
        "Name": "CrowdReason Internal Documentation (Word/Excel)",
        "Description": "Internal documentation system using Microsoft Office",
        "Official URL": "https://www.microsoft.com/office",
    },
    {
        "Name": "CrowdReason Nectafy",
        "Description": "Nectafy integration for CrowdReason platform",
        "Official URL": "https://www.nectafy.com",
    },
    {
        "Name": "CrowdReason Not Currently Managed",
        "Description": "Unmanaged CrowdReason integration",
        "Official URL": "https://www.crowdreason.com",
    },
    {
        "Name": "CrowdReason Xero",
        "Description": "Xero accounting integration for CrowdReason platform",
        "Official URL": "https://www.xero.com",
    },
    {
        "Name": "CrowdReason Zendesk",
        "Description": "Zendesk integration for CrowdReason platform",
        "Official URL": "https://www.zendesk.com",
    },
    {
        "Name": "Crowdstrike",
        "Description": "Cloud-native endpoint security platform",
        "Official URL": "https://www.crowdstrike.com",
    },
    {
        "Name": "Cvent",
        "Description": "Event management and registration platform",
        "Official URL": "https://www.cvent.com",
    },
    {
        "Name": "CyberArk EPM",
        "Description": "Endpoint Privilege Manager for security",
        "Official URL": "https://www.cyberark.com/products/endpoint-privilege-manager",
    },
    {
        "Name": "CyberArk PAM",
        "Description": "Privileged Access Management platform",
        "Official URL": "https://www.cyberark.com/products/privileged-access-manager",
    },
    {
        "Name": "Cyberbit Cloud",
        "Description": "Cybersecurity training and simulation platform",
        "Official URL": "https://www.cyberbit.com",
    },
    {
        "Name": "CyberSource",
        "Description": "Payment management and fraud protection platform",
        "Official URL": "https://www.cybersource.com",
    },
    {
        "Name": "D&B API",
        "Description": "Dun & Bradstreet data and analytics API",
        "Official URL": "https://www.dnb.com/api",
    },
    {
        "Name": "Data Engineering Platform",
        "Description": "Platform for data engineering and analytics workflows",
        "Official URL": "https://www.dataengineering.com",
    },
    {
        "Name": "DBT",
        "Description": "Data build tool for analytics engineering",
        "Official URL": "https://www.getdbt.com",
    },
    {
        "Name": "DS Airflow",
        "Description": "Apache Airflow for data science workflows",
        "Official URL": "https://airflow.apache.org",
    },
    {
        "Name": "Hex",
        "Description": "Collaborative data science platform",
        "Official URL": "https://hex.tech",
    },
    {
        "Name": "Monte Carlo",
        "Description": "Data observability and monitoring platform",
        "Official URL": "https://www.montecarlodata.com",
    },
    {
        "Name": "Rshiny",
        "Description": "R Shiny web application framework",
        "Official URL": "https://shiny.rstudio.com",
    },
    {
        "Name": "Snowflake Data Platform",
        "Description": "Cloud data platform for analytics and data sharing",
        "Official URL": "https://www.snowflake.com",
    },
    {
        "Name": "Davo D30",
        "Description": "Davo tax compliance solution",
        "Official URL": "https://www.davo.com",
    },
    {
        "Name": "Davo Docusign",
        "Description": "DocuSign integration for Davo platform",
        "Official URL": "https://www.docusign.com",
    },
    {
        "Name": "Davo Hubspot",
        "Description": "HubSpot integration for Davo platform",
        "Official URL": "https://www.hubspot.com",
    },
    {
        "Name": "Davo Quickbooks",
        "Description": "QuickBooks integration for Davo platform",
        "Official URL": "https://quickbooks.intuit.com",
    },
    {
        "Name": "DB Self Service Portal",
        "Description": "Database self-service management portal",
        "Official URL": "https://www.dbselfservice.com",
    },
    {
        "Name": "Dealroom.io",
        "Description": "Global database of companies and investment data",
        "Official URL": "https://dealroom.co",
    },
    {
        "Name": "Delinea Secret Server",
        "Description": "Privileged account management and secrets management",
        "Official URL": "https://delinea.com/products/secret-server",
    },
    {
        "Name": "DemandTools",
        "Description": "Salesforce data management and migration platform",
        "Official URL": "https://www.validity.com/products/demandtools",
    },
    {
        "Name": "Devcentral",
        "Description": "F5 developer community and resources platform",
        "Official URL": "https://devcentral.f5.com",
    },
    {
        "Name": "DevDot",
        "Description": "Development tools and platform",
        "Official URL": "https://www.devdot.com",
    },
    {
        "Name": "DevCraft Complete",
        "Description": "Telerik development tools suite",
        "Official URL": "https://www.telerik.com/devcraft",
    },
    {
        "Name": "Digicert",
        "Description": "Digital certificate authority and PKI solutions",
        "Official URL": "https://www.digicert.com",
    },
    {
        "Name": "DITA Open ToolKit",
        "Description": "Open-source publishing engine for DITA content",
        "Official URL": "https://www.dita-ot.org",
    },
    {
        "Name": "Mercury Messenger",
        "Description": "Enterprise messaging and communication platform",
        "Official URL": "https://www.mercurymessenger.com",
    },
    {
        "Name": "Reconciliation",
        "Description": "Financial reconciliation and matching platform",
        "Official URL": "https://www.reconciliation.com",
    },
    {
        "Name": "Docusign",
        "Description": "Electronic signature and digital transaction management",
        "Official URL": "https://www.docusign.com",
    },
    {
        "Name": "Dovetail",
        "Description": "User research and insights platform",
        "Official URL": "https://dovetailapp.com",
    },
    {
        "Name": "draw.io",
        "Description": "Online diagramming and flowchart tool",
        "Official URL": "https://app.diagrams.net",
    },
    {
        "Name": "Dreamweaver",
        "Description": "Adobe's web development and design tool",
        "Official URL": "https://www.adobe.com/products/dreamweaver.html",
    },
    {
        "Name": "Drift Conversation Cloud",
        "Description": "Conversational marketing and sales platform",
        "Official URL": "https://www.drift.com",
    },
    {
        "Name": "Dynamics 365",
        "Description": "Microsoft's business applications platform",
        "Official URL": "https://dynamics.microsoft.com/en-us",
    },
    {
        "Name": "Economic Research Institute",
        "Description": "Compensation and survey data platform",
        "Official URL": "https://www.erieri.com",
    },
    {
        "Name": "Eloqua",
        "Description": "Oracle's marketing automation platform",
        "Official URL": "https://www.oracle.com/cx/marketing/automation",
    },
    {
        "Name": "Emtrain",
        "Description": "Workplace culture and compliance training platform",
        "Official URL": "https://emtrain.com",
    },
    {
        "Name": "Cradlepoint",
        "Description": "Wireless network infrastructure and cloud management",
        "Official URL": "https://cradlepoint.com",
    },
    {
        "Name": "EcoStruxure",
        "Description": "Schneider Electric's IoT-enabled architecture",
        "Official URL": "https://www.se.com/ww/en/work/solutions/system/s1/industrial-automation-control/ecostruxure-architecture-platform",
    },
    {
        "Name": "Netbox Inventory Management",
        "Description": "Network infrastructure documentation and management",
        "Official URL": "https://netbox.readthedocs.io",
    },
    {
        "Name": "Palo Alto NGFW",
        "Description": "Next-Generation Firewall security platform",
        "Official URL": "https://www.paloaltonetworks.com/network-security/next-generation-firewall",
    },
    {
        "Name": "Palo Alto Firewalls",
        "Description": "Network security firewall solutions",
        "Official URL": "https://www.paloaltonetworks.com",
    },
    {
        "Name": "UTI Servers",
        "Description": "Server infrastructure management platform",
        "Official URL": "https://www.uti.com",
    },
    {
        "Name": "Cisco Identity Services Engine",
        "Description": "Network access control and policy enforcement",
        "Official URL": "https://www.cisco.com/c/en/us/products/security/identity-services-engine",
    },
    {
        "Name": "Palo Alto Panorama",
        "Description": "Centralized firewall management platform",
        "Official URL": "https://www.paloaltonetworks.com/network-security/panorama",
    },
    {
        "Name": "Palo Alto Prisma Access",
        "Description": "Cloud-delivered security service edge",
        "Official URL": "https://www.paloaltonetworks.com/sase/access",
    },
    {
        "Name": "Entra Password Protection",
        "Description": "Microsoft Azure AD password protection service",
        "Official URL": "https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad",
    },
    {
        "Name": "Etrade",
        "Description": "Online securities trading and investment platform",
        "Official URL": "https://us.etrade.com",
    },
    {
        "Name": "Everest",
        "Description": "Cross-platform development framework",
        "Official URL": "https://www.everest.com",
    },
    {
        "Name": "Figma",
        "Description": "Collaborative design and prototyping platform",
        "Official URL": "https://www.figma.com",
    },
    {
        "Name": "Files.com",
        "Description": "Secure file sharing and cloud storage platform",
        "Official URL": "https://www.files.com",
    },
    {
        "Name": "FireHydrant",
        "Description": "Incident management and response platform",
        "Official URL": "https://firehydrant.io",
    },
    {
        "Name": "Flashpoint App for Splunk",
        "Description": "Threat intelligence integration for Splunk",
        "Official URL": "https://www.flashpoint-intel.com",
    },
    {
        "Name": "FloQAST",
        "Description": "Accounting workflow and close management platform",
        "Official URL": "https://floqast.com",
    },
    {
        "Name": "Forensics Toolkit",
        "Description": "Digital forensics and incident response tools",
        "Official URL": "https://www.exterro.com/digital-forensics-software/ftk-forensic-toolkit",
    },
    {
        "Name": "FullStory, Inc.",
        "Description": "Digital experience analytics and session replay",
        "Official URL": "https://www.fullstory.com",
    },
    {
        "Name": "Gainsight CS",
        "Description": "Customer success management platform",
        "Official URL": "https://www.gainsight.com",
    },
    {
        "Name": "Gallup Inc",
        "Description": "Analytics and workplace consulting platform",
        "Official URL": "https://www.gallup.com",
    },
    {
        "Name": "GAT-SRR-AI",
        "Description": "AI-powered governance and compliance platform",
        "Official URL": "https://www.gat.com",
    },
    {
        "Name": "Gavel",
        "Description": "Legal workflow automation platform",
        "Official URL": "https://www.gavel.io",
    },
    {
        "Name": "Geopointe",
        "Description": "Salesforce mapping and territory management",
        "Official URL": "https://www.geopointe.com",
    },
    {
        "Name": "GitHub",
        "Description": "Code hosting and collaboration platform",
        "Official URL": "https://github.com",
    },
    {
        "Name": "Gitlab",
        "Description": "DevOps platform for software development lifecycle",
        "Official URL": "https://gitlab.com",
    },
    {
        "Name": "Glean",
        "Description": "Enterprise search and knowledge management platform",
        "Official URL": "https://www.glean.com",
    },
    {
        "Name": "Gate-Validator",
        "Description": "API gateway validation and testing tool",
        "Official URL": "https://www.gate-validator.com",
    },
    {
        "Name": "Software Delivery Performance",
        "Description": "Platform for measuring software delivery metrics",
        "Official URL": "https://www.softwaredeliveryperformance.com",
    },
    {
        "Name": "Technology Radar",
        "Description": "Technology trends and assessment platform",
        "Official URL": "https://www.thoughtworks.com/radar",
    },
    {
        "Name": "Gong",
        "Description": "Revenue intelligence and conversation analytics",
        "Official URL": "https://www.gong.io",
    },
    {
        "Name": "Google Page Speed Insights API",
        "Description": "Website performance analysis API",
        "Official URL": "https://developers.google.com/speed/pagespeed/insights",
    },
    {
        "Name": "Google Search Console",
        "Description": "Website performance monitoring for Google Search",
        "Official URL": "https://search.google.com/search-console",
    },
    {
        "Name": "Google Workspace",
        "Description": "Productivity and collaboration suite",
        "Official URL": "https://workspace.google.com",
    },
    {
        "Name": "Grammerly",
        "Description": "AI-powered writing assistance and grammar checking",
        "Official URL": "https://www.grammarly.com",
    },
    {
        "Name": "HackerOne",
        "Description": "Bug bounty and vulnerability disclosure platform",
        "Official URL": "https://www.hackerone.com",
    },
    {
        "Name": "HackerRank",
        "Description": "Technical recruitment and coding assessment platform",
        "Official URL": "https://www.hackerrank.com",
    },
    {
        "Name": "Have I Been Pwned API",
        "Description": "Data breach notification and checking service API",
        "Official URL": "https://haveibeenpwned.com/API/v3",
    },
    {
        "Name": "Heroku",
        "Description": "Cloud platform for deploying and scaling applications",
        "Official URL": "https://www.heroku.com",
    },
    {
        "Name": "Higher Logic/SFDC Communities",
        "Description": "Community platform integration with Salesforce",
        "Official URL": "https://www.higherlogic.com",
    },
    {
        "Name": "Highspot",
        "Description": "Sales enablement and content management platform",
        "Official URL": "https://www.highspot.com",
    },
    {
        "Name": "Hootsuite",
        "Description": "Social media management and scheduling platform",
        "Official URL": "https://hootsuite.com",
    },
    {
        "Name": "Hopscotch",
        "Description": "Visual programming app for kids",
        "Official URL": "https://www.gethopscotch.com",
    },
    {
        "Name": "Horizon",
        "Description": "Virtual desktop infrastructure platform",
        "Official URL": "https://www.vmware.com/products/horizon.html",
    },
    {
        "Name": "IBFD Tax Research Platform",
        "Description": "International tax research and information platform",
        "Official URL": "https://www.ibfd.org",
    },
    {
        "Name": "iCapture",
        "Description": "Document capture and management solution",
        "Official URL": "https://www.icapture.com",
    },
    {
        "Name": "Icims",
        "Description": "Talent acquisition and recruiting platform",
        "Official URL": "https://www.icims.com",
    },
    {
        "Name": "Impart WAF",
        "Description": "Web application firewall and security platform",
        "Official URL": "https://www.impart.security",
    },
    {
        "Name": "Infra - Grafana",
        "Description": "Infrastructure monitoring and observability platform",
        "Official URL": "https://grafana.com",
    },
    {
        "Name": "Infrastructure Patch Automation",
        "Description": "Automated infrastructure patching and management",
        "Official URL": "https://www.patchautomation.com",
    },
    {
        "Name": "Innovate",
        "Description": "Innovation management and ideation platform",
        "Official URL": "https://www.innovate.com",
    },
    {
        "Name": "InsightSquared",
        "Description": "Revenue operations and analytics platform",
        "Official URL": "https://www.insightsquared.com",
    },
    {
        "Name": "Integrate",
        "Description": "Marketing automation and demand generation platform",
        "Official URL": "https://www.integrate.com",
    },
    {
        "Name": "Intel471",
        "Description": "Cyberthreat intelligence platform",
        "Official URL": "https://intel471.com",
    },
    {
        "Name": "Intune",
        "Description": "Microsoft endpoint management and mobile device management",
        "Official URL": "https://www.microsoft.com/en-us/security/business/endpoint-management/microsoft-intune",
    },
    {
        "Name": "Inventory-mgmt",
        "Description": "Inventory management and tracking system",
        "Official URL": "https://www.inventory-mgmt.com",
    },
    {
        "Name": "InVision",
        "Description": "Digital product design and collaboration platform",
        "Official URL": "https://www.invisionapp.com",
    },
    {
        "Name": "Invoca",
        "Description": "Call tracking and conversation analytics platform",
        "Official URL": "https://www.invoca.com",
    },
    {
        "Name": "IronClad",
        "Description": "Contract lifecycle management platform",
        "Official URL": "https://ironcladapp.com",
    },
    {
        "Name": "ISO 27001 License Standards",
        "Description": "Information security management standards",
        "Official URL": "https://www.iso.org/isoiec-27001-information-security.html",
    },
    {
        "Name": "iStock Images for .com",
        "Description": "Stock photography and image licensing",
        "Official URL": "https://www.istockphoto.com",
    },
    {
        "Name": "IT Business Process",
        "Description": "IT service management and business process automation",
        "Official URL": "https://www.itbusinessprocess.com",
    },
    {
        "Name": "IT-ISAC",
        "Description": "IT Information Sharing and Analysis Center",
        "Official URL": "https://www.it-isac.org",
    },
    {
        "Name": "iText",
        "Description": "PDF creation and manipulation library",
        "Official URL": "https://itextpdf.com",
    },
    {
        "Name": "JetBrains",
        "Description": "Integrated development environment and developer tools",
        "Official URL": "https://www.jetbrains.com",
    },
    {
        "Name": "Jira",
        "Description": "Project management and issue tracking platform",
        "Official URL": "https://www.atlassian.com/software/jira",
    },
    {
        "Name": "Kainos",
        "Description": "Digital services and technology consulting",
        "Official URL": "https://www.kainos.com",
    },
    {
        "Name": "Kaltura",
        "Description": "Video platform and content management system",
        "Official URL": "https://corp.kaltura.com",
    },
    {
        "Name": "Kanbina",
        "Description": "Kanban board and project management tool",
        "Official URL": "https://www.kanbina.com",
    },
    {
        "Name": "Kandji",
        "Description": "Apple device management platform",
        "Official URL": "https://www.kandji.io",
    },
    {
        "Name": "Kaseya VSA",
        "Description": "IT management and remote monitoring platform",
        "Official URL": "https://www.kaseya.com/products/vsa",
    },
    {
        "Name": "Knowbe4",
        "Description": "Security awareness training and phishing simulation",
        "Official URL": "https://www.knowbe4.com",
    },
    {
        "Name": "PhishER",
        "Description": "Phishing incident response and management",
        "Official URL": "https://www.knowbe4.com/products/phisher",
    },
    {
        "Name": "KYCaaS",
        "Description": "Know Your Customer as a Service platform",
        "Official URL": "https://www.kycaas.com",
    },
    {
        "Name": "Lative.io",
        "Description": "Data integration and analytics platform",
        "Official URL": "https://lative.io",
    },
    {
        "Name": "LeanData",
        "Description": "Revenue operations and lead management platform",
        "Official URL": "https://www.leandata.com",
    },
    {
        "Name": "LeanIX",
        "Description": "Enterprise architecture management platform",
        "Official URL": "https://www.leanix.net",
    },
    {
        "Name": "Legisway Essentials",
        "Description": "Legal compliance and regulatory management",
        "Official URL": "https://www.legisway.com",
    },
    {
        "Name": "LexisNexis",
        "Description": "Legal research and information services",
        "Official URL": "https://www.lexisnexis.com",
    },
    {
        "Name": "LinkedIn Learning",
        "Description": "Professional development and online learning platform",
        "Official URL": "https://www.linkedin.com/learning",
    },
    {
        "Name": "LinkedIn Recruiting",
        "Description": "Professional recruiting and talent acquisition",
        "Official URL": "https://business.linkedin.com/talent-solutions/recruiter",
    },
    {
        "Name": "LinkedIn Sales Navigator",
        "Description": "Social selling and sales intelligence platform",
        "Official URL": "https://business.linkedin.com/sales-solutions/sales-navigator",
    },
    {
        "Name": "LinkPoint Connect for Salesforce",
        "Description": "Salesforce integration and connectivity platform",
        "Official URL": "https://www.linkpoint.com",
    },
    {
        "Name": "LionBridge Clay Tablet AEM",
        "Description": "Translation management for Adobe Experience Manager",
        "Official URL": "https://www.lionbridge.com",
    },
    {
        "Name": "Lionbridget Clay Tablet Eloqua",
        "Description": "Translation management for Oracle Eloqua",
        "Official URL": "https://www.lionbridge.com",
    },
    {
        "Name": "Logic Pro X",
        "Description": "Professional music production software",
        "Official URL": "https://www.apple.com/logic-pro",
    },
    {
        "Name": "LogMeln USA, Inc.",
        "Description": "Remote access and support software",
        "Official URL": "https://www.logmein.com",
    },
    {
        "Name": "Loopio RFP",
        "Description": "RFP response management and automation platform",
        "Official URL": "https://loopio.com",
    },
    {
        "Name": "Lucidchart",
        "Description": "Diagramming and visual collaboration platform",
        "Official URL": "https://www.lucidchart.com",
    },
    {
        "Name": "Lytics/Segment",
        "Description": "Customer data platform and analytics",
        "Official URL": "https://segment.com",
    },
    {
        "Name": "MadKudu",
        "Description": "Predictive analytics for sales and marketing",
        "Official URL": "https://www.madkudu.com",
    },
    {
        "Name": "Mailchimp",
        "Description": "Email marketing and automation platform",
        "Official URL": "https://mailchimp.com",
    },
    {
        "Name": "MailFinance Inc.",
        "Description": "Financial services and payment processing",
        "Official URL": "https://www.mailfinance.com",
    },
    {
        "Name": "MailSTAR Address Correction",
        "Description": "Address validation and correction service",
        "Official URL": "https://www.mailstar.com",
    },
    {
        "Name": "Mapbox, Inc.",
        "Description": "Location data and mapping platform",
        "Official URL": "https://www.mapbox.com",
    },
    {
        "Name": "Marketing Data Engineering Airflow",
        "Description": "Marketing data pipeline and workflow management",
        "Official URL": "https://airflow.apache.org",
    },
    {
        "Name": "marketing-poc",
        "Description": "Marketing proof of concept platform",
        "Official URL": "https://www.marketing-poc.com",
    },
    {
        "Name": "Marmoset",
        "Description": "Music licensing and content platform",
        "Official URL": "https://www.marmosetmusic.com",
    },
    {
        "Name": "MARVAR",
        "Description": "Marketing analytics and reporting platform",
        "Official URL": "https://www.marvar.com",
    },
    {
        "Name": "Media Temple",
        "Description": "Web hosting and cloud services platform",
        "Official URL": "https://mediatemple.net",
    },
    {
        "Name": "Melissa Data Corp.",
        "Description": "Data quality and address verification services",
        "Official URL": "https://www.melissa.com",
    },
    {
        "Name": "Meraki Security Cameras",
        "Description": "Cloud-managed security camera system",
        "Official URL": "https://meraki.cisco.com/products/security-cameras",
    },
    {
        "Name": "Microsoft CloudConnect",
        "Description": "Cloud connectivity and integration service",
        "Official URL": "https://www.microsoft.com/cloudconnect",
    },
    {
        "Name": "Microsoft Dynamics NAV",
        "Description": "Enterprise resource planning (ERP) system",
        "Official URL": "https://dynamics.microsoft.com/en-us/nav-overview",
    },
    {
        "Name": "Microsoft PowerBI Pro",
        "Description": "Business intelligence and data visualization",
        "Official URL": "https://powerbi.microsoft.com",
    },
    {
        "Name": "Microsoft Sharepoint",
        "Description": "Collaboration and document management platform",
        "Official URL": "https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration",
    },
    {
        "Name": "Microsoft Teams",
        "Description": "Collaboration and communication platform",
        "Official URL": "https://www.microsoft.com/en-us/microsoft-teams/group-chat-software",
    },
    {
        "Name": "Microsoft Visio",
        "Description": "Diagramming and vector graphics application",
        "Official URL": "https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software",
    },
    {
        "Name": "MigrationWiz",
        "Description": "Email and cloud migration platform",
        "Official URL": "https://www.bittitan.com/migrationwiz",
    },
    {
        "Name": "MILES 3",
        "Description": "Military logistics and supply chain management",
        "Official URL": "https://www.miles3.com",
    },
    {
        "Name": "MILES Activity Monitoring Service",
        "Description": "Activity monitoring and tracking service",
        "Official URL": "https://www.miles-monitoring.com",
    },
    {
        "Name": "MILES List Import Service",
        "Description": "List import and data management service",
        "Official URL": "https://www.miles-import.com",
    },
    {
        "Name": "Mimecast",
        "Description": "Email security and archiving platform",
        "Official URL": "https://www.mimecast.com",
    },
    {
        "Name": "Mimecast Brand Exploit Protect",
        "Description": "Brand protection and anti-phishing service",
        "Official URL": "https://www.mimecast.com/products/brand-exploit-protect",
    },
    {
        "Name": "MindMatrix",
        "Description": "Channel partner marketing platform",
        "Official URL": "https://mindmatrix.net",
    },
    {
        "Name": "Miro",
        "Description": "Online collaborative whiteboard platform",
        "Official URL": "https://miro.com",
    },
    {
        "Name": "Monday.com",
        "Description": "Work operating system and project management",
        "Official URL": "https://monday.com",
    },
    {
        "Name": "MongoDB",
        "Description": "NoSQL database management system",
        "Official URL": "https://www.mongodb.com",
    },
    {
        "Name": "n8n-Tier-1",
        "Description": "Workflow automation and integration platform",
        "Official URL": "https://n8n.io",
    },
    {
        "Name": "NC Squared Distribution Engine",
        "Description": "Content distribution and management engine",
        "Official URL": "https://www.ncsquared.com",
    },
    {
        "Name": "NCrunch",
        "Description": "Automated testing tool for .NET development",
        "Official URL": "https://www.ncrunch.net",
    },
    {
        "Name": "NDI",
        "Description": "Network Device Interface for video production",
        "Official URL": "https://www.ndi.tv",
    },
    {
        "Name": "Nessus",
        "Description": "Vulnerability assessment and management platform",
        "Official URL": "https://www.tenable.com/products/nessus",
    },
    {
        "Name": "NetSuite",
        "Description": "Cloud-based ERP and business management suite",
        "Official URL": "https://www.netsuite.com",
    },
    {
        "Name": "Netsuite E-Invoicing Support Portal",
        "Description": "Electronic invoicing support and management",
        "Official URL": "https://www.netsuite.com/portal/platform/developer/ecommerce",
    },
    {
        "Name": "Nutanix",
        "Description": "Hyperconverged infrastructure and cloud platform",
        "Official URL": "https://www.nutanix.com",
    },
    {
        "Name": "OCTO Inventory Survey 1.4",
        "Description": "IT inventory management and surveying tool",
        "Official URL": "https://www.ocsinventory-ng.org",
    },
    {
        "Name": "Okta",
        "Description": "Identity and access management platform",
        "Official URL": "https://www.okta.com",
    },
    {
        "Name": "Olono",
        "Description": "Digital transformation and consulting platform",
        "Official URL": "https://www.olono.com",
    },
    {
        "Name": "Omni",
        "Description": "Omnichannel retail and inventory management",
        "Official URL": "https://www.omni.com",
    },
    {
        "Name": "ON24",
        "Description": "Digital experience platform for webinars and events",
        "Official URL": "https://www.on24.com",
    },
    {
        "Name": "OneTrust",
        "Description": "Privacy, security, and third-party risk platform",
        "Official URL": "https://www.onetrust.com",
    },
    {
        "Name": "Oomnitza",
        "Description": "IT asset management and workflow automation",
        "Official URL": "https://www.oomnitza.com",
    },
    {
        "Name": "OpsGenie",
        "Description": "Incident management and alerting platform",
        "Official URL": "https://www.atlassian.com/software/opsgenie",
    },
    {
        "Name": "Outpost Security",
        "Description": "Cybersecurity and threat detection platform",
        "Official URL": "https://www.outpost24.com",
    },
    {
        "Name": "Outreach",
        "Description": "Sales engagement and automation platform",
        "Official URL": "https://www.outreach.io",
    },
    {
        "Name": "Oxygen XML Author",
        "Description": "Structured document authoring tool",
        "Official URL": "https://www.oxygenxml.com/xml_author.html",
    },
    {
        "Name": "Oxygen XML Editor",
        "Description": "XML development and editing environment",
        "Official URL": "https://www.oxygenxml.com/xml_editor.html",
    },
    {
        "Name": "Oxygen XML WebHelp",
        "Description": "Web-based help system and documentation",
        "Official URL": "https://www.oxygenxml.com/xml_webhelp.html",
    },
    {
        "Name": "Paligo",
        "Description": "Component-based authoring and publishing platform",
        "Official URL": "https://paligo.net",
    },
    {
        "Name": "Palo Alto Logging Service",
        "Description": "Security logging and analytics service",
        "Official URL": "https://www.paloaltonetworks.com/cortex/cortex-data-lake",
    },
    {
        "Name": "Partner Success Utility Service",
        "Description": "Partner success management and automation",
        "Official URL": "https://www.partnersuccess.com",
    },
    {
        "Name": "Patch My PC",
        "Description": "Third-party software update management",
        "Official URL": "https://patchmypc.com",
    },
    {
        "Name": "Pay Square (India)",
        "Description": "Payment processing platform for India",
        "Official URL": "https://www.paysquare.com",
    },
    {
        "Name": "Paylocity Corporation",
        "Description": "Payroll and human capital management platform",
        "Official URL": "https://www.paylocity.com",
    },
    {
        "Name": "Payment Acceptance App",
        "Description": "Payment processing and acceptance application",
        "Official URL": "https://www.paymentacceptance.com",
    },
    {
        "Name": "Payscale",
        "Description": "Compensation data and salary benchmarking",
        "Official URL": "https://www.payscale.com",
    },
    {
        "Name": "PDF2XL",
        "Description": "PDF to Excel conversion tool",
        "Official URL": "https://www.pdf2xl.com",
    },
    {
        "Name": "Phishme",
        "Description": "Phishing simulation and security awareness training",
        "Official URL": "https://cofense.com",
    },
    {
        "Name": "Photoshop",
        "Description": "Digital image editing and manipulation software",
        "Official URL": "https://www.adobe.com/products/photoshop.html",
    },
    {
        "Name": "PhpStorm",
        "Description": "PHP integrated development environment",
        "Official URL": "https://www.jetbrains.com/phpstorm",
    },
    {
        "Name": "Pingdom",
        "Description": "Website monitoring and performance analytics",
        "Official URL": "https://www.pingdom.com",
    },
    {
        "Name": "Pitchbook",
        "Description": "Private market data and research platform",
        "Official URL": "https://pitchbook.com",
    },
    {
        "Name": "Plant IO",
        "Description": "Industrial IoT and asset monitoring platform",
        "Official URL": "https://www.plantio.com",
    },
    {
        "Name": "PLANTAPP.IO",
        "Description": "Plant monitoring and management application",
        "Official URL": "https://plantapp.io",
    },
    {
        "Name": "poirot",
        "Description": "Data analysis and investigation tool",
        "Official URL": "https://www.poirot.com",
    },
    {
        "Name": "PoolParty",
        "Description": "Semantic technology and knowledge management",
        "Official URL": "https://www.poolparty.biz",
    },
    {
        "Name": "PORTSWIGGER LTD",
        "Description": "Web application security testing tools",
        "Official URL": "https://portswigger.net",
    },
    {
        "Name": "Postico",
        "Description": "PostgreSQL client for macOS",
        "Official URL": "https://eggerapps.at/postico",
    },
    {
        "Name": "POSTMAN",
        "Description": "API development and testing platform",
        "Official URL": "https://www.postman.com",
    },
    {
        "Name": "Power BI",
        "Description": "Microsoft's business analytics and visualization platform",
        "Official URL": "https://powerbi.microsoft.com",
    },
    {
        "Name": "Precisely",
        "Description": "Data integrity and location intelligence platform",
        "Official URL": "https://www.precisely.com",
    },
    {
        "Name": "Predictive Index Perform",
        "Description": "Talent optimization and performance platform",
        "Official URL": "https://www.predictiveindex.com",
    },
    {
        "Name": "Premium Beat",
        "Description": "Royalty-free music and audio platform",
        "Official URL": "https://www.premiumbeat.com",
    },
    {
        "Name": "Acunetix",
        "Description": "Web application security scanner",
        "Official URL": "https://www.acunetix.com",
    },
    {
        "Name": "Product Security / ALFA Ask-Seceng AI",
        "Description": "AI-powered security engineering assistant",
        "Official URL": "https://www.alfa-security.com",
    },
    {
        "Name": "Appsec Offboarding-Automation",
        "Description": "Application security offboarding automation",
        "Official URL": "https://www.appsec-automation.com",
    },
    {
        "Name": "AvAttacks CTF",
        "Description": "Capture the Flag cybersecurity training platform",
        "Official URL": "https://www.avattacks.com",
    },
    {
        "Name": "AvAttacks EC2 Infrastructure",
        "Description": "AWS EC2 infrastructure for security testing",
        "Official URL": "https://aws.amazon.com/ec2",
    },
    {
        "Name": "Checkmarx, Inc.",
        "Description": "Application security testing platform",
        "Official URL": "https://checkmarx.com",
    },
    {
        "Name": "Client Certificate Secret Manager (CCSM)",
        "Description": "Certificate and secret management system",
        "Official URL": "https://www.ccsm.com",
    },
    {
        "Name": "Endor Labs",
        "Description": "Application security and dependency management",
        "Official URL": "https://www.endorlabs.com",
    },
    {
        "Name": "IriusRisk",
        "Description": "Threat modeling and risk management platform",
        "Official URL": "https://www.iriusrisk.com",
    },
    {
        "Name": "Mend",
        "Description": "Open source security and compliance platform",
        "Official URL": "https://www.mend.io",
    },
    {
        "Name": "Ransomware Protection AWS Backup",
        "Description": "AWS backup service for ransomware protection",
        "Official URL": "https://aws.amazon.com/backup",
    },
    {
        "Name": "Secrets Backup Vault",
        "Description": "Secure backup and recovery for secrets management",
        "Official URL": "https://www.secretsbackup.com",
    },
    {
        "Name": "SQAI",
        "Description": "SQL and database artificial intelligence platform",
        "Official URL": "https://www.sqai.com",
    },
    {
        "Name": "Termination Logging",
        "Description": "Employee termination and audit logging system",
        "Official URL": "https://www.terminationlogging.com",
    },
    {
        "Name": "Transit Gateway Management System",
        "Description": "AWS Transit Gateway management and automation",
        "Official URL": "https://aws.amazon.com/transit-gateway",
    },
    {
        "Name": "VECTR",
        "Description": "Security assessment and purple team platform",
        "Official URL": "https://vectr.io",
    },
    {
        "Name": "WorkRamp Course Unassigner",
        "Description": "Learning management course assignment tool",
        "Official URL": "https://www.workramp.com",
    },
    {
        "Name": "Project",
        "Description": "Microsoft Project management software",
        "Official URL": "https://www.microsoft.com/en-us/microsoft-365/project/project-management-software",
    },
    {
        "Name": "Prometheus",
        "Description": "Open-source monitoring and alerting toolkit",
        "Official URL": "https://prometheus.io",
    },
    {
        "Name": "Proofpoint",
        "Description": "Cybersecurity and compliance platform",
        "Official URL": "https://www.proofpoint.com",
    },
    {
        "Name": "Proofpoint CASB",
        "Description": "Cloud Access Security Broker solution",
        "Official URL": "https://www.proofpoint.com/us/products/cloud-security/cloud-access-security-broker",
    },
    {
        "Name": "Proofpoint DLP",
        "Description": "Data Loss Prevention security solution",
        "Official URL": "https://www.proofpoint.com/us/products/information-protection/data-loss-prevention",
    },
    {
        "Name": "PROS CPQ",
        "Description": "Configure, Price, Quote solution for complex selling",
        "Official URL": "https://pros.com/products/configure-price-quote",
    },
    {
        "Name": "Prospect Database International Routing",
        "Description": "International prospect database and routing service",
        "Official URL": "https://www.prospectdatabase.com",
    },
    {
        "Name": "PRTG Network Monitor",
        "Description": "Network monitoring and infrastructure management",
        "Official URL": "https://www.paessler.com/prtg",
    },
    {
        "Name": "Pulseboard",
        "Description": "Real-time dashboard and analytics platform",
        "Official URL": "https://www.pulseboard.com",
    },
    {
        "Name": "QB *QUICKBASE",
        "Description": "Low-code application development platform",
        "Official URL": "https://www.quickbase.com",
    },
    {
        "Name": "Qualtrics",
        "Description": "Experience management and survey platform",
        "Official URL": "https://www.qualtrics.com",
    },
    {
        "Name": "QuarkXPress",
        "Description": "Desktop publishing and layout design software",
        "Official URL": "https://www.quark.com/products/quarkxpress",
    },
    {
        "Name": "Qubole",
        "Description": "Cloud-native data platform and analytics",
        "Official URL": "https://www.qubole.com",
    },
    {
        "Name": "Quest Change Auditor",
        "Description": "IT change tracking and compliance auditing",
        "Official URL": "https://www.quest.com/products/change-auditor",
    },
    {
        "Name": "Quickbooks",
        "Description": "Accounting and financial management software",
        "Official URL": "https://quickbooks.intuit.com",
    },
    {
        "Name": "Ransomware Orchestration",
        "Description": "Ransomware response and recovery orchestration",
        "Official URL": "https://www.ransomwareorchestration.com",
    },
    {
        "Name": "Backup Audit Manager",
        "Description": "Backup audit and compliance management",
        "Official URL": "https://www.backupaudit.com",
    },
    {
        "Name": "Rapid7 Ireland Ltd",
        "Description": "Security analytics and vulnerability management",
        "Official URL": "https://www.rapid7.com",
    },
    {
        "Name": "AWS Config",
        "Description": "AWS resource configuration management service",
        "Official URL": "https://aws.amazon.com/config",
    },
    {
        "Name": "Centralized Grafana",
        "Description": "Centralized monitoring and observability platform",
        "Official URL": "https://grafana.com",
    },
    {
        "Name": "DBaaS",
        "Description": "Database as a Service platform",
        "Official URL": "https://www.dbaas.com",
    },
    {
        "Name": "GitLab - Shared Runners - GCP",
        "Description": "GitLab CI/CD runners on Google Cloud Platform",
        "Official URL": "https://gitlab.com",
    },
    {
        "Name": "Internal DNS",
        "Description": "Internal domain name system management",
        "Official URL": "https://www.internaldns.com",
    },
    {
        "Name": "PostgreSQL",
        "Description": "Open source relational database management system",
        "Official URL": "https://www.postgresql.org",
    },
    {
        "Name": "RELE Jumpservers",
        "Description": "Remote access jump server management",
        "Official URL": "https://www.rele.com",
    },
    {
        "Name": "SumoLogic",
        "Description": "Cloud-native security and observability platform",
        "Official URL": "https://www.sumologic.com",
    },
    {
        "Name": "Venafi Trust Protection Platform",
        "Description": "Machine identity protection and certificate management",
        "Official URL": "https://www.venafi.com",
    },
    {
        "Name": "Retrium",
        "Description": "Team retrospective and collaboration platform",
        "Official URL": "https://www.retrium.com",
    },
    {
        "Name": "Rev.com",
        "Description": "Transcription, captioning, and translation services",
        "Official URL": "https://www.rev.com",
    },
    {
        "Name": "Revu Standard",
        "Description": "PDF markup and collaboration software for construction",
        "Official URL": "https://www.bluebeam.com/solutions/revu",
    },
    {
        "Name": "RightRev",
        "Description": "Revenue recognition and accounting automation",
        "Official URL": "https://rightrev.com",
    },
    {
        "Name": "RingCentral",
        "Description": "Cloud communications and contact center platform",
        "Official URL": "https://www.ringcentral.com",
    },
    {
        "Name": "RingCentral / InContact / NICE CXone",
        "Description": "Contact center and customer experience platform",
        "Official URL": "https://www.niceincontact.com",
    },
    {
        "Name": "RoboCop",
        "Description": "Automated security and compliance monitoring",
        "Official URL": "https://www.robocop.com",
    },
    {
        "Name": "SailPoint",
        "Description": "Identity governance and administration platform",
        "Official URL": "https://www.sailpoint.com",
    },
    {
        "Name": "Salesforce",
        "Description": "Customer relationship management (CRM) platform",
        "Official URL": "https://www.salesforce.com",
    },
    {
        "Name": "Salesforce Platform",
        "Description": "Cloud-based application development platform",
        "Official URL": "https://www.salesforce.com/products/platform",
    },
    {
        "Name": "Salesforce Revenue Cloud",
        "Description": "Revenue lifecycle management for Salesforce",
        "Official URL": "https://www.salesforce.com/products/revenue-cloud",
    },
    {
        "Name": "Salesforce Billing",
        "Description": "Billing and invoicing automation for Salesforce",
        "Official URL": "https://www.salesforce.com/products/billing",
    },
    {
        "Name": "Salesforce CPQ",
        "Description": "Configure, Price, Quote solution for Salesforce",
        "Official URL": "https://www.salesforce.com/products/cpq",
    },
    {
        "Name": "Salesforce.com Advanced Approvals",
        "Description": "Advanced approval workflows for Salesforce",
        "Official URL": "https://appexchange.salesforce.com/appxListingDetail?listingId=a0N30000004gHhNEAU",
    },
    {
        "Name": "Salesforce Subscription Management",
        "Description": "Subscription billing and management for Salesforce",
        "Official URL": "https://www.salesforce.com/products/billing",
    },
    {
        "Name": "Salesforce Sales Cloud",
        "Description": "Sales automation and CRM for Salesforce",
        "Official URL": "https://www.salesforce.com/products/sales-cloud",
    },
    {
        "Name": "Salesforce Communities",
        "Description": "Customer and partner community platform",
        "Official URL": "https://www.salesforce.com/products/community-cloud",
    },
    {
        "Name": "SalesMethods, Inc.",
        "Description": "Sales training and methodology platform",
        "Official URL": "https://www.salesmethods.com",
    },
    {
        "Name": "SAP Fieldglass Vendor Management System",
        "Description": "External workforce and vendor management",
        "Official URL": "https://www.fieldglass.com",
    },
    {
        "Name": "SatMetrix",
        "Description": "Customer experience and Net Promoter Score platform",
        "Official URL": "https://www.nice.com/products/cx-analytics/customer-analytics/satmetrix",
    },
    {
        "Name": "Screaming Frog",
        "Description": "SEO website crawler and technical audit tool",
        "Official URL": "https://www.screamingfrog.co.uk",
    },
    {
        "Name": "SDWorx",
        "Description": "Human resources and payroll services platform",
        "Official URL": "https://www.sdworx.com",
    },
    {
        "Name": "SecureSheet Technologies LLC",
        "Description": "Document security and protection platform",
        "Official URL": "https://www.securesheet.com",
    },
    {
        "Name": "SecureWorks Inc.",
        "Description": "Managed security services and threat intelligence",
        "Official URL": "https://www.secureworks.com",
    },
    {
        "Name": "Security Data Sync Service",
        "Description": "Security data synchronization and integration",
        "Official URL": "https://www.securitydatasync.com",
    },
    {
        "Name": "SecurityScorecard",
        "Description": "Security ratings and vendor risk management",
        "Official URL": "https://securityscorecard.com",
    },
    {
        "Name": "SEM Rush SEO Content tool",
        "Description": "SEO content optimization and marketing tool",
        "Official URL": "https://www.semrush.com",
    },
    {
        "Name": "SEMrush",
        "Description": "Digital marketing and SEO analytics platform",
        "Official URL": "https://www.semrush.com",
    },
    {
        "Name": "SendGrid",
        "Description": "Email delivery and marketing platform",
        "Official URL": "https://sendgrid.com",
    },
    {
        "Name": "Sendoso",
        "Description": "Direct mail and gifting automation platform",
        "Official URL": "https://sendoso.com",
    },
    {
        "Name": "Sertifi",
        "Description": "Digital signature and payment processing",
        "Official URL": "https://www.sertifi.com",
    },
    {
        "Name": "ServiceNow",
        "Description": "Digital workflow and IT service management platform",
        "Official URL": "https://www.servicenow.com",
    },
    {
        "Name": "ServiceNow IT Asset",
        "Description": "IT asset management within ServiceNow",
        "Official URL": "https://www.servicenow.com/products/it-asset-management.html",
    },
    {
        "Name": "ServiceNow IT Service Management",
        "Description": "IT service management and support platform",
        "Official URL": "https://www.servicenow.com/products/itsm.html",
    },
    {
        "Name": "ServiceNow SecOps",
        "Description": "Security operations within ServiceNow",
        "Official URL": "https://www.servicenow.com/products/security-operations.html",
    },
    {
        "Name": "ServiceSkills",
        "Description": "Service management and skills tracking platform",
        "Official URL": "https://www.serviceskills.com",
    },
    {
        "Name": "SERVICESTACK.NET",
        "Description": ".NET web services framework and platform",
        "Official URL": "https://servicestack.net",
    },
    {
        "Name": "Signal fx, Inc.",
        "Description": "Real-time operational intelligence platform",
        "Official URL": "https://www.splunk.com/en_us/investor-relations/acquisitions/signalfx.html",
    },
    {
        "Name": "Signicat Case Manager",
        "Description": "Digital identity verification and case management",
        "Official URL": "https://www.signicat.com",
    },
    {
        "Name": "Simpplr",
        "Description": "Employee experience and intranet platform",
        "Official URL": "https://www.simpplr.com",
    },
    {
        "Name": "Sisense",
        "Description": "Business intelligence and analytics platform",
        "Official URL": "https://www.sisense.com",
    },
    {
        "Name": "skan.ai",
        "Description": "AI-powered mobile attribution and analytics",
        "Official URL": "https://skan.ai",
    },
    {
        "Name": "Sketch",
        "Description": "Digital design and prototyping platform",
        "Official URL": "https://www.sketch.com",
    },
    {
        "Name": "Skilljar",
        "Description": "Customer training and education platform",
        "Official URL": "https://www.skilljar.com",
    },
    {
        "Name": "Skylab SDK Documentation Site",
        "Description": "Software development kit documentation platform",
        "Official URL": "https://www.skylab.com",
    },
    {
        "Name": "Skytap",
        "Description": "Cloud hosting for traditional enterprise applications",
        "Official URL": "https://www.skytap.com",
    },
    {
        "Name": "Slapfive",
        "Description": "Employee recognition and engagement platform",
        "Official URL": "https://www.slapfive.com",
    },
    {
        "Name": "SlideTeam.net",
        "Description": "PowerPoint templates and presentation resources",
        "Official URL": "https://www.slideteam.net",
    },
    {
        "Name": "Smartbear",
        "Description": "Software testing and development tools platform",
        "Official URL": "https://smartbear.com",
    },
    {
        "Name": "Smartdraw",
        "Description": "Diagramming and flowchart software",
        "Official URL": "https://www.smartdraw.com",
    },
    {
        "Name": "Smartling Translation Platform",
        "Description": "Translation management and localization platform",
        "Official URL": "https://www.smartling.com",
    },
    {
        "Name": "Smartsheet",
        "Description": "Work management and automation platform",
        "Official URL": "https://www.smartsheet.com",
    },
    {
        "Name": "SmartyStreets",
        "Description": "Address validation and geocoding API",
        "Official URL": "https://www.smartystreets.com",
    },
    {
        "Name": "Snagit",
        "Description": "Screen capture and image editing software",
        "Official URL": "https://www.techsmith.com/screen-capture.html",
    },
    {
        "Name": "Snowflake Data Cloud",
        "Description": "Cloud data platform for analytics and data sharing",
        "Official URL": "https://www.snowflake.com",
    },
    {
        "Name": "Snowflake",
        "Description": "Cloud-based data warehouse and analytics platform",
        "Official URL": "https://www.snowflake.com",
    },
    {
        "Name": "Snowflake EMEA",
        "Description": "Snowflake data platform for Europe, Middle East, and Africa",
        "Official URL": "https://www.snowflake.com",
    },
    {
        "Name": "SoapUI",
        "Description": "API testing and service virtualization platform",
        "Official URL": "https://www.soapui.org",
    },
    {
        "Name": "Softchoice Corporation",
        "Description": "Technology solutions and services provider",
        "Official URL": "https://www.softchoice.com",
    },
    {
        "Name": "SolarWinds",
        "Description": "IT infrastructure monitoring and management",
        "Official URL": "https://www.solarwinds.com",
    },
    {
        "Name": "SonarQube",
        "Description": "Code quality and security analysis platform",
        "Official URL": "https://www.sonarqube.org",
    },
    {
        "Name": "SPARKOL",
        "Description": "Video creation and animation software",
        "Official URL": "https://www.sparkol.com",
    },
    {
        "Name": "Splunk",
        "Description": "Security information and event management platform",
        "Official URL": "https://www.splunk.com",
    },
    {
        "Name": "Google Workspace for Splunk",
        "Description": "Google Workspace integration for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/5556",
    },
    {
        "Name": "Splunk Add-on for CrowdStrike FDR",
        "Description": "CrowdStrike integration for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/5082",
    },
    {
        "Name": "Splunk Add-on for Microsoft Office 365",
        "Description": "Office 365 integration for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/4055",
    },
    {
        "Name": "Splunk Add-on for ServiceNow",
        "Description": "ServiceNow integration for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/1928",
    },
    {
        "Name": "Splunk CrowdStrike App",
        "Description": "CrowdStrike application for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/3082",
    },
    {
        "Name": "Splunk DB Connect",
        "Description": "Database connectivity for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/2686",
    },
    {
        "Name": "Splunk Enterprise Security",
        "Description": "Security analytics platform for Splunk",
        "Official URL": "https://www.splunk.com/en_us/software/enterprise-security.html",
    },
    {
        "Name": "Thinkst Canary App for Splunk",
        "Description": "Thinkst Canary integration for Splunk",
        "Official URL": "https://splunkbase.splunk.com/app/4531",
    },
    {
        "Name": "Splunk SOAR",
        "Description": "Security orchestration, automation, and response",
        "Official URL": "https://www.splunk.com/en_us/software/splunk-security-orchestration-and-automation.html",
    },
    {
        "Name": "Sprinkler Replacement TBD",
        "Description": "Fire suppression system replacement project",
        "Official URL": "https://www.sprinklerreplacement.com",
    },
    {
        "Name": "SQL",
        "Description": "Structured Query Language database management",
        "Official URL": "https://www.sql.org",
    },
    {
        "Name": "SSIS Data Flow Components f or PostgreSQL",
        "Description": "SQL Server Integration Services for PostgreSQL",
        "Official URL": "https://www.postgresql.org/docs/current/datatype.html",
    },
    {
        "Name": "SSL Store",
        "Description": "SSL certificate provider and marketplace",
        "Official URL": "https://www.thesslstore.com",
    },
    {
        "Name": "Stacklet",
        "Description": "Cloud governance and compliance automation",
        "Official URL": "https://stacklet.io",
    },
    {
        "Name": "Stata/SE",
        "Description": "Statistical software package for data analysis",
        "Official URL": "https://www.stata.com",
    },
    {
        "Name": "Statista",
        "Description": "Market and consumer data platform",
        "Official URL": "https://www.statista.com",
    },
    {
        "Name": "Sterlingcheck.com",
        "Description": "Background check and employment screening",
        "Official URL": "https://www.sterlingcheck.com",
    },
    {
        "Name": "Stitch",
        "Description": "Data integration and ETL platform",
        "Official URL": "https://www.stitchdata.com",
    },
    {
        "Name": "strongDM",
        "Description": "Zero trust privileged access management",
        "Official URL": "https://www.strongdm.com",
    },
    {
        "Name": "SurveyMonkey",
        "Description": "Online survey and feedback platform",
        "Official URL": "https://www.surveymonkey.com",
    },
    {
        "Name": "Sush.io Inc.",
        "Description": "Customer communication and engagement platform",
        "Official URL": "https://sush.io",
    },
    {
        "Name": "SVGATOR",
        "Description": "SVG animation creation platform",
        "Official URL": "https://www.svgator.com",
    },
    {
        "Name": "Swagger",
        "Description": "API documentation and design platform",
        "Official URL": "https://swagger.io",
    },
    {
        "Name": "Synopsys Inc",
        "Description": "Software security and quality testing platform",
        "Official URL": "https://www.synopsys.com",
    },
    {
        "Name": "Tableau (Online)",
        "Description": "Data visualization and business intelligence platform",
        "Official URL": "https://www.tableau.com",
    },
    {
        "Name": "Tackle.io",
        "Description": "Cloud marketplace and partner ecosystem platform",
        "Official URL": "https://tackle.io",
    },
    {
        "Name": "Tag spider",
        "Description": "Web tagging and analytics management",
        "Official URL": "https://www.tagspider.com",
    },
    {
        "Name": "Talend, Inc.",
        "Description": "Data integration and management platform",
        "Official URL": "https://www.talend.com",
    },
    {
        "Name": "Tally ERP",
        "Description": "Enterprise resource planning and accounting software",
        "Official URL": "https://tallysolutions.com",
    },
    {
        "Name": "Tanium",
        "Description": "Endpoint management and security platform",
        "Official URL": "https://www.tanium.com",
    },
    {
        "Name": "TargetCW",
        "Description": "Contingent workforce management platform",
        "Official URL": "https://www.targetcw.com",
    },
    {
        "Name": "Tax Compliance SFTP",
        "Description": "Secure file transfer for tax compliance",
        "Official URL": "https://www.taxcompliancesftp.com",
    },
    {
        "Name": "Taxrates",
        "Description": "Tax rate data and calculation service",
        "Official URL": "https://taxrates.com",
    },
    {
        "Name": "TeamViewer",
        "Description": "Remote access and support software",
        "Official URL": "https://www.teamviewer.com",
    },
    {
        "Name": "Tenable.IO",
        "Description": "Vulnerability management and cyber exposure platform",
        "Official URL": "https://www.tenable.com",
    },
    {
        "Name": "TestComplete",
        "Description": "Automated UI testing platform",
        "Official URL": "https://smartbear.com/product/testcomplete",
    },
    {
        "Name": "TestHarness",
        "Description": "Automated testing framework and platform",
        "Official URL": "https://www.testharness.com",
    },
    {
        "Name": "TestRail",
        "Description": "Test case management and QA platform",
        "Official URL": "https://www.gurock.com/testrail",
    },
    {
        "Name": "The Martec",
        "Description": "Marketing technology consulting and services",
        "Official URL": "https://www.themartec.com",
    },
    {
        "Name": "think-cell",
        "Description": "PowerPoint charting and presentation software",
        "Official URL": "https://www.think-cell.com",
    },
    {
        "Name": "Thinkst Canary",
        "Description": "Network security monitoring and honeypot platform",
        "Official URL": "https://canary.tools",
    },
    {
        "Name": "Thycotic",
        "Description": "Privileged access management and secrets management",
        "Official URL": "https://thycotic.com",
    },
    {
        "Name": "Tines",
        "Description": "Security automation and orchestration platform",
        "Official URL": "https://www.tines.com",
    },
    {
        "Name": "TinyPulse",
        "Description": "Employee engagement and feedback platform",
        "Official URL": "https://www.tinypulse.com",
    },
    {
        "Name": "TOGGL",
        "Description": "Time tracking and productivity management",
        "Official URL": "https://toggl.com",
    },
    {
        "Name": "Toonly",
        "Description": "Animated video creation platform",
        "Official URL": "https://www.toonly.com",
    },
    {
        "Name": "Totara Compliance",
        "Description": "Learning management and compliance platform",
        "Official URL": "https://www.totaralearning.com",
    },
    {
        "Name": "TrackJS",
        "Description": "JavaScript error monitoring and tracking",
        "Official URL": "https://trackjs.com",
    },
    {
        "Name": "Travis CI",
        "Description": "Continuous integration and deployment platform",
        "Official URL": "https://travis-ci.org",
    },
    {
        "Name": "TrustRadius",
        "Description": "Technology review and comparison platform",
        "Official URL": "https://www.trustradius.com",
    },
    {
        "Name": "Twitter",
        "Description": "Social media and microblogging platform",
        "Official URL": "https://twitter.com",
    },
    {
        "Name": "Udemy",
        "Description": "Online learning and course platform",
        "Official URL": "https://www.udemy.com",
    },
    {
        "Name": "Uplevel",
        "Description": "Engineering productivity and analytics platform",
        "Official URL": "https://www.uplevelteam.com",
    },
    {
        "Name": "Uptempo",
        "Description": "Marketing planning and performance platform",
        "Official URL": "https://www.uptempo.io",
    },
    {
        "Name": "URLScan",
        "Description": "Website scanning and threat analysis service",
        "Official URL": "https://urlscan.io",
    },
    {
        "Name": "US INCOME/EGT/FOR CORE PLUS ALL STATE & ALL INTERNATIONAL",
        "Description": "Tax and income calculation service",
        "Official URL": "https://www.incometax.com",
    },
    {
        "Name": "UserTesting",
        "Description": "User experience research and testing platform",
        "Official URL": "https://www.usertesting.com",
    },
    {
        "Name": "Validity",
        "Description": "Data quality and email deliverability platform",
        "Official URL": "https://www.validity.com",
    },
    {
        "Name": "Veeam Backup",
        "Description": "Data backup and disaster recovery platform",
        "Official URL": "https://www.veeam.com",
    },
    {
        "Name": "Vettery Inc",
        "Description": "Talent marketplace and recruiting platform",
        "Official URL": "https://vettery.com",
    },
    {
        "Name": "Videate",
        "Description": "Automated video creation for software",
        "Official URL": "https://www.videate.com",
    },
    {
        "Name": "Vimeo",
        "Description": "Video hosting and streaming platform",
        "Official URL": "https://vimeo.com",
    },
    {
        "Name": "VirusTotal",
        "Description": "Malware and virus scanning service",
        "Official URL": "https://www.virustotal.com",
    },
    {
        "Name": "Visual Studio",
        "Description": "Integrated development environment (IDE)",
        "Official URL": "https://visualstudio.microsoft.com",
    },
    {
        "Name": "vSphere and vCenter",
        "Description": "VMware virtualization management platform",
        "Official URL": "https://www.vmware.com/products/vsphere.html",
    },
    {
        "Name": "Vyond",
        "Description": "Animated video creation platform",
        "Official URL": "https://www.vyond.com",
    },
    {
        "Name": "Waf WebAcl Remediator",
        "Description": "Web Application Firewall remediation tool",
        "Official URL": "https://www.wafremediator.com",
    },
    {
        "Name": "WebStorm",
        "Description": "JavaScript and web development IDE",
        "Official URL": "https://www.jetbrains.com/webstorm",
    },
    {
        "Name": "wheniwork.com",
        "Description": "Employee scheduling and workforce management",
        "Official URL": "https://wheniwork.com",
    },
    {
        "Name": "WhereScape",
        "Description": "Data warehouse automation platform",
        "Official URL": "https://www.wherescape.com",
    },
    {
        "Name": "Windows Certificate Services",
        "Description": "Microsoft certificate authority and PKI services",
        "Official URL": "https://docs.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/server-certs/install-the-certification-authority",
    },
    {
        "Name": "Windows Key Management Service",
        "Description": "Microsoft software activation management",
        "Official URL": "https://docs.microsoft.com/en-us/windows-server/get-started/kms-overview",
    },
    {
        "Name": "Windows Server DHCP",
        "Description": "Dynamic Host Configuration Protocol service",
        "Official URL": "https://docs.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top",
    },
    {
        "Name": "Winzip",
        "Description": "File compression and archive management",
        "Official URL": "https://www.winzip.com",
    },
    {
        "Name": "Wiz Deployment Bot",
        "Description": "Automated deployment and configuration tool",
        "Official URL": "https://www.wiz.io",
    },
    {
        "Name": "Workday",
        "Description": "Human capital management and ERP platform",
        "Official URL": "https://www.workday.com",
    },
    {
        "Name": "Workday Adaptive Planning",
        "Description": "Business planning and budgeting platform",
        "Official URL": "https://www.workday.com/en-us/products/adaptive-planning.html",
    },
    {
        "Name": "Workflow Platform (WfaaS)",
        "Description": "Workflow as a Service automation platform",
        "Official URL": "https://www.workflowplatform.com",
    },
    {
        "Name": "WorkFront",
        "Description": "Work management and project collaboration platform",
        "Official URL": "https://www.workfront.com",
    },
    {
        "Name": "Adobe Workfront Fusion",
        "Description": "Work automation and integration platform",
        "Official URL": "https://www.workfront.com/products/fusion",
    },
    {
        "Name": "Workiva",
        "Description": "Connected reporting and compliance platform",
        "Official URL": "https://www.workiva.com",
    },
    {
        "Name": "Workramp",
        "Description": "Learning management system for companies",
        "Official URL": "https://www.workramp.com",
    },
    {
        "Name": "WorkRamp LMS",
        "Description": "Learning management system platform",
        "Official URL": "https://www.workramp.com",
    },
    {
        "Name": "Workstation",
        "Description": "VMware desktop virtualization platform",
        "Official URL": "https://www.vmware.com/products/workstation-pro.html",
    },
    {
        "Name": "www.avalara.com CDN",
        "Description": "Content delivery network for Avalara website",
        "Official URL": "https://www.avalara.com",
    },
    {
        "Name": "Xactly Corporation",
        "Description": "Sales performance management platform",
        "Official URL": "https://www.xactlycorp.com",
    },
    {
        "Name": "xb-hsat",
        "Description": "Cross-border health and safety assessment tool",
        "Official URL": "https://www.xb-hsat.com",
    },
    {
        "Name": "XBO Hub",
        "Description": "Xbox business operations hub",
        "Official URL": "https://www.xbox.com/business",
    },
    {
        "Name": "XMLSpy",
        "Description": "XML editor and development environment",
        "Official URL": "https://www.altova.com/xmlspy-xml-editor",
    },
    {
        "Name": "XTM",
        "Description": "Translation management system",
        "Official URL": "https://xtm.cloud",
    },
    {
        "Name": "Youtube",
        "Description": "Video sharing and streaming platform",
        "Official URL": "https://www.youtube.com",
    },
    {
        "Name": "Zabbix",
        "Description": "Enterprise network monitoring and management",
        "Official URL": "https://www.zabbix.com",
    },
    {
        "Name": "zeroheight",
        "Description": "Design system documentation platform",
        "Official URL": "https://zeroheight.com",
    },
    {
        "Name": "ZeroTier",
        "Description": "Software-defined networking platform",
        "Official URL": "https://www.zerotier.com",
    },
    {
        "Name": "Zint",
        "Description": "Barcode generation library and software",
        "Official URL": "https://www.zint.org.uk",
    },
    {
        "Name": "Zone Billing Netsuite",
        "Description": "NetSuite billing and invoicing integration",
        "Official URL": "https://www.netsuite.com",
    },
    {
        "Name": "Zoom",
        "Description": "Video conferencing and communication platform",
        "Official URL": "https://zoom.us",
    },
    {
        "Name": "Zoomin",
        "Description": "Product documentation and knowledge management",
        "Official URL": "https://www.zoominsoftware.com",
    },
    {
        "Name": "ZoomInfo",
        "Description": "Sales intelligence and prospecting platform",
        "Official URL": "https://www.zoominfo.com",
    },
]


def create_excel_file():
    """Create Excel file with app data"""
    # Create DataFrame
    df = pd.DataFrame(apps_data)

    # Create Excel file with formatting
    filename = "app_directory.xlsx"

    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        # Write the data
        df.to_excel(writer, sheet_name="App Directory", index=False)

        # Get the workbook and worksheet
        workbook = writer.book
        worksheet = writer.sheets["App Directory"]

        # Format headers
        header_font = openpyxl.styles.Font(bold=True, color="FFFFFF")
        header_fill = openpyxl.styles.PatternFill(
            start_color="366092", end_color="366092", fill_type="solid"
        )

        for cell in worksheet[1]:
            cell.font = header_font
            cell.fill = header_fill

        # Adjust column widths
        worksheet.column_dimensions["A"].width = 30  # Name
        worksheet.column_dimensions["B"].width = 60  # Description
        worksheet.column_dimensions["C"].width = 40  # Official URL

        # Add borders and alignment
        thin_border = openpyxl.styles.Border(
            left=openpyxl.styles.Side(style="thin"),
            right=openpyxl.styles.Side(style="thin"),
            top=openpyxl.styles.Side(style="thin"),
            bottom=openpyxl.styles.Side(style="thin"),
        )

        for row in worksheet.iter_rows(
            min_row=1, max_row=len(df) + 1, min_col=1, max_col=3
        ):
            for cell in row:
                cell.border = thin_border
                cell.alignment = openpyxl.styles.Alignment(
                    wrap_text=True, vertical="top"
                )

    print(f"✅ Excel file created successfully: {filename}")
    print(f"📊 Total applications: {len(apps_data)}")
    return filename


if __name__ == "__main__":
    try:
        import openpyxl

        print("📝 Generating Excel file with application data...")
        filename = create_excel_file()
        print(f"\n🎉 Success! The Excel file '{filename}' has been created with:")
        print(f"   • {len(apps_data)} applications")
        print(f"   • Name, Description, and Official URL for each app")
        print(f"   • Professional formatting and styling")

    except ImportError as e:
        print("❌ Missing required packages. Please install them:")
        print("   pip install pandas openpyxl")
        print(f"\nError: {e}")
    except Exception as e:
        print(f"❌ Error creating Excel file: {e}")

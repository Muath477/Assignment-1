from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "Airtop Case Study Analysis", border=False, ln=True, align="R")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def create_pdf():
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 15, "Airtop Case Study Presentation", ln=True, align="C")
    pdf.ln(10)
    
    content = [
        ("Title & Case Study Overview", "H"),
        ("Company: Airtop", "B"),
        ("Industry: Software & Technology (GenAI Native)", "B"),
        ("Use case: Browser automation for AI agents", "B"),
        ("Reference: LangChain Blog Case Study: 'How Airtop built web-automation for AI agents powered by the LangChain ecosystem' (Nov 26, 2024)", "B"),
        ("Student Name: Muath hassan AL-mutairi", "B"),
        ("University: Tabuk University", "B"),
        ("Major: IT", "B"),
        
        ("Introduction to Airtop & The Problem", "H"),
        ("What is Airtop?: A powerful platform that provides cloud-based browsers, empowering developers to create scalable web automations using natural language commands.", "B"),
        ("The Challenge: AI agents need web data, but navigating websites at scale is difficult due to Captchas, authentication barriers, and complex layouts.", "B"),
        ("The Solution: Airtop bridges this gap by replacing brittle CSS selector hacks and Puppeteer scripts with reliable, natural language APIs.", "B"),
        
        ("Core Capabilities", "H"),
        ("Extract API: Extracts structured information from web pages (e.g., lists of speakers, flight prices, LinkedIn URLs). It works seamlessly even on authenticated sites.", "B"),
        ("Act API: Enables agents to take real-time actions on websites, such as entering search queries, clicking buttons, and interacting with UI elements.", "B"),
        
        ("Powering Airtop with the LangChain Ecosystem", "H"),
        ("LangChain: Provides a 'batteries-included' standardized interface to switch seamlessly between models (GPT-4, Claude, Gemini) for different use cases.", "B"),
        ("LangGraph: Powers a flexible agent architecture. Airtop builds individual browser automations as subgraphs, giving them dynamic control and ensuring the accuracy of agent steps.", "B"),
        ("LangSmith: Used for multimodal debugging and prompt engineering. It helps clarify nebulous error messages and provides a testing playground to simulate real-world use cases.", "B"),
        
        ("What is 'Agentic' vs. What is Not? (Crucial Analysis)", "H"),
        ("What IS Agentic? (LLM-Driven)", "Sb"),
        ("- Semantic Understanding: Interpreting natural language commands to decide what actions to take on a webpage.", "I"),
        ("- Dynamic Decision Making: Understanding the webpage layout visually/semantically to interact with elements (no hardcoded CSS selectors).", "I"),
        ("- Orchestration: LangGraph agents defining the control flow for multi-step, complex web tasks.", "I"),
        ("What is NOT Agentic? (Software Component / Non-LLM)", "Sb"),
        ("- Headless Browser Infrastructure: The actual underlying browser instances running on Airtop's cloud.", "I"),
        ("- Action Execution Engine: The traditional code executing the physical mouse clicks, keystrokes, and API payload parsing.", "I"),
        ("- Security Bypassing: The deterministic algorithms used for handling session authentication and Captcha solving.", "I"),
        
        ("Conclusion & Future Outlook", "H"),
        ("Impact: By leveraging LangChain, LangGraph, and LangSmith, Airtop drastically accelerated its time-to-market and improved agent reliability.", "B"),
        ("What's Next for Airtop?", "Sb"),
        ("- Building sophisticated agents for high-value tasks like stock market analysis.", "I"),
        ("- Expanding micro-capabilities to perform an unlimited range of actions across the web.", "I"),
    ]
    
    for text, style in content:
        if style == "H":
            pdf.ln(5)
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_text_color(0, 102, 204)
            pdf.cell(0, 10, text, ln=True)
            pdf.ln(2)
        elif style == "B":
            pdf.set_font("Helvetica", "", 12)
            pdf.set_text_color(0, 0, 0)
            parts = text.split(":", 1)
            if len(parts) == 2:
                pdf.set_font("Helvetica", "B", 12)
                pdf.write(8, "* " + parts[0] + ":")
                pdf.set_font("Helvetica", "", 12)
                pdf.write(8, parts[1] + "\n")
            else:
                pdf.write(8, "* " + text + "\n")
        elif style == "Sb":
            pdf.ln(2)
            pdf.set_font("Helvetica", "B", 13)
            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 8, "* " + text, ln=True)
        elif style == "I":
            pdf.set_x(25)
            pdf.set_font("Helvetica", "", 12)
            pdf.set_text_color(0, 0, 0)
            parts = text.split(":", 1)
            if len(parts) == 2:
                pdf.set_font("Helvetica", "B", 12)
                pdf.write(8, parts[0] + ":")
                pdf.set_font("Helvetica", "", 12)
                pdf.write(8, parts[1] + "\n\n")
            else:
                pdf.write(8, text + "\n\n")
                
    pdf.output("Airtop_Case_Study_Presentation.pdf")
    print("PDF generated successfully.")

if __name__ == "__main__":
    create_pdf()
